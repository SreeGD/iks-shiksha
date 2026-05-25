# Day 4 — Stair-Step Method (Nārāyaṇa)

**Module:** Magic Squares — Bhadragaṇita · **Band:** Senior · **Time:** 45 min

## Learning objective

By the end of this lesson, students will: apply nārāyaṇa's algorithm to build a 5×5 square.

## Materials

- Whiteboard / chart paper
- Notebook, pen per student
- (See lesson-plan.md for any day-specific materials)

## Vocabulary introduced today

- *bhadra-gaṇita* (IAST: bhadra-gaṇita; lit. ""auspicious arithmetic" — the Indian term for magic squares")


## Lesson flow

### Warm-up (5 min)

- Daily check-in: one-sentence response to *"What's one thing you remember about yesterday's lesson?"*
- Hook: introduce a phenomenon or question that motivates today's concept.

### Core (20 min)

1. **State Nārāyaṇa Paṇḍita's algorithm.** For any ODD n×n, follow these steps:
   - Step 1: Place 1 in the top-middle cell.
   - Step 2: From the cell with k, move one up and one right (diagonal) to place k+1.
   - Step 3: If you go off the top, wrap to the bottom (same column you'd have landed in).
   - Step 4: If you go off the right, wrap to the left (same row).
   - Step 5: If the target cell is occupied, place k+1 in the cell DIRECTLY BELOW the cell containing k instead.

2. **Demonstrate on 3×3.** Place 1 top-middle. Move up-right (wraps to bottom row, same column shift) → 2 goes bottom-right. Continue:
   ```
   8 1 6
   3 5 7
   4 9 2
   ```
   Verify: rows, columns, diagonals all = 15. ✓ (Note: this is a different symmetric variant of the 3×3 magic square than yesterday's.)

3. **Source.** Nārāyaṇa Paṇḍita's *Gaṇita-kaumudī* (1356 CE), Book 14 (*Bhadra-gaṇita*). He calls this method *turagagati* — "horse-step" (knight-like move).

4. **Cross-cultural.** The same method was independently discovered or transmitted in Arabic and European mathematics. The earliest extant Indian description is Nārāyaṇa's.

5. **Try on your own.** Each student applies the algorithm to construct another 3×3 magic square. Tomorrow we extend to 5×5.

### Activity (15 min)

A scaled version of *Class 3×3 Magic-Square Tournament* (see `activities/`). Today's slice: focus on the part of the activity that reinforces Stair-Step Method (Nārāyaṇa).

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
