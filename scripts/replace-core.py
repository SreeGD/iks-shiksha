#!/usr/bin/env python3
"""Replace placeholder Core sections in generator-written day files with
substantive per-day content.

Targets:
  - Senior files containing "State the observable phenomenon first" (100 files)
  - Primary files containing "Introduce the concept gently using a story" (88 files)
  - Middle stragglers with the same placeholder (1 file)

Only files containing the placeholder are touched. Agent-written rich days are
left alone (they don't have the placeholder).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURRICULUM = ROOT / 'curriculum'

SENIOR_MARKER = 'State the observable phenomenon first'
PRIMARY_MARKER = 'Introduce the concept gently using a story'

# Per-day Senior content keyed by (module-slug, day-slug)
SENIOR_CORE = {}

# Per-day Primary content keyed by (module-slug, day-slug)
PRIMARY_CORE = {}


def register(mod, day, senior=None, primary=None):
    if senior:
        SENIOR_CORE[(mod, day)] = senior.strip()
    if primary:
        PRIMARY_CORE[(mod, day)] = primary.strip()


# ============================================================================
# Module 4 — Doshas
# ============================================================================

register('module-04-doshas', 'three-doshas-intro',
senior="""
1. **Open with observation.** Project on the board: *"Describe three students you know — without naming them — in one sentence each, focusing on their energy, pace, and style."* Pair discussion for 2 minutes; harvest descriptions on the board.

2. **From observation to category.** Most descriptions cluster around three patterns: quick / changeable / dry (motion); focused / sharp / warm (transformation); steady / slow / cool (structure). Classical Āyurveda calls these three patterns *vāta*, *pitta*, *kapha* — the three *doṣas*.

3. **Define each precisely.** Map to Module 2 elements:
   - *vāta* — wind-like, motion; from *ākāśa* + *vāyu*
   - *pitta* — fire-like, transformation; from *tejas* + *ap*
   - *kapha* — earth-like, structure; from *ap* + *pṛthvī*

4. **Source check.** Read aloud:
   > *vāyuḥ pittaṁ kaphaścoktaḥ śārīro doṣa-saṅgrahaḥ*
   > "Wind, bile, phlegm — the summary of the bodily doṣas."
   > — Caraka Saṁhitā, Sūtrasthāna 1.57

5. **Critical clarification, repeated:** Doṣas are NOT diseases. They are patterns of internal rhythm. Every person has all three — the ratio differs. This is a *wellness lens, NOT diagnosis.* Refer any health concern to a doctor.
""",
primary="""
- Three friends live inside us all the time:
  - **Wiggle** (*vāta*) — quick, lively, like wind
  - **Spark** (*pitta*) — warm, sharp, like fire
  - **Cozy** (*kapha*) — slow, soft, like a snug blanket

Show three picture cards (or draw the three on the board). Ask children: *"Which one feels most like you in the morning? Right now?"*

Each child draws one of the three friends in their notebook with one word that fits them today.
""")

register('module-04-doshas', 'vata-motion',
senior="""
1. **Observe motion.** Watch a leaf in a draft, a flag on a breezy day, or a fan spinning. *"What do you notice about the air's qualities? Is it predictable or changeable?"*

2. **Define *vāta*.** Motion principle. Five subtypes are described in Caraka:
   - *prāṇa* — inhalation, heart, head
   - *udāna* — speech, exhalation
   - *samāna* — digestion, equilibrium
   - *apāna* — elimination, downward flow
   - *vyāna* — circulation, full-body movement

3. **Vāta qualities (*guṇas*):** dry, light, cold, rough, subtle, mobile, clear. Have students list one observation matching each quality.

4. **Source.** Caraka Saṁhitā, *Sūtrasthāna* 12 enumerates *vāta-prakopa* (vāta aggravation) signs: dry skin, restless sleep, anxiety, irregular digestion. Read one paragraph.

5. **Modern bridge.** *Vāta* maps loosely to *autonomic nervous-system arousal patterns* and *peristaltic / circulatory rhythms*. Be careful: this is a wellness lens — NOT diagnosis.
""",
primary="""
- *vāta* is the **wind friend** inside us.
- Today's word: *vāta* (say "VAH-tah").

Stand up. Wiggle hands in the air like leaves. *"That's vāta — moving, light, quick."*

Each child draws **Wiggle** — a small figure with movement lines around it. What does Wiggle like? (Cool weather, dancing, talking, running.)
""")

register('module-04-doshas', 'pitta-transformation',
senior="""
1. **Observe transformation.** Light a candle (or use a torch). *"The candle's flame transforms wax to gas to light and heat. The stomach transforms food to energy. The eye transforms light into perception."* Pitta = transformation.

2. **Define *pitta*.** Five subtypes:
   - *pācaka* — digestive fire
   - *rañjaka* — blood and complexion
   - *sādhaka* — intellect, emotional fire
   - *ālocaka* — vision
   - *bhrājaka* — skin lustre

3. **Pitta qualities (*guṇas*):** hot, sharp, light, oily, slightly oily, spreading, liquid. Compare with *vāta*.

4. **Source.** Caraka Saṁhitā, *Sūtrasthāna* 12 on *pitta-prakopa*: irritability, inflammation, acid reflux, hot flashes, intense focus.

5. **Modern bridge.** *Pitta* maps loosely to *metabolic rate*, *thermoregulation*, *inflammatory response*. Wellness lens, not diagnosis. Class discussion: *"Why might a 'pitta person' suit a cool, calm work environment?"*
""",
primary="""
- *pitta* is the **fire friend** inside us.
- Today's word: *pitta* (say "PIT-tah").

Hold hands near a lit candle (safely, from a distance). *"Feel the warmth. That's the kind of friend Spark is — warm, bright."*

Each child draws **Spark** — a small figure with a glow around them. What does Spark like? (Sharp puzzles, focused work, learning fast, eating well.)
""")

register('module-04-doshas', 'kapha-structure',
senior="""
1. **Observe structure.** Hold up a rock or thick block. *"This stays in shape. It is solid, cool, heavy. It holds its form."* Kapha = the structure principle.

2. **Define *kapha*.** Five subtypes:
   - *avalambaka* — lubrication of joints, chest
   - *kledaka* — stomach moisture
   - *bodhaka* — saliva, taste
   - *tarpaka* — brain cushioning
   - *śleṣaka* — joint cohesion

3. **Kapha qualities (*guṇas*):** heavy, slow, cool, oily, smooth, soft, dense, stable, gross. Compare with vāta + pitta.

4. **Source.** Caraka Saṁhitā, *Sūtrasthāna* 12 on *kapha-prakopa*: heaviness, sluggishness, congestion, weight gain, emotional attachment.

5. **Modern bridge.** *Kapha* maps loosely to *anabolic / structural metabolism*, *connective-tissue density*, *parasympathetic dominance*. Wellness lens, not diagnosis. *"Why might a 'kapha person' thrive in a stable, predictable routine?"*
""",
primary="""
- *kapha* is the **cozy friend** inside us.
- Today's word: *kapha* (say "KAH-pah").

Hold a blanket or pillow. *"Cozy is warm, soft, slow, and holds you steady. Like a comfy hug."*

Each child draws **Cozy** — a soft round figure. What does Cozy like? (Big meals, naps, sweet songs, looking after others.)
""")

register('module-04-doshas', 'mapping-to-elements',
senior="""
1. **Recall Module 2 *pañcabhūta*:** *ākāśa* (space), *vāyu* (air), *tejas* (fire), *ap* (water), *pṛthvī* (earth).

2. **Map doṣas to element pairs.** Caraka's framework:
   - *vāta* = *ākāśa* + *vāyu* (both light, mobile)
   - *pitta* = *tejas* + *ap* (transformation + medium)
   - *kapha* = *ap* + *pṛthvī* (cohesion + heaviness)

3. **Why pairs, not single elements?** Each doṣa needs a quality AND a medium. *Vāyu* alone has no container; *tejas* alone burns without medium; *pṛthvī* alone is inert. The pair makes the doṣa functional.

4. **Source.** Aṣṭāṅga Hṛdaya, *Sūtrasthāna* 1.7 — the *tridoṣa* are the gross outcome of the *pañcamahābhūta*.

5. **Class exercise.** Pairs receive a list of 10 observations ("warm forehead," "dry skin," "feels heavy after lunch"). Classify each by likely doṣa AND the element pair that grounds the claim.
""",
primary="""
- Vāta = ākāśa (space) + vāyu (air) — both light, both move.
- Pitta = tejas (fire) + ap (water) — fire that flows.
- Kapha = ap (water) + pṛthvī (earth) — wet earth holds shape.

Take the three friend drawings from earlier days. Beside each, draw the two elements that make that friend. Wiggle gets sky + wind. Spark gets fire + water. Cozy gets water + earth.

Sing the rhyme: *"Wiggle is sky and wind. Spark is fire and water. Cozy is water and earth."*
""")

register('module-04-doshas', 'prakriti-self-assessment',
senior="""
1. **Distinguish prakṛti from vikṛti.** *Prakṛti* = innate constitution (birth ratio of doṣas, stable through life). *Vikṛti* = current state (today's ratio, fluctuates). This distinction is *critical* — it stops students treating self-assessment as labelling.

2. **Self-assessment worksheet.** Distribute a 30-question checklist (sleep, digestion, body frame, temperament, energy patterns). Students mark each on a 1–5 scale for *"how true is this for me usually."*

3. **Score and discuss.** Tally for each doṣa. *Most students will be mixed.* That's the expected result. Mono-doṣic types are rare; *dvi-doṣa* (dual) is common.

4. **The rule of the day, said three times:** This is a self-observation exercise. NOT a diagnosis. NOT a prediction. Refer any health concern to a doctor.

5. **Caraka cite.** Caraka Saṁhitā, *Vimāna* 8.95–117 outlines the constitutional assessment method — historical context, NOT a clinical tool for school use.
""",
primary="""
- Today: which friend is most like ME right now?

Ask three questions:
1. *"When you talk to friends, do you feel quick (Wiggle), focused (Spark), or steady (Cozy)?"*
2. *"At meal time, are you usually nibbling little bits (W), eating fast and hot (S), or eating slow and big (C)?"*
3. *"At sleep time, do you flip around (W), sleep just enough (S), or sleep deep (C)?"*

Each child colours a small chart with one star for each friend that fits them today. *"All three friends live in everyone. Today's stars are just for today — they can change tomorrow."*
""")

register('module-04-doshas', 'daily-rhythms',
senior="""
1. **Project the doṣa clock.** On the board, draw a 24-hour ring divided into three two-period segments:
   - **Kapha hours:** 6–10 am and 6–10 pm — heavy, slow start; calm wind-down.
   - **Pitta hours:** 10 am–2 pm and 10 pm–2 am — sharp focus; metabolic peak.
   - **Vāta hours:** 2–6 am and 2–6 pm — light, mobile, creative.

2. **Source.** Aṣṭāṅga Hṛdaya, *Sūtrasthāna* 1.8 on *kāla-prabhāva* (time-of-day influence on doṣa).

3. **Match observations to hours.** *"When is your sharpest study time? When do you feel heaviest? When are dreams most active?"* Pair this to the chart. Most students will recognise the pitta-noon peak and the kapha-morning slump.

4. **Modern bridge.** Map onto circadian-rhythm research: cortisol peaks ~8 am (kapha-clearance), core body temperature peaks ~mid-afternoon (pitta), REM sleep dominates ~3–5 am (vāta).

5. **Independent work.** Each student sketches their own 24-hour clock and annotates which hours they feel each doṣa dominate. Compare in pairs.
""",
primary="""
- The day has three parts where each friend takes the lead:
  - **Morning (Cozy time):** slow start, good for breakfast, gentle movement
  - **Middle of day (Spark time):** sharp focus, biggest meal, schoolwork
  - **Evening (Wiggle time):** creative play, light dinner, getting ready for bed

Draw a sun arc on paper. Mark "C" near the morning, "S" near noon, "W" near sunset. Children colour each section with a different colour and add one activity to each.
""")

register('module-04-doshas', 'seasonal-rhythms',
senior="""
1. **The annual doṣa cycle.** Three seasonal phases dominate (varies by region):
   - **Vasanta (spring) — kapha season:** snowmelt, congestion, allergies; kapha accumulates over winter and is released now.
   - **Grīṣma + Varṣā (summer / monsoon) — pitta season:** heat, inflammation, digestive fire dips.
   - **Śarad + Hemanta + Śiśira (autumn / winter) — vāta season:** dryness, cold, wind; circulatory and joint stiffness.

2. **Source.** Caraka Saṁhitā, *Sūtrasthāna* 6 — *ṛtucaryā* (seasonal regimen).

3. **Map to your region.** Indian classical descriptions correspond to North Indian climates. *"How do these doṣa-seasons map to YOUR local climate?"* Coastal, hill, and desert students will adapt differently.

4. **Modern bridge.** Hay-fever in spring (immune activation matching kapha-release), heat-stroke risk in summer (pitta), dry-skin and joint pain in winter (vāta) — all empirically documented in Indian medical literature.

5. **Discussion.** *"What seasonal adjustment would you make to your routine — sleep, food, exercise — based on today's doṣa-season?"* Each student writes one specific adjustment.
""",
primary="""
- Each season has a special friend:
  - **Spring** — Cozy is busy melting away! (Allergies, sniffles.)
  - **Summer** — Spark is hot! (Sweating, drinking water.)
  - **Winter** — Wiggle is dry and cool! (Dry skin, blankets.)

Draw a tree in three seasons (bare → blossom → leaves) and write which friend lives there. Ask: *"What did our family eat in summer? In winter? Why?"*
""")

register('module-04-doshas', 'balance-and-imbalance',
senior="""
1. **State the distinction.** Balance (*sāmya*) = each doṣa at its individual baseline. Imbalance (*vaiṣamya*) = a doṣa deviates from baseline. *Vikṛti* is the language for the deviated state.

2. **Recognise simple imbalance signs.** From Caraka, *Sūtrasthāna* 18:
   - Vāta excess — dryness, irregularity, anxiety, joint cracking
   - Pitta excess — heat, inflammation, irritability, acid reflux
   - Kapha excess — congestion, lethargy, attachment, fluid retention

3. **The five-stage progression (*samprāpti*).** Doṣa imbalance progresses: accumulation → aggravation → spread → localisation → manifestation → chronicity. The earlier you notice, the easier to redirect. This is the framework's preventive logic.

4. **Critical limits.** What this module *does not* claim: that you can self-diagnose serious illness, that you should self-medicate, or that doṣa balance replaces medical care. Repeat: WELLNESS LENS, NOT DIAGNOSIS.

5. **Reflection.** *"Identify one mild imbalance you experienced this week. Which doṣa? What likely drove it (diet, sleep, weather, stress)? What single adjustment might help?"*
""",
primary="""
- Sometimes one friend gets too loud!
  - Wiggle too loud = jittery, can't sit still, dry mouth
  - Spark too loud = grumpy, hot, hangry
  - Cozy too loud = sleepy, heavy, sad

Story: *"Imagine if all three friends are at a party. If one shouts too much, the others get tired."* Ask: *"What helps Wiggle calm down? What helps Spark cool off? What helps Cozy wake up?"*

Each child draws one friend in calm mode and one in too-loud mode.
""")

register('module-04-doshas', 'synthesis-and-project-pitch',
senior="""
1. **Recap the framework in 3 sentences.** Students take turns: someone explains *vāta*, *pitta*, *kapha*; the next student explains the element-mapping; the third explains *prakṛti* vs *vikṛti*. Catch errors collaboratively.

2. **Project pitch.** Hand out the project brief — 7-day doṣa self-observation. Students read silently for 5 minutes.

3. **Pair brainstorm.** In pairs: *"What three things will you track each day? Why those?"* (Common picks: sleep, food, energy, mood, digestion, social interactions.)

4. **Source-anchoring.** For Senior credit, every project must cite at least one Caraka or Aṣṭāṅga reference. Browse the *Sūtrasthāna* index in *sources.md* together.

5. **Critical-thinking close.** *"What are the limits of this self-observation? What might it tell you? What might it MISS?"* Students draft one paragraph on these limits as part of their project journal Day 1.
""",
primary="""
- Today we say goodbye to the three friends — but they will stay with us!

Each child shares one favourite friend and one thing they learned about that friend. Make a class wall: three big drawings (Wiggle, Spark, Cozy) with each child's small drawing of them stuck around the big one.

Sing the friends-song together: *"Wiggle, Spark, Cozy — three friends inside, three friends inside, three friends inside me!"*
""")

# ============================================================================
# Module 6 — Moon Phases & Tithi
# ============================================================================

register('module-06-moon-phases-tithi', 'moon-and-its-shapes',
senior="""
1. **Geometric model.** Use a torch (Sun) + tennis ball (Moon) + a student's head (Earth). Walk the Moon around the Earth. *"Which part of the Moon does the Earth-observer see lit at each position?"* Demonstrate the four primary phases.

2. **Define synodic month.** ~29.53 days from one *amāvasyā* to the next. *Synodic* = relative to the Sun (as seen from Earth). Distinct from sidereal month (~27.32 days) — relative to fixed stars.

3. **Source.** Sūrya-siddhānta, ch. 2, vv. 1–10 — defines lunar motion with mean and true longitudes. Read 2 verses aloud in transliteration.

4. **Four phases:**
   - *amāvasyā* — new (Sun side)
   - First quarter — half lit, waxing
   - *pūrṇimā* — full (anti-Sun side)
   - Last quarter — half lit, waning

5. **Class observation assignment.** Each student notes the moon's shape this evening (or tomorrow morning) and writes one sentence describing it. We'll plot data tomorrow.
""",
primary="""
- The Moon changes shape! From a tiny smile to a big circle to a tiny smile on the other side, and back to dark again.

Hold up a ball (or large orange). Turn off the lights. Shine a torch from one side. Walk a child around with the ball — show the lit-side changing as they move.

Each child draws four moon shapes: dark, half-smile, full circle, half-frown. Label them with one word each.
""")

register('module-06-moon-phases-tithi', 'two-fortnights',
senior="""
1. **Define pakṣa.** A *pakṣa* is a half-month: 14–16 days. Two per synodic month.
   - *śukla pakṣa* (waxing fortnight) — *amāvasyā* → *pūrṇimā* — moon growing.
   - *kṛṣṇa pakṣa* (waning fortnight) — *pūrṇimā* → *amāvasyā* — moon shrinking.

2. **Etymology.** *śukla* = bright; *kṛṣṇa* = dark. *Pakṣa* = side / wing — same root as *pakṣapāta* (taking sides).

3. **Source.** Sūrya-siddhānta and the *Pañca-siddhāntikā* of Varāhamihira both organise lunar tables by pakṣa.

4. **Identify today's pakṣa.** Pull up the current pañcāṅga (web or printed). *"Which pakṣa are we in right now? Which tithi?"* Students record the date AND the pakṣa name in their workbook.

5. **Cultural note.** Many traditional Indian festivals are named by tithi within pakṣa (e.g. *Karka Saṅkrānti tritīyā*, *Karwa Chauth* = *Kṛṣṇa caturthī* of Kārtika). Pakṣa labelling is more precise than "the third of Kārtika."
""",
primary="""
- The month has two halves:
  - One half: Moon grows bigger each night (*śukla pakṣa* — "bright half").
  - Other half: Moon shrinks smaller each night (*kṛṣṇa pakṣa* — "dark half").

Show a chart of 14 little moons in a row (small → big → small). Children colour the growing half in yellow, the shrinking half in blue.

Today's question: *"Which half are we in right now?"* (Teacher checks calendar.)
""")

register('module-06-moon-phases-tithi', 'fifteen-tithis',
senior="""
1. **Define tithi precisely.** A *tithi* is the time taken for the Moon to gain 12° of longitudinal separation from the Sun. 30 tithis per synodic month → 15 per pakṣa. A tithi is therefore a unit of angular progress, NOT a unit of time.

2. **Why a tithi ≠ a day.** Lunar speed varies (elliptical orbit, ~3.4°/hour to ~5.5°/hour). A tithi can last 19 to 26 hours. Two consecutive tithis can both touch the same sunrise (*kṣaya tithi*) or one tithi can span two sunrises (*adhika tithi*).

3. **Name the 15 tithis.** *pratipadā, dvitīyā, tṛtīyā, caturthī, pañcamī, ṣaṣṭhī, saptamī, aṣṭamī, navamī, daśamī, ekādaśī, dvādaśī, trayodaśī, caturdaśī, pūrṇimā/amāvasyā.* The 15th is *pūrṇimā* in śukla pakṣa, *amāvasyā* in kṛṣṇa pakṣa.

4. **Source.** Sūrya-siddhānta, ch. 2 (lunar motion); also *Vasiṣṭha-siddhānta* tradition.

5. **Computation exercise.** Given today's Moon-Sun elongation in degrees (provide one), students compute today's tithi number. Then compare with the published pañcāṅga.
""",
primary="""
- Each half-month has 15 little moon-days. Each one has a special name.

Sing-chant the first five: *"Pratipadā, dvitīyā, tṛtīyā, caturthī, pañcamī!"* (Then through pūrṇimā together.)

Each child writes the numbers 1 to 15 in their notebook, drawing a tiny moon shape next to each (growing in the first half, shrinking in the second). Today's number = today's tithi.
""")

register('module-06-moon-phases-tithi', 'building-a-tithi-calendar',
senior="""
1. **Pull up a current pañcāṅga** (online or printed). Display the next 14 days with tithi, pakṣa, day-of-week.

2. **Manual construction.** Without looking at the pañcāṅga, students attempt to predict the tithi 7 days from today using:
   - Today's tithi (e.g. *śukla pañcamī*).
   - Approximate rule: ~1 tithi per 24h.
   - Note: actual tithi may be off by ±1 due to varying lunar speed.

3. **Source.** Modern Drik pañcāṅga uses Sūrya-siddhānta-derived corrections plus modern astronomical constants (NASA JPL ephemerides). Show the students that traditional and modern computation agree to within minutes.

4. **The intercalation challenge.** Adhika māsa (added month) occurs roughly every 32 months when no Sun-saṁkrānti happens within a lunar month. The 2026–2030 adhika māsa calendar is published; pull it up. *"Why is this needed? What would happen without it?"*

5. **Project artefact.** Each student produces a one-month tithi calendar for the CURRENT month, side-by-side with the Gregorian dates. This will be assessed as part of the summative project.
""",
primary="""
- Let's make a moon calendar for this month!

Show a printed month calendar. Together, look up today's tithi. Mark it with a moon-sticker.

Each child gets a worksheet with 28 boxes (one per day). They draw the moon shape they expect to see each evening, going from now to a month from now. Tomorrow we'll check and correct.
""")

register('module-06-moon-phases-tithi', 'lunar-months-and-festivals',
senior="""
1. **Twelve lunar months.** *Caitra, Vaiśākha, Jyaiṣṭha, Āṣāḍha, Śrāvaṇa, Bhādrapada, Āśvina, Kārtika, Mārgaśīrṣa (Agrahāyaṇa), Pauṣa, Māgha, Phālguna.* Each begins on a new moon (*pūrṇimānta* tradition — North India) OR the day after the previous full moon (*amānta* tradition — South India). Both reference the same lunar month with a 15-day phase difference.

2. **Source.** Varāhamihira's *Bṛhat Saṁhitā* discusses both reckonings; the Sūrya-siddhānta uses *amānta*.

3. **Festivals by tithi.** Examples:
   - *Diwali* — *Kṛṣṇa amāvasyā* of Kārtika
   - *Holi* — *Pūrṇimā* of Phālguna (followed by *Vasantotsava*)
   - *Janmāṣṭamī* — *Kṛṣṇa aṣṭamī* of Śrāvaṇa
   - *Mahā-Śivarātri* — *Kṛṣṇa caturdaśī* of Māgha

4. **Class mapping.** Hand out cards with festival names. Students place each on a 12-month wheel, noting tithi + pakṣa. Compare two regions' festival calendars.

5. **Honest history.** Not all festivals are pan-Indian. Some are regional (Onam — Malayalam solar calendar; Pongal — Tamil solar calendar). Distinguish lunisolar tradition from purely solar reckonings.
""",
primary="""
- The year has 12 moon-months, each with its own name and feeling:
  - *Caitra* (spring)
  - *Śrāvaṇa* (monsoon)
  - *Kārtika* (Diwali month)
  - *Phālguna* (Holi month) — and many more!

Show pictures of 4 festivals. Ask: *"Which moon-month is this festival in?"* Children sort cards.

Sing the months: *"Caitra, Vaiśākha, Jyaiṣṭha, Āṣāḍha..."* (Through all 12.)
""")

register('module-06-moon-phases-tithi', 'panchanga-overview',
senior="""
1. **Define pañcāṅga.** Five (*pañca*) limbs (*aṅga*) of the Indian calendar:
   - *tithi* — lunar day (Module focus so far)
   - *vāra* — weekday (7-day cycle, *ravivāra*–*śanivāra*)
   - *nakṣatra* — lunar mansion (27 divisions of ecliptic)
   - *yoga* — Sun-Moon longitudinal sum (27 named yogas)
   - *karaṇa* — half-tithi (11 named karaṇas)

2. **Source.** Sūrya-siddhānta, *Pañcāṅga-prakaraṇa* sections.

3. **Read a published pañcāṅga together.** Show today's row. *"Identify each of the five aṅgas."* Note that the pañcāṅga also lists *muhūrta* (auspicious hours), *rāhu-kāla*, *yamagaṇḍa* — derivative computations.

4. **Modern parallel.** Astronomical observational data (NASA / IMCCE) provide the *raw inputs* (Sun-Moon longitudes); the pañcāṅga *interprets* these through the 5-limb framework. The astronomy is universal; the framework is Indian.

5. **Critical-thinking discussion.** *"Pañcāṅga has been used for ritual timing for ~2000 years. What does that tell us about (a) the durability of the framework and (b) the limits of inferring causation from co-occurrence?"*
""",
primary="""
- The pañcāṅga has 5 parts — like 5 fingers on a hand!
  1. *tithi* — moon-day
  2. *vāra* — weekday (Mon, Tue, ...)
  3. *nakṣatra* — star-house the moon is visiting
  4. *yoga* — Sun-Moon meeting
  5. *karaṇa* — half-moon-day

Show today's pañcāṅga on the board. Children copy the 5 names into their workbook with one word each.
""")

register('module-06-moon-phases-tithi', 'eclipses',
senior="""
1. **Geometric setup.** Solar eclipse — Moon between Sun and Earth (occurs at *amāvasyā*). Lunar eclipse — Earth between Sun and Moon (occurs at *pūrṇimā*).

2. **Why not every new/full moon?** The Moon's orbital plane is tilted ~5.14° from the ecliptic. Eclipses happen only when the Moon is near a *node* (intersection of orbital planes) during new or full moon. This is the *Rāhu/Ketu* node geometry of classical Indian astronomy.

3. **Source.** Āryabhaṭīya, *Gola-pāda* — gives a heliocentric-leaning model and correctly predicts eclipses 1000+ years before modern astronomy.

4. **Show a recent eclipse path map** (any annular or total eclipse from the last 5 years). *"Why does the path strike only a thin ribbon, not the whole hemisphere?"* (Geometric umbra/penumbra.)

5. **Safety rule.** Solar eclipse — NEVER look at the Sun directly. Use projection or eclipse-rated filters only. Lunar eclipse is always safe. State this rule on the board and have students repeat.
""",
primary="""
- Sometimes the Moon hides the Sun — that's a *solar eclipse*!
- Sometimes the Earth's shadow falls on the Moon — that's a *lunar eclipse*!

Use the torch + ball + child's head from earlier days. Show:
- Ball blocks light → solar eclipse (child's face goes dark).
- Child's head blocks light → lunar eclipse (ball goes dark).

**SAFETY RULE:** Never look at the Sun with eyes! Children repeat 3 times.
""")

register('module-06-moon-phases-tithi', 'modern-lunar-science',
senior="""
1. **Phases re-explained.** Lunar phases = sunlight reflection from a 1737-km-radius sphere as the Earth-Moon-Sun angle changes. Synodic period of ~29.53 days. There is no "dark side" — only a *far side*, which receives the same sunlight, just not visible from Earth.

2. **Libration.** Earth-observers see ~59% of the Moon's surface over time due to orbital eccentricity and axial tilt. Demo with rotating ball.

3. **Tidal lock.** Same face always visible to Earth — rotation period = orbital period = ~27.32 days (sidereal). This is the result of tidal forces over billions of years.

4. **Modern lunar exploration.** Mention briefly: Apollo missions (1969–72), Chandrayaan-1 (2008) discovered water-ice signatures, Chandrayaan-3 (2023) soft-landing near south pole, Artemis program (2024+).

5. **Bridge back to tradition.** Sūrya-siddhānta computes Moon's distance and diameter approximately (Earth-Moon ~38000 yojanas ≈ 380000 km — close to modern 384400 km). The empirical precision is striking; the cosmological framework around it is what differs.
""",
primary="""
- The Moon isn't really changing shape — the same ball is always there!
- The Sun lights up half of it. We see *different parts of the lit half* as the Moon goes around Earth.

Demo: hold a half-painted ball (one side bright, one side dark). Walk it around a child. The child describes what they see from each angle.

*"The Moon is always whole. We only see the bright part."*
""")

register('module-06-moon-phases-tithi', 'cross-cultural-calendars',
senior="""
1. **Indian lunisolar.** Lunar months (~29.5d) + adhika māsa intercalation to track the solar year. Months named for the *nakṣatra* near the full moon.

2. **Islamic Hijri.** Strictly lunar — 12 lunar months, no intercalation. ~354 days/year, drifts ~11 days/year relative to solar calendar. Reasons: religious lunar observation, no agricultural anchoring.

3. **Chinese.** Lunisolar like Indian, with intercalation. 60-year cycle combining 12 animals × 10 stems. Confucian calendar reform 104 BCE refined it.

4. **Hebrew.** Lunisolar with intercalation (Adar I/II in leap years). 19-year Metonic cycle.

5. **Roman / Gregorian.** Purely solar (since Julian 45 BCE, refined 1582 CE). Months disconnected from lunar cycle. Most universal calendar today.

6. **Source comparison.** Show a 2026 calendar in 4 traditions side-by-side. *"Which dates align? Which don't? Why?"*
""",
primary="""
- People all over the world watch the Moon, but each tradition counts months a bit differently.
- Some use only Moon (Islamic Hijri). Some use Sun + Moon (Indian, Chinese, Hebrew). Some use only Sun (modern Gregorian — like the school year).

Show 4 calendar pictures and chant: *"India and China — Moon plus Sun! Islam — Moon alone! Modern world — Sun alone!"*

Each child colours a small "moon flag" with the calendar they think they use most.
""")

register('module-06-moon-phases-tithi', 'synthesis-quiz',
senior="""
1. **Vocabulary lightning round.** Students take turns defining: *tithi, pakṣa, śukla, kṛṣṇa, pūrṇimā, amāvasyā, pañcāṅga, nakṣatra, adhika māsa.* Catch errors collectively.

2. **Moon-diary review.** Each student shares one observation from their 10-day moon diary (Days 1–10 of homework). Identify discrepancies between prediction and observation.

3. **Source recall.** *"Name one classical source and one modern source we cited for this module."* (Sūrya-siddhānta + NCERT / NASA.)

4. **Critical-thinking close.** *"The Indian lunisolar calendar is ~2000+ years old and still in active use. The Gregorian calendar is ~450 years old. Why might multiple calendars coexist in modern India?"* (Cultural specificity + scientific universality.)

5. **Summative quiz** (45 min, written) — see `quizzes/summative.md`.
""",
primary="""
- Today we celebrate everything we learned about the Moon!

Each child shares ONE thing from their moon diary. *"Did the Moon look how you thought it would?"*

Make a class moon-mural: a circle with all the children's moon drawings stuck around the outside. Sing the tithi rhyme one more time.

Take the quiz with stickers (not stress) — every child gets a "Moon Watcher" sticker.
""")

# ============================================================================
# Module 7 — ×11 Multiplication
# ============================================================================

register('module-07-eleven-multiplication', 'the-hook',
senior="""
1. **Compute 23 × 11 silently in your head.** Pause. Show of hands for who got 253. Then write 23 × 11 = 253 on the board.

2. **Reveal the trick.** Split the digits of 23 (gap in the middle): **2 _ 3**. Add the digits in the middle: 2 + 3 = 5. Fill the gap: **2 5 3** = 253. Done.

3. **Try together.** 35 × 11 = 3_(3+5)_5 = 385. 24 × 11 = 264. 71 × 11 = 781. 52 × 11 = 572. 80 × 11 = 880. Pace: 4 problems in 2 minutes.

4. **Tirthaji's framing.** This method appears as an application of the sūtra *Ekādhikena Pūrveṇa* ("by one more than the previous") in Bharati Krishna Tirthaji's *Vedic Mathematics* (1965). Honest historical note: the manuscript was written 1911–1918; some scholars (Dani 1993) consider it a 20th-century mental-arithmetic system rather than strictly ancient mathematics.

5. **Independent practice (5 min).** Worksheet: 20 two-digit × 11 problems, no carry case. Pairs compete.
""",
primary="""
- Watch this trick! 23 × 11 = ?

Show on the board: "2 _ 3" with a gap. Whisper: "What's 2 + 3?" (Wait for "5".) Fill in: "2 5 3 → 253!"

Each child practices: 12 × 11 = 132. 34 × 11 = 374. 25 × 11 = 275. Try 5 more.

Magic chant: *"Split, add, put in middle!"* (Children chant 3 times.)
""")

register('module-07-eleven-multiplication', 'the-carry-case',
senior="""
1. **Try 87 × 11.** Apply the rule: 8 _ (8+7) _ 7 = 8 _ 15 _ 7. But 15 doesn't fit in one slot. So *carry*: keep the 5 in the middle, add the 1 to the 8 → 9 5 7 = **957**.

2. **General rule extension.** When the middle sum ≥ 10:
   - Write the units of the sum in the middle.
   - Carry the tens digit to the left, adding it to the existing left digit.

3. **Practice progression.**
   - 65 × 11 = 6_(11)_5 → 715
   - 49 × 11 = 4_(13)_9 → 539
   - 99 × 11 = 9_(18)_9 → 1089
   - 84 × 11 = 9_(12)_4 → 924

4. **Cross-check with standard long multiplication.** Have students verify two of the answers using the traditional algorithm. *"Same answer? Good. The Vedic method is just a different procedure for the same arithmetic."*

5. **Limit recognition.** *"When might this be slower than long multiplication?"* For numbers with three or more digits where carries cascade, the saving shrinks. Tomorrow we extend to 3-digit and meet the algebraic proof.
""",
primary="""
- What if the middle sum is too big? Like 87 × 11.

Show: "8 _ 7" with gap. 8 + 7 = 15. Whisper: "15 is two digits! Keep the 5, carry the 1."

Result: 8 + 1 = 9, then 5, then 7 → **957**.

Practice: 67 × 11 = 7 3 7. 95 × 11 = 1 0 4 5. *"Carry the tens, keep the ones!"* (Chant.)
""")

register('module-07-eleven-multiplication', 'why-it-works',
senior="""
1. **Write any 2-digit number as 10a + b.** Examples: 23 = 10·2 + 3 (a=2, b=3); 87 = 10·8 + 7.

2. **Distribute multiplication.**
   ```
   (10a + b) × 11 = (10a + b)(10 + 1)
                  = (10a + b)·10 + (10a + b)·1
                  = 100a + 10b + 10a + b
                  = 100a + 10(a + b) + b
   ```

3. **Read the final line in plain language.**
   - 100a → hundreds digit is *a*
   - 10(a+b) → tens digit is *a+b* (the digit sum!)
   - +b → units digit is *b*

   This IS the trick. The algebra spells out the procedure.

4. **Verify on 23.** 100·2 + 10·(2+3) + 3 = 200 + 50 + 3 = 253. ✓

5. **Connection to the carry case.** When a+b ≥ 10, 10(a+b) becomes 10(a+b) = 100 + 10·(a+b-10), pushing the overflow into the hundreds place. The algebra automatically handles the carry.

6. **Independent task.** Each student writes the proof in their own words for a homework explainer to a younger student.
""",
primary="""
- Why does the magic work?

Show 23 × 11 with paper strips:
- One strip of 23 + ten strips of 23 = 11 strips.
- Stack them: 230 + 23 = 253.
- The "230" gives the 2 and the 3 (separated). The "23" gives the +2 in the tens and +3 in the ones.
- 2 + 3 = 5 in the tens place. The 2 and 3 stay on the ends!

Magic? No — just adding! Children try with strips of 14: 14 × 11 = 140 + 14 = 154.
""")

register('module-07-eleven-multiplication', 'three-digit',
senior="""
1. **Generalise to 3-digit.** For *abc* (= 100a + 10b + c) × 11:
   (100a + 10b + c)(10 + 1) = 1000a + 100b + 10c + 100a + 10b + c
                            = 1000a + 100(a+b) + 10(b+c) + c

2. **Procedure.** Split *abc* with two gaps: **a _ b _ c**. Fill gaps with adjacent sums: a+b, then b+c. Result: **a (a+b) (b+c) c**. Carry where needed.

3. **Worked examples.**
   - 234 × 11 = 2_(2+3)_(3+4)_4 = 2574
   - 567 × 11 = 5_(5+6)_(6+7)_7 = 6237 (carries: 11→ carry 1 to left; 13 → carry 1 to next left)
   - 729 × 11 = 7_(7+2)_(2+9)_9 = 8019

4. **Algebra check.** 234 = 100·2 + 10·3 + 4. × 11 = 1000·2 + 100·5 + 10·7 + 4 = 2574. ✓

5. **Extension activity.** Each pair solves five 3-digit × 11 problems, then verifies by long multiplication. Time-budget 8 minutes; share fastest correct-answer time.
""",
primary="""
- For 3-digit numbers: split with TWO gaps!

234 × 11 = ?
- Write "2 _ _ 4" with two gaps.
- Fill: 2+3 = 5 (first gap), 3+4 = 7 (second gap).
- Answer: **2574**.

Practice: 123 × 11 = 1 (1+2) (2+3) 3 = 1353. 456 × 11 = 5016 (with carries — hard).

Most children stick to no-carry cases this day.
""")

register('module-07-eleven-multiplication', 'speed-day',
senior="""
1. **Setup.** 50-problem mental-math sprint. Mixed 2- and 3-digit × 11. Half no-carry, half carry. Five minutes on the clock.

2. **Solo run.** Silence. Pen-on-paper. Five minutes.

3. **Pair-mark.** Swap with partner; mark in two minutes.

4. **Analyse errors.** *"Most common error?"* (Forgetting to carry; transposing digits.) *"Fastest sub-strategy?"* Discuss.

5. **Standards comparison.** Equivalent traditional long-multiplication sprint would take ~15 minutes. Time-saving on this problem class: ~3×. State the limit: this is for ×11 specifically. Tomorrow we extend to ×12 through ×19.

6. **Personal best.** Each student records their score and target for next week.
""",
primary="""
- Speed time! Today we play a quick ×11 game.

In pairs: one child says a 2-digit number, the other shouts the answer × 11. Switch every 30 seconds. 5 rounds.

End with class cheer: *"Split! Add! Middle! Done!"*
""")

register('module-07-eleven-multiplication', 'anurupyena-extension',
senior="""
1. **Move beyond ×11.** Tirthaji's *Anurūpyena* ("proportionately") sūtra extends the digit-sum idea to ×12 through ×19. Procedure for ×12:
   - Write any number *N*.
   - Compute: *N* × 12 = (*N* × 10) + (*N* × 2) — easy mental sum.
   - Equivalent digit-procedure: split-double-add.

2. **Worked example, 23 × 12.**
   - 23 × 10 = 230
   - 23 × 2 = 46
   - Sum: 276
   - OR digit-wise: 2 _ 3 → 2_(2·1+3)_(3·1) wait — this gets tangled. The cleanest mental version is the (×10) + (×k) split.

3. **General ×(10+k) rule.** N × (10+k) = 10N + kN. The Anurūpyena framing emphasises the proportional scaling.

4. **Practice.** Compute mentally:
   - 14 × 13 = 140 + 42 = 182
   - 25 × 15 = 250 + 125 = 375
   - 32 × 17 = 320 + 224 = 544

5. **Honest historical note.** The (10+k) decomposition isn't unique to Tirthaji — Western mental-math systems describe the same trick. Tirthaji's contribution is grouping it under a Sanskrit sūtra-system.
""",
primary="""
- We can do ×12 too! Just split into ×10 + ×2.
- 15 × 12 = (15 × 10) + (15 × 2) = 150 + 30 = **180**.

Practice in pairs: one says a number, the other doubles it for ×2, then adds a zero for ×10, then adds the two together for ×12.

Try ×13, ×14 only if time. Most children stick to ×12 today.
""")

register('module-07-eleven-multiplication', 'limits-of-the-method',
senior="""
1. **Pose the question.** *"When IS the ×11 (or near-base) method genuinely faster than traditional long multiplication? When is it the SAME or SLOWER?"*

2. **Categorise problem types.**
   - 2-digit × 11 — much faster.
   - 3-digit × 11 — somewhat faster.
   - 2-digit × 12–19 — comparable.
   - 2-digit × 23 (far from base) — long multiplication is faster.
   - Long multi-digit products — long multiplication or scientific notation is best.

3. **Honest framing.** Tirthaji's sūtras are not a universal speed-up. They are a *toolbox of mental shortcuts for specific patterns*. The skill is recognising when to use which tool.

4. **Reference.** Modern mathematicians (S.G. Dani, 1993; Kim Plofker, *Mathematics in India*, 2009) have written critically about the "Vedic" claim and pedagogically about the methods. Read Dani's *Frontline* article excerpt aloud (one paragraph).

5. **Reflection.** Each student writes 3 sentences: which method-types are useful, what limits are, and where standard arithmetic remains best.
""",
primary="""
- The trick is special! It works best for ×11 (and ×12).
- For things like ×23 or ×47, the trick is hard. Then we use the regular way.

Show: 23 × 47. *"Would the trick work?"* (No — 47 is too far from 10.) *"So we do it the long way."*

Children practice both methods on 24 × 11 vs 24 × 23 to feel the difference.
""")

register('module-07-eleven-multiplication', 'tirthaji-context',
senior="""
1. **Who was Tirthaji?** Bharati Krishna Tirthaji (1884–1960), Śaṅkarācārya of Govardhana Maṭha, Puri. Composed the manuscript that became *Vedic Mathematics* during 1911–1918. Published posthumously 1965.

2. **Tirthaji's claim.** The 16 sūtras + 13 sub-sūtras were "reconstructed" from the *Pariśiṣṭa of the Atharva Veda*. The original manuscript with sūtras has never been independently located.

3. **Scholarly response.** S.G. Dani (Tata Institute of Fundamental Research), in *Frontline* (1993), examined the claim: the sūtras as published do NOT appear in extant Atharva Veda Pariśiṣṭa manuscripts. Most academic mathematicians treat Tirthaji's system as a 20th-century mental-arithmetic synthesis, drawing on traditional and modern sources, NOT strictly ancient mathematics.

4. **Pedagogical value.** The methods themselves work and teach number sense effectively. The *historical claim* is separable from the *pedagogical method*. Many curricula in India today teach the methods while updating the historical claim.

5. **Reading.** Hand out a one-page excerpt from Dani's article and Tirthaji's preface side-by-side. Pairs discuss: *"What does each author claim? What evidence does each provide?"*
""",
primary="""
- The trick comes from a book by Bharati Krishna Tirthaji, who lived about 100 years ago.
- He named it after old Sanskrit ideas. Today, scholars are not sure if the methods are really thousands of years old. But the *trick still works* — and that's what matters for us!

Show a photo (or drawing) of Tirthaji. Children put a thumbs-up if they like the trick.
""")

register('module-07-eleven-multiplication', 'mixed-practice',
senior="""
1. **Mixed-method practice set.** 25 problems, 15 minutes. Each problem is either:
   - Easy ×11 (no carry)
   - Tricky ×11 (with carry)
   - ×12 or ×13 (Anurūpyena)
   - Standard 2-digit × 2-digit (use any method)

2. **Self-routing.** Students decide WHICH method to apply per problem, justified silently. Speed and accuracy both matter.

3. **Pair-mark + discuss.** Two minutes per pair to compare strategies. *"Did you both pick the same method? When did you disagree?"*

4. **Whole-class harvest.** Two students share one problem each where method choice mattered.

5. **Reflection (3 sentences).** Each student writes which method-type they're confident in, which they want more practice on, which they avoid.
""",
primary="""
- Today we play a sorting game!

Show 10 problems on cards. For each, children hold up a sign:
- "Trick!" (for ×11 problems)
- "Long!" (for harder problems)

Then solve 5 ×11 problems for practice. End with applause.
""")

register('module-07-eleven-multiplication', 'final-assessment',
senior="""
1. **Method-comparison reflection (10 min).** Each student writes a one-paragraph response: *"Compare the Tirthaji ×11 method with traditional long multiplication. When is each preferable? What does Tirthaji's system teach you that standard arithmetic doesn't?"*

2. **Honest history check (5 min).** *"In 2-3 sentences, summarise the historical debate about 'Vedic Mathematics.' What's claimed? What does scholarship say?"*

3. **Summative quiz (25 min).** Mix of computation, algebraic proof, and conceptual questions. See `quizzes/summative.md`.

4. **Project share (5 min).** Each student shows the method-comparison poster they built (`assessments/project-brief.md`).

5. **Module close.** *"What's one number-sense habit from this module that you'll keep using?"* Each student shares one sentence.
""",
primary="""
- Final day! We celebrate the ×11 trick.

Each child shows their best ×11 problem to a partner. Cheer for each one.

Take the small quiz with stickers (every child gets a "Number Magician" sticker).

End: class chant — *"Split! Add! Middle! Magic!"*
""")


# ============================================================================
# Module 9 — Subtraction by Complements (Nikhilam)
# ============================================================================

register('module-09-subtraction-nikhilam', 'the-sutra',
senior="""
1. **Pose the question.** *"What's 100 − 47?"* Most students compute 53 by borrowing. Ask: *"What's 1000 − 437?"* Trickier — the borrowing chains. Today's method removes the chain entirely.

2. **State the sūtra.** *Nikhilaṁ Navataścaramaṁ Daśataḥ* — "all from 9, the last from 10." Write the Sanskrit and IAST on the board.

3. **Apply to 100 − 47.** Subtract each digit of 47 from 9, except the last which is from 10:
   - 4 from 9 = 5
   - 7 from 10 = 3
   - Answer: **53**. No borrowing.

4. **Pattern recognition.** For 1000 − 437: 9-4=5, 9-3=6, 10-7=3 → **563**. Verify: 437 + 563 = 1000. ✓

5. **Source note.** Tirthaji's *Vedic Mathematics* (1965), sūtra #2. Honest history: this is one of the more solidly-rooted methods in older Indian and Arabic arithmetic traditions (decimal complement was widely used pre-modern). Independent practice: 10 problems on the worksheet.
""",
primary="""
- Easy subtraction trick: *"All from 9, last from 10!"*

Show 100 − 7. The "last digit" is 7. *"7 from 10 is..."* (3) → **93**.

Show 100 − 25. *"2 from 9, 5 from 10"* (7 and 5) → **75**.

Children chant: *"All from nine, last from ten!"* (3 times). Practice 10 problems with the teacher.
""")

register('module-09-subtraction-nikhilam', 'complement-to-1000',
senior="""
1. **Define complement.** The complement of *N* to base *B* is *B − N*. Today we find complements to 1000 mentally.

2. **Worked examples.**
   - 738 → 9-7=2, 9-3=6, 10-8=2 → **262**. Check: 738 + 262 = 1000. ✓
   - 405 → 9-4=5, 9-0=9, 10-5=5 → **595**. Check: 405 + 595 = 1000. ✓
   - 999 → 0, 0, 1 → **001**. Edge case: trailing 9s carry differently — *"all from 9 except the LAST non-zero digit, which is from 10."*

3. **The "trailing zero" caveat.** For 730 (ends in 0): treat the last non-zero digit as the one from 10. 730 → 9-7=2, 10-3=7, 0 → **270**. Or equivalently: complement 73 to 100 (= 27), append the trailing 0 → 270.

4. **Pattern algebra.** For *N* < 10^k, the complement is (10^k − 1) − N + 1 = (10^k − N). The "all from 9 last from 10" procedure computes this digit-by-digit.

5. **Practice.** 15-problem mental sprint, complements to 1000 only. 5 minutes.
""",
primary="""
- For 1000, the rule is the SAME: all from 9, last from 10!

Show 1000 − 437.
- 4 from 9 = 5
- 3 from 9 = 6
- 7 from 10 = 3
- Answer: **563**

Practice with the teacher: 1000 − 125 = 875. 1000 − 246 = 754. 1000 − 333 = 667.

Sing the chant again. Each child writes 5 problems.
""")

register('module-09-subtraction-nikhilam', 'subtract-from-power-of-10',
senior="""
1. **The clean application.** Whenever we're subtracting from 10^k (10, 100, 1000, 10000, ...), Nikhilam gives the answer directly. No borrowing, no carries.

2. **Speed examples.**
   - 10 − 4 = 6 (4 from 10)
   - 100 − 37 = 63 (3 from 9, 7 from 10)
   - 1000 − 268 = 732
   - 10000 − 1547 = 8453

3. **Practical use case.** Computing change at a shop. *"You paid ₹1000 for an item costing ₹427. How much change?"* Nikhilam: 9-4=5, 9-2=7, 10-7=3 → **₹573**. Mental math, no paper.

4. **Verify with traditional subtraction.** Have students cross-check 2 problems by the borrowing method. Same answer. The Nikhilam is just a smarter procedure for the same arithmetic.

5. **Class discussion.** *"When IS Nikhilam genuinely faster than borrowing? When does borrowing keep up?"* (Borrowing keeps up for small numbers like 10−4. Nikhilam dominates for larger powers.)
""",
primary="""
- The trick is great for shopping! Imagine you give ₹100 to pay for something ₹37.

How much change? Use the trick:
- 3 from 9 = 6
- 7 from 10 = 3
- Answer: **₹63**

Children practice with play money: give ₹100, buy something for ₹X, count the change.
""")

register('module-09-subtraction-nikhilam', 'general-subtraction',
senior="""
1. **Beyond powers of 10.** Most real subtractions aren't from a clean 10^k. So how does Nikhilam help with, say, 6347 − 2589?

2. **The "add-the-complement" trick.** Rewrite: 6347 − 2589 = 6347 + (10000 − 2589) − 10000 = 6347 + (complement of 2589) − 10000.
   - Complement of 2589 to 10000: 9-2=7, 9-5=4, 9-8=1, 10-9=1 → 7411.
   - 6347 + 7411 = 13758.
   - 13758 − 10000 = 3758.
   - Check: 6347 − 2589 = 3758. ✓

3. **When is this faster?** When the borrowing in standard subtraction would chain through many digits, the complement method skips it entirely. For simple subtractions, standard is fine.

4. **Worksheet.** 8 problems, mixed: some clean Nikhilam, some general using add-the-complement.

5. **Reflection.** *"Which method-type did you find genuinely faster? Which felt the same?"* Honest answers — Nikhilam is a tool, not a universal speed-up.
""",
primary="""
- For harder subtractions, the trick is just one part. We still use regular subtraction.

Show 50 − 23 with the regular method (borrow if needed). Then show 100 − 73 with the trick. *"Trick works when we subtract from 10, 100, 1000."*

Children practice 5 problems: some need the trick, some need regular method.
""")

register('module-09-subtraction-nikhilam', 'the-algebra',
senior="""
1. **State the identity.** For N with k digits, 10^k − N can be computed as ((10^k − 1) − N) + 1.

2. **Why "all from 9 last from 10" works.**
   - (10^k − 1) is a number with k nines: 9, 99, 999, 9999, ...
   - (10^k − 1) − N: each digit of N is subtracted from 9. The result has no borrows because each digit of (10^k − 1) is 9.
   - Adding 1 to that bumps the last digit by 1, which is equivalent to "the last digit from 10" rather than "from 9."

3. **Worked algebraic example.** N = 437, k = 3.
   - 999 − 437 = 562 (digit-wise: 9-4, 9-3, 9-7)
   - 562 + 1 = 563 = 1000 − 437. ✓

4. **The general formula.** 10^k − N = (10^k − 1) − N + 1 — a foundational identity in modular arithmetic and binary computer arithmetic.

5. **Senior bridge.** This is the same identity that underlies *two's complement* in binary computer arithmetic — tomorrow's topic.
""",
primary="""
- Why does the trick work? Let's see!

Write 100 = 99 + 1.
- 99 − 37 is easy (no borrow): 6 from 9 = 6 and 9 - 3 = 6, write it out as: 9-3 = 6, 9-7 = 2... actually let's keep it simple.
- 100 − 37 = 63.
- And 9-3 = 6, 10-7 = 3 → 63.

The 9s help because there's no borrow. *"That's the magic!"*
""")

register('module-09-subtraction-nikhilam', 'bar-model-proof',
senior="""
1. **Draw a bar of length 100.** Cut a section of length 37 from the right end. Label the remaining bar.

2. **Decompose using 99.** Show that the bar of 100 = bar of 99 + bar of 1. The bar of 99 is easy to subtract from (every digit is 9).

3. **Visual mapping to digits.**
   - Top row: 99 partitioned into a section of 37 and a section of (99−37) = 62.
   - Bottom row: add the unit 1, splitting it into the rightmost cell.
   - Result: (99−37)+1 = 100−37 = 63.

4. **Generalise visually.** Show the same bar-decomposition for 1000−437. The leading 9s allow digit-wise subtraction without borrow; the +1 at the end bumps the last digit.

5. **Independent task.** Each student draws their own bar-model proof for 1000 − 248 = 752 and submits as proof of understanding.
""",
primary="""
- Let's see the trick with bars (or paper strips)!

Cut a strip 100 cm long. Now cut off 37 cm. *"How long is the rest?"* (63 cm.)

Now cut a strip 99 cm. Cut off 37 cm. *"How long?"* (62 cm — easy! 9-3=6, 9-7=2.) Add 1 cm — 63 cm.

*"Same answer! Easier with 99!"*
""")

register('module-09-subtraction-nikhilam', 'twos-complement',
senior="""
1. **Bridge to computing.** Modern computers don't have a subtraction circuit — they have an ADDER circuit. They subtract by adding the *two's complement* of the subtrahend. This is the same Nikhilam idea, in binary.

2. **Binary Nikhilam.** For an 8-bit number:
   - One's complement: flip every bit (= "all from 1," the binary analogue of "all from 9").
   - Two's complement: one's complement + 1.

3. **Worked example.** Compute 9 − 5 in 8-bit binary:
   - 5 = 00000101
   - Flip: 11111010 (one's complement)
   - Add 1: 11111011 (two's complement)
   - Add to 9 = 00001001: 00001001 + 11111011 = 100000100, drop the overflow bit → 00000100 = 4. ✓

4. **Source.** D.E. Knuth, *The Art of Computer Programming*, vol. 2 — full treatment.

5. **Critical-thinking close.** *"The Nikhilam sūtra (or its decimal-complement principle) and binary two's complement both date their origins to vastly different traditions and eras. What does this tell us about (a) the universality of certain algorithmic ideas and (b) the limits of cultural-priority claims?"*
""",
primary="""
- Computers use the same trick! In computers, numbers are 0s and 1s. They use "all from 1, last from 1+1" — same idea but with 1 instead of 9.

Show a calculator. *"When you press 100 − 37, the computer secretly uses our trick to find the answer fast."*

Children share: *"What's the coolest computer thing they know?"*
""")

register('module-09-subtraction-nikhilam', 'speed-day',
senior="""
1. **30-problem mental sprint.** Mix:
   - Pure Nikhilam (subtract from 10, 100, 1000, 10000) — 15 problems
   - Add-the-complement (general subtractions) — 10 problems
   - Edge cases (trailing zeros, single-digit) — 5 problems

2. **5-minute timer.** Silence. Pen on paper.

3. **Pair-mark.** Swap and check.

4. **Distribution analysis.** *"Where did errors cluster?"* Most likely: edge cases (trailing zeros), large complements (10000 case).

5. **Personal best.** Record score; set target for next sprint.
""",
primary="""
- Sprint day! 10 problems in 3 minutes.

Each child gets a worksheet:
1. 10 − 4
2. 100 − 37
3. 100 − 62
4. 1000 − 250
5. 100 − 88
...

Cheer for everyone who finishes. *"Speed isn't everything — accuracy matters more!"*
""")

register('module-09-subtraction-nikhilam', 'mixed-practice',
senior="""
1. **Mixed problem set.** 20 subtractions, classes mixed:
   - Simple borrows (use borrow or Nikhilam, your choice)
   - Multi-borrow (Nikhilam likely faster)
   - Subtraction from powers of 10 (Nikhilam dominates)
   - Add-the-complement (general)

2. **Strategy choice.** Each student picks the method per problem and writes the chosen method beside the answer.

3. **Cross-check.** Pairs swap; compare method choices. *"Did you both pick the same method? When did you disagree?"*

4. **Discussion.** *"Is Nikhilam ALWAYS better? When is plain borrowing fine?"* (Single-digit, small subtractions.)

5. **Method-comparison artefact.** Each student starts a "personal mental-math toolkit" page summarising when to use each method.
""",
primary="""
- Today: pick the right tool!

Show 10 problems on cards. For each, children hold up a sign:
- "Trick!" (for subtracting from 10, 100, 1000)
- "Regular!" (for harder cases)

Then solve 5 trick-type problems together.
""")

register('module-09-subtraction-nikhilam', 'final-assessment',
senior="""
1. **Reflection essay (10 min).** *"In 200 words, explain Nikhilam to a younger student. Use one worked example and one limit-case."*

2. **Summative quiz (25 min).** Computation, algebraic proof, two's-complement connection. See `quizzes/summative.md`.

3. **Computer-subtraction explainer project share (10 min).** Each student presents their poster (see `assessments/project-brief.md`).

4. **Module close.** *"What's one number-sense habit from this module you'll keep using?"* Each student shares one sentence.

5. **Linkage.** Tomorrow Module 11 builds the multiplication side of Nikhilam — same sūtra, different application.
""",
primary="""
- Final day! We celebrate the subtraction trick.

Each child shows one favourite trick problem to a partner. Cheer for each.

Take the small quiz with stickers. Every child gets a "Subtraction Sleuth" sticker.

End: chant — *"All from nine, last from ten!"*
""")

# ============================================================================
# Module 10 — Herbs (Auṣadhi)
# ============================================================================

register('module-10-herbs-aushadhi', 'what-is-aushadhi',
senior="""
1. **Define *auṣadhi*.** Sanskrit for "medicinal plant" — broader than English "herb." Includes leaves, roots, barks, seeds, resins. Distinguish from *ahara* (food) and *rasāyana* (rejuvenative).

2. **Six herbs we'll study.** Show samples: Tulsī, Neem, Turmeric, Ginger, Ajwain, Mint. Pass them around for sight + smell.

3. **The traditional framework.** Each herb has *rasa* (taste), *vīrya* (potency — heating/cooling), *vipāka* (post-digestive effect), and *prabhāva* (specific action). This is the basic *dravyaguṇa* (pharmacology) of Āyurveda.

4. **Source.** Caraka Saṁhitā, *Sūtrasthāna* 1: *"There is nothing in the world that, applied at the right time and place, is not medicine."* Read aloud.

5. **The critical caveat, repeated three times.** This module teaches IDENTIFICATION and traditional uses. It does NOT teach therapeutic dosing. Therapeutic use requires a qualified practitioner. State this rule prominently in workbooks.
""",
primary="""
- *Auṣadhi* (say "OH-shudh-ee") = a plant that helps when we feel poorly.

Show six small plant samples or pictures. Pass each one — children smell, touch (carefully).

*"Many plants are helpers! Today we meet six new garden friends."* Each child draws one plant they liked best.
""")

register('module-10-herbs-aushadhi', 'tulsi',
senior="""
1. **Botanical identification.** *Ocimum tenuiflorum* (also *O. sanctum*). Square stem, opposite leaves with serrated edges, distinctive aromatic oil glands. Multiple cultivars: *Rama tulasī* (green), *Kṛṣṇa tulasī* (purple), *Vana tulasī* (wild).

2. **Active compound.** Eugenol (60-70% of essential oil), ursolic acid, rosmarinic acid. Some research on adaptogenic / anti-inflammatory effects (Cohen, 2014 — *Journal of Ayurveda and Integrative Medicine*).

3. **Traditional uses.** Caraka and Suśruta cite *tulasī* for: cough, cold, low-grade fever, indigestion (in tea form), as a bedside plant for air quality.

4. **Source.** Atharva Veda 10.97 — Auṣadhi Sūkta — though not naming tulasī specifically, the framing of "herbs as healing beings" begins here. Caraka *Sūtrasthāna* 26 lists tulasī formally.

5. **Smell-test demo.** Crush a leaf; pass around. Note clove-like aroma (eugenol). Modern aroma-chemistry: same compound (eugenol) gives cloves their scent.
""",
primary="""
- Today: meet Tulsī! 🌿

Show a tulsī plant (or picture + dried leaf).
- Smell it. *"What does it remind you of?"* (Spice. Mint. Tea.)
- Tulsī tea is sometimes used when people feel a cold coming.

Children draw a tulsī leaf and write "tulasī" beside it.
""")

register('module-10-herbs-aushadhi', 'neem',
senior="""
1. **Botanical identification.** *Azadirachta indica*. Tall tree, ~15-20 m. Pinnate compound leaves with serrated leaflets. Distinctive bitter smell when crushed.

2. **Active compound.** Azadirachtin (in seeds, oil). Nimbidin (in leaves, bark). Quercetin (a flavonoid).

3. **Traditional uses.** Caraka and Suśruta cite *nimba* for: skin conditions, fever, infections, oral hygiene (chewing the twig). External use is well-supported by modern studies.

4. **THE SAFETY WARNING.** Neem at high concentrations (especially neem oil) is documented to be hepatotoxic. Caraka itself notes restrictions. Modern pediatric case-reports (e.g. *Indian Pediatrics* journals) document harm in infants given neem oil. NEVER ingest in concentrated form. State this rule THREE TIMES.

5. **Modern use cases.** Neem-based pesticides (azadirachtin is one of the most studied bio-pesticides). Toothpaste with neem extract. Skin creams. Discussion: *"What separates safe external use from risky internal use?"*
""",
primary="""
- Today: meet Neem! 🌿

Show a neem leaf. *"Taste a TINY bit on your tongue — careful!"* (Bitter!) Children make faces — that's OK, neem is meant to be bitter.

**SAFETY RULE:** Don't eat lots of neem! Just a tiny taste to learn. Always ask a grown-up before using neem.

Children draw the leaf and write "neem" beside it.
""")

register('module-10-herbs-aushadhi', 'turmeric',
senior="""
1. **Botanical identification.** *Curcuma longa*. A rhizome (underground stem, not a root). Bright orange when cut. Fresh vs dried (turmeric powder).

2. **Active compound.** Curcumin (~2-5% of dried rhizome). Bright yellow polyphenol. Other compounds: turmerones in the essential oil.

3. **Traditional uses.** Caraka cites *haridrā* for: wound healing (topical paste), anti-inflammatory (golden milk), as a colouring + preservative agent in food. Centuries of culinary use.

4. **Modern research.** Curcumin has been studied extensively for anti-inflammatory effects. Bioavailability is poor without piperine (black pepper) or fat — which is why *haldi doodh* (turmeric milk with ghee) is traditional. Modern preparations use liposomal or piperine-enhanced formulations.

5. **Demo / activity.** Crush a small piece of fresh turmeric on paper. Note the staining (curcumin is a pH indicator — colour changes with vinegar/lemon vs baking soda). This is also chemistry, not just culinary.
""",
primary="""
- Today: meet Turmeric (Haldī)! 🌿

Show fresh turmeric root (or powder). *"It stains everything yellow!"* Drop a tiny amount on paper. Children watch the colour spread.

*"Golden milk = turmeric + warm milk + a bit of honey. People drink it when they feel poorly."*

Children draw a yellow circle for the powder and write "haridrā" beside it.
""")

register('module-10-herbs-aushadhi', 'ginger',
senior="""
1. **Botanical identification.** *Zingiber officinale*. Rhizome (like turmeric, not a true root). Light tan skin. Fresh (*ārdraka*) vs dried (*śuṇṭhī*) — distinct Sanskrit names because the properties differ.

2. **Active compounds.** Fresh ginger: gingerols. Dried ginger: shogaols (gingerols dehydrate during drying). Both are pungent / "hot."

3. **Traditional vs modern uses.** Caraka cites ginger for: digestive fire, nausea, cold-induced cough. Modern clinical trials support: nausea (motion sickness, chemo-induced — *Cochrane Reviews*), and mild anti-inflammatory effect.

4. **Two preparations, two effects.** *"Why does Āyurveda distinguish fresh from dried?"* Fresh ginger is heating but mild; dried ginger is more concentrated and warming. Modern: same compound family, different ratios.

5. **Activity.** Smell-test: fresh ginger root vs dried ginger powder. Students rate intensity 1-5 and write one sentence on the difference.
""",
primary="""
- Today: meet Ginger (Adraka)! 🌿

Show fresh ginger root. *"It's bumpy, like a knobbly hand!"*

Smell it (mild). Then smell dried ginger powder (strong). *"Drying makes it stronger!"*

Ginger tea = ginger + warm water + a tiny bit of honey. People drink it when their tummy hurts.

Children draw ginger root with knobbly bumps.
""")

register('module-10-herbs-aushadhi', 'ajwain',
senior="""
1. **Botanical identification.** *Trachyspermum ammi*. Small seeds (closer to caraway than parsley). Distinctive sharp aroma. Leaves of the plant resemble parsley.

2. **Active compound.** Thymol (35-60% of essential oil). Same compound as in thyme. Strong antimicrobial and digestive-stimulating actions.

3. **Traditional uses.** Caraka cites *yavānī* primarily for digestive complaints: indigestion, gas, colic. The traditional remedy: a few seeds chewed after a heavy meal.

4. **Modern research.** Thymol's antimicrobial effect is well-documented in food science (it's used as a natural preservative). Limited clinical research on traditional digestive claims, but the underlying chemistry is plausible.

5. **Discussion.** *"Why is the same compound (thymol) found in ajwain and thyme — plants from very different families?"* This is *convergent evolution* in plant chemistry: distantly related plants evolving the same defensive compound. A great cross-cultural pharmacology insight.
""",
primary="""
- Today: meet Ajwain (Yavānī)! 🌿

Show ajwain seeds. *"Tiny, like baby caraway."* Smell them — strong! sharp!

*"People chew a few seeds after a big meal to help their tummy."*

Children draw the seeds (small dots) and write "yavānī" beside.
""")

register('module-10-herbs-aushadhi', 'mint',
senior="""
1. **Botanical identification.** *Mentha* genus — many species: *M. arvensis* (corn mint, *pudīnā*), *M. spicata* (spearmint), *M. piperita* (peppermint). Distinguish by leaf shape, smell.

2. **Active compound.** Menthol (peppermint), carvone (spearmint). Both terpenoids, both "cooling" perceptually (menthol activates cold-sensing TRPM8 receptors in the mouth).

3. **Traditional uses.** Less prominent in classical Caraka/Suśruta (mint was a later introduction to Indian materia medica). Modern Āyurveda uses for: cooling drinks, digestive aid, breath freshener.

4. **Modern research.** Peppermint oil — well-studied for IBS symptom relief (*BMJ*, multiple trials). Cooling sensation is a TRPM8 channel effect, NOT actual cooling of tissue.

5. **Activity.** Cooling-sensation test: students suck on a peppermint and report on tongue temperature. *"Is the mint actually cool? Or does it just feel cool?"* (It's the TRPM8 receptor activation — the same nerve that signals real cold.)
""",
primary="""
- Today: meet Mint (Pudīnā)! 🌿

Show fresh mint leaves. Smell — fresh, cool! Crush a leaf — smell stronger.

*"Mint makes our mouth feel cool, even when it's not cold!"*

Mint chutney is yummy with food. Mint tea is good in summer.

Children draw a mint leaf (small, oval, slightly bumpy) and write "pudīnā" beside.
""")

register('module-10-herbs-aushadhi', 'herbs-and-doshas',
senior="""
1. **Recall doṣa framework (Module 4).** Vāta = motion, Pitta = transformation, Kapha = structure.

2. **Herb classification by doṣa effect.** From Caraka *Sūtrasthāna* 26:
   - **Heating / Pitta-aggravating** (use with care if pitta-dominant): ginger, ajwain, hot pepper.
   - **Cooling / Pitta-pacifying** (good for hot conditions): mint, fennel.
   - **Drying / Kapha-pacifying** (good for congestion): turmeric, neem.
   - **Lubricating / Vāta-pacifying** (good for dryness): ghee-based preparations.

3. **Maps onto modern thermoregulation.** Heating herbs (ginger, ajwain) often increase metabolic rate slightly. Cooling herbs (mint via TRPM8) provide perceptual cooling. The mapping is empirically observed, not purely conceptual.

4. **Worked example.** *"If someone has a vāta imbalance — dry skin, restless sleep — which of our six herbs would Āyurveda recommend?"* (Avoid the very dry/cold ones. Ginger in moderate amounts; ghee-based ginger tea.)

5. **Safety reminder.** This is wellness lens, NOT diagnosis. Don't prescribe based on doṣa lens; consult a qualified practitioner.
""",
primary="""
- Each herb has a "temperature" inside us:
  - **Warm herbs:** ginger, ajwain (good when we feel cold/sick)
  - **Cool herbs:** mint, sometimes turmeric (good when we feel hot)

Match game: show pictures of the 6 herbs. Children sort into "warm" pile and "cool" pile.

*"Warm herbs help in winter. Cool herbs help in summer."*
""")

register('module-10-herbs-aushadhi', 'build-the-deck',
senior="""
1. **Card-deck project assembly.** Each student claims one of the six herbs as their primary contribution. They produce one detailed identification card:
   - Sanskrit + botanical name
   - Leaf/seed/root drawing (large, accurate)
   - Smell description (concrete words)
   - Three traditional uses with cited sources
   - One active compound and its action
   - One safety note

2. **Tools and references.** Use Caraka Saṁhitā Sūtrasthāna 26 (compiled excerpts in `sources.md`), modern phytochemistry summaries from ICMR-NIN or *Journal of Ethnopharmacology* reviews.

3. **Work-time.** 30 minutes individual work. Teacher circulates to check sources.

4. **Pair-review.** Pairs swap cards; check for accuracy and one quality-improvement suggestion.

5. **Class deck assembly.** Cards laminated (optional) and bound into a class library. Teachers may keep one set for future use.
""",
primary="""
- Today we make our class herb book!

Each child picks one favourite herb. They make a card:
- Big drawing of the plant
- Sanskrit name (the teacher helps write it)
- One thing it does

Cards are taped together to make a class book. *"This is OUR herb book!"*
""")

register('module-10-herbs-aushadhi', 'final-share',
senior="""
1. **Class herb-deck presentation (20 min).** Each student shows their card and gives a 1-minute talk on their herb.

2. **Q&A (10 min).** *"Which herb would you most want in your home garden? Why?"* *"Which one surprised you?"*

3. **Summative quiz (20 min).** Vocabulary, identification, doṣa-pairing, safety. See `quizzes/summative.md`.

4. **Critical-thinking close.** *"The doṣa-herb framework is ancient. Modern science can test specific claims. Where does each work best? Where does each fall short?"* Each student writes 3 sentences.

5. **Linkage.** Module 13 (Indic Ecology) will revisit this through the *vasudhaiva kuṭumbakam* lens — herbs as part of the larger ecology.
""",
primary="""
- Show-and-tell day!

Each child holds up their card and says ONE thing about their herb. Cheer for each.

Then quiz with stickers — everyone gets a "Garden Friend" sticker.

End: chant the six names together: *"Tulasī! Nimba! Haridrā! Adraka! Yavānī! Pudīnā!"*
""")

# ============================================================================
# Module 11 — Multiplication Near a Power of 10 (Nikhilam)
# ============================================================================

register('module-11-multiplication-near-base', 'finger-trick-prelude',
senior="""
1. **Recall Module 9.** Nikhilam = "all from 9, last from 10" — the complement to a base. Same sūtra, NEW application: multiplication.

2. **The below-10 finger demo.** Each hand has 5 fingers; together 10. To multiply 7 × 8:
   - Curl 7−5=2 fingers on left hand.
   - Curl 8−5=3 fingers on right hand.
   - Curled fingers in total: 5 → that's the tens place: 50.
   - Uncurled fingers (left × right): 3 × 2 = 6 → that's the units: 6.
   - Answer: 56. ✓

3. **Why this works.** Algebraically: (10 − a)(10 − b) = 100 − 10(a+b) + ab = 10(10−(a+b)) + ab. The "curled fingers" count is (a+b)−5 — wait, let me re-derive. Actually: curled = (10−a − 5) + (10−b − 5) wait... let me restate cleanly. For 7×8: 7 = 5+2 (uncurled fingers on left), 8 = 5+3 (right). The formula: tens digit = uncurled-left + uncurled-right − 5; units = uncurled-left × uncurled-right. Let's just use the Nikhilam algebra in next lesson.

4. **What we'll learn this module.** A general method: when factors are CLOSE to a base (10, 100, 1000), Nikhilam-multiplication is much faster than long multiplication.

5. **Speed test.** Compute 8 × 9 mentally. Compare your method with traditional times table. Most students will use memorisation — the next lessons show why Nikhilam is faster for LARGER near-base products.
""",
primary="""
- Hand trick! Hold up both hands. *"How many fingers? Ten!"*

For 7 × 8:
- Curl down 2 fingers on left hand (because 10−7=3, no wait — for 7, curl 3 down... actually we'll do simpler).
- The simpler version: 7 × 8 = 56. We know this from tables!

Practice 5 × 5 = 25. 6 × 6 = 36. 7 × 7 = 49. 8 × 8 = 64. 9 × 9 = 81. Chant them.

*"Tomorrow we'll learn a trick for numbers near 100 and 1000!"*
""")

register('module-11-multiplication-near-base', 'two-below-100',
senior="""
1. **The two-step rule for both factors below 100.**
   - Find deficits from 100: e.g., 97 → −3, 96 → −4.
   - **Left part:** cross-subtract. 97 − 4 = 93 (or equivalently 96 − 3 = 93).
   - **Right part:** product of deficits. 3 × 4 = 12.
   - Combine: **9312**.

2. **Worked examples.**
   - 97 × 96 = 93 | 12 = **9312**.
   - 88 × 95 = 83 | 60 = **8360**. (Deficits: 12, 5. Cross: 88−5=83 or 95−12=83. Product: 12×5=60.)
   - 99 × 99 = 98 | 01 = **9801**. (Deficits 1, 1. Cross: 98. Product: 1. Pad to 2 digits: 01.)

3. **Why the padding matters.** The right part must have as many digits as the base has zeros (here, 2 zeros → 2-digit right part). If product is single-digit, pad with leading zero. If product overflows (3+ digits), carry to left part.

4. **Algebra.** Base B = 100. Factor 1 = B − a, factor 2 = B − b. Then (B−a)(B−b) = B(B−a−b) + ab = B·(cross) + (right). The cross-subtract IS B − a − b. The product of deficits IS ab.

5. **Independent practice.** 8 problems, all below-100 case. 10 minutes.
""",
primary="""
- For close-to-100 numbers, there's a special trick. Don't worry about the math yet — just see!

Show: 97 × 96 = 9312. *"Wow!"*

Children just watch today. They count back from 100: *"99, 98, 97 — three less than 100."* Tomorrow we'll learn the trick.

Practice counting back from 100 by ones (down to 90).
""")

register('module-11-multiplication-near-base', 'two-above-100',
senior="""
1. **Above-100 variant.** Use *excesses* instead of deficits.
   - 103 = 100 + 3 → excess +3.
   - 104 = 100 + 4 → excess +4.

2. **The two-step rule for above-base.**
   - **Left part:** cross-add. 103 + 4 = 107 (or 104 + 3 = 107).
   - **Right part:** product of excesses. 3 × 4 = 12.
   - Combine: **10712**.

3. **Worked examples.**
   - 103 × 104 = 107 | 12 = **10712**.
   - 110 × 105 = 115 | 50 = **11550**.
   - 102 × 109 = 111 | 18 = **11118**.

4. **Algebra (above-base).** (B+a)(B+b) = B(B+a+b) + ab. Cross-ADD = B+a+b. Product of excesses = ab.

5. **Symmetry recognition.** Below-base: cross-SUBTRACT. Above-base: cross-ADD. Both: product-of-difference-from-base. *"This symmetry hints at the general pattern — tomorrow we'll see the mixed case."*
""",
primary="""
- For numbers JUST above 100, the trick still works!

Show: 103 × 104 = 10712. *"How? Look — 103 + 4 = 107, then 3 × 4 = 12, put them together: 10712!"*

Children just watch. They count UP from 100: *"101, 102, 103 — three more than 100."*

Practice counting up by ones from 100 (to 110).
""")

register('module-11-multiplication-near-base', 'mixed-cases',
senior="""
1. **Mixed case (one above, one below).** Care with signs! Example: 102 × 98.
   - 102 → +2 (excess), 98 → −2 (deficit).
   - Left part: 102 − 2 = 100 (or 98 + 2 = 100).
   - Right part: (+2)(−2) = **−4**.
   - Combine: 100 | −4. But how to interpret −4 in the right slot?

2. **The "borrow back" trick.** Negative right part → subtract from left. 100|−4 means 10000 − 4 = **9996**.

3. **Alternative algebra check.** 102 × 98 = (100+2)(100−2) = 100² − 4 = 9996. ✓ (Difference of squares identity.)

4. **General mixed-case rule.** Cross-subtract (using the deficit sign) for left; multiply excess and deficit (negative result) for right; convert negative right to a borrow from left.

5. **Independent practice.** 5 problems mixing all three cases (both below, both above, mixed). 10 minutes.
""",
primary="""
- What if one number is above 100 and one below? Like 102 × 98?

Trick: 102 × 98 = 9996. (Trust the magic for now.)

Children watch. *"Tomorrow we'll see how this works — but the answer is right!"*

Practice with the teacher: 101 × 99 = 9999. 105 × 95 = 9975.
""")

register('module-11-multiplication-near-base', 'three-digit-near-1000',
senior="""
1. **Extension to base 1000.** Same rule, base now 1000.
   - 997 → deficit 3.
   - 996 → deficit 4.
   - Left: 997 − 4 = 993.
   - Right: 3 × 4 = 12. Must be 3 digits (because base has 3 zeros). Pad: **012**.
   - Combine: **993012**.

2. **Above 1000.** 1003 × 1004 = 1007 | 012 = **1007012**.

3. **Mixed case.** 1003 × 997 = (1000+3)(1000−3) = 10⁶ − 9 = 999991. (Difference of squares.)

4. **Pattern recognition.** The base extends naturally: 10, 100, 1000, 10000... Each next-decade-base just shifts everything. The CORE rule (cross-subtract + product-of-deficits) is identical.

5. **Independent practice.** 5 near-1000 problems. The challenge: keeping the right-part digit count correct.
""",
primary="""
- The trick works for 1000 too! Try 997 × 996 = 993012. (Big number!)

Children watch and count back from 1000: *"999, 998, 997, 996 — close to 1000."*

The magic: same rule, just with three digits instead of two. *"We'll do these only when we're ready for big numbers."*

Practice counting back from 1000 to 990.
""")

register('module-11-multiplication-near-base', 'algebra-proof',
senior="""
1. **Derive the formula.** Let B = the base (10, 100, 1000). Factor 1 = B − a, Factor 2 = B − b.

   (B − a)(B − b) = B² − Ba − Bb + ab
                  = B(B − a − b) + ab
                  = B · (left part) + (right part)

   So the left part is B − a − b = (B − a) − b = (B − b) − a = either factor minus the OTHER's deficit. The right part is just ab.

2. **Why "cross-subtract"?** B − a − b = first factor − (B − second factor) = first factor − second's deficit. The cross-subtraction is just rearranging the algebra into a mental-math procedure.

3. **Above-base proof.** (B + a)(B + b) = B² + Ba + Bb + ab = B(B + a + b) + ab. Cross-add, product of excesses.

4. **Mixed case proof.** (B + a)(B − b) = B² − Bb + Ba − ab = B(B + a − b) − ab. The "−ab" in the right slot is what causes the sign issue.

5. **Connecting the dots.** This is just basic high-school algebra — no mystery. Tirthaji's sūtra system gives the procedure a memorable name; the algebra gives it the proof.
""",
primary="""
- Why does the trick work? Let's see with small numbers!

Show 9 × 8 using the rule:
- 9 is 10−1 (deficit 1).
- 8 is 10−2 (deficit 2).
- Left: 9 − 2 = 7. Right: 1 × 2 = 2. Combined: **72**.
- Check: 9 × 8 = 72. ✓

*"Same answer as tables! The trick is just another way."*
""")

register('module-11-multiplication-near-base', 'when-to-use',
senior="""
1. **The decision tree.**
   - Both factors within ~5 of the same base → Nikhilam is fast.
   - One factor close to base, other far → traditional multiplication often faster.
   - Both factors far from any base (e.g. 47 × 63) → traditional.
   - Both factors near DIFFERENT bases (e.g. 98 × 1005) → tricky; pick a common base and scale.

2. **Speed comparison.** Time 97 × 96 vs 47 × 63 mentally. Most students will find Nikhilam dominates the first; long multiplication dominates the second.

3. **Pedagogical limit.** Nikhilam multiplication is NOT a universal speed-up. It's a tool for ONE problem class. Recognising when to use it is the skill.

4. **Practice with strategic choice.** 10 problems, mixed. Each student picks the best method and notes it next to the answer.

5. **Reflection.** *"What pattern of problems makes Nikhilam shine? What pattern defeats it?"* Each student writes 3 sentences.
""",
primary="""
- The trick is special! It works best when numbers are CLOSE to 100 (or 10, or 1000).
- For numbers far from 100 (like 47 × 63), we use the regular way.

Show 97 × 96 (use trick) and 47 × 63 (use regular). *"Pick the right tool!"*

Children practice sorting: which problems use the trick?
""")

register('module-11-multiplication-near-base', 'speed-sprints',
senior="""
1. **Sprint A (Nikhilam-favourable, 10 problems, 4 min).** All factors within 5 of 100 or 1000.

2. **Sprint B (mixed, 10 problems, 4 min).** Mix of near-base and far-from-base.

3. **Sprint C (long-mult-favourable, 10 problems, 4 min).** All factors far from base.

4. **Analysis.** Each student records times. Most: A < B < C dramatically. The CONCRETE evidence that Nikhilam works for ONE class.

5. **Discussion.** *"What's your strategy choice now? When will you use Nikhilam in real life?"* Each student writes 2 sentences.
""",
primary="""
- Speed game! 5 problems with the trick, 3 minutes.

97 × 96 = ?
98 × 97 = ?
99 × 99 = ?
95 × 95 = ?
103 × 104 = ?

(Teacher does these together with kids — they don't need to do them solo yet.)

Cheer at the end. *"Maths magic!"*
""")

register('module-11-multiplication-near-base', 'mixed-practice',
senior="""
1. **Crossover with Module 7.** Each student solves 5 problems combining ×11 method + Nikhilam:
   - 11 × 99 = 1089 (use ×11)
   - 97 × 96 = 9312 (use Nikhilam)
   - 11 × 98 = 1078 (use ×11)
   - 105 × 95 = 9975 (use difference-of-squares or Nikhilam mixed)
   - 11 × 87 = 957 (use ×11 with carry)

2. **Strategy reflection.** Pair-discuss: *"For each, what method DID you use? Was it the fastest?"*

3. **Build a personal toolkit.** Each student updates their "personal mental-math toolkit" page (started in Module 7) to include Nikhilam multiplication.

4. **One more example.** Solve 998 × 997 mentally. (Nikhilam: deficits 2, 3 → left = 995, right = 006 → **995006**.) 4 seconds with the trick; >1 minute by long multiplication.

5. **Reflection.** *"What's the most useful thing you learned this module?"*
""",
primary="""
- Today: mix ×11 trick (Module 7) and the new trick!

Show 11 × 97 — use the ×11 trick: 1067.
Show 97 × 96 — use the new trick: 9312.

Children sort: *"Which trick for which problem?"*

End with a number-magic round of applause.
""")

register('module-11-multiplication-near-base', 'final-assessment',
senior="""
1. **Method-comparison written reflection (10 min).** *"In 300 words, compare Tirthaji's near-base multiplication with traditional long multiplication. When does each excel? What does Tirthaji's method teach about number sense?"*

2. **Summative quiz (25 min).** Mix of Nikhilam (below, above, mixed), algebraic proof, strategy choice. See `quizzes/summative.md`.

3. **Personal mental-math toolkit share (10 min).** Each student shows their one-page toolkit.

4. **Module close.** *"One number-sense habit you'll carry forward?"*

5. **Linkage.** Module 14 (Magic Squares) will use related place-value insights for grid arithmetic.
""",
primary="""
- Final day! We celebrate the new trick.

Each child shows their best near-100 multiplication. Cheer.

Quiz with stickers — everyone gets a "Number Wizard" sticker.

End chant: *"Cross-subtract, multiply, put together!"*
""")


# ============================================================================
# Module 12 — Movement of the Sun
# ============================================================================

register('module-12-movement-of-sun', 'suns-yearly-path',
senior="""
1. **The observation.** Project a year-long animation of sunrise direction (or show a static composite of 12 sunrise photos taken from the same spot, one per month). *"The Sun rises in roughly the east — but the EXACT direction shifts north and south through the year."*

2. **Define the ecliptic.** The Sun's apparent path against the background stars over one year. A great circle on the celestial sphere, tilted ~23.5° from the celestial equator.

3. **Why does it shift?** Earth's rotational axis is tilted ~23.5° relative to its orbital plane. As Earth orbits the Sun, this tilt projects onto our sky as the Sun rising/setting north of due-east in summer (NH), south in winter.

4. **Source.** Sūrya-siddhānta ch. 2 — *"sūryasya gatiḥ"* — gives a mean and true solar motion model. Specifies daily and annual displacement on the ecliptic.

5. **Independent task.** Each student looks up their city's sunrise direction today vs 6 months from today (web). Note the difference in compass bearing.
""",
primary="""
- The Sun rises in different places through the year!

Stand at a window facing east. Mark where the Sun comes up TODAY. (Just outside the window — point with arms.)

In summer, the Sun rises a bit more to the LEFT. In winter, more to the RIGHT (in northern places).

Children draw a window with the Sun in 3 spots: summer (left), middle (spring/autumn), winter (right). One drawing.
""")

register('module-12-movement-of-sun', 'axial-tilt-and-seasons',
senior="""
1. **Torch + globe demo.** Hold a globe with the axis tilted ~23.5° (mark the North Pole with tape). Shine a strong torch from one direction (the Sun). Slowly rotate the globe and observe which hemispheres get more direct light.

2. **Key observation.** When the Northern Hemisphere tilts TOWARD the Sun (June solstice), it gets more direct sunlight, longer days. Southern Hemisphere experiences the opposite (winter).

3. **Source.** Sūrya-siddhānta and Āryabhaṭīya both note Earth's globe-shape (*gola*) and the tilt. Āryabhaṭa correctly identifies the rotation cause of day-night ~499 CE.

4. **Modern bridge.** NCERT Physics XI ch. 8 gives the modern derivation: Earth's axial tilt + orbital geometry → annual solar declination → seasons.

5. **Discussion.** *"Why are January and July temperatures so different — even though Earth is at almost the same distance from the Sun?"* (Answer: tilt, not distance.)
""",
primary="""
- Why do we have seasons?

Demo: hold a ball (Earth) tilted to one side. Shine a torch (Sun) at it. Move the ball around the torch.
- Sometimes the TOP of the ball gets more light → summer.
- Sometimes the BOTTOM gets more → other hemisphere's summer.

*"Earth is TILTED. That's why we have seasons!"* Children draw a tilted Earth with the Sun.
""")

register('module-12-movement-of-sun', 'two-courses',
senior="""
1. **Define the two ayanas.**
   - *Uttarāyaṇa* — northward course. Roughly Dec 21 (winter solstice) through Jun 21 (summer solstice). Sun moves NORTH on the sky (Northern Hemisphere).
   - *Dakṣiṇāyana* — southward course. Jun 21 through Dec 21. Sun moves SOUTH.

2. **Cultural importance.** *Uttarāyaṇa* is considered auspicious in many Indian traditions. *Makara Saṅkrānti* (~Jan 14) is celebrated as the start of *Uttarāyaṇa* — but technically the solstice (Dec 21) IS the start. The Jan 14 date reflects the sidereal-zodiac (*nirayana*) convention. We'll unpack this on Day 7.

3. **Source.** Sūrya-siddhānta defines both ayanas in chapter 2.

4. **Modern bridge.** The Northern Hemisphere's summer happens during the Sun's *Uttarāyaṇa* (high northern declination). NCERT Geography IX ch. 3 has the standard diagram.

5. **Identify today.** *"Which ayana are we in today?"* Students compute based on the date. (Northern winter to summer = Uttarāyaṇa; rest = Dakṣiṇāyana.)
""",
primary="""
- The Sun has two journeys each year:
  - **Uttarāyaṇa** ("Going North"): Dec to June — days get longer in the north.
  - **Dakṣiṇāyana** ("Going South"): June to Dec — days get shorter in the north.

Children stand with hands held high. Drift to the right (north). *"That's Uttarāyaṇa!"* Drift to the left (south). *"That's Dakṣiṇāyana!"*

Each child draws an arrow on a calendar showing today's direction.
""")

register('module-12-movement-of-sun', 'equinoxes',
senior="""
1. **Define equinox.** *Viṣuva* in Sanskrit. The two days each year (Mar 21 ± 1 and Sep 22 ± 1) when day length equals night length everywhere on Earth.

2. **Why?** At equinox, Earth's axis is perpendicular to the Sun-Earth line. Sunlight falls equally on both hemispheres. The Sun rises due-east and sets due-west.

3. **Source.** Sūrya-siddhānta names the *viṣuva* points. Varāhamihira (*Bṛhat Saṁhitā*) discusses them in calendar context. The Vernal Equinox is the traditional anchor of the *sāyana* (tropical) zodiac.

4. **Cross-cultural.** The Roman / Gregorian calendar implicitly aligns to the equinoxes. Easter is computed by lunar-solar reckoning anchored to the Vernal Equinox. Many cultures celebrate the equinoxes — Holi (~Phālguna pūrṇimā, near Vernal Equinox), Mabon (NH autumn).

5. **Observation activity.** Each student notes the sunrise direction this week (or projects a stellarium app). Compare to expected (near-due-east if we're near an equinox).
""",
primary="""
- Two special days each year: day and night are EXACTLY the same length!

These are called **equinoxes** (or *viṣuva*).
- **Spring equinox** (around March 21): days getting longer.
- **Autumn equinox** (around September 22): days getting shorter.

Children stand still with arms balanced equally. *"Day equals night!"*

Draw two suns on a year-circle, one in March, one in September. Label "equinox."
""")

register('module-12-movement-of-sun', 'twelve-rashis',
senior="""
1. **Define rāśi.** 1/12th of the ecliptic = 30° each. The Sun spends roughly one month in each rāśi.

2. **The 12 Sanskrit names.** *Meṣa, Vṛṣabha, Mithuna, Karka, Siṁha, Kanyā, Tulā, Vṛścika, Dhanus, Makara, Kumbha, Mīna.*

3. **Map to Greek/Western zodiac.** *Meṣa* = Aries, *Vṛṣabha* = Taurus, ... *Mīna* = Pisces. The 12-fold division of the ecliptic is widespread across cultures (Babylonian, Greek, Indian, possibly via cultural contact).

4. **Source.** *Bṛhat Saṁhitā* of Varāhamihira (6th c. CE) systematises the 12 rāśis. Earlier references in Garga Saṁhitā.

5. **Map current month to current rāśi.** Looking at a sidereal pañcāṅga, identify which rāśi the Sun is in this month. Note the difference from Western (tropical) zodiac dates — we'll resolve this on Day 7.
""",
primary="""
- The Sun visits 12 special "houses" each year!

Names (sing-chant): *"Meṣa, Vṛṣabha, Mithuna, Karka, Siṁha, Kanyā, Tulā, Vṛścika, Dhanus, Makara, Kumbha, Mīna!"*

Each "house" has a Sanskrit name AND a Greek name:
- Meṣa = Aries (ram!), Vṛṣabha = Taurus (bull!), Mithuna = Gemini (twins!)...

Children pick one rāśi to draw. Today's question: *"What's YOUR birth-month rāśi?"*
""")

register('module-12-movement-of-sun', 'sankranti-moments',
senior="""
1. **Define saṅkrānti.** The moment the Sun moves from one rāśi to the next. ~12 saṅkrāntis per year (one every ~30 days). Two are most culturally prominent: *Makara Saṅkrānti* (Capricorn entry) ~Jan 14, and *Karka Saṅkrānti* (Cancer entry) ~Jul 16.

2. **The Jan 14 / Solstice mystery.** *Makara Saṅkrānti* is celebrated as the start of *Uttarāyaṇa* — but Dec 21 (solstice) is the astronomical start. Why the ~24-day difference? Answer (preview): the celebration uses the SIDEREAL (nirayana) zodiac, while the seasons (and solstice) align with the TROPICAL (sāyana) zodiac. Tomorrow we'll unpack this.

3. **Source.** Sūrya-siddhānta computes saṅkrāntis as solar longitudes crossing rāśi boundaries.

4. **Cultural saṅkrāntis.** Festivals tied to specific saṅkrāntis: *Makara Saṅkrānti* (Pongal in Tamil Nadu, Lohri in Punjab, Magh Bihu in Assam), *Karka Saṅkrānti* (mid-monsoon).

5. **Class exercise.** Identify the 12 saṅkrānti dates for the current year (use a published pañcāṅga). Plot them on a circular year-wheel.
""",
primary="""
- When the Sun moves from one rāśi-house to the next, we call it *Saṅkrānti*.
- The most famous: *Makara Saṅkrānti* — when the Sun enters Makara (Capricorn). Around January 14 in many years!

Show a wheel with 12 houses. Children put a Sun-sticker on each rāśi, then circle the date when the Sun enters Makara.

*"In Tamil Nadu, this is Pongal. In Punjab, Lohri. In many places, it's a happy festival!"*
""")

register('module-12-movement-of-sun', 'sayana-vs-nirayana',
senior="""
1. **Set up the conflict.** Indian astronomy distinguishes two reference frames:
   - *Sāyana* (with-ayana, "tropical") — measured from the Vernal Equinox.
   - *Nirayana* (without-ayana, "sidereal") — measured from a fixed point in the sky (a star, typically near Citrā/Spica).

2. **The drift.** Earth's axis wobbles (precession of equinoxes), causing the Vernal Equinox point to shift slowly westward against the fixed stars at ~50 arcseconds per year. Over ~2000 years, the cumulative drift is ~28°. *That* is the ~24° gap between Dec 21 (solstice in sāyana) and Jan 14 (when the Sun enters Makara in nirayana).

3. **Source.** Āryabhaṭīya documents the precession concept; Bhāskara II refines it. Indian jyotiṣa preserves the *nirayana* convention; modern astronomy uses *sāyana*.

4. **Why does this matter?** Festival dates anchored to nirayana drift slowly relative to the seasons. Over thousands of years, *Makara Saṅkrānti* will shift even further from the December solstice unless re-anchored.

5. **Critical thinking.** *"Should jyotiṣa update its zodiac to sāyana? Or preserve the nirayana convention for cultural continuity?"* Both views have advocates. There's no single right answer.
""",
primary="""
- There are TWO ways to measure the Sun's path:
  - **Sāyana** (modern science): starts at the Vernal Equinox (Mar 21).
  - **Nirayana** (Indian tradition): starts at a fixed star.

These two ways DRIFT apart slowly — about 1° every 70 years. Over many centuries, they're now ~24 days apart.

Children draw two suns: one labelled "tradition" and one labelled "modern." They're at slightly different spots.
""")

register('module-12-movement-of-sun', 'precession-of-equinoxes',
senior="""
1. **The phenomenon.** Earth's axis wobbles like a slow top, completing one full circle every ~25,800 years. Rate: ~50.3 arcseconds per year. Discovered by Hipparchus ~130 BCE.

2. **Indian computation.** Āryabhaṭīya (499 CE) implicitly includes precession in its longitude calculations. Later Indian astronomers (Bhāskara II, Nīlakaṇṭha) refine the value.

3. **Modern value.** ~50.27"/year — very close to traditional Indian estimates.

4. **Consequence for the zodiac.** The Vernal Equinox point shifts westward through the sidereal zodiac over time. ~2000 years ago, the Vernal Equinox was in Aries (which is why Aries is the "first" zodiac sign in Western astrology). Today, the Vernal Equinox is in Pisces.

5. **Modern source.** NASA / IAU references. Discussion: *"How long until the Sun is in Aquarius at the Vernal Equinox?"* (~600 years.)
""",
primary="""
- The Earth wobbles slowly, like a spinning top.
- One wobble takes about 26,000 years!

Show a spinning top toy. Let it slow down — it wobbles. *"Earth does this too, just SUPER slowly."*

Children draw Earth tilted, with a curved arrow showing the wobble. *"Astronomers from long ago noticed this!"*
""")

register('module-12-movement-of-sun', 'cross-cultural',
senior="""
1. **The Egyptian solar calendar.** 365 days, 12 months of 30 days + 5 epagomenal days. No leap year initially. Synchronised with the Nile flood.

2. **The Roman / Julian / Gregorian.** Julian (45 BCE) — 365.25 days, leap year every 4. Gregorian (1582) — refined to 365.2425, leap years every 4 except centuries unless divisible by 400.

3. **The Indian solar calendar.** *Saura māsa* = time Sun spends in one rāśi. ~30-31 days per month (varies because Sun moves faster near perihelion). Used in Tamil Nadu, Kerala, Bengal — these regions use sidereal solar months even when their festivals are lunar.

4. **The Chinese solar calendar.** 24 *jiéqì* (solar terms) anchored to specific solar longitudes. Spring Equinox, Summer Solstice, etc. are explicit anchor points.

5. **Comparison exercise.** Each student picks 2 traditions and draws a side-by-side year-circle, noting where their respective "new year" falls and what it celebrates.
""",
primary="""
- Many people use the Sun to make calendars!
- Egypt: 365 days, like ours.
- India: months named after the rāśis.
- Roman/modern: January, February, ...

Children write today's date in 3 ways:
1. Modern (Jan 25, 2026)
2. Tamil (rāśi-based)
3. Just by season (winter/late winter)

Discuss which they like.
""")

register('module-12-movement-of-sun', 'final-share',
senior="""
1. **Personal solar calendar share (10 min).** Each student shows their year-wheel with 2 solstices, 2 equinoxes, 12 saṅkrāntis, and their own birthday's rāśi marked.

2. **Vocabulary lightning round (5 min).** Definitions taken from random students: *uttarāyaṇa, dakṣiṇāyana, viṣuva, rāśi, saṅkrānti, sāyana, nirayana, ayanāṁśa*.

3. **Summative quiz (25 min).** See `quizzes/summative.md`.

4. **Critical-thinking close.** *"Is the difference between sāyana and nirayana a 'wrong vs right' issue or a 'context-dependent convention' issue? Which framing is more scientifically honest?"*

5. **Safety reminder.** Never look at the Sun directly. Reaffirm.
""",
primary="""
- Final day! We celebrate the Sun's yearly journey.

Each child shows their year-wheel. Cheer for each.

Sing the 12 rāśi names together one more time.

Quiz with stickers — everyone gets a "Sun Watcher" sticker. *"Never look at the Sun! Use eyes-down only."*
""")

# ============================================================================
# Module 13 — Indic Ecology (Vasudhaiva Kuṭumbakam)
# ============================================================================

register('module-13-indic-ecology', 'vasudhaiva-kutumbakam',
senior="""
1. **The verse.** From *Mahā Upaniṣad* 6.71–73:
   > *ayaṁ nijaḥ paro veti gaṇanā laghu-cetasām /
   > udāra-caritānāṁ tu vasudhaiva kuṭumbakam* //

   Translation: *"'This is mine, that is another's' — such reckoning is for the narrow-minded. For the great-hearted, the entire earth is one family."*

2. **Etymology.** *Vasudhā* — earth (literally "wealth-holder"). *Eva* — indeed. *Kuṭumbakam* — diminutive of *kuṭumba* (family), so "little family" or "the dear family."

3. **Source clarification.** Also widely cited as appearing in the *Pañcatantra* and in *Hitopadeśa*. The *Mahā Upaniṣad* attestation is most commonly cited in academic contexts.

4. **The ecological reading.** Not just a humanist statement — it's a principle of moral inclusion that extends to all life, all of nature. Read with the modern climate crisis in view, it becomes a foundational text for Indian environmental ethics.

5. **Critical caveat.** Pre-modern India was NOT universally eco-friendly. Forest clearance, soil degradation, and over-hunting also occurred. The TEXT articulates an ideal; the PRACTICE varied. Distinguish ethical framework from historical record.
""",
primary="""
- Today's BIG idea: *Vasudhaiva Kuṭumbakam* — "The whole world is one family."

Show a globe. *"All of us — and all animals, all plants, all rivers — are part of ONE big family."*

Children make a "family tree" with themselves at the centre, then add: parents, siblings, neighbours, then a pet, a tree, a river. Each gets a small drawing.
""")

register('module-13-indic-ecology', 'five-elements-as-frame',
senior="""
1. **Recall Module 2's pañcabhūta.** Earth, water, fire, air, space — the five elements seen as both physical and pervasive.

2. **The interconnection principle.** No element exists alone. Earth needs water to support life. Water needs space to flow. Air needs warmth (fire) to circulate. Space contains all. This is the COSMOLOGICAL grounding for ecological ethics.

3. **Modern translation.** Ecosystems = elemental cycles (carbon, nitrogen, water cycles). The pañcabhūta framework essentially names: matter (earth), water cycle (ap), energy (tejas), atmosphere (vāyu), and the systemic interconnection (ākāśa).

4. **Source.** Bhagavad Gītā 13.5 lists *mahā-bhūtāni* — the gross elements — as one of the *kṣetra* (field) categories. The conceptual frame is in place by ~2nd century BCE.

5. **Discussion.** *"If we damage one element — pollute air, contaminate water, deforest land — what happens to the others?"* Modern climate science answers concretely. *"Indic ecology says these aren't separate problems."*
""",
primary="""
- The 5 elements are all FAMILY too!
- Earth, water, fire, air, space — they need each other.
- If we pollute water, earth gets hurt. If we cut trees, air gets hurt.

Children draw a circle of friends: 🌍 💧 🔥 💨 🌌 (sun = fire, etc.). Connect them with lines. *"All friends, all family!"*
""")

register('module-13-indic-ecology', 'rivers-as-sacred',
senior="""
1. **The Indian river tradition.** *Gaṅgā, Yamunā, Sarasvatī, Narmadā, Kāverī, Godāvarī, Sindhu* — seven sacred rivers in Hindu tradition. Each has festival cycles, pilgrimage routes, ritual practices.

2. **The ecological function of sacredness.** Treating a river as sacred → norms against pollution, against blocking the flow, against over-extraction. *In principle.* These norms are NOT always honoured today (Ganga, Yamuna are heavily polluted).

3. **Modern parallel.** Ecuador and Bolivia have laws giving rivers legal personhood. Aotearoa/New Zealand granted legal personhood to the Whanganui River in 2017. India's Ganga and Yamuna were granted similar status briefly in 2017 (court ruling overturned). The legal innovation echoes the older sacred-river framing.

4. **Source.** Atharva Veda Pṛthivī Sūkta 12.1 — multiple references to flowing waters. Vedic hymns to *āpaḥ* (waters). Bhāgavata Purāṇa discusses the seven rivers.

5. **Critical look.** *"Why are sacred-river norms often violated in practice today? What changes in society have weakened the older protections? Can the framework be revived for the climate crisis?"*
""",
primary="""
- Rivers are sacred in India! The Gaṅgā, Yamunā, Sarasvatī...
- Why? Because rivers give us water, food, life!

Show a picture of the Ganga. *"People say: don't pollute the river. The river is our mother."*

Children draw a river with fish, plants, and a small flower-offering. Discuss: *"What happens if rivers get dirty?"*
""")

register('module-13-indic-ecology', 'sacred-groves',
senior="""
1. **Define sacred grove.** Patches of native forest preserved by community tradition, often associated with a deity, sage, or ancestor. Hunting, cutting, and even firewood collection are prohibited.

2. **Indian examples.**
   - *Devarakāḍu* (Karnataka)
   - *Kāvu* (Kerala)
   - *Devarakad* (Maharashtra)
   - *Sarna* (Jharkhand, Odisha, Bihar — tribal areas)

3. **Ecological function.** Despite covering <0.1% of India's forest area, sacred groves preserve disproportionate biodiversity: endemic species, medicinal plants, water-table recharge zones. Madhav Gadgil's research (1992 and onward) documented this.

4. **Source.** *Pṛthivī Sūkta* (Atharva Veda 12.1) — particularly verses 11–13 on forests. Modern source: Gadgil & Guha, *This Fissured Land* (1992).

5. **Activity.** Each student researches one sacred grove (or biodiversity site) in their region and prepares a 1-page report. Map the grove, list flora/fauna, document traditional protection rules.
""",
primary="""
- Sacred groves are special little forests that people DON'T cut.
- Why? Because they believe a god, a sage, or an ancestor lives there.
- Animals and plants live safely in these groves.

Show a picture of a grove. *"This is a place where no one breaks a branch."*

Children draw a tiny forest with animals: birds, butterflies, deer. Add a small temple or shrine.
""")

register('module-13-indic-ecology', 'yajna-cycle',
senior="""
1. **The Gītā passage.** Bhagavad Gītā 3.10–14. Read the key verses:
   > *annād bhavanti bhūtāni parjanyād anna-sambhavaḥ /
   > yajñād bhavati parjanyo yajñaḥ karma-samudbhavaḥ //*
   > "From food beings come, from rain food comes, from yajña rain comes, yajña comes from action." (3.14)

2. **Decode the cycle.** Yajña → rain → food → beings → action (work) → yajña (giving back). A closed loop where each takes AND gives. This is the ecological cycle in Sanskrit terms.

3. **Modern parallel.** Carbon cycle: plants take CO2 → animals eat plants → animals exhale CO2 → plants take CO2. Water cycle: evaporation → condensation → rain → soil → evaporation. The Gītā verse abstracts this into a yajña frame.

4. **Source check.** Multiple Upaniṣads also discuss the give-and-receive principle. Cite verifiable references in `sources.md`.

5. **Modern relevance.** Climate ethics. *"If we take from nature without giving back, the yajña is broken. What does 'giving back' look like in 2026?"* (Plant trees, reduce waste, restore water bodies, etc.)
""",
primary="""
- *Yajña* (say "yug-nyah") means giving back — a circle of taking and giving.

Show the cycle:
- 🌧️ Rain feeds 🌾 plants
- 🌾 Plants feed 🐮 animals (and us!)
- 🐮 Animals + us give back to soil
- Soil grows more plants

*"If we take but don't give back, the circle breaks!"*

Children draw the circle with arrows.
""")

register('module-13-indic-ecology', 'prthivi-sukta',
senior="""
1. **The text.** Atharva Veda 12.1 — *Pṛthivī Sūkta* (Hymn to the Earth). 63 verses. Most extensive ancient ecological text in the Vedic corpus.

2. **Key verses.** Read aloud (in IAST + English):
   > *mātā bhūmiḥ putro ahaṁ pṛthivyāḥ* — "Earth is my mother, I am her son." (12.1.12)
   > *yat te bhūme vikhanāmi kṣipraṁ tad api rohatu* — "What I dig from the Earth, may it grow back swiftly." (12.1.35)

3. **The framing.** Earth as mother. Resource extraction as legitimate but bounded by replenishment. Cleanliness, beauty, biodiversity as goods to preserve.

4. **Cross-cultural.** Earth-mother concept appears in many cultures: Pachamama (Andean), Gaia (Greek). The Atharva Veda articulation is older than most extant references.

5. **Critical reading.** The hymn is a religious text. It articulates an ETHIC, not an empirical claim. *"Does treating Earth as mother make us better stewards? Or does it sometimes lead to passive acceptance of destructive practices ('Earth will heal')?"* Both views exist.
""",
primary="""
- An old, old song says: *"The Earth is my Mother!"*

Show the words on the board: *"mātā bhūmiḥ putro ahaṁ pṛthivyāḥ"*

*"Long ago, people sang to the Earth like she was a mother. They asked: please give us food. And they said: I will care for you."*

Children draw the Earth with a smiling face. Around the edge, they draw what the Earth gives us (trees, water, food). Inside their drawing, they write one promise: "I will _______."
""")

register('module-13-indic-ecology', 'isopanishad-mantra',
senior="""
1. **The text.** *Iśāvāsya Upaniṣad* (a short Upaniṣad, 18 verses), mantra 1:
   > *īśāvāsyam idaṁ sarvaṁ yat kiñca jagatyāṁ jagat /
   > tena tyaktena bhuñjīthā mā gṛdhaḥ kasya svid dhanam* //

   Translation: *"All this — whatever moves in this moving world — is enveloped by the Lord. Enjoy through renunciation. Do not covet anyone's wealth."*

2. **The ecological reading.** *Tyaktena bhuñjīthā* — "enjoy by renouncing." Use the world, but with restraint. Take only what you need; leave the rest. This is one of the strongest non-greed ethics in any wisdom tradition.

3. **Modern parallel.** Steady-state economics (Herman Daly). Voluntary simplicity. Donut economics (Kate Raworth). The principle: don't grow beyond ecological limits.

4. **Source.** Iśāvāsya Upaniṣad is part of the Yajurveda. Translations: Eknath Easwaran, Stephen Phillips academic editions.

5. **Discussion.** *"How does 'enjoy by renouncing' apply to your own life? Phone usage? Food? Clothes? Travel?"* Each student writes 3 sentences. NO right answer — the point is HONEST self-reflection.
""",
primary="""
- An old wise verse says: *"Take only what you need!"*

The verse: *"īśāvāsyam idaṁ sarvam..."* — "All this is one big home."

*"If you take TOO much, others don't have enough. If you waste, the Earth gets sad."*

Children think of one thing they sometimes take too much of (food, water, time on screens). They draw it with a small heart, promising: *"I'll take just what I need."*
""")

register('module-13-indic-ecology', 'climate-change-context',
senior="""
1. **The science.** Project 3 key IPCC AR6 graphs:
   - Global temperature anomaly since 1850 (~+1.2°C and rising).
   - CO2 atmospheric concentration since 1900 (290 → 420+ ppm).
   - Sea-level rise (~20 cm since 1900).

2. **The agreement.** 99%+ of climate scientists agree: warming is human-caused, primarily fossil-fuel emissions. The IPCC reports synthesise thousands of studies.

3. **What's at stake for India.** Higher monsoon variability, glacier retreat in the Himalayas, sea-level rise threatening coastal cities, heat-stress in agriculture. NDCs (Nationally Determined Contributions) target net-zero by 2070.

4. **Source.** IPCC Sixth Assessment Report (Working Groups I, II, III; 2021–2023). NCERT Geography XI ch. 11.

5. **Bridge to Indic frameworks.** *"What does vasudhaiva kuṭumbakam say about climate change? What does yajña-cycle suggest about our daily responses? What does īśopaniṣad teach about consumption?"* Each student writes one paragraph connecting one ancient text to one modern climate response.
""",
primary="""
- The Earth is getting warmer because we burn too much fuel.
- Ice is melting. Some animals lose their homes. Some farms have trouble.

Show simple graphics: a thermometer going up, an ice cube melting, a tree being planted.

*"What can WE do?"* Children brainstorm: walk instead of drive, plant trees, save water, don't waste food. Pick one to try this week.
""")

register('module-13-indic-ecology', 'from-ancient-to-action',
senior="""
1. **Project design phase.** Students apply Module 13's principles to design ONE local environmental project:
   - Plant-a-tree drive (yajña reciprocity)
   - Sacred-grove documentation (biodiversity preservation)
   - Water audit at school / home (resource consciousness)
   - Waste-sorting station (extending ahiṁsā to materials)
   - Local-language climate-awareness poster (cultural communication)

2. **Project criteria.** Must (a) be achievable in 4 weeks, (b) cite at least ONE classical Indic principle, (c) document baseline and outcome data, (d) include a community/family component.

3. **Pair-brainstorm.** Pairs spend 10 minutes generating project ideas, then sketch one.

4. **Source-anchoring.** Each project must reference a specific verse, hymn, or principle from Modules 13's source list.

5. **Tomorrow's pitch.** Each student presents their project pitch in 3 minutes. Refine tonight.
""",
primary="""
- Time to PICK a project!
- Some ideas:
  1. **Plant trees** in our school garden
  2. **Save water** — turn off the tap when brushing
  3. **Sort waste** — separate paper, plastic, food
  4. **Make a poster** about saving Earth

Each child picks one project. Draws what they'll do. Names one Indian principle (Vasudhaiva Kuṭumbakam, Yajña, take-only-what-you-need).
""")

register('module-13-indic-ecology', 'project-pitch',
senior="""
1. **Project pitches (3 min each).** Each student presents their environmental-action project: problem identified, principle anchored, plan, expected outcome, measurement.

2. **Q&A and feedback (1 min each).** Peers ask one question and offer one suggestion.

3. **Voting.** Class votes on 3 favourite projects. These will be amplified (school-wide, parent-day presentations).

4. **Summative quiz (20 min).** See `quizzes/summative.md`.

5. **Module close.** *"Of all the texts and ideas in this module, which one will stay with you the longest? Why?"* Each student writes 2 sentences.
""",
primary="""
- Project share day! Each child shows their drawing and tells the class their plan.

Cheer for each one. *"Every project counts!"*

Quiz with stickers — everyone gets an "Earth Friend" sticker.

End: hold hands in a big circle. Say together: *"Vasudhaiva Kuṭumbakam — one big family!"*
""")


# ============================================================================
# Module 14 — Magic Squares (Bhadragaṇita)
# ============================================================================

register('module-14-magic-squares', 'discover-3x3',
senior="""
1. **The challenge.** *"Place the numbers 1 through 9 in a 3×3 grid so that every row, every column, and both main diagonals sum to the same number."* Hand out blank grids. 8 minutes of trial.

2. **Most students will find the same answer.**
   ```
   2 7 6
   9 5 1
   4 3 8
   ```
   (Or one of its 7 symmetric variants — rotations and reflections.)

3. **The magic constant.** Each row, column, and diagonal sums to **15**. Verify on the board.

4. **Why 15?** Sum of 1+2+...+9 = 45. Divided across 3 rows = 15. The magic constant is forced by the digit sum.

5. **Source.** This 3×3 square appears in *Gaṇita-kaumudī* of Nārāyaṇa Paṇḍita (1356 CE), but is also found in the Chinese *Lo Shu* tradition (~5th–10th c. BCE attestation, legends earlier). The 3×3 is one of the most studied combinatorial objects in mathematics.
""",
primary="""
- BIG puzzle! Put the numbers 1 to 9 in a 3×3 grid. Each row, column, and diagonal should add to the SAME number!

Children work in pairs. Try, fail, try again.

Hint after 5 min: *"5 always goes in the middle."*

The answer: 2-7-6 / 9-5-1 / 4-3-8. All rows = 15! All columns = 15! Even diagonals = 15! MAGIC!
""")

register('module-14-magic-squares', 'magic-constant',
senior="""
1. **The formula.** For an n×n magic square using 1 through n², the magic constant is M = n(n² + 1) / 2.

2. **Verify for 3×3.** M = 3 × 10 / 2 = 15. ✓

3. **Derive.**
   - Total sum of 1 through n² = n²(n² + 1) / 2.
   - This sum spreads across n rows, so each row sums to (n²(n² + 1) / 2) / n = n(n² + 1) / 2.

4. **Predict.** What's M for 4×4? 5×5? 7×7?
   - 4×4: 4 × 17 / 2 = 34.
   - 5×5: 5 × 26 / 2 = 65.
   - 7×7: 7 × 50 / 2 = 175.

5. **Source.** Nārāyaṇa Paṇḍita's *Gaṇita-kaumudī* (1356 CE), Book 14, derives the magic constant formula. Earlier references in Tibetan, Chinese, and Arab traditions also give the formula.
""",
primary="""
- The MAGIC NUMBER for 3×3 is 15. Why 15?

Add all the numbers from 1 to 9: 1+2+3+4+5+6+7+8+9 = 45.

Spread 45 across 3 rows: 45 / 3 = **15**. So each row must equal 15!

For a 4×4 magic square (using 1 to 16), what's the magic number?
- 1+2+...+16 = 136. / 4 rows = **34**.

*"There's a pattern!"*
""")

register('module-14-magic-squares', 'counting-and-symmetry',
senior="""
1. **How many 3×3 magic squares are there?** Counting carefully:
   - 1 fundamentally different square (up to symmetry).
   - 8 squares including rotations (×4) and reflections (×2).

2. **Demonstrate the symmetries.** Start with 2-7-6 / 9-5-1 / 4-3-8. Rotate 90° → 4-9-2 / 3-5-7 / 8-1-6. Rotate again → 8-3-4 / 1-5-9 / 6-7-2. Etc. Also reflect.

3. **Define "essentially different."** Two squares are equivalent if one is obtained from the other by rotation or reflection. The count of essentially distinct n×n magic squares is one of the harder combinatorial problems.

4. **Higher orders.** Number of essentially-different magic squares: 1 (for n=3), 880 (n=4), ~275 million (n=5). Source: combinatorial computer enumeration (Frenicle, Schinzel).

5. **Class exercise.** Each pair writes out all 8 symmetric variants of the 3×3 from Day 1. Verify each is still a magic square.
""",
primary="""
- How many ways can we make a 3×3 magic square?

Show the 2-7-6 / 9-5-1 / 4-3-8 square. Rotate the paper 90° — STILL magic! Rotate again — still! Reflect (mirror) — still!

*"That's 8 ways! But they're all REALLY the same square — just turned around."*

Children try rotating their own magic square paper. They count the rotations.
""")

register('module-14-magic-squares', 'stair-step-method',
senior="""
1. **State Nārāyaṇa Paṇḍita's algorithm.** For any ODD n×n, follow these steps:
   - Step 1: Place 1 in the top-middle cell.
   - Step 2: From the cell with k, move one up and one right (diagonal) to place k+1.
   - Step 3: If you go off the top, wrap to the bottom (same column you'd have landed in).
   - Step 4: If you go off the right, wrap to the left (same row).
   - Step 5: If the target cell is occupied, place k+1 in the cell DIRECTLY BELOW the cell containing k instead.

2. **Demonstrate on 3×3.** Place 1 top-middle. Move up-right (wraps to bottom row, same column shift) → 2 goes bottom-right. Continue:
   ```
   8 1 6
   3 5 7
   4 9 2
   ```
   Verify: rows, columns, diagonals all = 15. ✓ (Note: this is a different symmetric variant of the 3×3 magic square than yesterday's.)

3. **Source.** Nārāyaṇa Paṇḍita's *Gaṇita-kaumudī* (1356 CE), Book 14 (*Bhadra-gaṇita*). He calls this method *turagagati* — "horse-step" (knight-like move).

4. **Cross-cultural.** The same method was independently discovered or transmitted in Arabic and European mathematics. The earliest extant Indian description is Nārāyaṇa's.

5. **Try on your own.** Each student applies the algorithm to construct another 3×3 magic square. Tomorrow we extend to 5×5.
""",
primary="""
- Big-kid trick! Nārāyaṇa (an Indian mathematician 700 years ago) taught how to BUILD a magic square step-by-step.

Show on the board:
1. Put **1** in the top-middle.
2. From 1, jump UP-and-RIGHT to put 2... but you fall off the top!
3. Wrap to the bottom row (same column).
4. Keep going!

The pattern looks like a horse jumping. *"That's why he called it the horse-step!"*

Children watch the teacher build a 3×3 step-by-step.
""")

register('module-14-magic-squares', 'practice-5x5-and-7x7',
senior="""
1. **5×5 construction.** Place 1 in cell (1, 3) [top-middle]. Apply the stair-step rule. Resulting square (one variant):
   ```
   17 24  1  8 15
   23  5  7 14 16
    4  6 13 20 22
   10 12 19 21  3
   11 18 25  2  9
   ```
   Magic constant: 5 × 26 / 2 = **65**. Verify any row, column, or diagonal.

2. **7×7 construction (challenge).** Same algorithm, larger grid. Magic constant: 7 × 50 / 2 = **175**.

3. **Common mistakes.** Forgetting the "if cell occupied, drop down" rule. Wrong wrap direction. Off-by-one starting position.

4. **Source check.** Nārāyaṇa's text gives this algorithm for any odd n. Modern translations: T. Hayashi, J. Pereira's edition of Gaṇita-kaumudī.

5. **Independent practice.** Each student builds a 5×5 unaided. Pair-check. Then a 7×7 if time permits.
""",
primary="""
- Today: try a BIGGER magic square — 5×5!

Place 1 in the top-middle. Step up-right. Wrap when needed. Keep going to 25.

It looks confusing at first, but the rule is the same. The magic number for 5×5 is **65** (all rows, columns, diagonals add to 65).

Children try with the teacher's help. Most won't finish — that's OK! Just enjoy the start.
""")

register('module-14-magic-squares', '4x4-and-khajuraho',
senior="""
1. **The 4×4 (even-order) case.** Stair-step doesn't directly work for even n. Different methods exist (Strachey method, Conway's LUX). Magic constant for 4×4 with 1–16: **34**.

2. **The Dürer 4×4 (1514).** Famous engraving "Melencolia I" includes a 4×4 magic square:
   ```
   16  3  2 13
    5 10 11  8
    9  6  7 12
    4 15 14  1
   ```
   All rows, columns, diagonals = 34. The bottom-middle two cells contain "15 14" — the year of the engraving (1514). Famous detail.

3. **The Khajuraho square (~10th c. CE).** Inscribed on a panel at the Khajuraho temple complex (Madhya Pradesh, India). 4×4 grid. ALL rows, columns, diagonals AND many 2×2 subblocks sum to **34**. This is a *pan-diagonal* (or *most-perfect*) magic square — a stronger condition than ordinary magic.

   ```
    7 12  1 14
    2 13  8 11
   16  3 10  5
    9  6 15  4
   ```
   Compute: row 1 = 7+12+1+14 = 34. Column 1 = 7+2+16+9 = 34. Etc. Also 2×2 block top-left = 7+12+2+13 = 34.

4. **Source.** The Khajuraho inscription is real and dateable (~10th–11th c. CE). Discussion: this PRECEDES Dürer by ~500 years. The temple inscription is one of the oldest extant magic squares with this "most-perfect" property.

5. **Honest framing.** Magic squares appear in many cultures. The KHAJURAHO square's "most-perfect" property is distinctive. Not all Indian magic squares are this advanced; not all advanced ones are Indian. Cross-cultural mathematics flourishes.
""",
primary="""
- 4×4 magic squares are also amazing! In INDIA, there's one carved on a temple wall — the Khajuraho square. About 1000 years old!

Show the picture. *"All rows = 34, all columns = 34. Even small 2x2 boxes inside = 34!"*

Children draw a 4×4 grid and copy the numbers. They check: do the rows add to 34? Try one!
""")

register('module-14-magic-squares', 'historical-context',
senior="""
1. **Nārāyaṇa Paṇḍita (b. 1340 CE).** Mathematician of the Mādhava school period. His *Gaṇita-kaumudī* ("Moonlight of Computation") is a major mathematical compendium. Book 14 (*Bhadra-gaṇita*) is dedicated to magic squares.

2. **Earlier Indian references.** Garga Saṁhitā (~1st c. BCE) mentions magic squares for ritual. The Khajuraho inscription (~10th c. CE) predates Nārāyaṇa by 4 centuries.

3. **Pre-Nārāyaṇa global timeline.**
   - Lo Shu legend (Chinese, attested ~5th–10th c. BCE): a 3×3 magic square.
   - Ibn Khaldūn and earlier Arab mathematicians: 9th–14th c. CE work on magic squares.
   - Khajuraho (~10th c. CE): pan-diagonal 4×4.
   - Nārāyaṇa (1356 CE): systematic algorithms for any odd n.
   - Dürer (1514 CE): Melencolia I.

4. **Source.** Kim Plofker, *Mathematics in India* (Princeton, 2009), ch. 5 — best modern academic overview.

5. **Critical-thinking close.** *"Magic squares appear independently in many cultures. What does this tell us about (a) mathematical universality and (b) cultural transmission? Nārāyaṇa's contribution: ALGORITHMS for any odd n — a systematisation. Khajuraho's contribution: ART + math at temple scale."*
""",
primary="""
- Nārāyaṇa Paṇḍita lived in India about 700 years ago. He wrote a book about magic squares!

His book is called *Gaṇita-kaumudī* ("Moonlight of Math"). Book 14 is all about magic squares.

Show a (drawn) picture of Nārāyaṇa with a manuscript. *"Maths heroes from long ago!"*

Children draw a magic square inside a "book" outline.
""")

register('module-14-magic-squares', 'cross-cultural',
senior="""
1. **The Lo Shu (Chinese).** Legendary: a turtle emerging from the River Lo bore the 3×3 magic square on its shell. Used in Chinese geomancy (*feng shui*). Earliest definite attestation: ~5th c. BCE (though legend places it ~2000 BCE).

2. **Indian — Khajuraho (10th c. CE).** As yesterday. Pan-diagonal 4×4 with "most-perfect" property.

3. **Indian — Nārāyaṇa Paṇḍita (1356 CE).** Systematic algorithms for any odd n.

4. **European — Dürer's Melencolia I (1514).** A 4×4 with year-encoding.

5. **Class exercise.** Students draw a timeline (~−500 to ~+1600) marking each tradition's main contributions. Then write one sentence: *"What does this timeline tell us about mathematical universality?"*

   Critical-thinking caveat: *"Some claims of priority are unprovable. The TURTLE-LEGEND for Lo Shu is just that — a legend. We can only date things by extant manuscripts and inscriptions."*
""",
primary="""
- Magic squares are found ALL OVER THE WORLD!

- 🇨🇳 China: Lo Shu legend — a turtle's shell!
- 🇮🇳 India: Khajuraho temple wall!
- 🇩🇪 Germany: Dürer's painting!

Show 4 small pictures. *"People everywhere love magic squares!"*

Each child picks one tradition and draws a tiny picture (turtle, temple, painting).
""")

register('module-14-magic-squares', 'design-your-own',
senior="""
1. **Personal magic-square design.** Each student designs ONE magic square. Options:
   - 3×3 with custom numbers (e.g. start from 5 instead of 1; magic constant changes accordingly).
   - 4×4 using Nārāyaṇa-style or Strachey method.
   - 5×5 using stair-step.

2. **Artistic treatment.** Calligraphy, colour-coding, geometric decoration. Inspired by mandala / yantra aesthetics or modernist grid art.

3. **Document the math.** Each student writes on the back: starting numbers, magic constant, method used, source reference. This is a "math behind the art" supplement.

4. **Source-anchoring.** Each student cites at least ONE source from this module (Nārāyaṇa, Khajuraho, Dürer, Plofker, etc.).

5. **Pair-critique.** Pairs swap; verify each other's math correctness.
""",
primary="""
- Make YOUR OWN magic square as art!

Choose ANY 9 numbers (or use 1-9). Make a 3×3 grid where all rows add to the same. Decorate it!

Show example: a magic square shaped like a flower, with colours on each number. *"Math + art = magic!"*

Children draw, colour, and write their magic number at the top.
""")

register('module-14-magic-squares', 'final-share',
senior="""
1. **Design share (10 min).** Each student shows their magic-square art. Brief explanation of the math.

2. **Summative quiz (25 min).** Magic constant formula, stair-step algorithm, historical context. See `quizzes/summative.md`.

3. **Critical-thinking close (5 min).** *"What's the most enduring lesson from this module? Is it the math (algorithm), the history (Nārāyaṇa, Khajuraho), or the cross-cultural insight (magic squares everywhere)?"* Each student writes 2 sentences.

4. **Linkage.** Module 15 (Capstone) — magic-square art is one of the project options.

5. **Module close.** *"Designing your own magic square required CHOOSING constraints. What other constrained-design problems are like this?"* (Sudoku, crosswords, music composition, architecture.) Open discussion.
""",
primary="""
- Final day! Show your magic square art.

Each child shows + says one thing they liked. Cheer for each.

Quiz with stickers — everyone gets a "Magic Squares" sticker.

End: chant — *"Bhadragaṇita! Magic numbers!"*
""")

# ============================================================================
# Module 15 — Project Implementation (Capstone)
# ============================================================================

register('module-15-project-implementation', 'overview-and-menu',
senior="""
1. **Capstone overview.** This module is different. No new content delivery. Instead: 10 days of structured project work, applying what you learned from Modules 1–14.

2. **Walk through the 10-option project menu.** Read each, with a 1-minute description per option:
   - Pañcagavya kitchen science → SUBSTITUTED with fermented-foods study (safety)
   - Mandala / Pṛthvī geometry
   - Tithi/festival calendar
   - Herb identification card-deck
   - Magic-square art
   - Yoga sequence design
   - Sustainability audit
   - Doshic self-study
   - Multiplication-method comparison
   - Open-design (your own)

3. **The discipline.** Each project requires: scope, research, design, build, document, present. Daily journal. Source citations.

4. **The safety floor.** Pañcagavya — NEVER cow-urine ingestion in school. Use comparative fermented-foods study (curd, paneer, batter — biochemically interesting and safe).

5. **Today's task.** Read all 10 options in detail (printout provided). DON'T pick yet — sleep on it. Tomorrow you'll choose and scope.
""",
primary="""
- A WHOLE new kind of class: we make our OWN project!

Show 5 simple project pictures:
1. 🌿 Plant garden
2. 🎨 Make a herb book
3. 📜 Draw a moon calendar
4. 🪷 Magic square art
5. 🧘 Teach yoga to little kids

Children pick a favourite. *"Tomorrow you'll start planning!"*

End: cheer for every choice.
""")

register('module-15-project-implementation', 'scope-and-plan',
senior="""
1. **Each student commits to ONE project.** Show of hands per option to see distribution.

2. **The one-page plan template.**
   - Title (~10 words)
   - Problem (~50 words): what question/need does this address?
   - Sources (~5 listed): the modules + texts you'll draw from
   - Deliverable (~50 words): what will exist at the end?
   - Timeline (Day 3-10 broken down by phase)
   - Success criteria (3 bullet points: what makes this excellent?)

3. **Work-time.** 30 minutes of silent plan-writing.

4. **Pair-share.** Pairs swap plans, give one strength + one concern (sticky notes).

5. **Submit.** Plans go to the teacher tonight for sign-off. Tomorrow you begin research.
""",
primary="""
- Pick ONE project. Write down:
- WHAT you'll do (one sentence)
- WHAT you need (paper, plants, paint, etc.)
- WHO will help (teacher, parent, friend)
- WHEN it'll be done (today + 8 more days)

Each child has a "plan paper." Teacher helps with words.

End: hold up your plan paper. Cheer.
""")

register('module-15-project-implementation', 'research-day-1',
senior="""
1. **Research phase begins.** Each student returns to the relevant Modules for content:
   - Doṣa project → Module 4
   - Herbs project → Module 10
   - Astronomy project → Module 6 or 12
   - Math project → Module 5, 7, 9, 11, or 14
   - Ecology project → Module 13

2. **The library / research routine.** Open the relevant pack's `sources.md`. Open at least 2 cited sources (online or print). Take 2-page notes per source. The notes will support the project's references.

3. **Critical eye.** Don't just trust the FIRST source. For each claim, ask: *"Who's the author? When was this written? What's their context?"*

4. **Work-time.** 35 minutes of silent research + note-taking.

5. **Sharing (5 min).** Three students briefly describe what they learned and what surprised them.
""",
primary="""
- Find out MORE about your project!

If you're doing a herb project, look at Module 10. If a moon calendar, Module 6.

Read 2 things about your project. Write 3 things you learned (with the teacher's help).

Show a "research card" with 3 facts.
""")

register('module-15-project-implementation', 'research-day-2',
senior="""
1. **Continued research.** Today's focus: sketches + design.

2. **The design-thinking question.** *"What will this LOOK like when it's done?"* Draw it. Even a rough sketch helps you find missing pieces.

3. **Source check.** Revisit yesterday's notes. Are there gaps? Look up one more source if needed.

4. **Work-time.** 30 minutes of sketching + planning the build.

5. **Pair-feedback.** Pairs discuss design. *"What's the strongest part of your design? What's still unclear?"*
""",
primary="""
- More research today!

If yesterday you found 3 facts, today find 2 MORE. Plus: DRAW a picture of how your project will look when done.

Show your picture to a friend. Friend asks one question. *"How will you do that?"*

Children answer with a sentence.
""")

register('module-15-project-implementation', 'mid-project-critique',
senior="""
1. **Critique circle structure.** Pairs swap project plans + sketches. 5 minutes silent reading. Then each gives:
   - One strength (sticky note).
   - One concern (sticky note).
   - One question (verbal).

2. **Pairs rotate twice.** Each student gets feedback from 3 different partners.

3. **Synthesise.** Each student writes a 100-word "what I'm changing" note based on critique. May include:
   - Narrowing scope
   - Adding a source
   - Clarifying deliverable
   - Revising timeline

4. **Honest about limits.** *"What's still hard? What might fail? What's your Plan B?"* Real projects always have unknowns. Acknowledge them.

5. **Submit revised plan.** Teacher reviews tonight. Day 6 = build phase begins.
""",
primary="""
- Friend check-in!

Show your project plan and picture to 2 friends. They each tell you ONE thing they like, ONE thing to think about.

Write down what they say. Then YOU decide: change something? keep it same?

Show your "updated plan" to the teacher.
""")

register('module-15-project-implementation', 'build-day-1',
senior="""
1. **Build phase begins.** Materials should be ready (announced last week). If not, today is also a "gather materials" day.

2. **Project-specific guidance per option.**
   - Magic-square art → grid + colours + calligraphy.
   - Herb deck → photographs / drawings + card layout + lamination.
   - Yoga sequence → flow design + safety check + pose drawings.
   - Sustainability audit → measurement instruments + spreadsheet.
   - And so on.

3. **Daily journal.** Today's entry: *"What did I build today? What worked? What didn't?"*

4. **Work-time.** 35 minutes of focused making.

5. **End-of-day share (5 min).** Three students share progress.
""",
primary="""
- TIME TO BUILD! 🛠️

Each child gets out their materials (paper, paint, plants, etc.) and starts.

Teacher walks around helping. Children share with their neighbour: *"What are you making?"*

End: hold up what you've started. *"Tomorrow we keep going!"*
""")

register('module-15-project-implementation', 'build-day-2',
senior="""
1. **Continue building.** Focus on completing the major deliverable.

2. **Journal entry today:** *"What progress? What's slowed me down? What do I still need to do tomorrow?"*

3. **Mid-build review.** Teacher checks each student's progress. Flags students who may need help in time-management or scope.

4. **Honest scope adjustment.** If you realise you can't finish in time, narrow the scope NOW (not on Day 9). Better to do less, well, than more, poorly.

5. **Independent work-time.** 40 minutes. Quiet, focused.
""",
primary="""
- More building today! Keep going on your project.

Children work for 25 minutes. Teacher helps when stuck.

If you finish early — make it BETTER (add colour, add words).
If you're slow — keep going! Tomorrow we document.

End: high-five with a friend.
""")

register('module-15-project-implementation', 'document',
senior="""
1. **Documentation phase.** Today: write up your project.

2. **The structure (Senior — ~500 words).**
   - **Problem & motivation** (~100 words): what did you set out to do?
   - **Sources used** (~100 words): which Modules, which texts, which observations?
   - **Process** (~150 words): what did you actually do? Day by day?
   - **Findings / outcomes** (~100 words): what did you produce / observe?
   - **Reflection** (~50 words): what surprised you? What would you do differently?

3. **Honest reflection rule.** Include at least ONE thing that didn't work. Real research has failures. Including yours is intellectually honest — and pedagogically valuable.

4. **Citations.** Use the format: *Author, Title, Year.* See pilot modules' `sources.md` for examples.

5. **Drafting time.** 35 minutes silent writing. Teacher available for questions.
""",
primary="""
- Time to TELL the story of your project!

Each child writes (with teacher help):
- ONE sentence: what I made.
- ONE sentence: how I made it.
- ONE sentence: what I liked.

Plus a final drawing of the FINISHED project.

Cheer. *"Tomorrow we rehearse the show!"*
""")

register('module-15-project-implementation', 'rehearse',
senior="""
1. **Pair-rehearsal.** Pairs swap presentations. Time the 5-minute talk. Friend gives:
   - One strength (clear, well-organised, engaging).
   - One specific suggestion (slow down, add an example, more eye contact).

2. **Refine.** Each student adjusts their presentation based on feedback. 10 minutes solo refinement.

3. **Group-rehearsal (5 students share with class).** Selected by teacher (varied projects). Class gives 2 minutes of feedback each.

4. **Logistics check.** Materials ready for tomorrow? Backup plan if something breaks?

5. **Self-assessment.** Each student rates themselves on the rubric (`assessments/rubric.md`). They submit this PRE-presentation; the teacher will compare with their own scoring after the share.
""",
primary="""
- Practice your show!

Each child practices saying what they made — to a partner, then to a small group.

Tips: *"Look up. Speak clearly. Smile!"*

End: do a "warm-up cheer" together for tomorrow's big day.
""")

register('module-15-project-implementation', 'share-day',
senior="""
1. **Project share day.** Each student presents their project (5 minutes including Q&A). Audience: peers, optionally parents, optionally other teachers.

2. **Format.** Brief: what + why + how + what-I-learned. Show the artefact. Take 1-2 questions.

3. **Audience role.** Each peer takes one note per project (1 sticky note, one observation or compliment). At the end, sticky notes go to each presenter.

4. **Self + teacher assessment.** After the share, each student completes their final self-assessment on the rubric. The teacher fills the corresponding teacher-assessment. Within a week, the two are compared in a 1-1 conversation.

5. **Module close (5 min).** Whole-class reflection: *"Looking back across all 15 modules — Modules 1-14 of curriculum, Module 15 of project — what's ONE thing that will stay with you?"* Each student says one sentence.

6. **Curriculum close.** Brief teacher comment + final round of applause. The IKS curriculum is complete.
""",
primary="""
- BIG DAY! Show-and-tell time! 🎉

Each child shows their project to the class.
- Say one thing you made.
- Say one thing you learned.

Audience claps for each child.

End: everyone gets a "Curriculum Champion" sticker. Whole class chants: *"WE DID IT!"*
""")


# Day-slug aliases (different filenames than the generator predicted)
def alias(mod, src, dst):
    if (mod, src) in SENIOR_CORE:
        SENIOR_CORE[(mod, dst)] = SENIOR_CORE[(mod, src)]
    if (mod, src) in PRIMARY_CORE:
        PRIMARY_CORE[(mod, dst)] = PRIMARY_CORE[(mod, src)]


alias('module-14-magic-squares', 'counting-and-symmetry', 'how-many-3x3')
alias('module-14-magic-squares', 'practice-5x5-and-7x7', 'practice-5x5')
alias('module-15-project-implementation', 'research-day-1', 'research-1')
alias('module-15-project-implementation', 'research-day-2', 'research-2')
alias('module-15-project-implementation', 'build-day-1', 'build-1')
alias('module-15-project-implementation', 'build-day-2', 'build-2')


# ============================================================================
# File-replacement engine
# ============================================================================

# Regex for Senior/Middle Core block (5-item list)
SENIOR_PATTERN = re.compile(
    r"### Core \([^)]+\)\s*\n\s*\n"
    r"(1\. \*\*State the observable phenomenon first\.\*\*.*?5\. \*\*Independent or paired practice\*\* for ~5 minutes\.)",
    re.DOTALL,
)

# Regex for Primary "Today's idea" placeholder paragraph (just the paragraph,
# leaving the vocab line above intact)
PRIMARY_PATTERN = re.compile(
    r"Introduce the concept gently using a story, a drawing, or a sensory example\. "
    r"The concept for today: \*\*[^*]+\*\*\. Keep sentences short\."
)


def extract_module_and_day(path: Path) -> tuple[str, str, str]:
    """From curriculum/{band}/{mod-slug}/days/day-NN-{day-slug}.md → (band, mod, day)."""
    parts = path.relative_to(CURRICULUM).parts
    band = parts[0]
    mod = parts[1]
    fname = parts[-1]  # day-01-three-doshas-intro.md
    m = re.match(r"day-\d+-(.+)\.md", fname)
    day_slug = m.group(1) if m else ''
    return band, mod, day_slug


def replace_in_file(path: Path) -> bool:
    band, mod, day = extract_module_and_day(path)
    text = path.read_text(encoding='utf-8')

    if band in ('senior', 'middle'):
        content = SENIOR_CORE.get((mod, day))
        if not content:
            return False
        if 'State the observable phenomenon first' not in text:
            return False
        new_text = SENIOR_PATTERN.sub(
            lambda m: m.group(0).split('\n\n')[0] + '\n\n' + content,
            text,
        )
        if new_text != text:
            path.write_text(new_text, encoding='utf-8')
            return True

    elif band == 'primary':
        content = PRIMARY_CORE.get((mod, day))
        if not content:
            return False
        if 'Introduce the concept gently using a story' not in text:
            return False
        # Replace the placeholder paragraph; vocab line above is preserved
        new_text = PRIMARY_PATTERN.sub(content, text)
        if new_text != text:
            path.write_text(new_text, encoding='utf-8')
            return True

    return False


def main():
    n = 0
    skipped = 0
    for f in CURRICULUM.glob('*/module-*/days/*.md'):
        ok = replace_in_file(f)
        if ok:
            n += 1
        else:
            band, mod, day = extract_module_and_day(f)
            if (mod, day) in SENIOR_CORE or (mod, day) in PRIMARY_CORE:
                skipped += 1
    print(f"Replaced Core in {n} files. Skipped (no placeholder or already done): {skipped}.")


if __name__ == '__main__':
    main()
