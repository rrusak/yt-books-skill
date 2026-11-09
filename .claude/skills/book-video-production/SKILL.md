---
name: book-video-production
description: Produce the complete production package for a 20–25 minute YouTube book video told as a fairy tale in the channel's naïve colored-pencil style — a book folder with the color palette, character and scene image prompts, the narration script for voice generation, and title/thumbnail options, plus empty images/, voice/, thumbnails/, music/ and videos/ folders. Use this whenever the user names a book (novel, play, epic, classic) and asks for a video, episode, script, storyboard, illustration prompts, palette, voiceover text, thumbnails or titles for it, or says things like "do the next book", "let's make [book]", "prepare [book] for the channel", even if they ask for only part of the package. Also use it when the user says a book's script is approved (to record it in the narration history and video library and generate the per-scene speech with ElevenLabs), asks to generate or redo the voice/speech for a book's scenes, or says a video is published.
---

# Book Video Production

This skill turns one book into a ready-to-produce video package for the channel. The channel retells books as fairy tales: a narrator opens cold with a hook (a riddle-like quote, a vivid moment, a question, a surprising fact, a mystery or a bold claim, varied between books), a storyteller tells the plot scene by scene, and the narrator returns with two to five takeaways and closes by paying off the hook. Every scene has one illustration in a fixed colored-pencil style, and each book gets its own palette and character designs.

Three guides in `references/` hold the method. This file says how to run it and what to output.

## What you produce

One folder per book, named with a lowercase kebab-case slug of the title (`faust`, `the-great-gatsby`, `crime-and-punishment`):

```
<book-slug>/
├── 01-palette.md                  # world, color palette, motifs, prompt lines
├── 02-illustrations.md            # master prompt, characters, scene prompts
├── 03-script.md                   # narration script for voice generation
├── 04-titles-and-thumbnails.md    # titles, thumbnails, description, promotion
├── 05-narrator.md                 # narrator lines, calls to action, on-screen poses
├── images/                        # empty
├── voice/                         # speech per scene, generated after approval (step 12)
├── thumbnails/                    # empty
├── music/                         # empty
└── videos/                        # empty
```

The five main documents sit in the root of the book folder. The five subfolders are created empty. Once the script is approved, the skill fills `voice/` with ElevenLabs speech (step 12); the user fills the rest during production.

Next to the book folders, in the same base directory, sit three shared files:

- `narrator-bible.md`: who the narrator is. The narrator is the channel's creator, speaking in their own cloned voice. The file holds the true facts he may mention on air, background that is never mentioned, confirmed opinions, running jokes, things never to say, and a log of personal lines already used. Read it before writing narrator lines (step 6). Only the user adds facts; the skill adds to the log after approval (step 11).
- `narration-history.md`: the key narrator lines of every approved book, so later books do not repeat them. Read it before writing narrator lines (step 6).
- `video-library.md`: the channel's memory of its videos, with each book's themes, central question, takeaways, archetypes, spoiler to avoid and published status. Read it while planning (step 3) to find earlier videos worth pointing viewers to.

The history and the library are written only after the user approves a script (step 11).

The guides were written with their own document names. They map onto these files as follows:

| The guides call it | In this package |
| --- | --- |
| Book Style Sheet — [Book].md: world, palette, motifs | `01-palette.md` |
| Book Style Sheet — [Book].md: characters; Illustration Plan | `02-illustrations.md` |
| Narration Script | `03-script.md` |
| Packaging Sheet | `04-titles-and-thumbnails.md` |
| Narrator.md | `05-narrator.md` |

## Reference files

Read each guide in full before the step that needs it. They are the source of truth; this file only adds output formats and workflow.

- `references/scenario-guide.md` — structure, running order, opening hook types, narrator introduction beats, fairy-tale voice, quote scenes, takeaways, outro, illustration content rules. Read before planning (step 3).
- `references/visual-style.md` — channel constants, the master style prompt, flat equivalents for lighting words, palette structure, and the process for building a book's palette and characters. Read before writing `01-palette.md`.
- `references/title-thumbnail-guide.md` — hooks, three thumbnail types, title formulas, description, chapters, tags, Shorts. Read before writing `04-titles-and-thumbnails.md`.
- `references/spoken-style.md` — how to make spoken text sound said by a person: phrases never to use, patterns to ration, the read-aloud pass, imperfections allowed at each vlogger level. Read before writing `05-narrator.md` (step 6) and `03-script.md` (step 7).
- `references/elevenlabs-v4.md` — how to write spoken text for the Eleven v4 voice model: audio tags (which, how many, where), pauses, emphasis, pronunciation, and the tagging pass. Read before writing `05-narrator.md` (step 6) and `03-script.md` (step 7).
- `assets/narrator-bible-template.md` — the empty structure of `narrator-bible.md`, used only if the base directory has none yet.
- `assets/narrator/` — the channel narrator's finished pose images (`fullbody-N.png`, `halfbody-N.png`), character sheets, and `narrator_image_description.md`, which describes each pose's framing, gesture and EMOTION. Read the description file before writing `05-narrator.md`. Poses marked "do not use yet" are off limits.
- `assets/voice-config.json` — ElevenLabs settings for step 12: model, output format, how pause markers are sent, and one voice per `Voice:` name (`NARRATOR`, `STORYTELLER`) with its voice ID and voice settings. Values marked `SET_ME` are still to come from the user.
- `assets/gothic_bargain_at_midnight.png` — the channel's technique reference image (from *Faust*). Look at it once so your scene descriptions match what the style can draw. The user attaches it in the image generator; it is not copied into the book folder.

## Channel documents that are not in this skill

**Thumbnail typography** (typeface and text treatment for thumbnail text) lives in a separate channel document the user keeps. If it is attached or in the project, use it; if not, describe the text treatment generically and say so in your reply.

If the user supplies an existing palette, character designs or anchor image for the book, build on those instead of designing new ones.

## Inputs

- **Required:** the book. Identify the exact work and author.
- **Vlogger touch:** how much the narrator sounds like a YouTube host: `light`, `medium` or `high` (scenario guide, section 5, "Vlogger touch").
- **Optional:** target runtime (default ~22 minutes), video language (default English; write all five files in that language), preferred translation, which characters matter most to them.

**Always ask for the vlogger touch level** before starting, unless the user has already given it for this book. Ask it as one short question with the three levels (light, medium, high), each with a one-line description, and mark light as recommended. Do not carry a level over from an earlier book unless the user says so.

Otherwise, ask a question only if the book is genuinely ambiguous (two well-known works share the title) or the user's request contradicts the format. Ask any such question together with the vlogger-touch question, then start, and state any assumption at the top of your reply.

## Workflow

Set up a task list with these steps, since the package takes a while and the user may step away.

### 1. Create the folder

```bash
python <skill-dir>/scripts/init_book_folder.py <book-slug> <base-dir>
```

`<base-dir>` is the folder that holds the book folders and `narration-history.md`: `books-assets/` when working in the channel's repository (it has one), otherwise the working directory, or the user's connected folder if they asked for the package to go there.

If `<base-dir>/narrator-bible.md` does not exist, copy `assets/narrator-bible-template.md` there. Ask the user, together with the vlogger-touch question, a few short questions to fill it in: where and how they read, writers they love, what they are happy to mention, and anything never to say. Do not invent the answers. Blanks are fine.

### 2. Research the book

Verify facts before writing; the script is published under the channel's name, and wrong line numbers or misattributed quotes undermine it. Use web search and fetch for:

- the plot sequence and what happens in each beat, including the ending;
- character names, relationships and appearance cues given in the text;
- the author hook (how, when or why the book was written) and the origins hook (what came before and what the author changed);
- material for honest asides and the verdict: how the book was received (then and now), which parts readers find hard going, what translations lose, and which English translations or editions are well regarded and still available (translator, publisher, year), plus whether a free public-domain text exists;
- each key quote: exact wording in a public-domain English translation (published before 1929) or your own literal translation, the original-language text, speaker, and location (part, act/chapter/scene, line where the work has line numbers).

If you cannot confirm a line number, give the scene or chapter only. Keep the sources; they go at the end of `01-palette.md`.

### 3. Plan

Follow `references/scenario-guide.md` steps 1–3: plot beats, 5–7 key quotes, the opening hook (scenario guide section 4: pick the type that suits the book, not the type the previous book in `narration-history.md` used; a quote keeps its speaker hidden; every hook is paid off in the outro), 2–5 takeaways (as many as the book genuinely supports) in a takeaway shape (scenario guide section 7: separate lessons, one big idea, one question with several answers, where it turned, or two sides; not the previous book's shape unless the book clearly needs it), author and origins hooks, the intro shape (scenario guide section 5: about 90 seconds, at most one context fact, not the previous book's shape), recurring characters, the chronological timeline with quote scenes placed where they are spoken, and 35–40 scenes.

Use **one numbering for everything**: scene 07 in the script is image 07 in the plan, `07-*.png` in `images/` and `07.*` in `voice/`. The Faust guide shows illustration numbers in brackets because that project was renumbered later; new books do not need brackets.

Also pick the three hooks for packaging now (title-thumbnail guide, section 2), so the script and the packaging promise the same things.

**Links to earlier videos.** Read `<base-dir>/video-library.md` if it exists, and compare this book's themes, central question, takeaways and archetypes with each entry, using the three kinds in scenario guide section 7 ("Pointing to earlier videos"). Decide on 0–2 links, each tied to a specific takeaway or to the outro. Choose none rather than force one. If the library does not exist, there is nothing to link yet.

### 4. Write `01-palette.md`

Follow visual-style.md section 7, steps 1–3. The palette is the book's identity, so give each color a meaning in the story and make it clearly different from the previous book the user mentions (the Faust palette is cobalt, vermilion and ochre).

````markdown
# [Book] — Palette and World

Book layer for the channel style. Technique, rendering and composition come from the channel's Visual Style guide and never change per book.

## World
- Period and place:
- Mood:
- Central duality:
- Key settings: [4–8 recurring locations]
- Symbolic objects:

## Palette
| Role | Name | Hex | Meaning in the story |
| --- | --- | --- | --- |
| Paper | Ivory | #F5EAD5 | Open space, light |
| Line / dark | Charcoal | #242122 | Outlines, darkness |
| Dominant cool | | | |
| Dominant warm | | | |
| Earth / light | | | |
| Skin | | | |
| Optional accent | | | |

## Motif vocabulary
[6–10 decorative elements from the book's world, one line each]

## How this book shows light and time
[Night, day, fire, candlelight, the sacred, the supernatural — each as flat color fields and hand-shaded halos in this palette]

## Prompt lines
Palette line:
```text
[color names, comma-separated]
```
Motif line:
```text
[motifs, comma-separated]
```

## Status
Draft. Lock after the anchor image and 2–3 test scenes match (Visual Style guide, section 7, steps 5–7).

## Sources
- [Title](URL)
````


### 5. Write `02-illustrations.md`

This file is what the user pastes into the image generator, so every prompt sits in its own ```text fence for one-click copying, and every scene prompt is self-contained apart from the master prompt.

````markdown
# [Book] — Characters and Scenes

## How to use
1. In a new image-generator conversation for this book, attach the channel technique reference image (and, once it exists, this book's anchor image and character sheets).
2. Paste the master prompt below once.
3. Generate the anchor image (scene 01), then the character reference sheets, then the scenes one at a time in order, approving each before the next.

## Master prompt
```text
[Visual Style master prompt, with the palette and motif lines from 01-palette.md filled in]
```

## Characters
### [Name] — [variant, if any]
| Field | Description |
| --- | --- |
| Role | |
| Age and build | |
| Silhouette | |
| Signature elements | [2–3 that never change] |
| Hair and face | |
| Costume | [with palette color names] |
| Props | |
| Posture and gesture | |
| Appears in scenes | 05, 07, 12 |

Fixed descriptor:
```text
[One sentence, 25–40 words]
```
Reference sheet prompt:
```text
[Visual Style section 7 step 6 sheet prompt with the fixed descriptor]
```

## Recurring locations
### [Location]
```text
[Fixed description reused word for word in every scene set there]
```

## Scenes
| Block | Scenes | Count |
| --- | --- | --- |
| Introduction | 01–04 | 4 |
| … | | |
| **Total** | | **N** |

### 01 · [Title]
- Block: Introduction · Type: frame · Characters: [names or none]
```text
[Fixed descriptors of characters present, word for word.] [Scene: setting, action, props, emotion, composition.] Match the attached references' drawing technique, texture, palette and character designs, not their composition.
```

### NN · Quote: "[short form]"
- Block: Story · Type: quote · Characters: …
- Quote: "[English]" — *[original]* — [speaker], [location]
```text
[Symbolic image]
```
````

Rules that matter most, all from the guides:

- **Types:** `frame` (introduction), `story` (literal moment), `quote` (symbolic metaphor, never a repeat of a plot image), `takeaway` (modern universal metaphor), `verdict` (the book being read or carried in its own world, symbolic), `outro` (mirrors scene 01).
- **Flat language:** never write shadow, glow, beam, radiant, misty, blurred, smoke billows. Use the flat equivalents in visual-style.md section 2.4. The Faust plan broke this rule and its prompts fought the style.
- **Character consistency:** paste the fixed descriptor every time a recurring character appears, even if it feels repetitive; the image model has no memory of the previous prompt's wording. Give each age or costume variant its own descriptor.
- **No text in images**, no copyrighted characters, no identifiable modern people, nothing graphic (show tragedy at the moment before or after, or symbolically).
- **Every scene gets a book illustration**, composed as a full image. The narrator is never generated here, and no prompt leaves space for him or for text; the user adds both as overlays in editing.

### 6. Write `05-narrator.md`

The narrator is the channel's host. His look is fixed by the pose images in `assets/narrator/`, so this file never describes or prompts new narrator images. It sets what he says and which pose is on screen when. Write the persona, lines and calls to action first, so the script can use them, and fill in the on-screen plan once the script exists.

**Persona.** A warm, slightly theatrical host who tells the story to the viewer as a friend: conversational, gently amused, lightly ironic, sincere at the important moments, and modest enough to admit a personal feeling once per video. These traits match the EMOTION notes in `narrator_image_description.md`. Keep him the same in every book; only the tone shifts with the book.

**Who he is.** The narrator is the channel's creator, in their own cloned voice. Read `<base-dir>/narrator-bible.md` before writing any narrator line and follow it:

- Use at most one or two personal touches per video, drawn from its "On air" facts and opinions. Never contradict it or its anecdote log, and never reuse a logged anecdote.
- Never state or hint at anything in its "Background" section, including through metaphors that would give it away.
- Respect its "Never say" list and its running jokes' limits.
- Any personal line the file does not cover is written as `[CONFIRM: the line as spoken]`, in both `05-narrator.md` and `03-script.md`. This includes the video's personal moment, unless it is a general truth already in the file. That applies to a memory of reading this book, a feeling about it, or a new opinion. Never present an invented experience as fact.
- Atmosphere written for the viewer ("pull your chair a little closer") is not a personal claim and needs no confirmation.

**Vlogger touch.** Write all of the narrator's words at the level the user chose (scenario guide, section 5, "Vlogger touch"): the lines here, and the introduction, takeaways and outro in the script. The storyteller's story scenes are not affected.

**Sound like a person.** Follow `references/spoken-style.md`: none of the phrases in its section 1, the patterns in section 2 kept within their limits, and the read-aloud pass (section 3) on every line once the words are final. Add the small imperfections allowed for the book's vlogger level (section 4).

**Delivery for the voice model.** The narrator's lines are spoken by ElevenLabs, so write them for the model set in `assets/voice-config.json`, following `references/elevenlabs-v4.md` (by default Eleven v4). Write the words first. Then, in a separate pass, add the audio tags, the ellipses and dashes, and the occasional capitalised word that give the delivery, without changing a word. The narrator's tag density follows the vlogger level. A light touch means a few tags across the whole video, such as a `[chuckles]` on the joke or a `[softly]` on the personal moment. The subscribe line stays plain. Every line in this file carries exactly the tags it will have in the script.

**Avoid repetition.** Before writing any narrator line, read `<base-dir>/narration-history.md` if it exists. In this book's welcome, intro, takeaways, outro, invitation and sign-off, do not reuse any line recorded there or a close paraphrase of it, and use a different outro callback approach (scenario guide, section 7) from the last three books. The subscribe line is the one exception; it stays the same. If the file does not exist yet, this is the first recorded book and nothing needs to be avoided.

**Welcome, invitation and sign-off.** Write these for each book, in that book's tone and imagery, so they sound like part of this tale and not a stock formula. Each is short enough to say in one breath. The welcome greets the viewer and leads into the logline, the invitation points to the next tale, and the sign-off is a short, warm goodbye.

**Final-scene calls to action.** The final scene always contains both, in this order, before the invitation and sign-off:

1. **Comments and likes, said creatively.** Invite the viewer to answer the outro's reflective question in the comments and to leave a like, phrased in this book's own imagery and motifs and written fresh for every book. *Faust* examples: "Write your answer in the comments, and sign it in ink, not in blood." / "If this tale lit a small candle for you, leave a like so it can light the way for the next traveller."
2. **Subscribe and bell, said directly.** A plain, literal call to action with no metaphor: "Please subscribe to the channel and click the bell button, so you never miss a new tale." Keep this wording or a close, equally direct variant. It is never left out, never turned into a figure of speech, and never folded into the sign-off.

**On screen.** The narrator is on screen in every scene he voices: the introduction, the takeaways, the verdict and the outro. He is never on screen during the story. While he is on screen, the user overlays his pose image on part of the frame, with the scene's illustration playing in the background. This file only says which pose to use when; it does not change the illustrations.

- **Change pose at each beat** (the introduction beats in scenario guide section 5, each takeaway's claim, evidence and application, the outro steps in section 7), roughly every 15–30 seconds. Never change mid-sentence, and do not repeat the same pose twice in a row.
- **Match the EMOTION to the line.** For example, `fullbody-1.png` or `fullbody-11.png` for the welcome, `fullbody-6.png` or `halfbody-4.png` for the opening hook and its promise, `fullbody-12.png` for signposting the takeaways, `fullbody-13.png` for the personal moment, `fullbody-9.png` for an ironic aside, and `halfbody-14.png` (pointing at the viewer) for the subscribe call.

````markdown
# [Book] — Narrator

The channel narrator for this episode: his lines, the final-scene calls to action, and which pose is on screen during the introduction, takeaways, verdict and outro. Pose images are in the skill's `assets/narrator/` folder.

## Persona and voice
Vlogger touch: [light / medium / high]

[Two or three sentences: the fixed persona, and how he leans into this book's tone, e.g. hushed for a gothic tale, playful for a comedy.]

## Lines
| Line | Text |
| --- | --- |
| Welcome | […] |
| Invitation to the next tale | […] |
| Sign-off | […] |

## Final-scene calls to action
Comments and likes, in this book's imagery:
```text
[creative invitation]
```
Subscribe and bell, direct:
```text
Please subscribe to the channel and click the bell button, so you never miss a new tale.
```

## Links to earlier videos
[None, and why: e.g. "Library empty" or "Only surface overlap with Faust (both have a love story)". Or, per link:]
| Scene | Earlier video | Kind of overlap | Why it fits | Line |
| --- | --- | --- | --- | --- |
| 35 | Faust | Strong echo: a soul traded for desire | Takeaway 3 is about the price of the bargain | "[…]" |

## On screen
| Scene | From (first words) | Pose image | Why this pose |
| --- | --- | --- | --- |
| 01 | "[opening hook…]" | fullbody-6.png | Reflective, sets the puzzle |
| 02 | "[welcome…]" | fullbody-1.png | Welcoming host |
| … | | | |
| [last] | "Please subscribe…" | halfbody-14.png | Addresses the viewer directly |
````

### 7. Write `03-script.md`

The script is turned into speech scene by scene with ElevenLabs (step 12), so the spoken text lives in ```text fences and contains only what should be read aloud. Each fence becomes one audio file, read by the voice on its scene's `Voice:` line. Write story scenes first, then the introduction, then takeaways and outro (scenario guide, step 5), and assemble them in running order.

````markdown
# [Book] — Narration Script

[N] spoken words, about [M] minutes at 140 words per minute. [n] scenes. The NARRATOR voices the introduction, takeaways, verdict and outro; the STORYTELLER voices the story. They can be one voice actor in two registers.

## Voice notes
- `[pause]` ≈ 1 second, `[long pause]` ≈ 2 seconds. The voice generator converts them to the model's pause syntax (`pause_markup` in `voice-config.json`).
- Quotes are read by the voice of the scene they sit in.

### Pronunciation guide
| Word | Say it as | IPA (for Eleven v4) | Note |
| --- | --- | --- | --- |
| Mephistopheles | meh-fis-TOF-uh-leez | /ˌmɛfɪˈstɒfɪliːz/ | English stage pronunciation |

## Introduction

### 01 · [Hook title]
- Image: 01 · Voice: NARRATOR · ~[seconds] s · Hook: [riddle quote / cold image / question / surprising fact / mystery object / bold claim]
```text
[The hook. A quote goes in quotation marks, followed by the author and book.]
[long pause]
[Framing and promise …]
```

## [Part or act title]

### 04 · [Scene title]
- Image: 04 · Voice: STORYTELLER · ~[seconds] s
```text
[Orient. Event. Turn.]
```

## Takeaways and outro
…
````

Writing for the ear:

- Inside the fences, plain sentences only: no markdown, no parentheses, no symbols like `&`, `%`. Spell out abbreviations. The only brackets are the pause markers and the audio tags allowed by `references/elevenlabs-v4.md`. The only slashes are IPA spellings, used only for a name the model has misread.
- Follow `references/spoken-style.md` throughout: no phrase from its section 1, and the patterns in section 2 within their limits, in both voices.
- After the words are written, do the read-aloud pass (`references/spoken-style.md` section 3) over every narrator scene, with that guide's imperfections for the book's vlogger level. Then do the lighter storyteller version (section 5) over the story.
- After the read-aloud pass, do the tagging pass from `references/elevenlabs-v4.md` section 7 over every scene: tags, ellipses, dashes and rare capitals, within that guide's counts for the narrator's vlogger level and for the storyteller. Never change a word while tagging. Skip tags entirely if `voice-config.json` names a model other than Eleven v4 or v3.
- Put every name or foreign word a voice tool might mispronounce in the pronunciation guide.
- Seconds per scene = words ÷ 140 × 60, rounded.
- The narrator's welcome, invitation and sign-off come from `05-narrator.md` and go where the scenario guide places them.
- The outro returns to the opening hook and pays it off (scenario guide section 7). If the hook is a quote, it is credited to the author, never the character, until the story reveals the speaker, and the outro repeats it word for word.
- Links to earlier videos appear only where `05-narrator.md` places them, word for word, and must read as part of the narrator's thought, not as an inserted ad.
- The verdict is its own NARRATOR scene, just before the outro, with a heading that starts with "Verdict:" (for example `### 36 · Verdict: read Part One first`), so `check_book.py` can find it.
- The final scene always ends with, in this order: the creative comments-and-likes invitation, the direct "Please subscribe to the channel and click the bell button" call to action, then the invitation and sign-off, all word for word from `05-narrator.md`.

### 8. Write `04-titles-and-thumbnails.md`

Use the Packaging Sheet template in title-thumbnail-guide.md section 7, with two additions:

- Each thumbnail option has its image prompt in a ```text fence, assembled as in section 3.4 of that guide (master prompt reference + fixed descriptors + thumbnail composition block), and a target file name: `thumbnails/thumb-a.png`, `thumb-b.png`, `thumb-c.png`.
- Chapters are listed with the planned scene each one starts at and an estimated timestamp from the script's word counts, marked "estimated — replace with the edited video's timestamps".

Every title contains the book's title within the first ~40 characters, and no title repeats its paired thumbnail's text.

For every link in `05-narrator.md`, plan the matching card (at the estimated timestamp of that line) or end screen element (for an outro link) in the end screen and cards section, so the viewer can click through at the moment the narrator mentions the video.

### 9. Check

```bash
python <skill-dir>/scripts/check_book.py <book-folder>
```

It reports word counts per voice, estimated runtime, scene and illustration counts, numbering mismatches and missing folders. It also prints style warnings from `references/spoken-style.md`: banned phrases, too many "not X, but Y" or lists of three, and long narrator sentences. Fix what it flags, then go through the checklists in the scenario guide (section 11) and the title-thumbnail guide (section 8), and these cross-file checks:

- every quote has identical wording in the script, the illustration plan and the packaging;
- every character descriptor is identical wherever it is pasted;
- every color named in a prompt exists in the palette;
- no lighting words from visual-style.md section 2.4 slipped into prompts;
- every hook in the packaging is answered in the script;
- the three rituals (scenario guide section 1, "Channel signature") are in place: "Once upon a time…" ends the introduction, the outro asks the closing question, and the final scene has the direct subscribe line. Apart from these, no line's wording, including takeaway signposts, the welcome and the sign-off, matches the same beat in any book in `narration-history.md`;
- every personal line is covered by `narrator-bible.md` or marked `[CONFIRM: …]`; nothing contradicts the bible or its anecdote log, and nothing states or hints at its "Background";
- the spoken text passes the checklist in `references/spoken-style.md` section 7, and every style warning from `check_book.py` was either fixed or is a deliberate choice;
- audio tags, capitals and pauses follow the checklist in `references/elevenlabs-v4.md` section 9, with the narrator's tag count matching the book's vlogger level;
- the narrator's lines and calls to action, including their audio tags, are identical in `03-script.md` and `05-narrator.md`, and every "From" in its on-screen table appears in that scene's spoken text;
- narrator poses are planned for every introduction, takeaway, verdict and outro scene and for no story scene;
- honest asides (at most two) and the verdict follow scenario guide section 7. Their facts about reception, translation and editions come from the research, and any personal judgement is in `narrator-bible.md` or marked `[CONFIRM: …]`;
- every pose image named in `05-narrator.md` exists in `assets/narrator/` and is not marked "do not use yet";
- no intro, takeaway or outro line repeats or closely paraphrases a line in `narration-history.md`; the opening hook type differs from the previous book's, and the outro callback approach differs from the last three books there;
- the opening hook is true to the book, does not spoil the ending, and is paid off in the outro;
- the introduction follows one intro shape (scenario guide section 5), different from the previous book's. It runs about 90 seconds, 200–230 words and never over 240, across 2–3 scenes, with at most one context fact;
- the takeaways follow one takeaway shape (scenario guide section 7), different from the previous book's unless the book clearly needs the same one. The transition says what is coming, every scene has evidence from the story, the last scene carries the deepest meaning, and any takeaway question differs from the outro's closing question;
- every link to an earlier video is a strong echo or a telling contrast, points to a published video in `video-library.md`, sits in a takeaway or the outro, does not spoil that book, reads naturally when the scene is read aloud, and has a matching card or end screen element in the packaging.

### 10. Deliver

Zip the folder so the empty subfolders survive, then send the zip and the five documents:

```bash
python <skill-dir>/scripts/zip_book.py <book-folder>
```

If the user asked for the folder on their computer and it is connected, write it there as well and say where. Keep the reply short: the book folder's name, the totals (scenes, words, minutes), the palette in one line, any assumptions, and facts you could not verify. Mention the links to earlier videos in one line, or that there are none and why, plus any strong match left out because that video is not marked published. List every `[CONFIRM: …]` line with its scene number and ask the user to confirm, rewrite or delete each one. End by saying that once the user approves the script, it will be recorded in `narration-history.md` and `video-library.md` and the speech for each scene will be generated with ElevenLabs. Do not write to either file or generate any speech yet.

### 11. Record the approved narration

Do this only when the user says the script is approved (for example "approved", "final", "record it"), in this conversation or a later one. Never record a draft. If `03-script.md` or `05-narrator.md` still contains `[CONFIRM: …]`, the script is not ready: list those lines and ask the user to settle them first.

1. Read the book's `03-script.md` and `05-narrator.md` from disk again, since the user may have edited them after delivery, and take the lines from those files.
2. Open `<base-dir>/narration-history.md`, or create it with the heading `# Narration history` and the line `Key narrator lines of approved books, oldest first. Read before writing a new book; never reuse these lines.`
3. If the file already has an entry for this book slug, replace it; otherwise append a new entry at the end in this format, quoting each line's words exactly as approved, with audio tags and IPA removed (the history compares wording, not delivery):

```markdown
## [Book] · [book-slug] · approved [YYYY-MM-DD]
- Vlogger touch: [light / medium / high]
- Opening hook: [type, from scenario guide section 4]: "[the hook]"
- Intro shape: [Classic / Straight in / Map first / Hook as context], [n] scenes, [words] words; context fact: [author / origins / none]
- Framing and promise (right after the hook): "[…]"
- Welcome: "[…]"
- Line before "Once upon a time": "[…]"
- Takeaway transition: "[…]"
- Takeaway shape: [Separate lessons / One big idea / One question, several answers / Where it turned / Two sides]
- Takeaways ([count]): [title 1]; [title 2]; …
- Takeaway signposts: "[how each takeaway was opened]"
- Personal moment: [what the narrator admitted, in a few words]
- Honest asides: [kind: "line"; …] or [none]
- Verdict: "[…]"
- Outro callback approach: [which way in, from scenario guide section 7]; lead-in: "[…]"
- Question lead-in and question: "[…]"
- Comments invitation: "[…]"
- Like invitation: "[…]"
- Invitation to the next tale: "[…]"
- Sign-off: "[…]"
- Links to earlier videos: [none] or [book: "line"]
```

4. Open `<base-dir>/video-library.md`, or create it with the heading `# Video library`, the line `The channel's memory: one entry per approved video. Read while planning a new book to find earlier videos worth linking.`, and a `## Theme tags in use` section listing every tag used below. Reuse existing tags where they fit, so overlaps are easy to spot, and add new ones to that list. Then replace or append this book's entry:

```markdown
## [Book] · [book-slug] · [Author]
- Status: approved [YYYY-MM-DD] · not yet published
- Published title: [fill in when published]
- URL: [fill in when published]
- Theme tags: [3–6 tags from the list above]
- Central question: [the outro's reflective question, in plain words]
- Takeaways: [shape]; [one line per takeaway scene: the claim, or the angle it adds to the big idea or question]
- Archetypes and motifs: [e.g. pact with the devil; charming tempter; double life; ruined innocent]
- Spoiler to avoid when linking: [the ending or twist]
- Verdict: [who it is for, in a few words]; edition: [translation or edition recommended]
- Cut from the retelling: [parts left out and offered as a possible video, or none]
- Links to: [earlier videos this one points to, or none]
- Linked from: [later videos that point here; starts empty]
```

5. For each earlier video this book links to, add this book to that entry's "Linked from" line.
6. In `<base-dir>/narrator-bible.md`, add each personal line used in this video to the anecdote log (video, line as approved, kind, date). If the user confirmed a new general fact or opinion while settling `[CONFIRM: …]` lines, add it to "On air" or "Opinions" in their words.
7. Tell the user in one line that the entries were added, and where. Then go straight on to step 12.

### 12. Generate the voice with ElevenLabs

Do this right after step 11, or whenever the user asks to (re)generate speech for an approved book. Never generate speech for a draft: if the script has changed since approval, or was never approved, ask first. Each request costs ElevenLabs credits, roughly one per character.

**Setup (once per machine).** The script runs in the repo's virtual environment, `.venv` at the repo root (gitignored). If it does not exist, create it and install `requirements.txt` (`elevenlabs` and `python-dotenv`):
```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt   # Windows; on macOS/Linux use .venv/bin/python
```
Run `generate_voice.py` with that interpreter, `.venv/Scripts/python` (Windows) or `.venv/bin/python`, in place of `python` in the commands below. The API key lives in the project's `.env` as `ELEVENLABS_API_KEY`; the script loads the nearest `.env` with python-dotenv. If the key is missing or rejected, run `npx -y @elevenlabs/cli@latest onboard init` in the project folder and follow what it prints. Never open, print or ask for the key in chat, and never put it in a file other than `.env`.

1. **Check the voice config.** Read `assets/voice-config.json`. If `model_id` or any voice ID the script uses is still `SET_ME`, stop, tell the user which values are missing, and ask for them (model, a voice for the NARRATOR and one for the STORYTELLER, or one voice for both). Write their answers into the file. Do not pick a model or voice for them.
2. **Dry run.** No API calls. It lists every scene with its voice and character count, the total characters, and any config problems:
   ```bash
   python <skill-dir>/scripts/generate_voice.py <book-folder> --dry-run
   ```
   Fix any scene with no `Voice:` line or no spoken text in `03-script.md` before going on. Scenes with a `[CONFIRM: …]` line are always skipped, so no unconfirmed personal claim is ever voiced.
3. **Generate.** One request per scene. Files go to `voice/NN.mp3`, or the extension of the configured `output_format`, plus `voice/voice-log.json` (voice, model, characters and time per scene). Scenes whose file already exists are skipped, so an interrupted run can simply be restarted:
   ```bash
   python <skill-dir>/scripts/generate_voice.py <book-folder>
   ```
4. **Redo single scenes** after the user edits them or dislikes a take. Use `--force` to overwrite:
   ```bash
   python <skill-dir>/scripts/generate_voice.py <book-folder> --scenes 7,12-14 --force
   ```
5. **Report** in a few lines: how many scenes were generated, total characters, any that failed (with the rerun command), and the folder. Remind the user to listen to the first scenes and to the names in the pronunciation guide. If a name is misread, use its IPA form from the pronunciation guide in that scene's fence (Eleven v4), or a phonetic respelling for other models, and redo only that scene. If a tag is read aloud or produces a sound instead of a delivery, follow `references/elevenlabs-v4.md` section 8.

If the script is edited after generation, regenerate only the scenes whose text changed.

### 13. Mark a video as published

When the user says a video is live, or gives its title or URL, update its `video-library.md` entry: set the status to published with the date, and fill in the published title and URL. Only published videos are linked from new books.

## Production file names

Suggest these when the user asks how to fill the folders, so assets line up with scene numbers:

- `images/NN-short-title.png` (e.g. `images/07-the-earth-spirit.png`), plus `images/anchor.png` and `images/sheet-<character>.png`
- `voice/NN.mp3` (one file per scene, written by step 12) and `voice/voice-log.json`
- `thumbnails/thumb-a.png` … `thumb-c.png`
- `music/` — background tracks with their license notes
- `videos/<book-slug>-final.mp4`, plus Shorts as `videos/short-1.mp4` …

## Worked example

The appendices of all three guides show *Faust*: opening hook (a riddle quote), palette, Faust and Mephistopheles descriptors, 37 scenes, about 3,100 words, and complete packaging. Use it to calibrate depth and tone, not as a template to copy: each book needs its own palette, motifs, hooks and takeaways.
