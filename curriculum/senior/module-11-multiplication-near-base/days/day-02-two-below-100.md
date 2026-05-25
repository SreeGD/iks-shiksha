# Day 2 — Two-Digit × Two-Digit Near 100 (Below)

**Module:** Multiplication Near a Power of 10 — Nikhilam · **Band:** Senior · **Time:** 45 min

## Learning objective

By the end of this lesson, students will: compute 97 × 96 using deficits.

## Materials

- Whiteboard / chart paper
- Notebook, pen per student
- (See lesson-plan.md for any day-specific materials)

## Vocabulary introduced today

- *vinkulam* (IAST: vinkulam; lit. "deficit (number below base)")


## Lesson flow

### Warm-up (5 min)

- Daily check-in: one-sentence response to *"What's one thing you remember about yesterday's lesson?"*
- Hook: introduce a phenomenon or question that motivates today's concept.

### Core (20 min)

1. **The two-step rule for both factors below 100.**
   - Find deficits from 100: e.g., 97 → −3, 96 → −4.
   - **Left part:** cross-subtract. 97 − 4 = 93 (or equivalently 96 − 3 = 93).
   - **Right part:** product of deficits. 3 × 4 = 12.
   - Combine: **9312**.

2. **Worked examples.**
   - 97 × 96 = 93 | 12 = **9312**.
   - 88 × 95 = 83 | 60 = **8360**. (Deficits: 12, 5. Cross: 88−5=83 or 95−12=83. Product: 12×5=60.)
   - 99 × 99 = 98 | 01 = **9801**. (Deficits 1, 1. Cross: 98. Product: 1. Pad to 2 digits: 01.)

3. **Why the padding matters.** The right part must have as many digits as the base has zeros (here, 2 zeros → 2-digit right part). If product is single-digit, pad with leading zero. If product overflows (3+ digits), carry to left part.

4. **Algebra.** Base B = 100. Factor 1 = B − a, factor 2 = B − b. Then (B−a)(B−b) = B(B−a−b) + ab = B·(cross) + (right). The cross-subtract IS B − a − b. The product of deficits IS ab.

5. **Independent practice.** 8 problems, all below-100 case. 10 minutes.

### Activity (15 min)

A scaled version of *Method Speed Race* (see `activities/`). Today's slice: focus on the part of the activity that reinforces Two-Digit × Two-Digit Near 100 (Below).

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
