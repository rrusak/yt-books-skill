#!/usr/bin/env python3
"""Generate one speech file per scene of an approved script with ElevenLabs.

Usage:
    python generate_voice.py <path-to-book-folder> [--dry-run] [--scenes 1,5-7]
                             [--force] [--config path/to/voice-config.json]

Reads the ```text fences and Voice lines of 03-script.md (the same parsing as
check_book.py) and writes voice/NN.<ext> for each scene, plus voice/voice-log.json.
A narrator cut-in such as scene 14a is written to voice/14a.<ext>.

- --dry-run   no API calls; lists scenes, voices and characters to be billed.
- --scenes    only these scenes: a comma list such as 7,12-14,14a. A range includes
              the cut-ins inside it.
- --force     regenerate scenes whose file already exists (default: skip them).
- --config    voice settings; default is ../assets/voice-config.json.

The API key is read from ELEVENLABS_API_KEY. If it is not set, the nearest
.env file in the book folder, the current folder or their parents is loaded.
The key is never printed.
"""
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from elevenlabs import ElevenLabs, VoiceSettings

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from check_book import CONFIRM, SceneId, parse_scenes  # noqa: E402

DEFAULT_CONFIG = SCRIPT_DIR.parent / "assets" / "voice-config.json"
LONG_PAUSE = re.compile(r"\[long pause[^\]]*\]", re.IGNORECASE)
PAUSE = re.compile(r"\[pause[^\]]*\]", re.IGNORECASE)
AUDIO_TAG = re.compile(r"\[(?!(?:long |short )?pause\b)[^\]]*\]\s*", re.IGNORECASE)
TAG_MODELS = ("eleven_v4", "eleven_v3")  # models that act on audio tags instead of reading them aloud
EXTENSIONS = {"mp3": ".mp3", "wav": ".wav", "pcm": ".pcm", "opus": ".opus", "ulaw": ".ulaw", "alaw": ".alaw"}


def load_env_file(start_dirs):
    """Load the nearest .env with python-dotenv, without overriding the environment."""
    if os.environ.get("ELEVENLABS_API_KEY"):
        return
    for start in start_dirs:
        for folder in [start, *start.parents]:
            env = folder / ".env"
            if env.is_file():
                load_dotenv(env, override=False)
                if os.environ.get("ELEVENLABS_API_KEY"):
                    return


def select_scenes(spec, scenes):
    """Scenes named in a list like "7,12-14,14a". A range includes the cut-ins inside it."""
    chosen, missing = set(), []
    for part in spec.split(","):
        part = part.strip().lower()
        if not part:
            continue
        rng = re.fullmatch(r"(\d+)-(\d+)", part)
        if rng:
            a, b = int(rng.group(1)), int(rng.group(2))
            hits = {k for k in scenes if a <= k.number <= b}
            chosen |= hits
            if not hits:
                missing.append(part)
            continue
        one = re.fullmatch(r"(\d+)([a-z]?)", part)
        key = SceneId(one.group(1), one.group(2)) if one else None
        if key in scenes:
            chosen.add(key)
        else:
            missing.append(part)
    return chosen, missing


def supports_tags(model_id):
    model = str(model_id or "").lower()
    return model == "set_me" or model.startswith(TAG_MODELS)


def spoken_text(lines, pause_markup, keep_tags=True):
    text = "\n".join(lines).strip()
    if not keep_tags:
        text = re.sub(r"[ \t]{2,}", " ", AUDIO_TAG.sub("", text))
    text = LONG_PAUSE.sub(pause_markup.get("long_pause", "... ..."), text)
    text = PAUSE.sub(pause_markup.get("pause", "..."), text)
    return text


def check_config(config, voices_needed):
    problems = []
    if str(config.get("model_id", "SET_ME")).upper() == "SET_ME":
        problems.append("model_id is not set")
    voices = config.get("voices", {})
    for name in sorted(voices_needed):
        entry = voices.get(name)
        if not entry:
            problems.append(f"no voice configured for {name}")
        elif str(entry.get("voice_id", "SET_ME")).upper() == "SET_ME":
            problems.append(f"voice_id for {name} is not set")
    return problems


def main() -> int:
    argv = sys.argv[1:]
    flags = {"--dry-run": False, "--force": False}
    options = {"--scenes": None, "--config": None}
    positional = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in flags:
            flags[a] = True
        elif a in options and i + 1 < len(argv):
            options[a] = argv[i + 1]
            i += 1
        else:
            positional.append(a)
        i += 1
    if not positional:
        print(__doc__)
        return 1

    root = Path(positional[0]).resolve()
    script_path = root / "03-script.md"
    if not script_path.exists():
        print(f"Not found: {script_path}")
        return 1
    config_path = Path(options["--config"]).resolve() if options["--config"] else DEFAULT_CONFIG
    config = json.loads(config_path.read_text(encoding="utf-8"))

    scenes = parse_scenes(script_path.read_text(encoding="utf-8"))
    if options["--scenes"]:
        wanted, missing = select_scenes(options["--scenes"], scenes)
        if missing:
            print(f"Scenes not in the script: {', '.join(missing)}")
            return 1
    else:
        wanted = set(scenes)

    fmt = config.get("output_format") or "mp3_44100_128"
    ext = EXTENSIONS.get(fmt.split("_")[0], ".bin")
    voice_dir = root / "voice"
    voice_dir.mkdir(exist_ok=True)
    pause_markup = config.get("pause_markup", {})

    order = sorted(scenes)
    def model_for(voice_name):
        return config.get("voices", {}).get(voice_name, {}).get("model_id") or config.get("model_id")

    texts = {
        n: spoken_text(scenes[n]["spoken"], pause_markup, supports_tags(model_for(scenes[n]["voice"])))
        for n in order
    }
    stripped = [n for n in order if n in wanted and not supports_tags(model_for(scenes[n]["voice"]))]
    if stripped:
        print(f"Model does not support audio tags: tags are removed before sending ({len(stripped)} scene(s)).")
    jobs = []
    unconfirmed = []
    for n in order:
        if n not in wanted:
            continue
        s = scenes[n]
        out = voice_dir / f"{n:02d}{ext}"
        if not s["voice"]:
            print(f"Scene {n:02d}: no Voice line, skipped")
            continue
        if not texts[n]:
            print(f"Scene {n:02d}: no spoken text, skipped")
            continue
        if CONFIRM.search("\n".join(s["spoken"])):
            print(f"Scene {n:02d}: has an unconfirmed [CONFIRM: ...] personal line, skipped. Settle it in 03-script.md first.")
            unconfirmed.append(n)
            continue
        if out.exists() and not flags["--force"]:
            print(f"Scene {n:02d}: {out.name} exists, skipped (use --force to redo)")
            continue
        jobs.append(n)

    chars = sum(len(texts[n]) for n in jobs)
    print(f"{len(jobs)} scene(s) to generate, {chars} characters, model {config.get('model_id')}, format {fmt}")
    for n in jobs:
        print(f"  {n:02d} | {scenes[n]['voice']:<11} | {len(texts[n]):>5} chars | {scenes[n]['title']}")

    problems = check_config(config, {scenes[n]["voice"] for n in jobs})
    if problems:
        print(f"\nVoice config not ready ({config_path}):")
        for p in problems:
            print(f"  - {p}")
        return 0 if flags["--dry-run"] else 1
    if flags["--dry-run"] or not jobs:
        return 0

    load_env_file([root, Path.cwd()])
    if not os.environ.get("ELEVENLABS_API_KEY"):
        print("ELEVENLABS_API_KEY is not set and no .env with it was found. "
              "Run `npx -y @elevenlabs/cli@latest onboard init` in the project folder.")
        return 1

    # The SDK reads the variable at import time, before .env is loaded, so pass it on.
    client = ElevenLabs(api_key=os.environ["ELEVENLABS_API_KEY"])
    log_path = voice_dir / "voice-log.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}
    failures = []

    for n in jobs:
        s = scenes[n]
        voice = config["voices"][s["voice"]]
        kwargs = {
            "voice_id": voice["voice_id"],
            "text": texts[n],
            "model_id": model_for(s["voice"]),
            "output_format": fmt,
        }
        settings = voice.get("voice_settings")
        if settings:
            kwargs["voice_settings"] = VoiceSettings(**settings)
        for key in ("language_code", "apply_text_normalization", "seed"):
            if config.get(key) is not None:
                kwargs[key] = config[key]
        if config.get("stitch_neighbouring_scenes"):
            same = [m for m in order if scenes[m]["voice"] == s["voice"] and texts[m]]
            idx = same.index(n)
            if idx > 0:
                kwargs["previous_text"] = texts[same[idx - 1]]
            if idx + 1 < len(same):
                kwargs["next_text"] = texts[same[idx + 1]]

        out = voice_dir / f"{n:02d}{ext}"
        part = out.with_suffix(out.suffix + ".part")
        for attempt in range(1, 4):
            try:
                with open(part, "wb") as f:
                    for chunk in client.text_to_speech.convert(**kwargs):
                        f.write(chunk)
                part.replace(out)
                break
            except Exception as e:  # noqa: BLE001 - report any API error per scene
                if part.exists():
                    part.unlink()
                status = getattr(e, "status_code", None)
                if status == 429 and attempt < 3:
                    wait = 10 * attempt
                    print(f"Scene {n:02d}: rate limited, retrying in {wait} s")
                    time.sleep(wait)
                    continue
                failures.append(n)
                print(f"Scene {n:02d}: failed ({status or type(e).__name__}): {e}")
                break
        if n in failures:
            continue
        log[f"{n:02d}"] = {
            "file": out.name,
            "voice": s["voice"],
            "voice_id": kwargs["voice_id"],
            "model_id": kwargs["model_id"],
            "characters": len(texts[n]),
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        log_path.write_text(json.dumps(log, indent=2, sort_keys=True), encoding="utf-8")
        print(f"Scene {n:02d}: wrote voice/{out.name}")

    done = len(jobs) - len(failures)
    print(f"\n{done} of {len(jobs)} scene(s) generated.")
    if failures:
        print(f"Failed: {', '.join(f'{n:02d}' for n in failures)}. Rerun with --scenes to retry them.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
