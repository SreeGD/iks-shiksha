# Day 2 — The Magic Constant

**Module:** Magic Squares (*Bhadragaṇita*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will (a) derive the magic constant *S = n(n² + 1)/2* for the 3×3 case by direct argument, and (b) apply the formula to predict the constant for *n* = 4, 5, 6, 7.

## Materials

- Whiteboard
- Notebook + pen
- The 3×3 magic square from Day 1, visible on the board

## Vocabulary review

- *magic square*, *magic constant* — defined Day 1.

## Lesson flow

### Warm-up (5 min)

- Recall chant: *"3×3 square with 1 to 9 — magic constant is ____?"* Class: "15."
- *"Why exactly 15, though? Why not 14 or 17?"* Take 2 student responses.

### Core (20 min)

1. **The sum argument.** Write on the board:

   > Add up all the numbers in the square: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45.

   *"This total goes into the square once. Now — the square has 3 rows. Each row has the same sum S. So 3 × S = 45 → S = 15."*

   Repeat the logic with student input. They should arrive at the formula step-by-step.

2. **Generalise.** For an *n × n* square containing the numbers 1, 2, ..., *n*²:

   > Sum of all numbers = 1 + 2 + ... + *n*² = *n*²(*n*² + 1) / 2
   >
   > The square has *n* rows, each summing to *S*. So:
   >
   > *n* × *S* = *n*²(*n*² + 1) / 2 → **S = n(n² + 1) / 2**

3. **Apply.** Compute together for several *n*:

   | *n* | *n*² | *n*²+1 | *n*(*n*²+1)/2 |
   |-----|------|--------|---------------|
   | 3   | 9    | 10     | 3 × 10 / 2 = **15** |
   | 4   | 16   | 17     | 4 × 17 / 2 = **34** |
   | 5   | 25   | 26     | 5 × 26 / 2 = **65** |
   | 6   | 36   | 37     | 6 × 37 / 2 = **111** |
   | 7   | 49   | 50     | 7 × 50 / 2 = **175** |

4. **A paraphrase from the source.** Nārāyaṇa Paṇḍita, in *Bhadragaṇita* (Book 14 of *Gaṇita-kaumudī*, 1356 CE), gives the magic-constant rule explicitly: the common sum is one *n*-th of the sum of the numbers in the square. We've just re-derived his rule. *(See `sources.md`.)*

### Activity (15 min) — Formative quiz Part A

- Hand out `quizzes/formative.md` Part A.
- Students complete individually. 10 minutes; 3 minutes for self-check against the board answer key.
- Part A is 6 short questions: 3 on the formula, 3 on verifying given squares.

### Wrap-up (5 min)

- *"Quick check: what would the magic constant be for a 10×10 magic square with the numbers 1 to 100?"* Class works it out: S = 10 × 101 / 2 = **505**.
- Preview Day 3: *"Tomorrow we ask: how many different 3×3 magic squares are there with 1 to 9? Take guesses tonight."*

## Student-facing content

> **The magic constant formula.**
>
> For an *n × n* magic square containing the numbers 1, 2, ..., *n*²:
>
> > **S = n(n² + 1) / 2**
>
> **Why?** The sum of all *n*² numbers is *n*²(*n*² + 1) / 2 (the standard sum-to-*n* formula). This total is split equally among the *n* rows, each of which sums to *S*. So *n × S* = *n*²(*n*² + 1) / 2 → divide both sides by *n*.
>
> | *n* | Constant |
> |-----|----------|
> | 3 | 15 |
> | 4 | 34 |
> | 5 | 65 |
> | 6 | 111 |
> | 7 | 175 |
>
> Nārāyaṇa Paṇḍita stated this rule in *Bhadragaṇita* (1356 CE).

## Homework

- Verify the formula for *n* = 8 and *n* = 9. (Answers: 260 and 369.)
- For each, also compute the total sum *n*²(*n*² + 1)/2 directly and confirm it equals *n × S*.

## Differentiation

- **One tier up:** What if the magic square contains *consecutive* numbers but starting at *k*, not at 1? (E.g. a 3×3 with 5, 6, 7, ..., 13.) Derive a formula for the new magic constant. (Answer: *S* = *n × k* + *n*(*n*²−1)/2.)
- **One tier down:** Focus on the 3×3 case alone. Verify the constant 15 by summing every row, column, and diagonal of the Day-1 square. Do it slowly.

## Teacher notes

- A common stumble: students compute 1 + 2 + ... + 9 incorrectly. Remind them that 1+9, 2+8, 3+7, 4+6 each = 10, plus 5 = 45. This itself is a pretty argument worth pausing on.
- For the generalisation, some students will struggle with the *n*² notation. Walk them through the *n* = 5 case explicitly: 1 + 2 + ... + 25 = 25 × 26 / 2 = 325; split among 5 rows → 65.
- The formula *S = n(n² + 1)/2* is **the** rule of this module. Drill it.

## Citation(s) used in this lesson

- Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī*, Book 14 (*Bhadragaṇita*), 1356 CE — paraphrased here: the magic constant equals one *n*-th of the total sum of the *n*² entries.
