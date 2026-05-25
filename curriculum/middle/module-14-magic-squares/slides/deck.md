---
marp: true
theme: default
class: lead
paginate: true
---

# Module 14
## Magic Squares — *Bhadragaṇita*
### Middle Band — Grades 6–8 · 10 sessions

---

## What is a magic square?

An *n × n* grid of distinct numbers where:

- Every **row** sums to the same total
- Every **column** sums to the same total
- Both main **diagonals** sum to the same total

That common total is the **magic constant**.

---

## The 3×3 with 1–9

```
2 | 7 | 6
---------
9 | 5 | 1
---------
4 | 3 | 8
```

Magic constant: **15**.

Verify: rows, columns, diagonals — all 15.

---

## The magic constant formula

For an *n × n* magic square with 1 to *n*²:

> ***S = n(n² + 1) / 2***

Because:
- Sum of 1 to *n*² = *n*²(*n*² + 1)/2
- Distributed across *n* equal rows → each row sums to *S*

---

## Quick table

| *n* | *S* |
|-----|-----|
| 3 | 15 |
| 4 | 34 |
| 5 | 65 |
| 6 | 111 |
| 7 | 175 |
| 8 | 260 |

---

## How many 3×3 magic squares are there?

With the numbers 1–9: **ONE** — up to symmetry.

- **8 arrangements** (4 rotations + 4 reflections)
- All the same square in disguise

5 must be in the centre. Even numbers at the corners.

---

## The stair-step rule (*turagagati*)

For odd-order *n × n*:

1. Place **1** in the **top-middle**.
2. From *k*, move **up-right** for *k* + 1.
3. Off-top → wrap to **bottom**.
4. Off-right → wrap to **left**.
5. **Blocked** → place *k* + 1 **directly below**.

---

## Nārāyaṇa Paṇḍita (14th c. CE)

- Wrote ***Gaṇita-kaumudī*** in **1356 CE**
- 14 books on math: arithmetic, algebra, combinatorics
- **Book 14: *Bhadragaṇita*** — magic squares
- The same odd-order method appeared in Europe ~1687 (de la Loubère) — 300+ years later

---

## Construct a 5×5

```
17 | 24 |  1 |  8 | 15
23 |  5 |  7 | 14 | 16
 4 |  6 | 13 | 20 | 22
10 | 12 | 19 | 21 |  3
11 | 18 | 25 |  2 |  9
```

Magic constant: 65.

Same rule. Different size.

---

## Khajuraho (India, ~10th–11th c. CE)

```
 7 | 12 |  1 | 14
 2 | 13 |  8 | 11
16 |  3 | 10 |  5
 9 |  6 | 15 |  4
```

Magic constant: **34**.

Also: every **2×2 panel** sums to 34. *Panel-magic.*

---

## The 4×4 needs a different method

The *turagagati* algorithm is **odd-order only**.

For 4×4, *Bhadragaṇita* gives the **complement method**:

- Fill 1–16 in natural order
- Replace each *off-diagonal* cell *v* with *17 − v*

A different rule for a different beast.

---

## Lo Shu (China, ~5th c. BCE attested)

```
4 | 9 | 2
---------
3 | 5 | 7
---------
8 | 1 | 6
```

Same 3×3 magic constant: **15**.

Same square as our Day-1 — just rotated.

---

## Dürer's *Melencolia I* (1514 CE)

```
16 |  3 |  2 | 13
 5 | 10 | 11 |  8
 9 |  6 |  7 | 12
 4 | 15 | 14 |  1
```

Magic constant: 34. **Panel-magic.**

Bottom-middle two cells: **15 14** = the year 1514.

---

## A cross-cultural pattern

| Square | Date | Culture | Order | Constant |
|--------|------|---------|-------|----------|
| Lo Shu | ~5th c. BCE | Chinese | 3 | 15 |
| Khajuraho | ~10th–11th c. | Indian | 4 | 34 |
| Nārāyaṇa | 1356 CE | Indian | any odd | varies |
| Dürer | 1514 CE | German | 4 | 34 |

No single inventor. Independent encounters (and some transmission).

---

## Sudoku vs magic square

| | Magic square | Sudoku 3×3 |
|---|---|---|
| Rows sum to same total? | **Yes** | No |
| Each row has all 9 digits? | No | **Yes** |
| Diagonals constrained? | **Sums** | Not required |

Different constraints. Both: constraint-satisfaction puzzles.

---

## Your project (Days 8–10)

Pick ONE format. Construct a 5×5 or larger:

1. **Labelled poster** — A3, step-by-step
2. **60-second demo video** — Grade 5 audience
3. **Written exposition** — 2 pages

Required: verification panel + citation.

---

## Citation format

> Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī*, Book 14 (*Bhadragaṇita*), 1356 CE.

Visible. Spoken (for video). Written (for poster and exposition).

---

## What we'll grade

- **Method correctly demonstrated** (× 2)
- **Magic constant verified** (× 1.5)
- **Source cited** (× 1)
- **Original design choice** (× 1)
- **Communication / craft** (× 0.5)

See `assessments/rubric.md`.

---

## Day 10

- 15-min summative quiz (closed notebook)
- 2-min project presentations + 1-min Q&A
- Reflection slip

---

## What you take home

- The *turagagati* algorithm, automatic.
- The magic-constant formula, memorised.
- Honest understanding: Nārāyaṇa was a systematiser, not the sole inventor.
- One artefact you can show a younger student tomorrow.

---

## Questions?

---

## Thank you

*śubham astu*
