# Book Video Scenario Guide

A reusable method for producing 20–25 minute book videos for the channel. Each video retells a book as a fairy tale, framed by the channel's narrator, and is illustrated with one image per scene. The method was developed on Goethe's *Faust* and is written so it can be applied to any book, or handed to an AI assistant as instructions.

Each video produces two documents:

1. **Illustration Plan**: a numbered list of scenes, each with a ready-to-paste image prompt.
2. **Narration Script**: the spoken text for every scene, in the same order and numbering.

## Related documents

This guide covers **structure and scenario development only**. All stylistic decisions live in separate documents, which take precedence over anything in this guide where they overlap:

| Document | Contains |
| --- | --- |
| **Narrator.md** | The narrator's appearance, persona, tone of voice, recurring phrases (welcome, invitation, sign-off), reference sheet and rules for which scenes the narrator appears in. |
| **Visual Style.md** | The channel's master style: the master prompt for every image, words and effects that prompts must avoid, and the process for building each book's style sheet. |
| **Book Style Sheet — [Book].md** | One per book, built with the process in Visual Style.md: the book's palette, motifs, and fixed descriptors and reference sheets for its recurring characters. |

Packaging (titles, thumbnails, description, chapters and other promotion) is covered in **Title and Thumbnail Guide.md**.

Wherever this guide says "see Narrator.md", "see Visual Style.md" or "see Book Style Sheet — [Book].md", take the content from that document.

---

## 1. Format at a glance

| Element | Specification |
| --- | --- |
| Runtime | 20–25 minutes (target ~22–23) |
| Script length | 3,000–3,300 words (140 words per minute) |
| Illustrations | 35–40, one roughly every 35–40 seconds |
| Words per scene | 60–100 for story scenes; 80–150 for narrator scenes |
| Voices | **Narrator** (introduction, takeaways, outro) and **storyteller** (the story itself) |
| Order | Strictly chronological within the story, with key quotes placed where they are spoken |
| Structural devices | Opening riddle quote, "Once upon a time" handoff, five takeaways, callback ending |

Timing formula: `illustrations ≈ runtime in seconds ÷ 37`. Words ≈ `runtime in minutes × 140`.

---

## 2. The running order

| # | Block | Voice | Runtime | Scenes | Purpose |
| --- | --- | --- | --- | --- | --- |
| 1 | Opening quote | Narrator | 0:00–0:30 | 1 (shared with title card) | Hook. A line that sounds like a riddle out of context. |
| 2 | Introduction | Narrator | 0:30–2:30 | 3–4 | Welcome, logline, author, origins, structure. Ends with "Once upon a time…" |
| 3 | The story | Storyteller | 2:30–19:00 | 24–28 | The plot in fairy-tale voice, chronologically, with 4–6 key quotes woven in. |
| 4 | Takeaways | Narrator | 19:00–22:30 | 5 | Five lessons, each grounded in the story. |
| 5 | Outro | Narrator | 22:30–23:30 | 1 | Callback to the opening quote, reflective question, call to action, sign-off. |

For a book in two or more parts (or with a clear midpoint), split block 3 into sub-headings (e.g. "Part One: from Heaven to the devil's door", "Part One: the pact and Gretchen", "Part Two: the great world"). Give each part a share of screen time proportional to its importance to a general audience, not its page count. In *Faust*, Part One got ~19 scenes and the much longer Part Two got 8.

---

## 3. Workflow

### Step 1 — Gather the material

Before writing anything, list:

- **Plot beats**: 20–28 moments that carry the story. Each must be visually distinct (a different place, action or character). Merge beats that would produce near-identical images.
- **Key quotes**: 5–7 famous or meaningful lines. For each, record the speaker, the location (part, act/scene, line number), the original-language text, and the English translation used.
- **The opening quote**: one of the key quotes, chosen with the criteria in section 4.
- **Five takeaways**: lessons a modern viewer can apply. Each must be supported by at least one concrete event in the story.
- **Author hook**: one surprising fact about how, when or why the book was written (Goethe: sixty years, from his twenties to months before his death).
- **Origins hook**: what existed before the book and what everyone expected (Faust: the puppet-play legend in which the doctor is always damned), and how the author broke with it.
- **Characters**: the book characters who will appear in several images. Make sure each has fixed descriptors in Book Style Sheet — [Book].md before writing prompts.

### Step 2 — Build the timeline

- Put every plot beat in the order it happens in the book.
- Insert each key quote **at the moment it is spoken**, as its own scene, immediately next to the plot scene it belongs to.
- When a quote is set up early and paid off later (e.g. "Stay, thou art so fair!" is the wager's condition in Part One and Faust's last words in Part Two), place the quote scene at the first occurrence and repeat the line inside the narration of the payoff scene.
- Number scenes 1…N in final running order. Keep the illustration number in brackets beside each scene so the plan and the script can always be matched, e.g. `### 11 · Quote: "Two souls…" [26]`.

### Step 3 — Allocate illustrations

- One illustration per scene. Introduction ≈ 4, story ≈ 24–28, takeaways 5, outro 1.
- If the total exceeds ~40, merge adjacent minor beats. If it falls below ~33, split the densest scenes.
- Optional extra quotes can reuse an existing image with a slow zoom rather than a new illustration.
- Which intro, takeaway and outro scenes show the narrator instead of a book illustration is decided by Narrator.md.

### Step 4 — Write the Illustration Plan

Follow the rules in section 8. Write the overview table first (segments, runtime, counts), then a pointer to the style block in Visual Style.md, then the scenes.

### Step 5 — Write the Narration Script

Write in this order: story scenes first (they set the facts), then the introduction (so it can foreshadow precisely), then takeaways and outro (so they can call back to specific moments). Follow sections 4–7.

### Step 6 — Check and finalise

Run the checklist in section 11. Update the word count and runtime in the script's header.

---

## 4. The opening quote technique

The video opens cold on a quote, spoken by the narrator, before any welcome.

**Choosing the quote.** It should:

- sound like a riddle or paradox out of context ("which always wills the Bad, and always works the Good");
- be spoken by a character whose identity is itself a small reveal;
- be paid off by the story, so the ending can answer it;
- be short enough to read slowly in 10–15 seconds.

**Hiding the speaker.** On screen and in the script, credit the quote to the **author and book**, not the character (e.g. "— Johann Wolfgang von Goethe, *Faust*, Part One"). The character is revealed when the quote recurs in the story.

**The three-step arc:**

1. **Opening (scene 1).** The narrator speaks the quote, pauses, then frames it as a puzzle and makes a promise: by the end, you will know who said it and whether they were telling the truth.
2. **Recurrence (story scene).** The quote appears where it is spoken, as its own scene. The viewer now hears it in context.
3. **Callback (outro).** The narrator repeats the quote word for word, names the speaker, and answers the promise ("The devil was telling the truth after all").

---

## 5. The narrator introduction

The introduction is the narrator speaking directly to the viewer. It runs 400–500 words across 4 scenes. The narrator's persona, tone and recurring phrases come from Narrator.md; this section defines only the beats and their order.

| Beat | Content | Example (Faust) |
| --- | --- | --- |
| a. Quote | The opening quote, then *(pause)*. | "Part of that Power, not understood…" |
| b. Riddle and promise | Comment on why the line is strange; tell the viewer to remember it; promise the answer by the end. | "A strange thing to say about yourself, isn't it?… by the end you'll know who he was, and whether he was telling the truth." |
| c. Welcome and logline | The narrator's welcome (see Narrator.md), then the protagonist's lack + the temptation or inciting offer + the title. | "Tonight's story is about a man who knew everything written in books and still felt he knew nothing at all… This is the tale of Doctor Faust." |
| d. Author hook | One surprising fact that makes the author human and the book special. | "He spent almost his whole life telling it… Sixty years." |
| e. Origins and expectation | What the story or genre was before, what everyone expected, and the line "X dared to change it." | "Every audience knew how this story ended. Goethe was the one who dared to change it." |
| f. Structure map | How the book is built, described as a journey; invite the viewer along. | "One long road… and tonight we will walk beside him." |
| g. Handoff | Switch into the storyteller voice. | "So let us begin, the way all good tales do. Once upon a time…" |

Writing rules:

- Speak to "you"; use "we" for the shared journey ("what we will discover together").
- Use one or two rhetorical questions, never more.
- Each scene ends on a turn or open question that pulls into the next.
- Do not summarise the plot. Tease the central conflict only.

---

## 6. The story narration (fairy-tale voice)

**Voice.** Third person, past tense, the cadence of a told tale. Plain words, concrete images, short-to-medium sentences with occasional longer, rolling ones. No modern slang, no academic vocabulary, no critical commentary inside the story; interpretation belongs to the takeaways.

**Each scene passage (60–100 words):**

1. **Orient**: where and when ("That night…", "Far below, in a cramped Gothic room…", "Years passed.").
2. **Event**: one clear action or change.
3. **Turn**: end on a consequence, decision or ominous detail that pulls forward ("Faust chose to live.", "and the trap was set.").

**Cast.** Name only the characters the viewer must track. Introduce each with a single defining trait ("the soldier Valentin", "the airy spirit Ariel"). Refer to minor figures by role.

**Unfamiliar ideas.** Explain them inside the sentence, in a clause, never in a separate aside ("Homunculus, a bright little spirit without a body").

**Dark material.** State tragedies plainly and briefly, without graphic detail ("lost in grief and madness, she had drowned their baby"). The fairy-tale voice should make hard events bearable, not hide them.

**Compression.** Large sections of a book can become one scene if their meaning is kept. In *Faust*, the five acts of Part Two became eight scenes.

**Quote scenes** follow a fixed pattern:

1. One sentence of setup (who is speaking, to whom, in what mood).
2. The quote, in quotation marks.
3. One or two sentences restating its meaning in plain language.
4. One sentence linking it to the character or the larger story ("That single line held the whole of Faust's character.").

**Motifs.** Repeat a few images throughout (in *Faust*: the study, the candle, light from above, the road) so the introduction, story and outro feel like one piece.

---

## 7. Takeaways and outro

### Takeaways (5 scenes, ~80–100 words each)

- **Transition** (start of the first takeaway): a pause, then a line that turns from story to meaning ("And there our tale ends. *(pause)* … let me leave five things in your hands.").
- **Numbered openers**: "The first:", "The second:", … "And the fifth:". This gives the viewer a clear map.
- **Each takeaway**: claim in one sentence → evidence from one or two specific events or characters → a universal application to the viewer's life.
- **Callbacks**: reuse earlier quotes inside takeaways where they fit, and point out a surprising detail ("And notice who gave that advice to the young student: the devil himself.").
- **One personal moment**: once per video, the narrator admits sharing the feeling being discussed.
- **The fifth takeaway** is the book's deepest or most surprising meaning, and connects to how the author changed the expected ending (the origins hook from the introduction).

Typical takeaway types to draw from: the central virtue or drive; the cost to others; the gap between knowledge and life; the divided self; the role of grace, chance or love; the danger of a specific temptation; what the ending reveals.

### Outro (1 scene, ~130–150 words)

1. **Callback**: "Do you remember the words we began with?" + the opening quote word for word.
2. **Reveal**: name the speaker.
3. **Answer**: resolve the promise from the introduction in one or two sentences.
4. *(pause)*
5. **Reflective question** for the viewer, drawn from the book's central dilemma ("what would you give to feel that your life was truly complete?").
6. **Call to action**: invite comments.
7. **Invitation and sign-off**: the narrator's recurring invitation to the next tale and signature sign-off, word for word from Narrator.md.

---

## 8. Illustration Plan rules

### Document structure

1. **Overview**: total count, pacing, and a table of segments (runtime, illustration count, numbers).
2. **Style**: a one-line note that the style block from Visual Style.md is appended to every prompt.
3. **Scenes**, grouped by block, each as a numbered entry.

### Entry format

```
NN — Short title. [Setting]. [Characters, using fixed descriptors]. [Action]. [Key props]. [Emotion]. [Composition note, if any].
```

Example:

> **06 — Faust in despair.** An aging scholar in a long robe sits slumped at a cluttered desk in a vaulted Gothic study at night. Shelves of dusty books, a human skull, glass flasks, brass astronomical instruments. His face shows exhaustion and frustration.

### Content rules

- Describe **content only**: setting, characters, action, props, emotion, composition. Everything about the look of the image comes from Visual Style.md.
- Check each description against Visual Style.md and avoid any words or effects it rules out.
- For recurring characters, paste their fixed descriptors from Book Style Sheet — [Book].md every time they appear. Name famous people only where the image needs it (the author portrait).
- Narrator scenes follow Narrator.md.
- One clear moment per image. Avoid "and then" sequences; if two moments are essential, compose them as two planes or a split frame and say so.
- Recurring locations reuse the same description so they look like the same place (the Gothic study in images 06, 07, 10 and 37).
- **Story scenes** are literal depictions of the moment.
- **Quote scenes** are **symbolic**, never a repeat of a plot image: a visual metaphor for the line (two figures pulling in opposite directions for "two souls", a gray library split by a green tree for "gray are all theories"). Leave open space for the quote as a text overlay; state where ("open sky at the top of the frame").
- **Takeaway scenes** are modern, universal metaphors (a climber, a tower beside a small cottage, a mirror, two hands reaching).
- **Book-ends**: the first and last images mirror each other (the scholar's study at night → the same study, empty, at dawn).
- Never ask the image to render text. Titles and quotes are overlays added in editing.
- Avoid copyrighted characters, identifiable modern people and existing artworks.

---

## 9. Quotes and translations

- Use a **public-domain translation** (published before 1929) or your own literal translation of the original. For *Faust*, the Bayard Taylor translation (1870) was used, with some lines rendered literally.
- Use the same English wording everywhere the quote appears: illustration plan, script, opening, callback.
- In the Illustration Plan, record for each quote: English text, original text in italics, speaker, and location (part, scene, line), e.g.:
  `"Two souls, alas! reside within my breast." (Zwei Seelen wohnen, ach! in meiner Brust, Part One, "Outside the City Gate", line 1112.)`
- Hide the speaker of the opening quote (credit the author) until it recurs in the story.

---

## 10. Templates

### Narration Script skeleton

```markdown
# [Book] Video — Narration Script

The script tells [Book] as a fairy tale, one passage per scene in timeline order, about [N] words. At 140 words per minute it runs about [M] minutes. The introduction and the takeaways are spoken by the channel's narrator; the story in between is told in the fairy-tale voice. Bracketed numbers match the illustrations in the Illustration Plan.

## Introduction (narrator)

*Spoken by the narrator. Scene numbers mark where each illustration cuts in.*

### 1 · Opening quote and title card [01]

"[Opening quote]"

*(pause)*

[Riddle and promise.]

[Narrator's welcome, from Narrator.md.] [Logline.] This is the tale of [title/protagonist].

### 2 · [Author hook] [02]
### 3 · [Origins and expectation] [03]
### 4 · [Structure map] [04]

[Structure.] So let us begin, the way all good tales do. Once upon a time…

## [Part / Act title]

### 5 · [Scene title] [05]
[Orient. Event. Turn.]

### N · Quote: "[quote]" [NN]
[Setup. "Quote." Plain meaning. Link to character.]

## Takeaways and outro (narrator)

*Spoken by the narrator, returning after the story ends.*

### [n] · [Takeaway 1] [..]
And there our tale ends. *(pause)* … let me leave five things in your hands.
The first: [claim]. [Evidence]. [Application].

### [n+1…n+4] · [Takeaways 2–5]
The second: … / The third: … / The fourth: … / And the fifth: …

### [last] · Outro: [closing image] [..]
Do you remember the words we began with? "[Opening quote]" Now you know who spoke them: [speaker]. [Answer to the promise.]

*(pause)*

So here is a question to take with you tonight: [question]? [Comment invitation.] [Narrator's invitation and sign-off, from Narrator.md.]
```

### Illustration Plan skeleton

```markdown
# [Book] Video — Illustration Plan

## Overview
The video needs **[N] illustrations**, one roughly every 35–40 seconds across a ~[M]-minute runtime.

| Segment | Runtime | Illustrations | Numbers |
| --- | --- | --- | --- |
| 1. Introduction | … | … | … |
| … | … | … | … |
| **Total** | … | **[N]** | |

Each description below is written to paste directly as a prompt. Append the style block from Visual Style.md to every prompt, and the fixed descriptors from Book Style Sheet — [Book].md wherever a recurring character appears. Quote illustrations leave open space for the quote as a text overlay.

## Segment 1: Introduction
1. **01 — [Title].** [Description.]
…
```

---

## 11. Quality checklist

**Structure and timing**

- [ ] Total words 3,000–3,300; runtime 20–25 minutes at 140 wpm.
- [ ] 35–40 illustrations; every scene in the script has exactly one matching illustration number.
- [ ] Story scenes are in the book's chronological order; each quote sits where it is spoken.

**Narration**

- [ ] The script opens with the quote, credited to the author, not the character.
- [ ] The introduction contains: riddle and promise, welcome and logline, author hook, origins and "dared to change it", structure map, "Once upon a time…"
- [ ] Every story scene orients, shows one event, and ends on a turn.
- [ ] Every quote scene: setup → quote → plain meaning → link.
- [ ] Exactly five takeaways, each with evidence from the story; one personal moment from the narrator.
- [ ] The outro repeats the opening quote word for word, reveals the speaker and answers the promise.
- [ ] The narrator's welcome, invitation and sign-off match Narrator.md.
- [ ] Facts, names, dates and line references checked against the source.

**Illustrations**

- [ ] Prompts describe content only; the style block from Visual Style.md is appended to each.
- [ ] No descriptions conflict with Visual Style.md.
- [ ] Recurring characters use their fixed descriptors from Book Style Sheet — [Book].md; narrator scenes follow Narrator.md.
- [ ] Recurring locations use identical descriptions.
- [ ] Quote and takeaway images are symbolic and leave space for text.
- [ ] First and last images mirror each other.
- [ ] No text rendered inside images; no copyrighted characters or real modern people.

---

## Appendix: Faust as the worked example

| Element | Faust |
| --- | --- |
| Opening quote | "Part of that Power, not understood, which always wills the Bad, and always works the Good." (Mephistopheles, credited to Goethe) |
| Author hook | Written over sixty years, from Goethe's twenties to months before his death in 1832 |
| Origins hook | The puppet-play legend in which the doctor is always dragged to hell; Goethe dared to save him |
| Structure map | Part One: a story of the heart. Part Two: a story of the world. "One long road." |
| Story scenes | 27 (19 from Part One including 6 quote scenes, 8 from Part Two) |
| Key quotes | "Man errs, as long as he doth strive." · "Two souls, alas!…" · "In the beginning was the Deed." · "Part of that Power…" · "Stay, thou art so fair!" · "Gray are all theories…" · "The Eternal-Feminine draws us on." (closing line, inside the last story scene) |
| Takeaways | Striving is the point · Ambition has victims · Knowledge is not living · We are divided · Grace meets effort |
| Reflective question | "What would you give to feel that your life was truly complete?" |
| Book-end images | Scholar in the Gothic study at night → the same study, empty, at dawn |
| Totals | 37 illustrations · ~3,100 words · ~22 minutes |
