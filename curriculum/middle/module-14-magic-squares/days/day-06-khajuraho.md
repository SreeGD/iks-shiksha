# Day 6 — The 4×4 Square and Khajuraho

**Module:** Magic Squares (*Bhadragaṇita*) · **Band:** Middle · **Time:** 45 min

## Learning objective

By the end of this lesson, students will (a) recognise the Khajuraho 4×4 magic square, (b) verify its rows, columns, diagonals, and 2×2 panels all sum to 34, and (c) explain why this "panel-magic" property is *stronger* than the basic magic-square property.

## Materials

- Printed image of the Khajuraho inscription panel (or a clean diagram of the square)
- Printed copy of the Khajuraho 4×4 grid (one per student) for sum-checking
- Coloured pencils

## Vocabulary introduced today

- *Khajuraho* — site in Madhya Pradesh, India, with a temple complex dating to roughly the 10th–11th c. CE (Chandela dynasty). One temple wall carries a numbered 4×4 grid inscription.
- *panel-magic square* (also called *pandiagonal* or *most-perfect* in modern terminology) — a magic square where, in addition to rows, columns, and main diagonals, **every 2×2 panel** sums to the magic constant, and so do the **broken diagonals**.

## Lesson flow

### Warm-up (5 min)

- *"Yesterday you built a 5×5 from scratch. The same algorithm doesn't work for 4×4 — odd-order only. Today we look at one famous 4×4 — from a temple wall in central India, roughly 10th–11th c. CE."*
- Show the Khajuraho image. Don't analyse yet. Just let students look.

### Core (20 min)

1. **The Khajuraho 4×4.** Project or hand out:

   ```
    7 | 12 |  1 | 14
   ----------------
    2 | 13 |  8 | 11
   ----------------
   16 |  3 | 10 |  5
   ----------------
    9 |  6 | 15 |  4
   ```

   *"Magic constant should be 34. Let's verify."* Walk through together:

   - Row 1: 7 + 12 + 1 + 14 = 34 ✓
   - Row 2: 2 + 13 + 8 + 11 = 34 ✓
   - Rows 3, 4 — students verify independently.
   - All four columns — students verify in pairs.
   - Both main diagonals: 7+13+10+4 = 34 ✓; 14+8+3+9 = 34 ✓.

2. **The "extra magic" — panel sums.** *"Try any 2×2 block. Does it also sum to 34?"*

   Pick a few:
   - Top-left 2×2: 7 + 12 + 2 + 13 = 34 ✓
   - Top-right 2×2: 1 + 14 + 8 + 11 = 34 ✓
   - Centre 2×2: 13 + 8 + 3 + 10 = 34 ✓
   - Any 2×2, including those that "wrap" around the edge: also 34.

   *"This is a stronger property than just being a magic square. It is called* **panel-magic** *(or* most-perfect *or* pandiagonal*). Not every magic square has this."*

3. **A historical note.** The Khajuraho square is a real artefact — carved into a temple wall during the Chandela dynasty (~10th–11th c. CE). It is one of the earliest dated panel-magic 4×4 squares we have evidence of, anywhere. It predates Nārāyaṇa Paṇḍita (1356 CE) by several centuries; Nārāyaṇa later gave systematic methods for constructing such squares.

   **Honest framing:** the exact dating of the Khajuraho inscription is debated among historians, but most place it in the 10th–11th century CE. The Chandela dynasty built the temple complex roughly between 950 and 1050 CE.

4. **The 4×4 construction (preview, not drilled).** The 4×4 cannot be built with the *turagagati* method. Nārāyaṇa's *Bhadragaṇita* gives a different recipe for orders divisible by 4 (called the *complement method*):

   - Fill the 4×4 with 1–16 in natural order.
   - Mark the cells on both main diagonals.
   - For each *unmarked* cell, replace its value *v* with *17 − v* (its complement to 17).

   Demonstrate this on the board:

   Natural-order fill:
   ```
    1 |  2 |  3 |  4
   ----------------
    5 |  6 |  7 |  8
   ----------------
    9 | 10 | 11 | 12
   ----------------
   13 | 14 | 15 | 16
   ```

   After complementing unmarked cells:
   ```
    1 | 15 | 14 |  4
   ----------------
   12 |  6 |  7 |  9
   ----------------
    8 | 10 | 11 |  5
   ----------------
   13 |  3 |  2 | 16
   ```

   Verify one row, one column, one diagonal — all 34. *(Note: this is a standard magic square, but not the same as the Khajuraho one, and not all such are panel-magic.)*

### Activity (15 min) — Discussion + verification

- Pairs verify all eight 2×2 panels of the Khajuraho square — including the four "corner panels" formed by wrapping (top row joining bottom row, etc.).
- Class discussion: *"Why is the Khajuraho square called 'most-perfect'?"* — student answers. Note their wording. The teacher's frame: more constraints satisfied = more impressive.

### Wrap-up (5 min)

- *"Two takeaways. One: the 4×4 is built differently from the 5×5. Two: not all magic squares are equal — Khajuraho's is unusually strong."*
- Preview Day 7: *"Tomorrow we look at the mathematician who wrote down the methods: Nārāyaṇa Paṇḍita."*

## Student-facing content

> **The Khajuraho 4×4 magic square** — inscribed on a temple wall in Madhya Pradesh, ~10th–11th c. CE.
>
> ```
>  7 | 12 |  1 | 14
> ----------------
>  2 | 13 |  8 | 11
> ----------------
> 16 |  3 | 10 |  5
> ----------------
>  9 |  6 | 15 |  4
> ```
>
> Magic constant: 34.
>
> **Extra property:** every 2×2 panel also sums to 34. So do the "broken diagonals" (diagonals that wrap around the edges). This is called the **panel-magic** or **most-perfect** property — a much stronger constraint than the basic magic-square definition.
>
> Nārāyaṇa Paṇḍita, in *Bhadragaṇita* (Book 14 of *Gaṇita-kaumudī*, 1356 CE), gave systematic methods for constructing such squares centuries later — though the Khajuraho artefact itself predates his treatise by 300+ years.

## Homework

- Pick any 2×2 panel of the Khajuraho square. Verify the sum is 34. Now find a 2×2 panel that *wraps around* the edge (uses cells from both the top row and the bottom row). Verify that too. Write down both.

## Differentiation

- **One tier up:** Find a 4×4 magic square that is *not* panel-magic — i.e. its rows/columns/diagonals work but some 2×2 panel does not equal 34. (Hint: the complement-method result given above.)
- **One tier down:** Just verify the basic property — rows, columns, diagonals. The panel property can come later.

## Teacher notes

- Show the Khajuraho image if at all possible. Even a low-resolution photo. The artefact makes the lesson land.
- Don't oversell the dating. "10th–11th century" is the conservative estimate; some sources claim earlier. Use the conservative range.
- The complement method shown is one of several 4×4 construction methods. Don't drill it — Middle band only needs to know that *a* method exists.
- A few students will ask "is Sudoku a magic square?" Hold that question for Day 9. Short answer: no — Sudoku constrains rows/columns/boxes but not diagonals or sums.

## Citation(s) used in this lesson

- Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī*, Book 14 (*Bhadragaṇita*), 1356 CE — for the 4×4 construction methods.
- Material evidence: Khajuraho temple inscription (Madhya Pradesh, India), Chandela period (~10th–11th c. CE).
