# Day 5 — Why It Works — The Algebra

**Module:** Subtraction — Nikhilam (All from 9) · **Band:** Senior · **Time:** 45 min

## Learning objective

By the end of this lesson, students will: derive the place-value identity that makes the rule work.

## Materials

- Whiteboard / chart paper
- Notebook, pen per student
- (See lesson-plan.md for any day-specific materials)

## Vocabulary introduced today

- *Nikhilaṁ Navataścaramaṁ Daśataḥ* (IAST: Nikhilaṁ Navataścaramaṁ Daśataḥ; lit. ""all from 9, the last from 10"")


## Lesson flow

### Warm-up (5 min)

- Daily check-in: one-sentence response to *"What's one thing you remember about yesterday's lesson?"*
- Hook: introduce a phenomenon or question that motivates today's concept.

### Core (20 min)

1. **State the identity.** For N with k digits, 10^k − N can be computed as ((10^k − 1) − N) + 1.

2. **Why "all from 9 last from 10" works.**
   - (10^k − 1) is a number with k nines: 9, 99, 999, 9999, ...
   - (10^k − 1) − N: each digit of N is subtracted from 9. The result has no borrows because each digit of (10^k − 1) is 9.
   - Adding 1 to that bumps the last digit by 1, which is equivalent to "the last digit from 10" rather than "from 9."

3. **Worked algebraic example.** N = 437, k = 3.
   - 999 − 437 = 562 (digit-wise: 9-4, 9-3, 9-7)
   - 562 + 1 = 563 = 1000 − 437. ✓

4. **The general formula.** 10^k − N = (10^k − 1) − N + 1 — a foundational identity in modular arithmetic and binary computer arithmetic.

5. **Senior bridge.** This is the same identity that underlies *two's complement* in binary computer arithmetic — tomorrow's topic.

### Activity (15 min)

A scaled version of *Complement Flashcards* (see `activities/`). Today's slice: focus on the part of the activity that reinforces Why It Works — The Algebra.

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
