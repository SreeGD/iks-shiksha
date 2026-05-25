# Day 4 — Three-Digit × 11

**Module:** ×11 (*Ekādhikena Pūrveṇa*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will compute any 3-digit × 11 product using the running "neighbour-sum" pattern, including carry cases, and will complete Part A of the formative quiz.

## Materials

- Whiteboard.
- Printed worksheet of 10 three-digit × 11 problems.
- Formative quiz Part A (`quizzes/formative.md`).

## Lesson flow

### Warm-up (5 min)

- Neighbour-sum chorus: 10 quick 2-digit × 11 problems including carry cases. (Should be near-instant by now.)

### Core (18 min) — The 3-digit pattern

1. **Set up.** *"Yesterday we proved (10a+b)×11. What happens with a 3-digit number 100a + 10b + c?"*

2. **Derive together** (or have students derive):

   ```
   (100a + 10b + c) × 11
       = (100a + 10b + c)(10 + 1)
       = 1000a + 100b + 10c + 100a + 10b + c
       = 1000a + 100(a + b) + 10(b + c) + c
   ```

3. **Read the result.** *"Thousands = a. Hundreds = a + b. Tens = b + c. Units = c."*

   In words: **first digit stays, then each pair of adjacent digits sums and slides into the gap, then the last digit stays.**

4. **Worked example: 234 × 11.**

   ```
   Splits and gaps:    2  _  _  4
                        ↑     ↑
                     (a+b) (b+c)
   2 + 3 = 5
   3 + 4 = 7
   Answer:             2  5  7  4   →   2574.
   ```

   Check: 234 × 11 = 234 × 10 + 234 = 2340 + 234 = **2574**. ✓

5. **Worked example with carry: 567 × 11.**

   ```
   5  _  _  7
   5 + 6 = 11   ← carry case
   6 + 7 = 13   ← carry case
   ```

   Strategy: work **right to left** to handle carries properly.

   ```
   Units: 7.
   Tens: b + c = 6 + 7 = 13. Write 3, carry 1.
   Hundreds: a + b + carry = 5 + 6 + 1 = 12. Write 2, carry 1.
   Thousands: a + carry = 5 + 1 = 6.
   Answer:    6  2  3  7   →   6237.
   ```

   Check: 567 × 11 = 5670 + 567 = **6237**. ✓

6. **Generalisation.** For an *n*-digit number, the trick is the same pattern:
   - Outer digits stay.
   - Every interior digit becomes the sum of the two original digits flanking that position.
   - Carries cascade from right to left.

### Activity (15 min) — Worksheet

- 10 problems mixing 3-digit no-carry and carry cases:

  ```
  123 × 11    234 × 11    345 × 11    456 × 11    142 × 11
  365 × 11    478 × 11    529 × 11    687 × 11    818 × 11
  ```

- Pair work, self-check by long multiplication on any 3.

### Formative Quiz Part A (5 min)

- Distribute `quizzes/formative.md` Part A.
- 5 quick problems, mixed 2- and 3-digit × 11. Closed-notebook.

### Wrap-up (2 min)

- Preview Day 5: *"Tomorrow — speed day. We'll retest your Day 1 problem (73 × 11) using the trick."*

## Student-facing content

> **3-digit × 11**
>
> For a number *abc* × 11:
> 1. Write *a _ _ c* (outer digits unchanged).
> 2. Fill the first gap with *a* + *b*.
> 3. Fill the second gap with *b* + *c*.
> 4. Handle carries right to left.
>
> Example: 234 × 11 → 2 _ _ 4 → 2 (2+3) (3+4) 4 → 2574.
>
> The algebraic identity: (100*a* + 10*b* + *c*) × 11 = 1000*a* + 100(*a*+*b*) + 10(*b*+*c*) + *c*.

## Homework

- Solve 10 three-digit × 11 problems on the back of today's worksheet. Time yourself — goal: under 90 seconds total.

## Differentiation

- **Tier up:** Try a 4-digit × 11 problem. Derive the pattern first (the identity will give you 5 terms). Test on 2345 × 11.
- **Tier down:** Stay on 2-digit × 11 problems with carries; build speed there before adding the 3-digit layer.

## Teacher notes

- The right-to-left direction for carry handling is the key procedural insight. Some students will try left-to-right and run into trouble; redirect them.
- For 567 × 11, the cascading carries (13 in tens, 12 in hundreds) are dramatic. Use that example.
- The pattern is sometimes taught with "underline carries" notation; we use right-to-left because it generalises better to *n*-digit numbers.

## Citation(s) used in this lesson

- *Vedic_Maths.pdf* (ISKCON Desire Tree) — practice problems.
- Tirthaji (1965), sūtra 1.
