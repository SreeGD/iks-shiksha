# Day 1 — The Hook: *2 _ 3 = 253*

**Module:** ×11 (*Ekādhikena Pūrveṇa*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will compute any 2-digit × 11 product where the digit-sum is less than 10, in under 3 seconds, and will have recorded a personal baseline time for the same problem using standard long multiplication.

## Materials

- Printed baseline sheet: ONE multiplication problem (73 × 11). One per student.
- Stopwatch or wall clock with a second hand. (One per pair is plenty.)
- Whiteboard / large paper to demonstrate.

## Vocabulary introduced today

- *Ekādhikena Pūrveṇa* (IAST: ekādhikena pūrveṇa; lit. "by one more than the previous") — the Sanskrit name Tirthaji (1965) gives the underlying sūtra. We use it as the cultural anchor; the technique is what students take home.

## Lesson flow

### Warm-up (5 min)

- Teacher: *"How long does it take you to compute 73 × 11 the normal way? Make a guess."*
- Take 3–4 guesses. Write the range on the board.

### Baseline timing (8 min)

- Hand out the baseline sheet face-down. Students write their name and predicted time on the back.
- On "Go," flip and solve 73 × 11 using long multiplication.
- Record actual time honestly. Mark answer themselves.
- Expected range: 15–60 seconds.

### Teacher demonstration (12 min) — The trick

- Write on the board:

  ```
  73 × 11 = ?
  ```

- *"I'm going to show you a method that takes about 2 seconds, then we'll figure out why it works."*

  ```
  Step 1: Write the digits, with a gap:    7  _  3
  Step 2: Add the two digits: 7 + 3 = 10.
                                Wait — that's the carry case. Park it.
  ```

- *Reset. Different number first.* Try **23 × 11**:

  ```
  Step 1: Split:    2  _  3
  Step 2: Add:      2 + 3 = 5
  Step 3: Drop in:  2  5  3   →   253.
  ```

  Check on the board with long multiplication: 23 × 11 = 23 × 10 + 23 = 230 + 23 = 253. ✓

- Try **45 × 11**:
  ```
  4 _ 5  →  4 + 5 = 9  →  4 9 5  →  495.
  ```

- Try **62 × 11**:
  ```
  6 _ 2  →  6 + 2 = 8  →  6 8 2  →  682.
  ```

- *"Pattern: outer digits stay the same; middle digit = their sum."*

- Now name it. *"Tirthaji (1965) calls this **Ekādhikena Pūrveṇa** — 'by one more than the previous.' That is the Sanskrit name of the sūtra. The trick itself is just (10a + b) × 11 = 100a + 10(a+b) + b, which we'll prove on Day 3."*

### Activity (15 min) — Try it yourself

- Worksheet (handed out): 10 two-digit × 11 problems, ALL with digit-sum < 10.

  ```
  12 × 11    23 × 11    34 × 11    45 × 11    52 × 11
  61 × 11    16 × 11    27 × 11    35 × 11    44 × 11
  ```

- Pair work. Partner times each other. Goal: each problem under 3 seconds.

- After 10 min, students re-do **73 × 11** on the back of the baseline sheet. *Hmm — 7 + 3 = 10. That's tomorrow's lesson.*

### Wrap-up (5 min)

- Show of hands: who finished all 10 in under 30 seconds? (Most will.)
- Tease tomorrow: *"73 × 11 broke the rule because 7 + 3 = 10 and you can't write 10 in the middle of a number. Tomorrow — the carry case."*

## Student-facing content

> **The ×11 Trick (no-carry case)**
>
> For any 2-digit number with digit-sum < 10:
> 1. **Split** the digits with a gap.
> 2. **Add** the two digits.
> 3. **Drop** the sum into the gap.
>
> Example: 34 × 11 → 3 _ 4 → 3+4 = 7 → 374.
>
> Tirthaji (1965) names the underlying sūtra ***Ekādhikena Pūrveṇa*** — "by one more than the previous." The trick is older than its modern Sanskrit name; the algebra (which we'll do on Day 3) is the same in every language.

## Homework

- Find any two 2-digit numbers (digit-sum < 10) in your house — phone numbers, page numbers, prices. Compute each × 11 using the trick. Bring 5 worked examples to class tomorrow.

## Differentiation

- **Tier up:** Try 3-digit × 11 (e.g. 234 × 11, 152 × 11). See if you can guess the pattern before Day 4.
- **Tier down:** If the gap is confusing, write the answer as a 3-digit number directly: hundreds = first digit, tens = sum, units = second digit.

## Teacher notes

- **The baseline time matters.** Day 5's retest depends on having a Day 1 record.
- Don't dwell on the Sanskrit name today. *Ekādhikena Pūrveṇa* is the cultural anchor; the win is mental speed.
- Some students will already know the trick (especially those from competitive-math backgrounds). Have them be peer-coaches. Reframe their advantage as "you'll learn the WHY this week."
- About 30% of randomly-chosen 2-digit numbers have digit-sum ≥ 10 (the carry case). So today's worksheet hand-picks the no-carry ones; tomorrow we add the carries.

## Citation(s) used in this lesson

- Tirthaji, B. K. (1965). *Vedic Mathematics*. Motilal Banarsidass. Sūtra 1, *Ekādhikena Pūrveṇa*.
