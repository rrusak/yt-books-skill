---
name: book-video-production
description: Produce the complete production package for a 20–25 minute YouTube book video told as a fairy tale in the channel's naïve colored-pencil style — a book folder with the color palette, character and scene image prompts, the narration script for voice generation, and title/thumbnail options, plus empty images/, voice/, thumbnails/, music/ and videos/ folders. Use this whenever the user names a book (novel, play, epic, classic) and asks for a video, episode, script, storyboard, illustration prompts, palette, voiceover text, thumbnails or titles for it, or says things like "do the next book", "let's make [book]", "prepare [book] for the channel", even if they ask for only part of the package.
---

# Book Video Production

This skill turns one book into a ready-to-produce video package for the channel. The channel retells books as fairy tales: a narrator opens with a riddle-like quote, a storyteller tells the plot scene by scene, the narrator returns with five takeaways and closes by answering the riddle. Every scene has one illustration in a fixed colored-pencil style, and each book gets its own palette and character designs.

Three guides in `references/` hold the method. This file says how to run it and what to output.

## What you produce

One folder per book, named with a lowercase kebab-case slug of the title (`faust`, `the-great-gatsby`, `crime-and-punishment`):

```
<book-slug>/
├── 01-palette.md                  # world, color palette, motifs, prompt lines
├── 02-illustrations.md            # master prompt, characters, scene prompts
├── 03-script.md                   # narration script for voice generation
├── 04-titles-and-thumbnails.md    # titles, thumbnails, description, promotion
├── images/                        # empty
├── voice/                         # empty
├── thumbnails/                    # empty
├── music/                         # empty
└── videos/                        # empty
```

The four main documents sit in the root of the book folder. The five subfolders are created empty; the user fills them during production.

The guides were written with their own document names. They map onto these files as follows:

| The guides call it | In this package |
| --- | --- |
| Book Style Sheet — [Book].md: world, palette, motifs | `01-palette.md` |
| Book Style Sheet — [Book].md: characters; Illustration Plan | `02-illustrations.md` |
| Narration Script | `03-script.md` |
| Packaging Sheet | `04-titles-and-thumbnails.md` |

## Reference files

Read each guide in full before the step that needs it. They are the source of truth; this file only adds output formats and workflow.

- `references/scenario-guide.md` — structure, running order, opening-quote technique, narrator introduction beats, fairy-tale voice, quote scenes, takeaways, outro, illustration content rules. Read before planning (step 3).
- `references/visual-style.md` — channel constants, the master style prompt, flat equivalents for lighting words, palette structure, and the process for building a book's palette and characters. Read before writing `01-palette.md`.
- `references/title-thumbnail-guide.md` — hooks, three thumbnail types, title formulas, description, chapters, tags, Shorts. Read before writing `04-titles-and-thumbnails.md`.
- `assets/gothic_bargain_at_midnight.png` — the channel's technique reference image (from *Faust*). Look at it once so your scene descriptions match what the style can draw. The user attaches it in the image generator; it is not copied into the book folder.

## Channel documents that are not in this skill

Some decisions live in separate channel documents the user keeps:

- **Narrator.md**: the narrator's persona, appearance, welcome line, invitation to the next tale, sign-off, and which scenes show the narrator instead of a book illustration.
- **Thumbnail typography**: typeface and text treatment for thumbnail text.

If the user has attached these, or they are in the project or a connected folder, use them. If not, do not invent them. Write placeholders exactly as `{{NARRATOR_WELCOME}}` and `{{NARRATOR_INVITATION_AND_SIGNOFF}}` in the script, give every scene a book illustration, and mention the placeholders in your final reply. The narrator is a recurring channel character, so inventing a persona or look would create an inconsistency the user has to undo.

If the user supplies an existing palette, character designs or anchor image for the book, build on those instead of designing new ones.

## Inputs

- **Required:** the book. Identify the exact work and author.
- **Optional:** target runtime (default ~22 minutes), video language (default English; write all four files in that language), preferred translation, which characters matter most to them.

Ask a question only if the book is genuinely ambiguous (two well-known works share the title) or the user's request contradicts the format. Otherwise start, and state any assumption at the top of your reply.

## Workflow

Set up a task list with these steps, since the package takes a while and the user may step away.

### 1. Create the folder

```bash
python <skill-dir>/scripts/init_book_folder.py <book-slug> <base-dir>
```

`<base-dir>` is the working directory, or the user's connected folder if they asked for the package to go there.

### 2. Research the book

Verify facts before writing; the script is published under the channel's name, and wrong line numbers or misattributed quotes undermine it. Use web search and fetch for:

- the plot sequence and what happens in each beat, including the ending;
- character names, relationships and appearance cues given in the text;
- the author hook (how, when or why the book was written) and the origins hook (what came before and what the author changed);
- each key quote: exact wording in a public-domain English translation (published before 1929) or your own literal translation, the original-language text, speaker, and location (part, act/chapter/scene, line where the work has line numbers).

If you cannot confirm a line number, give the scene or chapter only. Keep the sources; they go at the end of `01-palette.md`.

### 3. Plan

Follow `references/scenario-guide.md` steps 1–3: plot beats, 5–7 key quotes, the opening quote (riddle-like, speaker hidden, paid off by the story), five takeaways, author and origins hooks, recurring characters, the chronological timeline with quote scenes placed where they are spoken, and 35–40 scenes.

Use **one numbering for everything**: scene 07 in the script is image 07 in the plan, `07-*.png` in `images/` and `07.*` in `voice/`. The Faust guide shows illustration numbers in brackets because that project was renumbered later; new books do not need brackets.

Also pick the three hooks for packaging now (title-thumbnail guide, section 2), so the script and the packaging promise the same things.

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
[Fixed descriptors of characters present, word for word.] [Scene: setting, action, props, emotion, composition, open area for text if needed.] Match the attached references' drawing technique, texture, palette and character designs, not their composition.
```

### NN · Quote: "[short form]"
- Block: Story · Type: quote · Characters: …
- Quote: "[English]" — *[original]* — [speaker], [location]
```text
[Symbolic image with open space for the quote overlay, and where]
```
````

Rules that matter most, all from the guides:

- **Types:** `frame` (introduction), `story` (literal moment), `quote` (symbolic metaphor, never a repeat of a plot image, open space for text), `takeaway` (modern universal metaphor), `outro` (mirrors scene 01).
- **Flat language:** never write shadow, glow, beam, radiant, misty, blurred, smoke billows. Use the flat equivalents in visual-style.md section 2.4. The Faust plan broke this rule and its prompts fought the style.
- **Character consistency:** paste the fixed descriptor every time a recurring character appears, even if it feels repetitive; the image model has no memory of the previous prompt's wording. Give each age or costume variant its own descriptor.
- **No text in images**, no copyrighted characters, no identifiable modern people, nothing graphic (show tragedy at the moment before or after, or symbolically).
- **Narrator scenes:** only if Narrator.md says which scenes show the narrator. Mark them `Type: narrator` and take the description from Narrator.md.

### 6. Write `03-script.md`

The script is pasted into a text-to-speech tool scene by scene, so the spoken text lives in ```text fences and contains only what should be read aloud. Write story scenes first, then the introduction, then takeaways and outro (scenario guide, step 5), and assemble them in running order.

````markdown
# [Book] — Narration Script

[N] spoken words, about [M] minutes at 140 words per minute. [n] scenes. The NARRATOR voices the introduction, takeaways and outro; the STORYTELLER voices the story. They can be one voice actor in two registers.

## Voice notes
- `[pause]` ≈ 1 second, `[long pause]` ≈ 2 seconds. Convert to your voice tool's syntax (for example a break tag) or cut the audio there.
- Quotes are read by the voice of the scene they sit in.

### Pronunciation guide
| Word | Say it as | Note |
| --- | --- | --- |
| Mephistopheles | meh-fis-TOF-uh-leez | English stage pronunciation |

## Introduction

### 01 · Opening quote and title card
- Image: 01 · Voice: NARRATOR · ~[seconds] s
```text
"[Opening quote.]"
[long pause]
[Riddle and promise …]
```

## [Part or act title]

### 05 · [Scene title]
- Image: 05 · Voice: STORYTELLER · ~[seconds] s
```text
[Orient. Event. Turn.]
```

## Takeaways and outro
…
````

Writing for the ear:

- Inside the fences, plain sentences only: no markdown, no brackets except pause markers, no parentheses, no symbols like `&`, `%`, `/`. Spell out abbreviations.
- Put every name or foreign word a voice tool might mispronounce in the pronunciation guide.
- Seconds per scene = words ÷ 140 × 60, rounded.
- Narrator placeholders `{{NARRATOR_WELCOME}}` and `{{NARRATOR_INVITATION_AND_SIGNOFF}}` go inside the fences where the scenario guide puts those lines, if Narrator.md is not available.
- The opening quote is credited to the author, never the character, until the story reveals the speaker. The outro repeats it word for word.

### 7. Write `04-titles-and-thumbnails.md`

Use the Packaging Sheet template in title-thumbnail-guide.md section 7, with two additions:

- Each thumbnail option has its image prompt in a ```text fence, assembled as in section 3.4 of that guide (master prompt reference + fixed descriptors + thumbnail composition block), and a target file name: `thumbnails/thumb-a.png`, `thumb-b.png`, `thumb-c.png`.
- Chapters are listed with the planned scene each one starts at and an estimated timestamp from the script's word counts, marked "estimated — replace with the edited video's timestamps".

Every title contains the book's title within the first ~40 characters, and no title repeats its paired thumbnail's text.

### 8. Check

```bash
python <skill-dir>/scripts/check_book.py <book-folder>
```

It reports word counts per voice, estimated runtime, scene and illustration counts, numbering mismatches and missing folders. Fix what it flags, then go through the checklists in the scenario guide (section 11) and the title-thumbnail guide (section 8), and these cross-file checks:

- every quote has identical wording in the script, the illustration plan and the packaging;
- every character descriptor is identical wherever it is pasted;
- every color named in a prompt exists in the palette;
- no lighting words from visual-style.md section 2.4 slipped into prompts;
- every hook in the packaging is answered in the script.

### 9. Deliver

Zip the folder so the empty subfolders survive, then send the zip and the four documents:

```bash
python <skill-dir>/scripts/zip_book.py <book-folder>
```

If the user asked for the folder on their computer and it is connected, write it there as well and say where. Keep the reply short: the book folder's name, the totals (scenes, words, minutes), the palette in one line, any assumptions, any placeholders waiting for Narrator.md, and facts you could not verify.

## Production file names

Suggest these when the user asks how to fill the folders, so assets line up with scene numbers:

- `images/NN-short-title.png` (e.g. `images/07-the-earth-spirit.png`), plus `images/anchor.png` and `images/sheet-<character>.png`
- `voice/NN.mp3` (one file per scene)
- `thumbnails/thumb-a.png` … `thumb-c.png`
- `music/` — background tracks with their license notes
- `videos/<book-slug>-final.mp4`, plus Shorts as `videos/short-1.mp4` …

## Worked example

The appendices of all three guides show *Faust*: opening quote, palette, Faust and Mephistopheles descriptors, 37 scenes, about 3,100 words, and complete packaging. Use it to calibrate depth and tone, not as a template to copy: each book needs its own palette, motifs, hooks and takeaways.
