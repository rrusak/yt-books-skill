# Visual Style Guide — Naïve Colored-Pencil Editorial

The channel's master visual style, used for every illustration in every video. It defines what stays **constant across the channel**, and how to build the **Book Style Sheet** that each book gets: its own palette, motifs and character descriptions.

The style was established on Goethe's *Faust*. The reference image `gothic_bargain_at_midnight.png` (Faust and Mephistopheles at the desk) is the channel's **technique reference**.

## Related documents

| Document | Role |
| --- | --- |
| **Visual Style.md** (this document) | Channel-wide technique, rendering rules, composition, the master prompt, and the process for building a Book Style Sheet. |
| **Book Style Sheet — [Book].md** | One per book: palette, motif vocabulary, setting notes, character descriptions, anchor image and reference sheets. Built with the process in section 7. |
| **Narrator.md** | Written for each book (`05-narrator.md`): the narrator's lines and which finished pose image from `assets/narrator/` is overlaid when. The narrator is never generated in scene prompts. |
| **Book Video Scenario Guide.md** | Structure, scenes and image-prompt content. Prompts written under that guide get this style appended. |

---

## 1. Two layers: channel and book

Every illustration combines two layers. The channel layer never changes; the book layer is designed once per book and then locked.

| Layer | What it contains | Where it is defined |
| --- | --- | --- |
| **Channel (constant)** | Medium and mark-making, paper, figure simplification, flat rendering, how light and darkness are shown, composition principles, framing, format, palette structure, what to avoid | This document |
| **Book (per title)** | The specific 6–7 colors and their meanings, decorative motifs, architecture and costume period, recurring characters, symbolic props | Book Style Sheet |

**Rule of thumb:** a viewer should recognise any frame as belonging to the channel from its *technique* alone, and recognise which book it belongs to from its *palette, motifs and characters*.

---

## 2. Channel constants

### 2.1 Medium and surface

- Looks like an original hand-drawn editorial poster made **entirely with colored pencils** on **warm ivory paper with a visible tooth**.
- Paper texture shows through every area, including the darkest fields. Dark areas are built from dense, layered pencil marks, never a solid digital fill.
- Every frame should look handmade and slightly imperfect, never digitally polished.

### 2.2 Mark-making

- Visible, rough, directional pencil strokes, with overlapping hatching, small gaps and variations in pressure.
- Large color fields (night skies, cloaks, curtains) are filled with short, energetic strokes that give a speckled, woven surface.
- Outlines are irregular and sketchy, with imperfect hand-drawn contours, never clean vector lines.
- Color filling is slightly uneven, and may drift a little past outlines.

### 2.3 Figures (all books)

- Simplified, charmingly awkward folk-art figures with whimsical proportions.
- **Elongated bodies and limbs**; long fingers for expressive gestures.
- Faces: small eyes (dots or short strokes), simple noses, minimal mouths, a few lines for brows and age. Emotion is carried by **posture, gesture and the tilt of the head** more than facial detail.
- Stylized hair as solid shapes with a few curling strokes.
- Deliberately imperfect anatomy; poses slightly theatrical, as on a stage.
- Costumes are bold, flat silhouettes with one or two contrasting linings or trims (e.g. a black cloak with a red lining).
- Each recurring character must be identifiable **by silhouette alone**.

### 2.4 Flat rendering, light and darkness

- Flat two-dimensional shapes, simplified perspective, no modelled volume.
- **No** realistic cast shadows, gradients, gloss, 3D rendering, airbrush, cinematic lighting or lens effects.
- Darkness and mood are expressed through **color fields, symbolism and composition**, not light simulation.
- Light sources are drawn as **objects plus a soft pencil halo**: a candle is an ivory stick with a small ochre-and-vermilion flame, surrounded by a loose patch of pale ochre strokes on the paper. A halo is a hand-shaded patch, never a smooth glow.
- Night is a cobalt or navy field scattered with ivory star dots and a simple crescent moon; day is open ivory paper with peach or ochre accents. (Exact hues come from the book palette.)

Content descriptions in image prompts must avoid realistic lighting language. Use these flat equivalents:

| Instead of | Write |
| --- | --- |
| "sinks into deep shadow" | "that side of the room is a dense field of navy pencil" |
| "a beam of light falls on her" | "a pale ochre wedge of pencil strokes falls across her" |
| "glowing", "radiant" | "surrounded by a loose halo of pale ochre strokes" |
| "casting two shadows" | "two flat silhouette shapes in contrasting colors stretch from his feet" |
| "blurred like a memory", "misty" | "drawn in faint, sparse pencil strokes on bare paper" |
| "smoke billows" | "curling ribbons of grey pencil" |
| "fire", "flames" | "flat vermilion and ochre flame shapes with sketchy edges" |
| "moonlight falls through the window" | "a crescent moon and stars in the window; a pale ivory patch on the floor" |

### 2.5 Composition

- **Format:** wide 16:9 horizontal, for YouTube. If the tool outputs another ratio, crop to 16:9 and keep important elements away from the top and bottom edges.
- **Theatrical framing:** scenes are often framed like a stage set, with curtains, arches, doorways, window frames or foliage at the left and right edges.
- **Clear silhouettes and balanced negative space.** Include one calm, open area (usually bare or lightly shaded paper) where the eye can rest.
- **Duality through the frame:** contrasts in the story can be shown as contrasts across the frame (warm/cool, day/night, interior/exterior, left/right).
- **Decorative but not crowded:** ornamental borders, patterned textiles, stylized plants, stars and small symbolic props fill the edges; the centre stays readable.
- **Small symbolic details** reward a second look (in *Faust*: a skull, an hourglass, an armillary sphere, a black cat, a gargoyle).
- No lettering, watermarks or borders unless explicitly requested. All text is added in editing.

### 2.6 Palette structure (fixed); hues (per book)

Every book palette has the same structure: 6–7 matte colors in fixed roles. The two neutrals are the same for every book; the others are chosen per book (section 7, step 2).

| Role | Purpose | Channel rule |
| --- | --- | --- |
| **Paper** | Background, open space, light | Always warm ivory, about `#F5EAD5` |
| **Line / dark** | Outlines, dark fields, black costumes | Always charcoal, about `#242122` |
| **Dominant cool** | Night, distance, the spiritual or the cold | Chosen per book |
| **Dominant warm** | Passion, danger, power, key costumes | Chosen per book |
| **Earth / light** | Wood, gold, candlelight, halos | Chosen per book |
| **Skin** | Faces and hands | Chosen per book; one consistent tone per character |
| **Optional accent** | One extra hue for a specific motif | Use sparingly or not at all |

Colors are always matte and rendered as layered pencil marks. No neon, no metallic or glossy effects; gold is drawn as ochre.

### 2.7 Atmosphere

Whimsical yet sophisticated, literary, poetic, slightly theatrical. A fairy tale for adults: dark subjects are allowed, but never graphic or gory. Violence, death and tragedy are shown symbolically or at the moment just before or after.

### 2.8 Avoid (all books)

Photorealism; polished digital painting; gradients; realistic cast shadows; 3D rendering; gloss; cinematic lighting; lens flare or depth of field; airbrush textures; detailed realistic anatomy; perfectly clean vector outlines; artificial-looking texture overlays; text, lettering or watermarks; copyrighted characters; identifiable modern people; reproductions of existing artworks.

---

## 3. Master style prompt

This block is the channel layer. Paste it at the start of every image prompt, with the bracketed lines filled from the Book Style Sheet.

> Create an illustration in a contemporary, sophisticated naïve-art style, resembling an original hand-drawn editorial poster made entirely with colored pencils on warm, slightly textured ivory paper.
>
> **Drawing technique:** Visible, rough colored-pencil strokes; irregular, sketchy outlines; imperfect hand-drawn contours; slightly uneven color filling. Pencil marks remain visible, including overlapping strokes, subtle gaps and variations in pressure. Large dark areas are built from dense layered strokes with the paper texture still showing. The artwork must look handmade, not digitally polished.
>
> **Characters:** Simplified, charmingly awkward figures with whimsical proportions, elongated bodies and long expressive hands, minimally detailed faces with small eyes, simple noses and stylized hair. Deliberately imperfect anatomy with a gentle folk-art quality. Poetic, slightly theatrical and emotionally expressive through posture and gesture.
>
> **Palette:** Limited, rich, contrasting matte colors: [BOOK PALETTE: names of the 6–7 colors]. Colors are densely layered colored-pencil marks.
>
> **Composition:** Flat two-dimensional shapes, simplified perspective, clear silhouettes and balanced negative space. Theatrical framing at the edges. [BOOK MOTIFS: decorative architecture, ornaments, plants and symbols]. High-end editorial poster aesthetic without overcrowding.
>
> **Atmosphere:** Whimsical yet sophisticated, literary, slightly mysterious and poetic. Express mood through color, symbolism and composition rather than realistic lighting. Light sources are drawn as objects with a loose hand-shaded halo, never a smooth glow.
>
> **Avoid:** Photorealism, polished digital painting, gradients, realistic cast shadows, 3D rendering, gloss, cinematic lighting effects, airbrush textures, detailed realistic anatomy, perfectly clean vector outlines and artificial-looking texture.
>
> **Output:** Wide 16:9 horizontal composition for a YouTube video; no lettering, watermarks or borders.

---

## 4. Assembling a scene prompt

Build each prompt in this order:

1. **Master style prompt** (section 3), with the book's palette and motif lines filled in.
2. **Characters in this scene**: the fixed descriptor of each recurring character who appears, copied word for word from the Book Style Sheet.
3. **Scene description**: from the Illustration Plan (content only, using the flat equivalents in 2.4).
4. **Reminder line**: "Match the attached references' drawing technique, texture, palette and character designs, not their composition."

Attach as references, in this priority:

1. The **book anchor image** (once it exists; see section 7).
2. The **character reference sheets** for characters in the scene.
3. The **channel technique reference** (`gothic_bargain_at_midnight.png`), with the instruction to take only technique, texture and figure simplicity from it, not its palette or setting. Once a book has its own anchor image, this reference becomes optional.

---

## 5. Generating a series

- Work in **one conversation per book** so references and corrections stay in context.
- Generate **one scene at a time** and approve it before moving on.
- Treat references as **style references**, not scenes to duplicate. Adapt objects, characters and framing to each description.
- Keep approved images: a strong approved scene can be attached as an extra reference for later scenes in the same setting.

**When drift happens**, name the specific problem and regenerate. Do not rewrite the whole prompt. For example:

| Symptom | Correction to add |
| --- | --- |
| Too polished or digital | "Rougher, more visible pencil strokes; paper texture visible everywhere; less smooth filling." |
| Shading or 3D volume appears | "Completely flat shapes; no shading, no cast shadows, no gradients." |
| Smooth glow around lights | "Replace the glow with a loose patch of pale ochre pencil strokes." |
| Characters too realistic | "Simpler, more naïve figures; elongated bodies; dot-like eyes; less facial detail." |
| Character looks different | Re-attach the character sheet; repeat the fixed descriptor and name the signature elements that changed. |
| Colors outside the palette | "Use only these colors: [palette]." |
| Too crowded | "Fewer objects; larger open area of bare paper in the [position]." |

---

## 6. Quality checklist (per image)

- [ ] Looks like colored pencil on warm textured paper; strokes and paper tooth visible, including in dark areas.
- [ ] No gradients, cast shadows, gloss, 3D or cinematic light.
- [ ] Only the book palette's colors.
- [ ] Figures are naïve and elongated with minimal faces; recurring characters match their sheets and are recognisable by silhouette.
- [ ] Clear silhouettes, an open resting area, and uncluttered centre.
- [ ] 16:9, with nothing important at the very edges.
- [ ] No text, watermark or border.
- [ ] Consistent with neighbouring scenes in the same setting.

---

## 7. Building a Book Style Sheet

Each book gets its own sheet before any scene is generated. The sheet adapts the channel style to the book; it never changes the technique.

### Step 1 — Read the book visually

Note, in a few lines each:

- **Period and place**: the era, country and architecture of the story's world.
- **Mood**: two or three adjectives for the book's atmosphere.
- **Central duality or tension**: the opposition that drives the story (Faust: heaven and hell, spirit and earth, learning and life). The palette and composition should be able to show it.
- **Key settings**: the 4–8 locations that recur in the Illustration Plan.
- **Symbolic objects**: props that carry the book's meaning.

### Step 2 — Derive the palette

1. Keep the two channel neutrals: **ivory paper** and **charcoal**.
2. Choose a **dominant cool** and a **dominant warm** that express the central duality, and decide which side of the story each one represents.
3. Choose an **earth/light** tone for wood, gold and light sources, and a **skin** tone.
4. Add an **optional accent** only if a single motif needs it.
5. Give each color a **name, a hex value and a meaning** in the story.
6. Check: strong contrast between cool and warm; every color works as layered pencil on ivory paper; the palette is clearly different from the previous book on the channel, so each video has its own identity.

### Step 3 — Define the motif vocabulary

List 6–10 decorative elements drawn from the book's world: architecture, ornaments and patterns, textiles, plants, celestial symbols, recurring props, creatures. These fill the [BOOK MOTIFS] line of the master prompt and give scenes their ornamental edges.

### Step 4 — Design the recurring characters

List every character who appears in more than one illustration. For each, define:

| Field | Content |
| --- | --- |
| Role | Who they are in the story |
| Age and build | Including any transformation (older/younger, before/after) |
| Silhouette | The overall shape that identifies them (e.g. tall and angular, small and round) |
| **Signature elements** | 2–3 features that must never change between scenes (e.g. horns, a red-lined cloak, curly dark hair) |
| Hair and face | Hair shape and color; facial hair; one or two facial cues |
| Costume | Main garments with their palette colors |
| Props | Objects they usually hold |
| Posture and gesture | How they typically stand and move |
| Variants | Different costumes or ages, each with its own descriptor |
| **Fixed descriptor** | One sentence of 25–40 words, pasted word for word into every prompt where they appear |

Make characters distinguishable **by silhouette and color pairing**, so they read clearly even when small in the frame. Avoid giving two main characters the same dominant color.

### Step 5 — Create the book anchor image

Generate one key scene, usually the opening scene (01), using the master prompt, the new palette and motifs, the main characters' descriptors, and the channel technique reference. Iterate until it fully matches the channel style and the book's identity. This image becomes the book's **primary style reference**.

### Step 6 — Create character reference sheets

For each main character, generate a sheet using the anchor image as reference:

> Character reference sheet on plain ivory paper, in the same colored-pencil naïve style as the attached image: [fixed descriptor]. Show the full figure from the front, three-quarter view and side, plus four small head studies with different expressions (calm, worried, angry, joyful). No background scene, no text.

Create separate sheets for major variants (e.g. old Faust and rejuvenated Faust).

### Step 7 — Test and lock

Generate 2–3 test scenes that differ from the anchor: an exterior, a crowded scene, and a symbolic quote image. If they match the anchor and the character sheets, **lock** the sheet: the palette, motifs and descriptors do not change for the rest of the book. Record the locked state and the reference image file names in the sheet.

---

## 8. Book Style Sheet template

```markdown
# Book Style Sheet — [Book title]

Channel style: Visual Style.md. This sheet defines only the book layer.

## World
- Period and place:
- Mood:
- Central duality:
- Key settings:
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

Palette line for the master prompt: "[color], [color], [color], …"

## Motif vocabulary
Motif line for the master prompt: "[architecture], [ornaments], [plants], [symbols], …"

## Characters
### [Name]
- Role:
- Age and build:
- Silhouette:
- Signature elements (never change):
- Hair and face:
- Costume:
- Props:
- Posture and gesture:
- Variants:
- **Fixed descriptor:** "…"

## References
- Anchor image: [file name]
- Character sheets: [file names]
- Status: Draft / Locked on [date]
```

---

## Appendix: *Faust* as the worked example

The channel technique reference doubles as the *Faust* anchor image.

**Palette**

| Role | Name | Hex | Meaning |
| --- | --- | --- | --- |
| Paper | Ivory | `#F5EAD5` | Open sky, daylight, the page |
| Line / dark | Charcoal | `#242122` | Robes, cloaks, the devil's figure |
| Dominant cool | Cobalt blue | `#18549A` | Night, the heavens, the spirit world (with dark navy for depth) |
| Dominant warm | Vermilion | `#AC3932` | Mephistopheles, passion, blood, curtains |
| Earth / light | Ochre | `#BC813F` | Candlelight, wood, gold instruments, learning |
| Skin | Peach | `#E9AC86` | Faces and hands |

**Motif vocabulary:** Gothic arches and window tracery, cathedral spires on the skyline, heavy red curtains with fleur-de-lis, patterned table runners, climbing ivy, stars and a crescent moon, skull, hourglass, armillary sphere, quills and parchment, a black cat, gargoyles.

**Composition in the anchor image:** the frame is split into warm (left, the scholar's world of books and candlelight) and cool (right, night, spires and the devil). A large open ivory sky fills the centre. Curtains and arches frame the scene like a stage.

**Characters (from the anchor image)**

- **Faust (young, after the Witch's Kitchen):** "A slender man with a mass of dark curly hair and a thin moustache, in a long black scholar's robe with red lining over a white shirt with ruffled cuffs, thoughtful, holding a white quill." Signature elements: dark curls, black robe with red lining, quill.
- **Mephistopheles:** "A very tall, thin, elongated figure in a black cape with a high red collar and red lining, two curving black horns, slicked black hair, a pointed beard and moustache, long spidery fingers, leaning forward with a sly look." Signature elements: horns, high red collar, spidery hands.

Still to be designed for the *Faust* sheet: old Faust (same curls turned grey, lined face, same robe), Gretchen, Wagner, Valentin, Helen, Euphorion and Homunculus.
