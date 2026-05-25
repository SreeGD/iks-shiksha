# Day 6 — 4×4 and the Khajuraho Square

**Module:** Magic Squares — Bhadragaṇita · **Band:** Senior · **Time:** 45 min

## Learning objective

By the end of this lesson, students will: examine the khajuraho inscription and its panel-magic property.

## Materials

- Whiteboard / chart paper
- Notebook, pen per student
- (See lesson-plan.md for any day-specific materials)

## Vocabulary introduced today

- *kothumi vidhi* (IAST: kothumi vidhi; lit. "Nārāyaṇa's algorithm for odd-order squares")


## Lesson flow

### Warm-up (5 min)

- Daily check-in: one-sentence response to *"What's one thing you remember about yesterday's lesson?"*
- Hook: introduce a phenomenon or question that motivates today's concept.

### Core (20 min)

1. **The 4×4 (even-order) case.** Stair-step doesn't directly work for even n. Different methods exist (Strachey method, Conway's LUX). Magic constant for 4×4 with 1–16: **34**.

2. **The Dürer 4×4 (1514).** Famous engraving "Melencolia I" includes a 4×4 magic square:
   ```
   16  3  2 13
    5 10 11  8
    9  6  7 12
    4 15 14  1
   ```
   All rows, columns, diagonals = 34. The bottom-middle two cells contain "15 14" — the year of the engraving (1514). Famous detail.

3. **The Khajuraho square (~10th c. CE).** Inscribed on a panel at the Khajuraho temple complex (Madhya Pradesh, India). 4×4 grid. ALL rows, columns, diagonals AND many 2×2 subblocks sum to **34**. This is a *pan-diagonal* (or *most-perfect*) magic square — a stronger condition than ordinary magic.

   ```
    7 12  1 14
    2 13  8 11
   16  3 10  5
    9  6 15  4
   ```
   Compute: row 1 = 7+12+1+14 = 34. Column 1 = 7+2+16+9 = 34. Etc. Also 2×2 block top-left = 7+12+2+13 = 34.

4. **Source.** The Khajuraho inscription is real and dateable (~10th–11th c. CE). Discussion: this PRECEDES Dürer by ~500 years. The temple inscription is one of the oldest extant magic squares with this "most-perfect" property.

5. **Honest framing.** Magic squares appear in many cultures. The KHAJURAHO square's "most-perfect" property is distinctive. Not all Indian magic squares are this advanced; not all advanced ones are Indian. Cross-cultural mathematics flourishes.

### Activity (15 min)

A scaled version of *Class 3×3 Magic-Square Tournament* (see `activities/`). Today's slice: focus on the part of the activity that reinforces 4×4 and the Khajuraho Square.

### Wrap-up (5 min)

- One-sentence exit ticket: *"What's one thing you learned today?"*
- Preview tomorrow.

## Homework

(See `homework.md` for today's task.)

## Differentiation

- **Extension:** offer one open question or extra problem for fast finishers.
- **Support:** pair students who need scaffolds; offer partial outlines.

## Teacher notes

- Citations: at least one quoted verse with citation per module. Day 1 already includes one if applicable; you may add more.
- Connect to prior modules where natural (especially Module 2 pañcabhūta).
