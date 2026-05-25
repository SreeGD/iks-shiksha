# Slide Deck — Module 7 ×11 (Middle)

Source markdown for ~22 slides. Convert to PPTX via the `pptx` skill into `exports/pptx/middle-module-07-eleven-multiplication.pptx`.

---

# Module 7

## ×11 — *Ekādhikena Pūrveṇa*

Grades 6–8 · 10 sessions

---

# How fast can you do 73 × 11?

Try it now. Time yourself.

The usual way:
```
   73
×  11
-----
   73
 730+
-----
  803
```

How long did that take? 20 seconds? 40?

---

# Watch this

**23 × 11 = ?**

Split: **2 _ 3**

Add the digits: 2 + 3 = **5**

Drop in: **2 5 3 = 253**.

In under 2 seconds.

---

# The trick (no carry case)

For *ab* × 11, with *a* + *b* < 10:

> 1. **Split** the digits with a gap.
> 2. **Add** them.
> 3. **Drop** the sum in the middle.

Examples:
- 34 × 11 → 3 (7) 4 → **374**
- 52 × 11 → 5 (7) 2 → **572**
- 81 × 11 → 8 (9) 1 → **891**

---

# When the sum is ≥ 10 (carry case)

**73 × 11:** 7 + 3 = 10. Can't put 10 in the middle.

Fix: write the **units digit** of the sum (0) in the middle, carry the **1** into the leftmost digit (7 → 8).

```
73 × 11 = 7  (10)  3
        = 8    0   3 = 803.
```

Check: 73 × 10 + 73 = 730 + 73 = **803**. ✓

---

# The dramatic case: 99 × 11

```
99 × 11:
  9 + 9 = 18
  Middle = 8; carry 1 into the leftmost 9 → 10.
  But 10 isn't a single digit — cascade.
  Answer: 1 0 8 9 = 1089.
```

Check: 99 × 11 = 990 + 99 = **1089**. ✓

---

# Why it works — the algebra

For *ab* = 10*a* + *b*:

```
(10a + b) × 11
    = (10a + b)(10 + 1)
    = 100a + 10b + 10a + b
    = 100a + 10(a + b) + b.
```

In plain English:
- Hundreds = *a*
- Tens = *a* + *b*
- Units = *b*

**That IS the trick.** It is not magic. It's the distributive law.

---

# 3-digit × 11

Pattern for *abc* × 11:

```
a  (a+b)  (b+c)  c
```

Example: **234 × 11 → 2 5 7 4 = 2574.**

Carries cascade right-to-left.

---

# A 3-digit carry example: 567 × 11

```
5  _  _  7
b + c = 6 + 7 = 13   → write 3, carry 1
a + b + carry = 5 + 6 + 1 = 12   → write 2, carry 1
a + carry = 5 + 1 = 6
Answer: 6 2 3 7 = 6237.
```

Check: 567 × 11 = 5670 + 567 = **6237**. ✓

---

# Extending: ×12 to ×19 — *Anurūpyeṇa*

The same idea, scaled by *k* (where multiplier = 10 + *k*):

For *ab* × (10+*k*):
- units = *b* × *k* (carry if ≥ 10)
- tens = *a* × *k* + *b* + carry
- hundreds = *a* + carry

When *k* = 1 (i.e. ×11), it's the original trick.

Tirthaji (1965) names this *Anurūpyeṇa* — "proportionally."

---

# Worked example: 45 × 13

```
units = 5 × 3 = 15   → write 5, carry 1
tens = 4 × 3 + 5 + 1 = 18   → write 8, carry 1
hundreds = 4 + 1 = 5
Answer: 5 8 5 = 585.
```

Check: 45 × 13 = 450 + 135 = **585**. ✓

---

# When the trick doesn't help

The ×11-family trick works for multipliers **10 + *k*** (single digit *k*).

For multipliers FAR from 10 — like ×23, ×47, ×98 — use a different sūtra:

- **Nikhilam** (sūtra 2) — for numbers near 100.
- **Ūrdhva-tiryagbhyāṁ** (sūtra 3) — general multiplication.

Every trick has a domain.

---

# Where does the trick come from?

**Bharati Krishna Tirthaji** (1884–1960).
Śaṅkarācārya of Govardhana Maṭha, Puri.

Wrote *Vedic Mathematics* between roughly 1911 and 1918.
Manuscript published **1965** — five years after his death.

The book lists **16 sūtras** + 13 sub-sūtras.

---

# Is the trick "Vedic"?

Tirthaji claimed the sūtras come from an *Atharva-veda Pariśiṣṭa* — a Vedic appendix.

**The problem:** no other scholar has produced this manuscript.

**S. G. Dani** (mathematician, TIFR/IIT Bombay) published a critique in 1993 (reprinted *Resonance*, October 2001):
- No manuscript evidence.
- Sanskrit style not Vedic.
- Mathematical techniques have 20th-century parallels.

---

# Two things can be true

1. The trick **works**. It is a useful, elegant piece of arithmetic.

2. The trick is **probably not 3000 years old**. It's most likely Tirthaji's 20th-century synthesis.

The Indian intellectual achievement (the *pedagogy*) is real either way.

We teach the math enthusiastically. We are honest about the history.

---

# Day 1 baseline → Day 5 retest

Same problem (73 × 11).

Day 1 (long multiplication): your time
Day 5 (trick): your time

**% reduction:** mostly 70–80%.

The visible speedup is the proof.

---

# Activity: Speed Race (Day 5)

24 flashcards.

Round 1 solo. Round 2 paired. Round 3 chorus. Round 4 quick-fire.

Target: under 5 seconds per problem.

---

# Activity: *Anurūpyeṇa* drill (Day 6)

16 problems across ×12, ×13, ×14, ×17, ×19.

Paired self-check.

---

# Your project (Days 9–10)

Pick ONE format:

1. **60-second teaching video** — for Grade 4
2. **Printed workbook** — 25 problems, worked examples, answer key
3. **Proof poster** — derive (10*a*+*b*)·11 = 100*a* + 10(*a*+*b*) + *b*

---

# What we'll grade you on

- **Method demonstrated correctly** (×2)
- **Algebraic justification** (×1.5)
- **Use of sources** (×1)
- **Audience suitability** (×1)
- **Originality** (×0.5)
- **Communication / craft** (×1)

See the rubric.

---

# Sources

- Tirthaji, *Vedic Mathematics* (1965), Motilal Banarsidass — sūtra 1, *Ekādhikena Pūrveṇa*.
- *Microsoft Word - sutras1.pdf* — list of 16 sūtras.
- *Vedic_Maths.pdf* (ISKCON Desire Tree) — practice problems.
- Dani, S. G. (1993/2001) — historical critique.

All in `sources.md`.

---

# Day 10

- 15-min summative quiz (closed notebook).
- 2-min project presentations + 1-min audience question.
- Reflection slip.

---

# What you take home

- Mental ×11 (and ×12–×19) on any 2- or 3-digit number, fast.
- One algebraic identity: (10*a*+*b*) × 11 = 100*a* + 10(*a*+*b*) + *b*.
- Honest understanding of what "Vedic mathematics" includes — and what it doesn't.
- One artefact you can share with a younger student.

---

# Questions?

---

# Thank you

*śubham astu*
