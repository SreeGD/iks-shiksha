# Day 7 — Two's Complement in Computers

**Module:** Subtraction — Nikhilam (All from 9) · **Band:** Senior · **Time:** 45 min

## Learning objective

By the end of this lesson, students will: show how the same idea underlies binary computer subtraction.

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

1. **Bridge to computing.** Modern computers don't have a subtraction circuit — they have an ADDER circuit. They subtract by adding the *two's complement* of the subtrahend. This is the same Nikhilam idea, in binary.

2. **Binary Nikhilam.** For an 8-bit number:
   - One's complement: flip every bit (= "all from 1," the binary analogue of "all from 9").
   - Two's complement: one's complement + 1.

3. **Worked example.** Compute 9 − 5 in 8-bit binary:
   - 5 = 00000101
   - Flip: 11111010 (one's complement)
   - Add 1: 11111011 (two's complement)
   - Add to 9 = 00001001: 00001001 + 11111011 = 100000100, drop the overflow bit → 00000100 = 4. ✓

4. **Source.** D.E. Knuth, *The Art of Computer Programming*, vol. 2 — full treatment.

5. **Critical-thinking close.** *"The Nikhilam sūtra (or its decimal-complement principle) and binary two's complement both date their origins to vastly different traditions and eras. What does this tell us about (a) the universality of certain algorithmic ideas and (b) the limits of cultural-priority claims?"*

### Activity (15 min)

A scaled version of *Complement Flashcards* (see `activities/`). Today's slice: focus on the part of the activity that reinforces Two's Complement in Computers.

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
