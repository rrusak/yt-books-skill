# Book Video Scenario Guide

A reusable method for producing 20–25 minute book videos for the channel. Each video retells a book as a fairy tale, framed by the channel's narrator, and is illustrated with one image per scene. The method was developed on Goethe's *Faust* and is written so it can be applied to any book, or handed to an AI assistant as instructions.

Each video produces two documents:

1. **Illustration Plan**: a numbered list of scenes, each with a ready-to-paste image prompt.
2. **Narration Script**: the spoken text for every scene, in the same order and numbering.

## Related documents

This guide covers **structure and scenario development only**. All stylistic decisions live in separate documents, which take precedence over anything in this guide where they overlap:

| Document | Contains |
| --- | --- |
| **Narrator.md** | Written for each book (`05-narrator.md` in the book folder). The narrator's persona and tone, his welcome, invitation and sign-off, the final-scene calls to action, and which pose is on screen during the introduction and outro. |
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
| Structural devices | Opening hook (a riddle quote or another type, varied between books), "Once upon a time" handoff, 2–5 takeaways, callback ending |

Timing formula: `illustrations ≈ runtime in seconds ÷ 37`. Words ≈ `runtime in minutes × 140`.

---

## 2. The running order

| # | Block | Voice | Runtime | Scenes | Purpose |
| --- | --- | --- | --- | --- | --- |
| 1 | Opening hook | Narrator | 0:00–0:30 | 1 | A riddle quote, cold image, question, surprising fact, mystery object or bold claim that raises one question the video answers (section 4). |
| 2 | Introduction | Narrator | 0:30–2:30 | 3–4 | Welcome, logline, author, origins, structure. Ends with "Once upon a time…" |
| 3 | The story | Storyteller | 2:30–19:00 or later | 24–31 | The plot in fairy-tale voice, chronologically, with 4–6 key quotes woven in. |
| 4 | Takeaways | Narrator | 19:00–22:30 or shorter | 2–5 | Two to five lessons, each grounded in the story. Fewer takeaways leave more time for the story. |
| 5 | Outro | Narrator | 22:30–23:30 | 1 | Callback to the opening hook, reflective question, call to action, sign-off. |

For a book in two or more parts (or with a clear midpoint), split block 3 into sub-headings (e.g. "Part One: from Heaven to the devil's door", "Part One: the pact and Gretchen", "Part Two: the great world"). Give each part a share of screen time proportional to its importance to a general audience, not its page count. In *Faust*, Part One got ~19 scenes and the much longer Part Two got 8.

---

## 3. Workflow

### Step 1 — Gather the material

Before writing anything, list:

- **Plot beats**: 20–28 moments that carry the story. Each must be visually distinct (a different place, action or character). Merge beats that would produce near-identical images.
- **Key quotes**: 5–7 famous or meaningful lines. For each, record the speaker, the location (part, act/scene, line number), the original-language text, and the English translation used.
- **The opening hook**: its type and wording, chosen with section 4 and of a different type from the previous book. If it is a quote, it is one of the key quotes.
- **Takeaways, 2–5**: lessons a modern viewer can apply. Each must be supported by at least one concrete event in the story. Choose the number from the book: a tight fable may carry two strong lessons, a sprawling epic five. Never pad with a weak or repeated lesson to reach a number; give the time it frees to the story.
- **Author hook**: one surprising fact about how, when or why the book was written (Goethe: sixty years, from his twenties to months before his death).
- **Origins hook**: what existed before the book and what everyone expected (Faust: the puppet-play legend in which the doctor is always damned), and how the author broke with it.
- **Characters**: the book characters who will appear in several images. Make sure each has fixed descriptors in Book Style Sheet — [Book].md before writing prompts.

### Step 2 — Build the timeline

- Put every plot beat in the order it happens in the book.
- Insert each key quote **at the moment it is spoken**, as its own scene, immediately next to the plot scene it belongs to.
- When a quote is set up early and paid off later (e.g. "Stay, thou art so fair!" is the wager's condition in Part One and Faust's last words in Part Two), place the quote scene at the first occurrence and repeat the line inside the narration of the payoff scene.
- Number scenes 1…N in final running order. Keep the illustration number in brackets beside each scene so the plan and the script can always be matched, e.g. `### 11 · Quote: "Two souls…" [26]`.

### Step 3 — Allocate illustrations

- One illustration per scene. Introduction ≈ 4, story ≈ 24–31 (more when there are fewer takeaways), takeaways 2–5, outro 1.
- If the total exceeds ~40, merge adjacent minor beats. If it falls below ~33, split the densest scenes.
- Optional extra quotes can reuse an existing image with a slow zoom rather than a new illustration.
- Every scene gets a full book illustration. The narrator is on screen in the introduction, takeaways and outro as an overlay the user adds in editing, with the illustration behind him; Narrator.md plans his poses. In the story he is heard, not seen.

### Step 4 — Write the Illustration Plan

Follow the rules in section 8. Write the overview table first (segments, runtime, counts), then a pointer to the style block in Visual Style.md, then the scenes.

### Step 5 — Write the Narration Script

Write in this order: story scenes first (they set the facts), then the introduction (so it can foreshadow precisely), then takeaways and outro (so they can call back to specific moments). Follow sections 4–7.

### Step 6 — Check and finalise

Run the checklist in section 11. Update the word count and runtime in the script's header.

---

## 4. The opening hook

The video opens cold on a hook, spoken by the narrator, before any welcome. These first 10–30 seconds decide whether a viewer stays, so the hook raises one question that the video answers by the end. A riddle-like quote is one way to do it, not the only one. Choose the type that suits the book, and vary it between books.

**Hook types.**

| Type | The narrator opens with | The outro pays it off by | Example |
| --- | --- | --- | --- |
| **Riddle quote** | A line from the book that sounds like a riddle or paradox out of context, speaker hidden | Repeating the quote word for word, naming the speaker, answering the riddle | *Faust*: "Part of that Power, not understood, which always wills the Bad, and always works the Good." |
| **Cold image** | One vivid moment from the story, told in two or three sentences without context | Returning to that moment, now that the viewer understands it | *Dorian Gray*: a man climbs to the top of his own house at night, unlocks a door no one else may open, and lifts a cloth from a painting |
| **Question to the viewer** | A personal "what would you do" dilemma the book turns on | Asking it again, now that the viewer has seen what the hero chose | "If you could stay exactly as you are tonight, forever, what would you be willing to give up?" |
| **Surprising fact** | A true fact about the book, its author or its afterlife that sounds impossible | Explaining what the fact meant, once the story is known | *Dorian Gray*: this novel was once read aloud in a courtroom, as evidence against the man who wrote it |
| **Mystery object** | One object, place or rule at the heart of the story, presented as a puzzle | Revealing what it was, or what it cost | "There's a painting in this story that no one is allowed to see. Not even the man in it, most days." |
| **Bold claim** | A belief held by a character, stated as if it were true, for the viewer to test | Judging the claim with the whole story in view | "Beauty is the only thing worth having. One man in this story believed that completely." |

The examples show the shape of each type only; write every hook fresh from the book.

**Every hook must:**

- raise one clear question that the outro answers: who said it, what it meant, what it cost, or what you would choose;
- come from the book and be true. Never invent a fact or a scene;
- not spoil the ending. A cold image or mystery object from late in the story is fine only if it hides what it means;
- run 10–30 seconds with its framing, about 25–70 words;
- lead toward the book's central question, so the outro's reflective question grows out of it.

**Choosing the type.** Start from the strongest material gathered in step 1:

- a famous line that sounds like a paradox suggests a riddle quote;
- a single striking picture suggests a cold image;
- a dilemma everyone has felt suggests a question to the viewer;
- a strange true story about the book suggests a surprising fact;
- a central object such as a portrait, ring, letter or locked door suggests a mystery object;
- a seductive but wrong idea suggests a bold claim.

Read `narration-history.md` (the "Opening hook" line of each book). Do not use the same type as the previous book. When two types fit equally well, take the one used least recently. If the hook is a surprising fact, the author hook (section 5, beat d) uses a different fact.

**Framing and promise.** After the hook and a pause, the narrator says in a sentence or two why it is strange or worth keeping in mind, and promises the answer by the end. Write the framing fresh for each book. Do not reuse a framing from the narration history.

**The three-step arc**, for every type:

1. **Plant (scene 1).** The hook, a pause, then the framing and promise.
2. **Recurrence (story).** The story reaches the hook: the quote is spoken in its own quote scene, the cold image happens, the object appears, or the hero faces the question or acts on the claim. A surprising fact about the book has no recurrence; it goes straight from plant to callback.
3. **Callback (outro).** The narrator returns to the hook and answers the promise (section 7, outro).

Scene 01's illustration shows the hook when it can be drawn: the moment of a cold image, the mystery object, or a symbol for a question, fact or claim. Follow the illustration rules in section 8.

**When the hook is a quote.** The quote should:

- sound like a riddle or paradox out of context ("which always wills the Bad, and always works the Good");
- be spoken by a character whose identity is itself a small reveal;
- be paid off by the story, so the ending can answer it;
- be short enough to read slowly in 10–15 seconds.

On screen and in the script, credit the quote to the **author and book**, not the character (e.g. "— Johann Wolfgang von Goethe, *Faust*, Part One"). The character is revealed when the quote recurs in the story. The outro repeats it word for word, names the speaker and answers the riddle ("The devil was telling the truth after all").

---

## 5. The narrator introduction

The introduction is the narrator speaking directly to the viewer. It runs 400–500 words across 4 scenes. The narrator's persona, tone and welcome come from Narrator.md; this section defines only the beats and their order.

| Beat | Content | Example (Faust) |
| --- | --- | --- |
| a. Hook | The opening hook (section 4), then *(pause)*. | "Part of that Power, not understood…" |
| b. Framing and promise | Say why the hook is strange or worth keeping in mind; ask the viewer to hold on to it; promise the answer by the end. | "A strange thing to say about yourself, isn't it?… by the end you'll know who he was, and whether he was telling the truth." |
| c. Welcome and logline | The narrator's welcome (see Narrator.md), then the protagonist's lack + the temptation or inciting offer + the title. | "Tonight's story is about a man who knew everything written in books and still felt he knew nothing at all… This is the tale of Doctor Faust." |
| d. Author hook | One surprising fact that makes the author human and the book special. | "He spent almost his whole life telling it… Sixty years." |
| e. Origins and expectation | What the story or genre was before, what everyone expected, and the line "X dared to change it." | "Every audience knew how this story ended. Goethe was the one who dared to change it." |
| f. Structure map | How the book is built, described as a journey; invite the viewer along. | "One long road… and tonight we will walk beside him." |
| g. Handoff | Switch into the storyteller voice. | "So let us begin, the way all good tales do. Once upon a time…" |

Writing rules:

- Speak to "you"; use "we" for the shared journey ("what we will discover together").
- Use one or two rhetorical questions, never more (a few more are allowed at the medium and high vlogger touch, below).
- Each scene ends on a turn or open question that pulls into the next.
- Do not summarise the plot. Tease the central conflict only.

### Vlogger touch

The narrator speaks to camera like a real person, a YouTube host rather than a reciting voice. How strongly is set per book with one of three levels; the default is **light**. The level applies to everything the narrator says (introduction, takeaways, outro) and never to the storyteller: the story stays in the fairy-tale voice of section 6 at every level. At every level the facts, beats and word counts stay the same, the subscribe line stays word for word, and there is no slang, no profanity and no hype ("smash that like button", "you won't believe what happens next").

| Level | What it sounds like |
| --- | --- |
| **Light** (default) | The current narrator, spoken rather than recited. Contractions throughout ("you'll", "wasn't"). A few spoken openers ("Okay", "So", "Now"). One or two short personal asides per block ("And I'll be honest, that bit hit close to home"). At most one light joke in the introduction and one in the outro. A casual welcome and goodbye ("Hi, and welcome back", "take care"). The fairy-tale warmth and cadence stay in front. |
| **Medium** | Clearly a host talking to you. Everything in light, plus: a personal aside or reaction in most narrator scenes, short fragments for rhythm ("Rich. Charming. Barely more than a boy."), two or three light jokes across the narrator blocks, a few direct check-ins with the viewer ("be honest", "you know the type"), and modern everyday comparisons in the takeaways. Up to three rhetorical questions in the introduction. |
| **High** | Openly vlog-style, still warm and never loud. Everything in medium, plus: a quick, chatty rhythm, frequent direct address, small self-aware moments about the video itself ("stick with me, this part's worth it"), reactions to the story ("I mean, come on, Dorian"), and humour in every narrator block. Up to four rhetorical questions in the introduction. The callback, the payoff of the opening hook and the last takeaway still land sincerely. |

The examples show the register only; do not reuse them as lines. How many self-corrections, fillers and spoken openers each level allows, and the read-aloud pass every narrator scene goes through, are in `spoken-style.md` (sections 3 and 4).

---

## 6. The story narration (fairy-tale voice)

**Voice.** Third person, past tense, the cadence of a told tale. Plain words, concrete images, short-to-medium sentences with occasional longer, rolling ones. No modern slang, no academic vocabulary, no critical commentary inside the story; interpretation belongs to the takeaways. Keep to `spoken-style.md` section 5: no stock AI phrases, lists of three rationed, and most scenes ending on an event or image rather than a moral.

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

**Beats, not set phrases.** The beats below are fixed; the wording is not. Example lines in this section and in the skeleton show one way to say a beat, and should not be reused as is. Write each transition, callback and question lead-in for this book, out of its last story image, its motifs or the line just spoken, so that no two videos open the takeaways or the outro the same way. Where a narration history of earlier approved books exists, avoid every line recorded there as well. Only the subscribe line (step 7 of the outro) stays word for word the same.

### Takeaways (2–5 scenes, ~80–100 words each)

- **Transition** (start of the first takeaway): a pause, then a line that turns from story to meaning and names the actual number of takeaways (e.g. "And there our tale ends. *(pause)* … let me leave three things in your hands."). Vary it: start from the story's final image, from the narrator's own reaction, or from a question the ending leaves open.
- **Numbered openers**: "The first:", "The second:", … and "And the last:" for the final one. This gives the viewer a clear map.
- **Each takeaway**: claim in one sentence → evidence from one or two specific events or characters → a universal application to the viewer's life.
- **Callbacks**: reuse earlier quotes inside takeaways where they fit, and point out a surprising detail ("And notice who gave that advice to the young student: the devil himself.").
- **One personal moment**: once per video, the narrator admits sharing the feeling being discussed. The narrator is the channel's creator, so the moment must be true. Draw it from `narrator-bible.md`, or mark it `[CONFIRM: …]` for the creator to confirm. Never repeat one from its anecdote log.
- **The last takeaway** is the book's deepest or most surprising meaning, and connects to how the author changed the expected ending (the origins hook from the introduction).

Typical takeaway types to draw from: the central virtue or drive; the cost to others; the gap between knowledge and life; the divided self; the role of grace, chance or love; the danger of a specific temptation; what the ending reveals.

### Outro (1 scene, ~150–180 words; up to ~200 with a link to an earlier video)

1. **Callback**: return to the opening hook through a lead-in written for this book. A quote comes back word for word. An image, question, fact, object or claim comes back in the same words where possible. Do not use a stock opener such as "Do you remember the words we began with?" in every video: it quickly sounds mechanical. Ways in, to vary between books:
   - return to the place or moment of the hook ("Somewhere in that sunlit studio, the words are still hanging in the air…");
   - start from the story's final image and let the hook surface from it;
   - repeat the hook cold, after a pause, and only then step back and comment;
   - for a quote, name the speaker first, then give the quote as the surprise;
   - turn the hook back on the viewer ("At the start, I asked you to keep something in mind…").
2. **Reveal**: for a quote, name the speaker. For other types, say what the hook really meant: what the cloth was hiding, what the hero chose, what the fact cost the author.
3. **Answer**: resolve the promise from the introduction in one or two sentences.
4. *(pause)*
5. **Reflective question** for the viewer, drawn from the book's central dilemma ("what would you give to feel that your life was truly complete?"). Vary how it is introduced; do not open it with the same "So here is a question…" every time.
6. **Comments and likes, said creatively**: ask the viewer to answer the question in the comments and to leave a like, but put it in the book's own world and motifs rather than as a stock request. Write it fresh for every book. Examples for *Faust*: "Write your answer in the comments, and sign it in ink, not in blood." / "If this tale lit a small candle for you, leave a like so it can light the way for the next traveller."
7. **Subscribe and bell, said directly**: always include a plain, literal call to subscribe and turn on notifications, with no metaphor, e.g. "Please subscribe to the channel and click the bell button, so you never miss a new tale." It is never left out and never folded into the sign-off.
8. **Invitation and sign-off**: the narrator's invitation to the next tale and sign-off, from Narrator.md. If an earlier video is linked in the outro (below), the link goes here, just before the invitation.

### Pointing to earlier videos

A good host connects episodes: "if this one got you thinking, the video on X goes even further". Done well, it helps the viewer and keeps them on the channel. Done by formula, it sounds like an ad. So links to earlier videos are **optional**, made only when two books really share something, and never forced.

**Where the memory lives.** The video library (`video-library.md`, next to the book folders) holds one entry per approved video: its theme tags, central question, takeaways, archetypes, the spoiler to avoid, and whether it is published.

**Finding an overlap.** While choosing the takeaways (step 1), compare this book with every library entry and sort each into one of three kinds:

| Kind | What it means | Example | Link? |
| --- | --- | --- | --- |
| **Strong echo** | Same central dilemma or archetype, so the earlier video adds a second angle on the same lesson. | *Dorian Gray* and *Faust*: both trade a soul for what they desire. | Yes, if it fits a takeaway or the outro naturally. |
| **Telling contrast** | Same question, opposite answer, and the contrast sharpens this book's point. | Faust is saved by striving; a hero destroyed by the same striving. | Only if the contrast makes the takeaway better. |
| **Surface only** | A broad shared theme ("love", "death", "power") or the same period, with nothing more specific. | Two books that simply both have a love story. | No. |

A shared theme tag is only a reason to look. The test is whether a viewer who has just finished this video would honestly want to watch that one next.

**How to link.**

- 0–2 links per video: at most one inside a takeaway and one in the outro. Zero is a perfectly good answer, and the usual one while the library is small.
- Only in the takeaways or the outro, never in the introduction or the story.
- Put it where the overlap actually is: inside the takeaway whose lesson the books share, or in the outro next to the invitation if the link is about the book as a whole.
- One or two sentences that add something: a detail from the earlier book that shines a new light on this one ("Faust at least had to sign in blood. Dorian didn't even need ink."). Name the book plainly so the viewer can find it ("our Faust video").
- Never spoil the earlier book's ending or twist; the library entry says what to avoid.
- Write it in this book's vlogger-touch level, and vary the wording between videos like every other narrator line.
- Link only to videos marked published. If the best match is approved but not yet published, leave it out and mention it to the user.
- Do not link the same earlier video from two videos in a row unless it is clearly the strongest match.

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
- One clear moment per image. Avoid "and then" sequences; if two moments are essential, compose them as two planes or a split frame and say so.
- Recurring locations reuse the same description so they look like the same place (the Gothic study in images 06, 07, 10 and 37).
- **Story scenes** are literal depictions of the moment.
- **Quote scenes** are **symbolic**, never a repeat of a plot image: a visual metaphor for the line (two figures pulling in opposite directions for "two souls", a gray library split by a green tree for "gray are all theories").
- **Takeaway scenes** are modern, universal metaphors (a climber, a tower beside a small cottage, a mirror, two hands reaching).
- **Book-ends**: the first and last images mirror each other (the scholar's study at night → the same study, empty, at dawn).
- Never ask the image to render text.
- Avoid copyrighted characters, identifiable modern people and existing artworks.

---

## 9. Quotes and translations

- Use a **public-domain translation** (published before 1929) or your own literal translation of the original. For *Faust*, the Bayard Taylor translation (1870) was used, with some lines rendered literally.
- Use the same English wording everywhere the quote appears: illustration plan, script, opening, callback.
- In the Illustration Plan, record for each quote: English text, original text in italics, speaker, and location (part, scene, line), e.g.:
  `"Two souls, alas! reside within my breast." (Zwei Seelen wohnen, ach! in meiner Brust, Part One, "Outside the City Gate", line 1112.)`
- If the opening hook is a quote, hide its speaker (credit the author) until it recurs in the story.

---

## 10. Templates

### Narration Script skeleton

```markdown
# [Book] Video — Narration Script

The script tells [Book] as a fairy tale, one passage per scene in timeline order, about [N] words. At 140 words per minute it runs about [M] minutes. The introduction and the takeaways are spoken by the channel's narrator; the story in between is told in the fairy-tale voice. Bracketed numbers match the illustrations in the Illustration Plan.

## Introduction (narrator)

*Spoken by the narrator. Scene numbers mark where each illustration cuts in.*

### 1 · Opening hook [01]

[Opening hook: the quote in quotation marks, or the image, question, fact, object or claim.]

*(pause)*

[Framing and promise.]

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
[Transition from story to meaning, written for this book, naming the number of takeaways.] *(pause)*
The first: [claim]. [Evidence]. [Application].

### [n+1…] · [Remaining takeaways, up to five in all]
The second: … / … / And the last: …

### [last] · Outro: [closing image] [..]
[Lead-in written for this book.] [The hook again: the quote word for word, or the image, question, fact, object or claim.] [Reveal: the speaker, or what the hook really meant.] [Answer to the promise.]

*(pause)*

[Lead-in to the question, varied.] [Question]? [Creative invitation to comment and like, in the book's own imagery.] Please subscribe to the channel and click the bell button, so you never miss a new tale. [Narrator's invitation and sign-off, from Narrator.md.]
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

Each description below is written to paste directly as a prompt. Append the style block from Visual Style.md to every prompt, and the fixed descriptors from Book Style Sheet — [Book].md wherever a recurring character appears.

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

- [ ] The script opens cold on a hook (section 4) of a different type from the previous book. If it is a quote, it is credited to the author, not the character.
- [ ] The introduction contains: framing and promise, welcome and logline, author hook, origins and "dared to change it", structure map, "Once upon a time…"
- [ ] Every story scene orients, shows one event, and ends on a turn.
- [ ] Every quote scene: setup → quote → plain meaning → link.
- [ ] Two to five takeaways, as many as the book supports, each with evidence from the story; one personal moment from the narrator.
- [ ] The outro returns to the opening hook (a quote word for word), reveals the speaker or the hook's meaning, and answers the promise.
- [ ] The outro asks for comments and likes in the book's own imagery, then gives a direct, literal "subscribe to the channel and click the bell button" call to action.
- [ ] The narrator's welcome, invitation, calls to action and sign-off match Narrator.md.
- [ ] Facts, names, dates and line references checked against the source.

**Illustrations**

- [ ] Prompts describe content only; the style block from Visual Style.md is appended to each.
- [ ] No descriptions conflict with Visual Style.md.
- [ ] Recurring characters use their fixed descriptors from Book Style Sheet — [Book].md.
- [ ] Recurring locations use identical descriptions.
- [ ] Quote and takeaway images are symbolic.
- [ ] First and last images mirror each other.
- [ ] No text rendered inside images; no copyrighted characters or real modern people.

---

## Appendix: Faust as the worked example

| Element | Faust |
| --- | --- |
| Opening hook (riddle quote) | "Part of that Power, not understood, which always wills the Bad, and always works the Good." (Mephistopheles, credited to Goethe) |
| Author hook | Written over sixty years, from Goethe's twenties to months before his death in 1832 |
| Origins hook | The puppet-play legend in which the doctor is always dragged to hell; Goethe dared to save him |
| Structure map | Part One: a story of the heart. Part Two: a story of the world. "One long road." |
| Story scenes | 27 (19 from Part One including 6 quote scenes, 8 from Part Two) |
| Key quotes | "Man errs, as long as he doth strive." · "Two souls, alas!…" · "In the beginning was the Deed." · "Part of that Power…" · "Stay, thou art so fair!" · "Gray are all theories…" · "The Eternal-Feminine draws us on." (closing line, inside the last story scene) |
| Takeaways | Striving is the point · Ambition has victims · Knowledge is not living · We are divided · Grace meets effort |
| Reflective question | "What would you give to feel that your life was truly complete?" |
| Book-end images | Scholar in the Gothic study at night → the same study, empty, at dawn |
| Totals | 37 illustrations · ~3,100 words · ~22 minutes |
