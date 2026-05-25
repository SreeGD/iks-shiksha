# Day 2 — The Carry Case

**Module:** ×11 (*Ekādhikena Pūrveṇa*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will correctly handle the carry case in 2-digit × 11 (where the digit sum ≥ 10), including problems like 87 × 11 = 957, in under 5 seconds.

## Materials

- Whiteboard.
- Printed worksheet of 12 problems, mixing no-carry and carry cases.
- Stopwatch.

## Lesson flow

### Warm-up (5 min)

- Neighbour-sum drill: teacher calls a 2-digit number with digit-sum < 10; class chorus the ×11 product.
- *"12 times 11!" → "132!" — "34 times 11!" → "374!" —* 10 in a minute.

### Recall (3 min)

- Yesterday's problem: 73 × 11. 7 + 3 = 10. Why was this awkward?
- *"You can't put 10 in the middle of a 3-digit number. So what do we do? Carry the 1 — exactly like in standard addition."*

### Core (15 min) — The carry case

1. **Demonstrate 73 × 11 fully:**

   ```
   Step 1: Split:    7  _  3
   Step 2: Add:      7 + 3 = 10
   Step 3: Write the units digit of the sum (0) in the middle:    7  0  3
   Step 4: Carry the tens digit of the sum (1) into the leftmost digit: 7 + 1 = 8.
   Step 5: Answer:   8  0  3   →   803.
   ```

   Check: 73 × 11 = 73 × 10 + 73 = 730 + 73 = **803**. ✓

2. **Try 87 × 11:**

   ```
   8  _  7
   8 + 7 = 15
   Middle = 5; carry 1 into the 8 → 9.
   Answer: 9  5  7 → 957.
   ```

   Check: 87 × 11 = 870 + 87 = **957**. ✓

3. **Try 99 × 11:**

   ```
   9 _ 9
   9 + 9 = 18
   Middle = 8; carry 1 into the 9 → 10.
   But 10 isn't a single digit — so it becomes a "1" carried further: leftmost = 0, with a 1 carried to the left of that.
   Answer: 1  0  8  9 → 1089.
   ```

   Check: 99 × 11 = 990 + 99 = **1089**. ✓ (4-digit answer because the carry cascaded.)

4. **The full procedure** (boxed on the board):

   > **For any 2-digit number *ab* × 11:**
   > 1. Compute *a* + *b*.
   > 2. If the sum is < 10: answer is *a* (*a+b*) *b*.
   > 3. If the sum is ≥ 10: middle digit = units digit of sum; add 1 to *a*.
   > 4. If the new *a* is ≥ 10 (only happens at 99): cascade the carry.

### Activity (17 min) — Mixed practice

- Worksheet of 12 problems, half no-carry, half carry:

  ```
  21 × 11    35 × 11    47 × 11    58 × 11
  62 × 11    74 × 11    83 × 11    89 × 11
  91 × 11    99 × 11    18 × 11    27 × 11
  ```

- Round 1 (8 min): solo, untimed. Self-check with long multiplication on any 3 of them.
- Round 2 (8 min): paired. Partner calls a problem; you answer aloud. Goal: under 5 seconds per problem.

### Wrap-up (5 min)

- Quick chorus: *"What does the trick break into?"* — Split, add, drop (and carry if needed).
- Tease Day 3: *"Tomorrow we PROVE why this works. You'll write the algebra yourself."*

## Student-facing content

> **The ×11 Trick (with carry)**
>
> 1. Split the digits.
> 2. Add them.
> 3. **If the sum < 10:** drop it in the middle. Done.
> 4. **If the sum ≥ 10:** keep the units digit of the sum as the middle; add 1 to the leftmost digit.
>
> Examples:
> - 45 × 11: 4+5=9 → 4**9**5 = **495**
> - 87 × 11: 8+7=15 → 8**(1)5**7 → **9**57 = **957**
> - 99 × 11: 9+9=18 → 9**(1)8**9 → cascade → 1**0**89 = **1089**

## Homework

- 8 mental ×11 problems (carry case): 76, 84, 85, 88, 93, 96, 67, 78 — multiplied by 11. Write the answers.
- Time yourself. Goal: under 30 seconds total.

## Differentiation

- **Tier up:** Find a 2-digit number where the trick gives a 4-digit answer (i.e. 99 × 11 = 1089). Can you find any others, or is 99 unique? Justify.
- **Tier down:** Solve only the no-carry problems on the worksheet today. We'll cement carries on Day 4.

## Teacher notes

- The most common error: students remember to write the units digit of the middle sum but **forget** to add the carry into the leftmost digit. Watch for "73 × 11 = 7**0**3" with no carry added — this is a classic mistake.
- The 99 × 11 case (and the cascading carry) genuinely surprises students. Lean into it — it's evidence the algebra is doing real work, not arithmetic by coincidence.
- If a student asks "why does this work?" — that's Day 3. Park it. Honour the curiosity by writing the question on a board sticky.

## Citation(s) used in this lesson

- Tirthaji (1965), sūtra 1 (*Ekādhikena Pūrveṇa*) — the technique name.
- *Vedic Mathematics Batch1.pdf* (Vedic Cultural Center) — worked examples of the carry case.
