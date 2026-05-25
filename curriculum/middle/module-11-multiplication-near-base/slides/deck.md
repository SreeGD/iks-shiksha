# Slide Deck — Module 11 Nikhilam Multiplication (Middle)

Source markdown for ~22 slides. Convert to PPTX via the `pptx` skill into `exports/pptx/middle-module-11-multiplication-near-base.pptx`.

---

# Module 11

## Nikhilam — Multiplication of Numbers Close to a Power of 10

Grades 6–8 · 10 sessions

---

# 97 × 96 in three seconds

```
97 × 96 = ?
```

How long would it take you? Make a guess.

---

# The Nikhilam method — first look

```
    97 │ −3        ← 3 below 100
  × 96 │ −4        ← 4 below 100
  ────┼────
    93 │ 12        → 9312
```

`97 − 4 = 93` (or `96 − 3 = 93`).
`3 × 4 = 12`.

Same answer. Different speed.

---

# What you'll learn

- Find each number's **deficit** from a base (10, 100, 1000).
- **Cross-subtract** for the left part.
- **Multiply deficits** for the right part.
- **Pad** the right to match the base.

By Day 9, you'll re-do `97 × 96` 5–10× faster than Day 1.

---

# The foundational skill: complement from 10

```
1 → 9    2 → 8    3 → 7    4 → 6    5 → 5
6 → 4    7 → 3    8 → 2    9 → 1
```

This is the same drill from Module 5 / Module 9. Reuse it.

Recall any deficit in under 1 second.

---

# Single-digit example (base 10)

```
    7 │ −3
  × 8 │ −2
  ───┼────
    5 │ 6        → 56
```

`7 − 2 = 5`. `3 × 2 = 6`. Done.

---

# Both below 100

| Problem | Deficits | Left | Right | Answer |
|---|---|---|---|---|
| 97 × 96 | 3, 4 | 93 | 12 | **9312** |
| 99 × 98 | 1, 2 | 97 | **02** | **9702** |
| 88 × 89 | 12, 11 | 77+1 | 32 | **7832** |

Pad to **2 digits**. Carry the overflow.

---

# Both above 100

```
    103 │ +3
  × 104 │ +4
  ─────┼─────
    107 │ 12     → 10712
```

Cross-**ADD** (instead of subtract).

`103 + 4 = 107`. `3 × 4 = 12`. Pad to 2 digits.

---

# Mixed case (one above, one below)

```
    102 │ +2
  ×  98 │ −2
  ─────┼─────
    100 │ −4     → 10000 − 4 = 9996
```

Right part is **negative**.

Subtract from `LEFT × 100`.

---

# Near 1000

```
    998 │ −2
  × 997 │ −3
  ─────┼──────
    995 │ 006    → 995006
```

Pad to **3 digits** (because base 1000 has 3 zeros).

General rule: pad-width = number of zeros in base.

---

# The carry-overflow case

```
    88 │ −12
  × 89 │ −11
  ───┼─────
    77 │ 132    overflow!

  carry 1 to left → 78 │ 32  → 7832
```

If RIGHT ≥ base, carry the overflow to the LEFT.

---

# Why it works

```
(B − a)(B − b) = B² − B(a + b) + ab
              = B(B − a − b) + ab
              = B · LEFT + RIGHT
```

- LEFT = `B − a − b` (cross-subtract).
- RIGHT = `ab` (deficit × deficit).
- Concatenation = `B × LEFT + RIGHT`.

Not magic. Just algebra.

---

# The Sanskrit sūtra

***Nikhilam Navataścaramaṁ Daśataḥ***

"All from 9 and the last from 10"

— Tirthaji's 2nd sūtra, from *Vedic Mathematics* (1965).

Same sūtra you used in **Module 9** for subtraction.

---

# When NOT to use Nikhilam

| Use Nikhilam | Use long multiplication |
|---|---|
| Both factors near same power of 10 | One factor "random" |
| `97 × 96`, `103 × 104`, `998 × 997` | `47 × 53`, `73 × 84` |

The method has a **narrow regime**. Long multiplication remains the workhorse.

---

# The other Tirthaji sūtra (Day 8 mention)

***Ūrdhva-tiryagbhyāṁ*** — "vertically and crosswise."

The **general** multiplication sūtra (any two numbers).

Topic for a future module. Just notice: Ūrdhva covers what Nikhilam can't.

---

# A historical note

The Nikhilam name and the multiplication procedure appear in **Tirthaji's *Vedic Mathematics*** (published 1965, posthumous; manuscript dated 1911–1918).

Tirthaji claimed the sūtras came from an *Atharva-veda Pariśiṣṭa*. **No other scholar has produced this manuscript.**

Modern historians (Dani 1993, Plofker 2009) treat the system as **20th-century synthesis**, not strictly ancient.

The math is real. The history is contested.

---

# Day 1 baseline → Day 9 retest

Same problem: `97 × 96`.

Day 1 (long multiplication): _____ sec
Day 9 (Nikhilam): _____ sec

The visible speedup is the proof.

---

# Sprint activity (Day 9)

10 problems. 3 minutes.

Mix of: both-below, both-above, mixed, near-1000.

By end: sub-10-sec on any 2-digit Nikhilam problem.

---

# Your project (Days 9–10)

Pick ONE format:

1. **60-second teaching video** — teach Grade 4.
2. **Printed workbook** — 20 problems, 4 difficulty levels.
3. **Comparative data project** — time 5–10 people on long vs. Nikhilam.

---

# What we'll grade you on

- **Method demonstrated correctly** (×2)
- **Use of sources** (×1.5) — cite the PDF + sūtra
- **Audience suitability** (×1.5)
- **Originality** (×1)
- **Communication / craft** (×1)

Plus: **acknowledge when NOT to use Nikhilam** → "Exceeds" bonus.

---

# Sources

- *Vedic Mathematics Batch1.pdf* (Vedic Cultural Center, Sammamish WA)
- *Microsoft Word - sutras1.pdf* — Tirthaji's 16 sūtras
- *Vedic_Maths.pdf* (ISKCON Desire Tree) — practice problems

All in `sources.md`.

---

# Day 10

- 15-min summative quiz (closed notebook).
- 3-min project presentations + 1-min Q&A.
- Reflection slip.

---

# What you take home

- Mental multiplication of 2-digit pairs near 100 in under 5 seconds.
- Knowing **when** to use Nikhilam — and when not to.
- An algebraic proof of the method.
- Honest understanding of what "Vedic mathematics" includes and what it doesn't.

---

# Questions?

---

# Thank you

*śubham astu*
