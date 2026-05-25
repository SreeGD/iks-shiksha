# Slide Deck — Module 9 Nikhilam Subtraction (Middle)

Source markdown for ~22 slides. Convert to PPTX via the `pptx` skill into `exports/pptx/middle-module-09-subtraction-nikhilam.pptx`.

---

# Module 9

## Subtraction by Complements — *Nikhilam Sūtra*

Grades 6–8 · 10 sessions

---

# How fast can you subtract?

`10 000 − 4 567 = ?`

How long would it take you? Make a guess.

---

# The sūtra — six Sanskrit words

> ***Nikhilaṁ Navataścaramaṁ Daśataḥ***
>
> "All from nine and the last from ten."

Tirthaji's *Vedic Mathematics* (1965), sūtra #2.

---

# What you'll learn

- Find the complement (*pūraka*) of any number to 100, 1000, 10 000.
- Subtract from any power of ten with NO borrowing.
- Combine the method for general subtractions like `8 243 − 567`.
- Explain *why* it works, algebraically.
- See the same idea in binary computers — *two's complement*.

---

# The rule applied to one example

`10 000 − 4 567`

|  | Apply rule | Result |
|---|---|---|
| 4 | from 9 | **5** |
| 5 | from 9 | **4** |
| 6 | from 9 | **3** |
| 7 | from 10 | **3** |

Answer: **5 433**. Check: 4 567 + 5 433 = 10 000. ✓

---

# Complement to 100

For 2-digit numbers AB:

- Tens digit: **9 − A**
- Units digit: **10 − B**

```
73 → 27         41 → 59
28 → 72         86 → 14
```

Aim: under 3 seconds per complement.

---

# Complement to 1000

For 3-digit numbers ABC:

- First: 9 − A
- Second: 9 − B
- Last: 10 − C

```
738 → 262       419 → 581
256 → 744       803 → 197
```

Same rule. One more "from 9" step.

---

# Padding rule

If the subtrahend has fewer digits than the base — pad with leading zeros.

```
1000 − 7    → treat as 1000 − 007  → 993
10 000 − 89 → treat as 10 000 − 0089 → 9 911
```

Common error: forgetting to pad.

---

# Why it works — the identity

> **10ⁿ − A = (10ⁿ − 1) − A + 1**

- `10ⁿ − 1` is "all nines."
- Subtracting A from all-nines: no borrow ever (9 ≥ any digit).
- The "+ 1" gets absorbed into the LAST digit.
- That's why "the last from ten" — `10 − x = (9 − x) + 1`.

Not magic. Just algebra.

---

# Bar model

```
|--------- 1000 ---------|
| 567 |   complement     |
|     |   = 433          |
```

Or: `999` is the bar shortened by 1.

`999 − 567 = 432`. Add the missing 1 back: `433`. Done.

---

# Honest history note

The sūtra is in Tirthaji's *Vedic Mathematics* (1965).

Tirthaji claims it comes from a Vedic appendix-text (*Atharva-veda Pariśiṣṭa*).

**No other Sanskritist has produced that text.**

The method is real. The Vedic provenance is unverified.

---

# Two's complement = Nikhilam in base 2

|  | Base 10 | Base 2 |
|---|---|---|
| Max digit | 9 | 1 |
| "All from max" | from 9 | flip each bit |
| "Last from base" | from 10 | add 1 |

Same algebra. Different base.

---

# Binary example

`7 − 5` in 4 bits:

- 7 = `0111`, 5 = `0101`
- Two's-comp of 5: flip → `1010`, +1 → `1011`
- Add: `0111 + 1011 = 1 0010`
- Drop top bit: `0010` = **2** ✓

Your phone's CPU does this in nanoseconds.

---

# General subtraction

`8 243 − 567`

Identity: **M − S = (M − B) + (B − S)**

- Pick base B = 1000 (closest power of 10 > 567)
- Complement: B − S = 433
- M − B = 7 243
- Answer: 7 243 + 433 = **7 676** ✓

---

# When to pick which method

| Situation | Faster |
|---|---|
| From 100 / 1000 / 10 000 | Nikhilam |
| Subtrahend close to round base | Nikhilam + adjust |
| Both mid-range | Standard borrowing |
| Both small | Either |

The mature move: pick the right tool.

---

# Activity: Complement Drill (Day 4)

8 mixed problems.

Pair self-correction.

By end of class: `1000 − N` in under 5 sec each.

---

# Activity: Shopkeeper Role-Play (Day 8)

Pretend currency.

10 transactions.

Compute change mentally.

By end of class: full transaction in under 10 sec.

---

# Your project (Days 8–10)

Pick ONE format:

1. **Shopkeeper's quick-change chart** — usable by a real shopkeeper
2. **60-second teaching video** — Grade 4 audience
3. **Two's-complement explainer poster** — connect to binary CS

---

# What we'll grade you on

- **Method demonstrated correctly** (×2)
- **Use of sources** (×1.5) — Tirthaji + one supporting
- **Audience suitability** (×1.5)
- **Originality** (×1)
- **Communication / craft** (×1)
- **+2 honesty bonus** for engaging with the provenance question

See the rubric.

---

# Sources

- Tirthaji, *Vedic Mathematics* (1965), sūtra Nikhilam — primary
- *Microsoft Word - sutras1.pdf* — sūtra list
- *FUNDAMENTAL AND VEDIC MATHEMATICS .pdf* — worked examples
- *Patterson & Hennessy, Computer Organization* — for two's complement

All in `sources.md`.

---

# Day 10

- 20-min summative quiz (closed notebook, 25 marks)
- 3-min project presentations + 1-min Q&A
- Self-reflection slip

---

# What you take home

- The Sanskrit sūtra in memory.
- Fluent complements to any power of ten.
- A real algebraic understanding of why it works.
- The surprising binary connection.
- Honest framing of "what is and isn't Vedic."
- One artefact you can share.

---

# Questions?

---

# Thank you

> *Nikhilaṁ Navataścaramaṁ Daśataḥ* — and your time is yours back.

*śubham astu.*
