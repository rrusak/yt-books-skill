# Writing narration for ElevenLabs Eleven v4

How to write the spoken text in `03-script.md` and `05-narrator.md` so Eleven v4 reads it well. Adapted for this channel from ElevenLabs' text-to-speech best practices, section "Prompting Eleven v4" (https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices#prompting-eleven-v4, read 2026-11-09). Most of it also holds for Eleven v3.

## 1. When this applies

Check `model_id` in `assets/voice-config.json`:

- `eleven_v4` or `eleven_v3`, or still `SET_ME`: write for v4 as described here. v4 is the recommended model, so a book written before the model is chosen is written for v4.
- Any other model (for example `eleven_multilingual_v2` or a Flash model): write plain text with pause markers only, no audio tags. If tags are already in the script, `generate_voice.py` strips them for these models so they are not read aloud.

## 2. What v4 listens to

v4 takes its delivery from the text itself, not from markup or sliders:

- **Audio tags** in square brackets, such as `[whispers]` or `[sighs]`, steer how the next words are said.
- **Punctuation:** ellipses add a pause and weight, dashes give a short break, capitals add emphasis, and ordinary punctuation sets the rhythm.
- **Text structure:** narrative writing with clear emotional context. A sentence that is plainly tender is read tenderly even without a tag.

What v4 does **not** take:

- SSML, including `<break>` tags.
- The `style` and `speed` voice settings. Only `stability` and `similarity_boost` apply, plus `clone_strength` for v4-tuned professional voice clones. Lower stability gives more emotional range and makes tags land more strongly; higher stability gives a steadier, more even read.

## 3. Pauses

Keep the channel's markers: `[pause]` (about 1 second) and `[long pause]` (about 2 seconds). `generate_voice.py` converts them using `pause_markup` in `voice-config.json`.

Inside a sentence, use punctuation instead of markers:

- an ellipsis for hesitation or weight ("He signed it... and smiled.");
- a dash for a quick turn ("It was a fair price — or so he thought.").

Do not stack them. One ellipsis per thought is enough, and not every sentence needs one.

## 4. Audio tags for this channel

A tag goes immediately before the words it colours and affects that phrase or sentence. Tags describe **the voice only**. The channel's narrator is warm and never loud, so the palette is small.

**NARRATOR** (introduction, takeaways, outro):

| Use for | Tags |
| --- | --- |
| Warmth, welcome, sincerity | `[warmly]`, `[softly]`, `[gently]` |
| Light humour, irony | `[chuckles]`, `[laughs softly]`, `[mischievously]`, `[dryly]` |
| The riddle, a secret, a twist | `[whispers]`, `[curious]`, `[conspiratorially]` |
| The personal moment, a heavy truth | `[sighs]`, `[thoughtfully]`, `[quietly]` |

**STORYTELLER** (story scenes): the fairy-tale voice stays even, so tags are rare: `[softly]`, `[whispers]`, `[sighs]`, `[hushed]`. When a character's line needs a different colour, describe the voice quality rather than naming an emotion. ElevenLabs recommends this because it is less likely to be read as a sound effect. For example: `[low, gravelly voice] "Sign here."`

**Never use:**

- sound-effect tags (`[gunshot]`, `[applause]`, `[explosion]`, `[clapping]` and the like), since music and sound are added in editing;
- `[shouts]`, `[crying]`, `[laughs harder]`, `[wheezing]`, `[snorts]`, `[sings]` or accent tags;
- experimental tags;
- any tag that contradicts the meaning of the line.

**How many tags.** Tags are seasoning. Most sentences have none.

| Voice and level | Tags per scene | Across all narrator scenes |
| --- | --- | --- |
| Narrator, light vlogger touch | 0–1 | about 4–8 |
| Narrator, medium | 0–2 | about 8–12 |
| Narrator, high | 0–3 | about 12–16 |
| Storyteller (any level) | 0–1, most scenes none | about 5–10 in the whole story |

Never put two tags side by side. If two qualities are needed, combine them in one descriptive tag such as `[softly, amused]`.

**Lines that stay plain:**

- The subscribe line stays plain and literal. At most it may start with `[warmly]`.
- The opening quote is read straight; a tag may come after it, on the riddle.
- The quote repeated in the outro is read the same way as in the opening.

## 5. Emphasis with capitals

Capitals make v4 stress a word ("It was NEVER about the painting."). Use them on at most one word in a narrator scene, only where a speaker would naturally lean on it. Use them at most once every few scenes in the story. Never capitalise a whole sentence, and never capitalise names or the book's title for emphasis.

## 6. Pronunciation

- v4 reads IPA written between forward slashes inside the text, for example `/məˈfɪstəfiːliːz/`. Include stress marks. Results can still vary between takes, so regenerate a scene if a name comes out wrong.
- Phoneme tags do not work on v4 (they are for Flash v2 only).
- Keep every hard name in the script's pronunciation guide. Add an IPA column when writing for v4, and use the IPA form in the fence only for a name that v4 actually misreads, after hearing it. Plain respelling ("meh-fis-TOF-uh-leez") is the fallback.

## 7. How to add tags: a separate pass

Write and finish the words first. Only then add tags and emphasis in a second pass, following the rules ElevenLabs uses for its own tag "Enhance" feature:

- Never change, add or remove a word while tagging. Tags and capitals go on top of the finished text.
- Do not turn narrative description into tags. If the line already says "she whispered", it needs no `[whispers]`.
- Vary the delivery across the video, so the same tag does not open every scene.
- In the gravest moments (a death, a damnation, a cruelty), use no tag or only a quiet one (`[softly]`, `[quietly]`). Let the words carry them.

Lines shared between `05-narrator.md` and `03-script.md` carry the same tags in both files.

## 8. After choosing voices

Tags behave differently on different voices. Deliveries a voice was trained on (a soft voice whispering, for example) come out most reliably. Once the user has set the NARRATOR and STORYTELLER voices:

- listen to the first narrator and story scenes before trusting the full run;
- if a tag is read aloud, does nothing, or produces a sound instead of a delivery, replace it with a descriptive tag (`[low, warm voice]`) or remove it, and regenerate only that scene;
- a serious, deep voice may not suit playful tags such as `[mischievously]`. Prefer `[dryly]` or no tag.

## 9. Checklist

- [ ] Tags only if the model is v4, v3 or not yet chosen.
- [ ] Every tag is from section 4 or is a short description of the voice; no sound effects.
- [ ] Tag counts are within the table for the book's vlogger level and for the storyteller.
- [ ] No two tags side by side; the subscribe line is plain.
- [ ] At most one capitalised word per narrator scene; none for whole sentences.
- [ ] Pause markers are only `[pause]` and `[long pause]`; ellipses and dashes are used sparingly.
- [ ] Narrator lines carry identical tags in `05-narrator.md` and `03-script.md`.
