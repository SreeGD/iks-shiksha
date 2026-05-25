# Day 1 — The Hook: 97 × 96 in Three Seconds

**Module:** Nikhilam Multiplication · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will record a personal baseline time for `97 × 96` solved by long multiplication, and will have seen the *Nikhilam* method produce the same answer in under 5 seconds.

## Materials

- Printed baseline sheet: a single problem `97 × 96 = ?` with workspace and "your time" line. One per student.
- Stopwatch or wall clock with a second hand. One per pair is enough.
- Whiteboard with a single vertical dividing line drawn down the middle (the "Nikhilam split").

## Vocabulary introduced today

- *Nikhilam* (IAST: nikhilam; lit. "all" — short for *Nikhilam Navataścaramaṁ Daśataḥ*, "all from 9 and the last from 10") — Tirthaji's 2nd sūtra; here, the rule for multiplication near a base.
- *deficit* — how much a number falls short of the base (97 is 3 short of 100; deficit = 3).
- *base* — a power of 10 the two numbers are close to (here, 100).

## Lesson flow

### Warm-up (5 min)

- Teacher: *"How long does it take you to multiply 97 × 96?"* Take 3–4 guesses. Write the range (e.g. "15 sec to 1 min").
- Teacher: *"I'll show you a way to do it in under 5 seconds. Then we'll talk about why."*

### Baseline timing (10 min)

- Hand out the baseline sheet face-down.
- Students write their name and predicted time on the back.
- On "Go," flip and solve `97 × 96` using long multiplication.
- Record actual time. Mark answer; honest self-correction. (Correct answer: 9312.)
- Teacher walks around. Most will take 30–60 seconds. A few faster, a few slower.

### Teacher demonstration (10 min)

- On the board, write the problem:

  ```
     97  ← (3 below 100, deficit = 3)
   × 96  ← (4 below 100, deficit = 4)
  ─────
  ```

- **Step 1: Find the deficits from 100.** Write `−3` next to 97 and `−4` next to 96.

  ```
     97 │ −3
     96 │ −4
  ```

- **Step 2: Cross-subtract for the LEFT part.** "Take one number minus the *other* number's deficit. 97 − 4 = **93**. (Equivalently: 96 − 3 = 93. Either cross gives the same answer.)"

- **Step 3: Multiply the deficits for the RIGHT part.** "3 × 4 = **12**."

- **Step 4: Stick them together.** "93 on the left, 12 on the right → **9312**."

  ```
     97 │ −3
     96 │ −4
  ─────┼────
     93 │ 12      → 9312
  ```

- Verify: long-multiplication gives 9312. ✓

- *"I never multiplied any 2-digit number by another 2-digit number. I only did 97 − 4 and 3 × 4. That's the entire trick — when both numbers are near a base."*

### Activity (15 min) — First try

- Hand each student a second sheet with four problems:
  - `98 × 97`, `96 × 95`, `99 × 99`, `97 × 92`.
- Students try the Nikhilam method on each, then verify with long multiplication.
- Time themselves. Expect mistakes and slow times on the first try.

### Wrap-up (5 min)

- Show of hands: who got at least one right with Nikhilam? Who was *faster* with Nikhilam already? (Most won't be — yet.)
- Preview Day 2: *"Tomorrow we'll work on the foundational skill — instantly finding the deficit of any number from 10 or 100."*

## Student-facing content

> **The Nikhilam Method — Multiplication Near a Base**
>
> When both numbers are near a power of 10 (10, 100, 1000):
>
> 1. **Find the deficit** of each from the base.
> 2. **Cross-subtract** for the LEFT part (one number minus the *other's* deficit).
> 3. **Multiply the deficits** for the RIGHT part.
> 4. **Concatenate**: LEFT | RIGHT = the answer.
>
> Today's baseline: my time on `97 × 96` using long multiplication = ____ seconds.
> My time using Nikhilam (first try) = ____ seconds.
>
> I expect this gap to FLIP by Day 9.

## Homework

- Practice the "complement to 10" reflex: write the deficit of each from 10.
  - 7 → __, 8 → __, 9 → __, 6 → __, 5 → __, 4 → __, 3 → __, 2 → __, 1 → __.
- Do all 9 in under 10 seconds.

## Differentiation

- **Tier up:** Try `103 × 104` (both *above* 100). Note: instead of cross-subtract, you'll need to cross-*add*. See if you can work out the pattern before Day 4.
- **Tier down:** If 2-digit feels too fast, drop to single-digit near 10 (7 × 8, 6 × 9). We'll formally do this on Day 2.

## Teacher notes

- The baseline time is the *single most important* artefact of Day 1. Make sure every student records it honestly. Day 9's retest depends on it.
- Don't promise a specific speedup. Say "you'll likely be faster by Day 9; how much depends on you."
- Some students will ask "why does this work?" — defer to Day 7. *"Great question. We'll prove it. For now, just notice that it does work."*
- A few students will try to short-cut and use `−3 × −4` as the right part, getting a sign-error. Wait until Day 5 for the mixed case. For today, all deficits are positive.

## Citation(s) used in this lesson

- *Vedic Mathematics Batch1.pdf* (Vedic Cultural Center, Sammamish WA) — Nikhilam multiplication section.
- *Microsoft Word - sutras1.pdf* — sūtra #2: *Nikhilam Navataścaramaṁ Daśataḥ*.
