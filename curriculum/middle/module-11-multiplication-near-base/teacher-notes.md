# Teacher Notes — Module 11 Multiplication Near a Base (Middle)

## Posture

This module trades on a specific, narrow win: when both factors are within ~5–10 of a power of 10, the Nikhilam method beats long multiplication by a wide margin. *Outside that regime, it loses.* Frame this honestly from Day 1. The point is not "Vedic math beats Western math" — both are useful in different regimes.

The Sanskrit sūtra name (*Nikhilam Navataścaramaṁ Daśataḥ*) is the cultural anchor. The *technique* is what students take home. Repeat the name often enough that students know what it sounds like by Day 6; don't quiz them on the Sanskrit until Day 10 (and even then it's a 1-mark question).

## Honest framing in three sentences

1. The *Nikhilam* sūtra name is genuine — it appears in Bharati Krishna Tirthaji's *Vedic Mathematics* (1965, posthumous; manuscript dated 1911–1918).
2. Tirthaji claimed the sūtra came from an *Atharva-veda Pariśiṣṭa* (Vedic appendix-text); **no other scholar has produced this manuscript**, and S. G. Dani (1993) argues the sūtras are 20th-century synthesis rather than ancient.
3. The mathematics is genuine and pedagogically valuable. The provenance is contested. At Middle band, just be honest about both; at Senior band, students read the debate.

Avoid claims like "ancient Indians knew this 3000 years ago." There is no scholarly evidence for that specific claim about this specific technique.

## Common misconceptions

1. **"This works for any multiplication."** No. It works *only* when both numbers are close to the same power of 10. 47 × 53 (not near 50, not near 100) loses every advantage. Day 8 handles this honestly.
2. **"The right part is just deficit × deficit, no rules."** Wrong — the right part must be padded to match the number of zeros in the base. For base 100, the right part takes *two* digits (e.g. `97 × 96 → 3 × 4 = 12 → '12'`); for `99 × 98 → 1 × 2 = 02`, not `2`. For base 1000, three digits.
3. **"If the right part overflows (≥ base), I'm stuck."** Handle by carrying. For 88 × 89: deficits 12 and 11; right part = 132 (3 digits, but base is 100 → 2-digit pad). Carry the 1 to the left part: left = (88 − 11) = 77 → 77 + 1 = 78; right = 32. Answer: 7832. Day 4 / Day 5 covers this gotcha.
4. **"In the mixed case (one above, one below) the right part is just deficit × excess."** Sign matters. For 102 × 98: excess +2, deficit −2. Right part = (+2)(−2) = −4. The "left" computed by either cross gives 100. So: 100 × 100 + (−4) = 10000 − 4 = 9996. Day 5 handles the sign care.
5. **"The dot/Nikhilam is the same as the long-multiplication carry."** Conceptually related but procedurally different. The deficit-and-cross is what makes it fast. Don't blur the methods on Day 1; introduce Nikhilam cleanly first.

## Differentiation hints

- **Tier up:** Move to base 50 (a "working base"). For 48 × 47, deficits from 50 are 2 and 3. Cross-subtract: 48 − 3 = 45. Multiply: 45 × 50 = 2250. Add the deficit product: 6. Answer 2256. Tirthaji calls this *sub-base* multiplication; sūtra *Ānurūpyeṇa*. Optional enrichment for fast finishers.
- **Tier down:** Stay with single-digit near-10 (7 × 8, 6 × 9) for the full first week. Don't push 2-digit until the student is fluent at the 1-digit case.

## Differential pacing

- A strong class can compress to 7 days by combining Days 3+4 and Days 5+6.
- A class shaky on multiplication tables should NOT skip Day 2. The "complement from 10" reflex is the prerequisite. Pull strugglers into extra drill at break.

## Sensitivity notes

- Timed mental-math activities can spike anxiety. Frame them as **personal baselines** — students race themselves over the module, not each other. No public leaderboards.
- Some families teach "Vedic mathematics" with religious / patriotic pride. The honest historical framing may feel diminishing. The teacher line: *"The method is a real Indian achievement. We just don't oversell its age."* If a parent objects, point them to the parent guide and offer to talk after class.
- Avoid framing this as "Indian math vs Western math." Both are useful. The standard long-multiplication algorithm is itself of mixed origin (al-Khwārizmī built on Brahmagupta).

## Common arithmetic errors to watch for

- **Forgetting to pad the right part.** 99 × 98 → right part = 2, but it should be `02`. Answer should be 9702, not 972.
- **Forgetting to carry when the right part overflows.** 88 × 89 → right part 132; needs to carry 1 to the left.
- **Sign error in mixed case.** Most students will try to write a negative right part directly. Show them the "borrow from the left" maneuver: 102 × 98 → left = 100, right = −4 → borrow 1 from left × 100 = 100; (99 × 100) + (100 − 4) = 9900 + 96 = 9996. Or compute directly: (100)(100) − 4 = 9996.
- **Confusion between base 10 and base 100.** For 9 × 8 (base 10), pad to 1 digit. For 99 × 98 (base 100), pad to 2 digits. Reinforce: number of zeros in base = number of digits in the padded right part.

## Project oversight

- Three project formats (60-sec teaching video, 20-problem workbook, comparative speed-test data project) each have different production challenges. See Module 5's notes for the cross-cutting issues — they apply here too.
- For the data project, students need a partner / family member who'll let themselves be timed on long multiplication. Confirm by Day 9 that this is actually arranged.

## Citation discipline

Citations for this module name **both** the Sanskrit sūtra (*Nikhilam Navataścaramaṁ Daśataḥ*) AND the modern source (e.g. *Vedic Mathematics Batch1.pdf*). Student projects should cite at minimum the modern PDF; mentioning the sūtra by name is encouraged but optional.

## If you only have 6 days

- Day 1: hook + baseline + Day 2 (deficit setup) combined.
- Day 2: Day 3 (both below 100) — the core case.
- Day 3: Day 5 (mixed cases) — covers Day 4 incidentally.
- Day 4: Day 7 (algebra) + Day 8 (when to use it) combined.
- Day 5: project work.
- Day 6: assessment + showcase.

Drop Day 6 (near 1000) and Day 9 (sprint) if pressed; preserve the algebra (Day 7) and the "when to use" discussion (Day 8).
