# Spoken style

How to make the spoken text sound said by a person, not written by a model. Polished written prose read by a voice model is the clearest sign of AI content, so every script goes through these rules. They cover both voices. The narrator gets the full read-aloud pass (section 3), and the storyteller a lighter version (section 5).

Use this guide in step 6 (`05-narrator.md`) and step 7 (`03-script.md`). Write the words first, then do the read-aloud pass, and only then the tagging pass from `elevenlabs-v4.md`.

## 1. Never use

Stock phrases that mark text as machine-written. Do not use them in any spoken text, in any form or tense. `check_book.py` flags every one of them.

- `here's the thing`
- `here's the kicker`
- `here's where it gets interesting`
- `a testament to`
- `in a world where`
- `imagine a world`
- `let's dive in`
- `dive into`
- `deep dive`
- `changes everything`
- `tapestry`
- `delve`
- `embark on`
- `navigate life`
- `navigate the complexities`
- `timeless tale`
- `timeless classic`
- `stands the test of time`
- `resonates`
- `now more than ever`
- `in today's world`
- `fast-paced world`
- `it's important to note`
- `it's worth noting`
- `at its core`
- `serves as a reminder`
- `a powerful reminder`
- `a stark reminder`
- `stark contrast`
- `little did he know`
- `little did she know`
- `without further ado`
- `buckle up`
- `in conclusion`
- `to sum up`
- `multifaceted`
- `intricate`
- `nuanced`
- `beacon of`
- `the realm of`
- `let's unpack`
- `unpack this`
- `and that, my friends`

Also avoid "journey" as a metaphor for an experience ("Dorian's journey of self-discovery"). A real road, voyage or walk in the story is fine.

## 2. Patterns to ration

These are normal in human speech but give AI text away when they appear everywhere. Each has a limit.

| Pattern | Example | Limit |
| --- | --- | --- |
| Lists of three | "Children watched, parents shuddered, and everyone knew." | At most one per scene. Use two or four items too, or just one. |
| "Not X, but Y" in any form | "Not in a church, but in a studio." / "It's not about the painting. It's about him." / "not just X, but Y" | At most two in the whole video. |
| Scene ending on a neat aphorism | "And that is the price of beauty." | At most one in three scenes. End story scenes on an event or image more often than on a moral. |
| Question, then its own answer | "The result? Ruin." | At most one in the video. |
| Balanced antithesis | "He had everything, and yet he had nothing." | At most one in the video. |
| Closing fragment | "Sixty years." / "Just words." | At most one per block (introduction, takeaways, outro), and never two scenes in a row. |
| Dashes | "a fair price — or so he thought" | At most two per scene. v4 reads each one as a pause. |
| Adjective stacks | "a dark, cold, silent room" | At most two adjectives before a noun. |
| Same scene opener | Three scenes in a row starting with "And", "But" or "So" | Never three in a row. |
| Written connectors | however, moreover, furthermore, therefore, thus, indeed, nevertheless | Never in narrator lines. In the story, "yet" and "still" are fine; the rest are not. |

## 3. The read-aloud pass (narrator)

Do this over every narrator scene, and over every line in `05-narrator.md`, once the words are final. Say each scene in your head at speaking pace (140 words per minute), as if telling it to a friend across a table, and fix whatever you would not actually say.

- **Short and uneven.** Most sentences 5–15 words. Split anything over about 22 words, unless it is one deliberate, rolling sentence in the scene. Never three sentences in a row of about the same length or shape.
- **Contractions** wherever a person would use them: you'll, wasn't, he'd, that's, didn't. Use the full form only for emphasis ("he did not come back").
- **Spoken connectors:** but, so, and, still, anyway, which means. Not however, therefore or moreover.
- **Subject first.** "Wilde wrote it in a few months", not "Having been commissioned by an American editor, Wilde…". Keep openings before the subject to a few words.
- **Concrete.** Name the thing: "the portrait", not "the artwork"; "he lied to her", not "he engaged in deception".
- **Thinking out loud.** At most one or two per narrator scene, by vlogger level (section 4):
  - a self-correction ("He was cruel. Well, not exactly cruel. Careless.");
  - a reaction ("which, honestly, is a terrible idea");
  - a short check-in with the viewer ("you know the type").
- **Easy to say.** No tongue twisters or clumps of s-sounds. Avoid words with two pronunciations where context does not settle it (read, lead, live, tear).
- **One test per sentence:** would you say this sentence, in this order, to a friend? If not, rewrite it until you would.

The read-aloud pass never changes facts, quotes, the subscribe line or links to earlier videos. It changes only how things are said.

## 4. Controlled imperfections by vlogger level

Real speech has small imperfections. A few, placed well, make the narrator sound like a person. Too many sound like an act. These counts are for the narrator across the whole video.

| | Light | Medium | High |
| --- | --- | --- | --- |
| Self-corrections ("well, not exactly") | 0–1 | 1–3 | 2–4 |
| Spoken openers ("Okay,", "So,", "Now,", "Look,") | 2–4 | 4–7 | 6–10 |
| Fillers ("I mean", "honestly", "you know") | 0–1 | 2–4 | 3–6 |
| Trailing thought ("And then… well. You'll see.") | 0 | 0–1 | 1–2 |
| Restart ("He was — okay, let me put it this way.") | 0 | 0 | 0–2 |

Rules for all levels:

- Never in the opening hook, the payoff of the hook in the outro, the last takeaway's claim, or the subscribe line. Those land clean.
- Never two imperfections in the same sentence, or in two sentences in a row.
- Do not write "um", "uh" or "er" as words. If a hesitation is wanted, use an ellipsis or a dash.
- Every imperfection must sound like the narrator thinking, never like a mistake in the facts.
- Do not repeat the same filler or opener more than twice in a video.

## 5. The storyteller

The story keeps its fairy-tale cadence (scenario guide, section 6), so it gets no fillers, self-corrections or check-ins. These still apply:

- section 1 in full;
- the limits in section 2, especially lists of three, aphorism endings and same scene openers;
- shorter sentences where a sentence trips when read aloud;
- end most scenes on an event, a decision or an image, not on a lesson.

## 6. Before and after

This example shows the change in register only. Do not reuse its lines.

**Before** (*Faust*, introduction):

> But the tale is older than Goethe. Long before him, in the market squares of Germany, puppeteers acted out the life of a wandering scholar who was said to have sold himself to the devil. Children watched, parents shuddered, and everyone knew the ending: when the time ran out, the devil came, and the doctor was dragged off to hell.

Two lists of three, a 31-word sentence, and no contractions.

**After** (light vlogger touch):

> But the story's much older than Goethe. Long before him, puppeteers were acting it out in German market squares. A wandering scholar, a deal with the devil. And everybody in the crowd knew how it ended. Time runs out, the devil comes to collect, and the doctor gets dragged off to hell.

One list of three is left, the sentences are short and uneven, and it is said the way a person tells it.

## 7. Checklist

- [ ] No phrase from section 1, and no "journey" as a metaphor.
- [ ] Every pattern in section 2 within its limit.
- [ ] Read-aloud pass done on every narrator scene and every line in `05-narrator.md`.
- [ ] Imperfections within the counts for the book's vlogger level, and none in the hook, payoff, last takeaway claim or subscribe line.
- [ ] The storyteller has no fillers or self-corrections, and most story scenes end on an event or image.
- [ ] `check_book.py` shows no banned phrases, and every style warning has been looked at.
