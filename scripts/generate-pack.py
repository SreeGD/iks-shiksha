#!/usr/bin/env python3
"""Generate minimum-viable pack files for IKS modules across all bands.

The 10 new modules each need ~15 essential files per band so the site can
render them and teachers/parents/students get usable content. This script
produces those files deterministically from per-module data and per-band
templates, then writes them under curriculum/{band}/{slug}/.

It only writes files that don't already exist (so agent-produced content
is preserved).
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
CURRICULUM = ROOT / 'curriculum'

BAND_INFO = {
    'primary': {
        'label': 'Primary',
        'grades': 'Grades 3–5',
        'duration': '30 min',
        'voice': 'story-led, sensory, drawing-heavy',
        'sentence': '8–12 words on average',
        'citations_to_students': False,
    },
    'middle': {
        'label': 'Middle',
        'grades': 'Grades 6–8',
        'duration': '45 min',
        'voice': 'inquiry-driven, balanced text + activity',
        'sentence': '15–20 words on average',
        'citations_to_students': True,
    },
    'senior': {
        'label': 'Senior',
        'grades': 'Grades 9–12',
        'duration': '45 min',
        'voice': 'analytical, comparative, primary-source aware',
        'sentence': '20–30 words on average',
        'citations_to_students': True,
    },
}

# ---------------------------------------------------------------------------
# Per-module data
# ---------------------------------------------------------------------------

MODULES = {
    'module-04-doshas': {
        'title': 'Doshas — Vāta, Pitta, Kapha',
        'sanskrit': 'Tri-doṣa',
        'subtitle': 'Three biological-rhythm types in Āyurvedic thought',
        'description': (
            "Three patterns of internal rhythm — *vāta* (motion), *pitta* "
            "(transformation), and *kapha* (structure) — that Āyurveda uses "
            "to describe individual constitutional differences. Mapped to "
            "*pañcabhūta* from Module 2 and framed as wellness lens, NOT "
            "medical diagnosis."
        ),
        'nep': [
            '§4.6 — Integration of Indian Knowledge Systems',
            '§4.23 — Experiential learning (self-observation projects)',
            '§11.8 — Holistic, multidisciplinary education',
        ],
        'key_terms': [
            ('doṣa', 'doṣa', 'humour / functional principle'),
            ('vāta', 'vāta', 'motion principle (wind, ākāśa+vāyu)'),
            ('pitta', 'pitta', 'transformation principle (fire, tejas+ap)'),
            ('kapha', 'kapha', 'structure principle (cohesion, ap+pṛthvī)'),
            ('prakṛti', 'prakṛti', 'innate constitution'),
            ('vikṛti', 'vikṛti', 'current imbalance'),
        ],
        'sources': [
            'Caraka Saṁhitā, *Sūtrasthāna* 1.57–58 (definition of three doṣas)',
            'Aṣṭāṅga Hṛdaya, *Sūtrasthāna* 1.7 (doṣa-dhātu-mala framework)',
            'Robert Svoboda, *Prakriti: Your Ayurvedic Constitution* (1998) — modern intro',
            'NCERT Biology Class XII, Chapter on human physiology (compare physiological rhythms)',
        ],
        'days': [
            ('three-doshas-intro', 'Three Doshas Introduction', 'Name vāta, pitta, kapha and recognise one observable trait of each.'),
            ('vata-motion', 'Vāta — The Motion Principle', 'Identify vāta-style behaviours (quick, dry, cold, moving) in self and surroundings.'),
            ('pitta-transformation', 'Pitta — The Transformation Principle', 'Identify pitta-style behaviours (warm, sharp, focused, transforming).'),
            ('kapha-structure', 'Kapha — The Structure Principle', 'Identify kapha-style behaviours (steady, cool, moist, structured).'),
            ('mapping-to-elements', 'Mapping to the Five Elements', 'Connect each doṣa to its two constituent elements (vāta=ākāśa+vāyu, pitta=tejas+ap, kapha=ap+pṛthvī).'),
            ('prakriti-self-assessment', 'Prakṛti Self-Assessment', 'Use a worksheet to estimate own dominant doṣa(s) — emphasising NOT diagnosis.'),
            ('daily-rhythms', 'Doṣa Rhythms in a Day', 'Map the kapha-pitta-vāta cycle across morning/noon/evening hours.'),
            ('seasonal-rhythms', 'Doṣa Rhythms Across Seasons', 'Map doṣa cycles to monsoon/summer/winter.'),
            ('balance-and-imbalance', 'Balance and Imbalance', 'Distinguish prakṛti (innate) from vikṛti (current state); recognise simple imbalance signs.'),
            ('synthesis-and-project-pitch', 'Synthesis and Project Pitch', 'Pitch the 7-day self-observation project and answer assessment quiz.'),
        ],
        'activity': {
            'slug': 'dosha-rhythm-clock',
            'title': 'Build a Doṣa Rhythm Clock',
            'duration': 30,
            'materials': 'circular paper plate, coloured markers, ruler',
            'description': (
                'Students mark a 24-hour clock face into three doṣa segments — '
                'kapha (6–10 am and 6–10 pm), pitta (10 am–2 pm and 10 pm–2 am), '
                'vāta (2–6 am and 2–6 pm). They note one personal activity that '
                'fits each segment and share with a partner.'
            ),
        },
        'project': {
            'slug': '7-day-dosha-observation',
            'title': 'Seven-Day Doṣa Self-Observation',
            'description': (
                'Chart your daily routine — sleep, food, energy, mood — for 7 days '
                'through the doṣa lens. Write a one-page reflection. THIS IS NOT '
                'DIAGNOSIS. Refer any health concern to a doctor.'
            ),
        },
        'parent_note': (
            "Doṣas in Āyurveda describe individual differences — like introvert/"
            "extrovert or morning-person/night-owl, NOT diseases. Your child's "
            "self-observation is a wellness lens, not a diagnosis. If you have "
            "any health concern, please consult a doctor."
        ),
    },

    'module-06-moon-phases-tithi': {
        'title': 'Moon Phases and Tithi',
        'sanskrit': 'Candra-pakṣa, Tithi',
        'subtitle': 'The Moon\'s monthly cycle and the Indian lunar calendar',
        'description': (
            "The Moon's apparent change of shape across ~29.5 days is the "
            "synodic month. Indian astronomy divides this into 30 *tithi*s "
            "(lunar days), grouped into a waxing fortnight (*śukla pakṣa*) "
            "and waning fortnight (*kṛṣṇa pakṣa*). This module connects "
            "observation, lunar geometry, calendar construction, and the "
            "panchanga framework."
        ),
        'nep': [
            '§4.6 — Integration of Indian Knowledge Systems',
            '§4.23 — Experiential learning (moon-watching)',
            '§11.8 — Holistic, multidisciplinary (astronomy + calendar + culture)',
        ],
        'key_terms': [
            ('candra', 'candra', 'Moon'),
            ('pakṣa', 'pakṣa', 'fortnight (half-month)'),
            ('śukla pakṣa', 'śukla pakṣa', 'waxing fortnight (new → full)'),
            ('kṛṣṇa pakṣa', 'kṛṣṇa pakṣa', 'waning fortnight (full → new)'),
            ('tithi', 'tithi', 'lunar day (1/30 of synodic month)'),
            ('amāvasyā', 'amāvasyā', 'new moon'),
            ('pūrṇimā', 'pūrṇimā', 'full moon'),
            ('pañcāṅga', 'pañcāṅga', 'five-limbed Indian calendar (tithi, vāra, nakṣatra, yoga, karaṇa)'),
        ],
        'sources': [
            'Sūrya-siddhānta (c. 5th–10th c. CE), chapter 2 on lunar motion',
            'Varāhamihira, *Pañcasiddhāntikā* (6th c. CE)',
            'NCERT Physics Class XI, ch. 8 (Gravitation)',
            'NCERT Geography Class VI, ch. 1 (The Earth in the Solar System)',
            'NASA Lunar Phase educational pages',
        ],
        'days': [
            ('moon-and-its-shapes', 'The Moon and Its Shapes', 'Observe and name the four basic phases (new, first quarter, full, last quarter).'),
            ('two-fortnights', 'Two Fortnights — Pakṣa', 'Distinguish śukla pakṣa from kṛṣṇa pakṣa and name today\'s.'),
            ('fifteen-tithis', 'Fifteen Tithis per Pakṣa', 'Recite the 15 tithi names (pratipadā, dvitīyā, ...) and explain why a tithi isn\'t exactly a day.'),
            ('building-a-tithi-calendar', 'Building a Tithi Calendar', 'Construct a tithi calendar for the current month using observation and computation.'),
            ('lunar-months-and-festivals', 'Lunar Months and Festivals', 'Map the 12 lunar months (caitra, vaiśākha, ...) to major festivals.'),
            ('panchanga-overview', 'Panchanga — Five Limbs', 'Identify the five components: tithi, vāra, nakṣatra, yoga, karaṇa.'),
            ('eclipses', 'Why Eclipses Happen', 'Explain solar/lunar eclipses using orbital plane geometry (5° tilt of Moon\'s orbit).'),
            ('modern-lunar-science', 'Modern Lunar Science', 'Phases as Sun\'s illumination of Moon; mention libration, tides.'),
            ('cross-cultural-calendars', 'Cross-cultural Calendars', 'Compare with Hijri (Islamic), Chinese, and Hebrew lunar calendars.'),
            ('synthesis-quiz', 'Synthesis and Quiz', 'Final quiz and 10-day moon-diary share.'),
        ],
        'activity': {
            'slug': 'moon-diary',
            'title': '10-Day Moon Observation Diary',
            'duration': 30,
            'materials': 'notebook, pencils, ~15 minutes per evening',
            'description': (
                'Each evening for 10 days, students sketch the moon shape they '
                'see, note the time, the tithi name, and one feeling/observation. '
                'On Day 10 they compare sketches with the actual calendar.'
            ),
        },
        'project': {
            'slug': 'class-tithi-calendar',
            'title': 'Class Tithi Calendar for the Current Month',
            'description': (
                'Each student picks 3 dates in the current calendar month. They '
                'compute (or look up) the tithi, identify the pakṣa, and produce '
                'a visual class calendar with all entries combined.'
            ),
        },
        'parent_note': (
            "This month, your child is keeping a 10-day moon diary. Please "
            "give them ~15 minutes each evening to observe the moon (a balcony "
            "or window is fine). Discussing what they see is part of the learning."
        ),
    },

    'module-07-eleven-multiplication': {
        'title': '×11 Multiplication — Ekādhikena Pūrveṇa',
        'sanskrit': 'Ekādhikena Pūrveṇa',
        'subtitle': 'Mental multiplication by 11 from Tirthaji\'s Vedic Mathematics',
        'description': (
            "A mental-arithmetic method for multiplying any number by 11 "
            "instantly: split the digits, add adjacent pairs, place sums "
            "in between. Tirthaji's *Vedic Mathematics* (1965) labelled "
            "this an application of the *Ekādhikena Pūrveṇa* sūtra. Honest "
            "history is taught alongside: this is a 20th-century mental-"
            "arithmetic system, not strictly ancient mathematics."
        ),
        'nep': [
            '§4.6 — Integration of Indian Knowledge Systems',
            '§4.23 — Experiential learning (mental-math practice)',
            '§4.27 — Local context and language',
        ],
        'key_terms': [
            ('Ekādhikena Pūrveṇa', 'Ekādhikena Pūrveṇa', '"by one more than the previous" — sūtra 1 in Tirthaji'),
            ('sūtra', 'sūtra', 'aphorism / formula'),
            ('Anurūpyena', 'Anurūpyena', '"proportionately" — sūtra used for ×12, ×13 extensions'),
        ],
        'sources': [
            'Bharati Krishna Tirthaji, *Vedic Mathematics* (1965, posthumous; manuscript 1911–1918)',
            'S. G. Dani, "Myths and reality: On Vedic mathematics," *Frontline* (1993) — critical historical perspective',
            'Kenneth R. Williams, *Vedic Mathematics — Teacher\'s Manual* (2002)',
            'NCERT Mathematics Class VI, ch. 2 (Whole numbers)',
        ],
        'days': [
            ('the-hook', 'The Hook — What Is the Trick?', 'Compute 23×11, 35×11 mentally using the split-and-sum method.'),
            ('the-carry-case', 'The Carry Case', 'Compute 87×11, 65×11 correctly using the carry rule.'),
            ('why-it-works', 'Why It Works — The Algebra', 'Derive (10a+b)×11 = 100a + 10(a+b) + b and explain.'),
            ('three-digit', '3-Digit × 11', 'Compute 234×11 = 2_5_7_4 using the extended split method.'),
            ('speed-day', 'Speed Day', 'Complete a 50-problem mental-math sprint in 5 minutes.'),
            ('anurupyena-extension', 'Anurūpyena — ×12 to ×19', 'Extend the method to ×12 and ×13 using one-more-digit adjustments.'),
            ('limits-of-the-method', 'Limits of the Method', 'Recognise when traditional long multiplication is faster than the sūtra method.'),
            ('tirthaji-context', 'Tirthaji and Historical Context', 'Explain who Tirthaji was and why scholars debate the "Vedic" attribution.'),
            ('mixed-practice', 'Mixed Practice', 'Solve a mixed problem set using best-fit method per problem.'),
            ('final-assessment', 'Final Assessment', 'Take the summative quiz and reflect on which method works best.'),
        ],
        'activity': {
            'slug': 'mental-math-sprint',
            'title': 'Mental Math Sprint Cards',
            'duration': 20,
            'materials': 'flashcards (20–50 pre-printed ×11 problems), stopwatch',
            'description': (
                'In pairs: one student holds up a card, the other answers within '
                '3 seconds using the ×11 method. Swap. Track personal best time.'
            ),
        },
        'project': {
            'slug': 'method-comparison-poster',
            'title': 'Method Comparison Poster',
            'description': (
                'Choose 5 multiplication problems and solve them using both the '
                '×11 method and traditional long multiplication. Time yourself. '
                'Make a poster showing when each method is faster and why.'
            ),
        },
        'parent_note': (
            "Your child is learning a mental-math shortcut for ×11 problems. "
            "Help by giving them 2-digit numbers to multiply by 11 in spare "
            "moments (waiting for the bus, walking home). The aim is speed "
            "plus understanding — not memorisation."
        ),
    },

    'module-09-subtraction-nikhilam': {
        'title': 'Subtraction — Nikhilam (All from 9)',
        'sanskrit': 'Nikhilaṁ Navataścaramaṁ Daśataḥ',
        'subtitle': 'Subtraction by complements using Tirthaji\'s second sūtra',
        'description': (
            "*Nikhilaṁ Navataścaramaṁ Daśataḥ* — \"all from 9, the last "
            "from 10\" — is Tirthaji's second sūtra. It produces fast "
            "complements to powers of 10, removing the need for borrowing "
            "in many subtractions. Conceptually identical to two's-complement "
            "binary arithmetic used in modern computers."
        ),
        'nep': [
            '§4.6 — Integration of Indian Knowledge Systems',
            '§4.23 — Experiential learning',
            '§11.8 — Holistic, multidisciplinary (math + computing)',
        ],
        'key_terms': [
            ('Nikhilam', 'Nikhilaṁ Navataścaramaṁ Daśataḥ', '"all from 9, the last from 10"'),
            ('complement', 'pratiyogi (modern coinage)', 'the number that adds to a base'),
        ],
        'sources': [
            'Bharati Krishna Tirthaji, *Vedic Mathematics* (1965), sūtra 2',
            'S. G. Dani, "Myths and reality: On Vedic mathematics," *Frontline* (1993)',
            'NCERT Mathematics Class V, ch. 1 (The Fish Tale — subtraction)',
            'D. E. Knuth, *The Art of Computer Programming*, Vol. 2 (on complements in computing)',
        ],
        'days': [
            ('the-sutra', 'The Sūtra — All from 9, Last from 10', 'Compute the complement of any 2-digit number to 100.'),
            ('complement-to-1000', 'Complement to 1000 and Beyond', 'Compute complements to 1000 and 10000 mentally.'),
            ('subtract-from-power-of-10', 'Subtract from a Power of 10', 'Compute 1000−567 and similar instantly.'),
            ('general-subtraction', 'General Subtraction via Complements', 'Use add-the-complement trick for arbitrary subtractions.'),
            ('the-algebra', 'Why It Works — The Algebra', 'Derive the place-value identity that makes the rule work.'),
            ('bar-model-proof', 'Bar Model Proof', 'Draw a visual proof using bar models and number lines.'),
            ('twos-complement', 'Two\'s Complement in Computers', 'Show how the same idea underlies binary computer subtraction.'),
            ('speed-day', 'Speed Day', 'Complete a 30-problem mental subtraction sprint.'),
            ('mixed-practice', 'Mixed Practice', 'Solve a mixed problem set comparing complement vs traditional borrow.'),
            ('final-assessment', 'Final Assessment', 'Take the summative quiz.'),
        ],
        'activity': {
            'slug': 'complement-flashcards',
            'title': 'Complement Flashcards',
            'duration': 20,
            'materials': '40 flashcards (target − number) pre-made',
            'description': (
                'In pairs, one student holds up "1000 − 738" (etc.), the other '
                'shouts the answer within 3 seconds using the Nikhilam method.'
            ),
        },
        'project': {
            'slug': 'computer-complement-explainer',
            'title': 'Computer Subtraction Explainer',
            'description': (
                'Make a one-page explainer poster: "How does my calculator '
                'subtract?" Show two\'s complement subtraction in binary using '
                'the same principle as Nikhilam.'
            ),
        },
        'parent_note': (
            "Your child is learning a fast mental subtraction method. Ask "
            "them to demonstrate by computing change at the shop, or how "
            "much time until dinner. The goal is fluent number sense."
        ),
    },

    'module-10-herbs-aushadhi': {
        'title': 'Herbs — Auṣadhi',
        'sanskrit': 'Auṣadhi',
        'subtitle': 'Six common kitchen-and-garden healing plants',
        'description': (
            "Six widely-available herbs — Tulsī, Neem, Turmeric, Ginger, "
            "Ajwain, Mint — studied through botanical identification, "
            "traditional uses from Āyurveda, modern phytochemistry "
            "(active compounds), and safety. The module emphasises that "
            "kitchen amounts are safe, but therapeutic doses require a "
            "qualified practitioner."
        ),
        'nep': [
            '§4.6 — Integration of Indian Knowledge Systems',
            '§4.23 — Experiential learning (plant identification)',
            '§4.27 — Local context (locally-available plants)',
        ],
        'key_terms': [
            ('auṣadhi', 'auṣadhi', 'medicinal plant / herb'),
            ('tulasī', 'tulasī', 'holy basil — *Ocimum tenuiflorum*'),
            ('nimba', 'nimba', 'neem — *Azadirachta indica*'),
            ('haridrā', 'haridrā', 'turmeric — *Curcuma longa*'),
            ('ārdraka', 'ārdraka', 'ginger — *Zingiber officinale*'),
            ('yavānī', 'yavānī', 'ajwain — *Trachyspermum ammi*'),
            ('pudīnā', 'pudīnā', 'mint — *Mentha* spp.'),
        ],
        'sources': [
            'Caraka Saṁhitā, *Sūtrasthāna* 1 (introduction to auṣadhi framework)',
            'Atharva Veda 10.97 — Auṣadhi Sūkta (hymn to herbs)',
            'Ayurvedic Pharmacopoeia of India (Indian Council of Medical Research)',
            'P. K. Warrier et al., *Indian Medicinal Plants* (1994)',
            'Modern phytochemistry reviews in *Journal of Ethnopharmacology*',
        ],
        'days': [
            ('what-is-aushadhi', 'What is Auṣadhi?', 'Define auṣadhi and recognise the six herbs of this module.'),
            ('tulsi', 'Tulsī — Holy Basil', 'Identify tulasī by leaf and smell; name the active compound (eugenol).'),
            ('neem', 'Neem — Bitter Healer', 'Identify nimba; learn about azadirachtin; understand high-dose safety warning.'),
            ('turmeric', 'Turmeric — Golden Root', 'Distinguish fresh root vs powder; identify curcumin as active compound.'),
            ('ginger', 'Ginger — Warming Root', 'Distinguish fresh vs dried; gingerol vs shogaol.'),
            ('ajwain', 'Ajwain — Carom Seed', 'Recognise seeds and leaves; identify thymol; traditional digestive use.'),
            ('mint', 'Mint — Cooling Leaf', 'Recognise several Mentha varieties; identify menthol.'),
            ('herbs-and-doshas', 'Herbs and the Doṣas', 'Categorise the six herbs by heating/cooling effect (links to Module 4).'),
            ('build-the-deck', 'Build the Class Deck', 'Each student contributes one identification card to the class library.'),
            ('final-share', 'Final Share and Assessment', 'Present the class herb deck; take summative quiz.'),
        ],
        'activity': {
            'slug': 'smell-test',
            'title': 'Blind Smell-Test Identification',
            'duration': 30,
            'materials': 'small samples of each of the six herbs, blindfolds (optional), notebook',
            'description': (
                'Students close their eyes and try to identify each herb by '
                'smell. They record their guess + observation, then check.'
            ),
        },
        'project': {
            'slug': 'class-herb-deck',
            'title': 'Class Herb Identification Deck',
            'description': (
                'Each student creates one identification card for one of the '
                'six herbs: Sanskrit/botanical name, leaf drawing, smell '
                'description, three traditional uses, one active compound, '
                'one safety note. Cards combined into class library.'
            ),
        },
        'parent_note': (
            "Many of these herbs are in your kitchen already. Help your "
            "child by letting them touch, smell, and learn to identify "
            "them in your home. IMPORTANT: this module teaches identification "
            "and traditional uses — not self-medication. Consult a doctor for "
            "any health concern."
        ),
    },

    'module-11-multiplication-near-base': {
        'title': 'Multiplication Near a Power of 10 — Nikhilam',
        'sanskrit': 'Nikhilaṁ Navataścaramaṁ Daśataḥ (Multiplication)',
        'subtitle': 'Fast multiplication when factors are close to 10, 100, or 1000',
        'description': (
            "When both factors are within a few units of a power of 10 "
            "(e.g. 97 × 96, 103 × 104), Tirthaji's Nikhilam sūtra gives "
            "a two-step mental method that is much faster than long "
            "multiplication. Uses deficits/excesses from a base, with "
            "cross-subtraction on one side and product-of-deficits on "
            "the other."
        ),
        'nep': [
            '§4.6 — Integration of Indian Knowledge Systems',
            '§4.23 — Experiential learning',
            '§4.27 — Local context and language',
        ],
        'key_terms': [
            ('Nikhilam', 'Nikhilaṁ', 'the Nikhilam sūtra (also used in Module 9 for subtraction)'),
            ('vinkulam', 'vinkulam', 'deficit (number below base)'),
            ('ādhikya', 'ādhikya', 'excess (number above base)'),
            ('Ūrdhva-tiryagbhyāṁ', 'Ūrdhva-tiryagbhyāṁ', '"vertically and crosswise" — the general-purpose sūtra'),
        ],
        'sources': [
            'Bharati Krishna Tirthaji, *Vedic Mathematics* (1965), chapter on multiplication',
            'S. G. Dani, "Myths and reality: On Vedic mathematics," *Frontline* (1993)',
            'NCERT Mathematics Class VII, ch. 1 (Integers, including multiplication)',
        ],
        'days': [
            ('finger-trick-prelude', 'Finger-Trick Prelude', 'Practice the below-10 finger method (e.g., 7 × 8 using deficits).'),
            ('two-below-100', 'Two-Digit × Two-Digit Near 100 (Below)', 'Compute 97 × 96 using deficits.'),
            ('two-above-100', 'Two-Digit × Two-Digit Near 100 (Above)', 'Compute 103 × 104 using excesses.'),
            ('mixed-cases', 'Mixed — One Above, One Below', 'Compute 102 × 98 with sign care.'),
            ('three-digit-near-1000', '3-Digit × 3-Digit Near 1000', 'Compute 997 × 996 mentally.'),
            ('algebra-proof', 'Why It Works — The Algebra', 'Derive (B−a)(B−b) = B(B−a−b) + ab.'),
            ('when-to-use', 'When To Use It', 'Identify problems where Nikhilam is faster than long multiplication.'),
            ('speed-sprints', 'Speed Sprints', 'Race traditional vs Nikhilam on 30 problems.'),
            ('mixed-practice', 'Mixed Practice + Module 7 Crossover', 'Solve problems combining ×11 and near-base methods.'),
            ('final-assessment', 'Final Assessment', 'Summative quiz and method-comparison reflection.'),
        ],
        'activity': {
            'slug': 'speed-race',
            'title': 'Method Speed Race',
            'duration': 20,
            'materials': '20 problem cards, stopwatches, two columns on whiteboard',
            'description': (
                'Split class in two: one team solves with traditional long '
                'multiplication, the other with Nikhilam. Race on identical '
                'problems. Discuss which problems favour which method.'
            ),
        },
        'project': {
            'slug': 'mental-math-toolkit',
            'title': 'Personal Mental-Math Toolkit',
            'description': (
                'Each student compiles a one-page toolkit: when to use ×11, '
                'when Nikhilam multiplication, when traditional long-mult. '
                'Include 3 worked examples for each method.'
            ),
        },
        'parent_note': (
            "Your child can now multiply numbers like 97×96 mentally. Test "
            "them at the shop or during meals. The goal is fluent number "
            "sense, not memorisation of a trick."
        ),
    },

    'module-12-movement-of-sun': {
        'title': 'Movement of the Sun',
        'sanskrit': 'Sūrya-gati — Uttarāyaṇa and Dakshiṇāyana',
        'subtitle': 'Solar year, solstices, equinoxes, and the 12 Rāśis',
        'description': (
            "Earth\'s axial tilt produces an apparent annual path of the "
            "Sun along the ecliptic. Indian astronomy names the northward "
            "course *Uttarāyaṇa* and southward course *Dakshiṇāyana*, with "
            "12 *Rāśi* (zodiacal divisions) and *saṁkrānti* moments when "
            "the Sun crosses between them. Sāyana (tropical) vs nirayana "
            "(sidereal) reference frames are introduced for senior students."
        ),
        'nep': [
            '§4.6 — Integration of Indian Knowledge Systems',
            '§4.23 — Experiential learning (sunrise observation)',
            '§11.8 — Holistic, multidisciplinary (astronomy + calendar)',
        ],
        'key_terms': [
            ('Sūrya', 'Sūrya', 'the Sun'),
            ('Uttarāyaṇa', 'Uttarāyaṇa', 'northward solar course (Dec 21 – June 21)'),
            ('Dakshiṇāyana', 'Dakṣiṇāyana', 'southward solar course (June 21 – Dec 21)'),
            ('saṁkrānti', 'saṁkrānti', 'Sun\'s crossing from one Rāśi to the next'),
            ('rāśi', 'rāśi', '1/12th of the ecliptic; zodiacal sign'),
            ('sāyana', 'sāyana', 'tropical zodiac (linked to seasons)'),
            ('nirayana', 'nirayana', 'sidereal zodiac (linked to fixed stars)'),
        ],
        'sources': [
            'Sūrya-siddhānta (c. 5th–10th c. CE), chapters on solar motion',
            'Āryabhaṭīya (499 CE), on precession',
            'Varāhamihira, *Bṛhat Saṁhitā* (6th c. CE)',
            'NCERT Physics Class XI, ch. 8 (Gravitation)',
            'NCERT Geography Class IX, ch. 3 (Motions of the Earth)',
        ],
        'days': [
            ('suns-yearly-path', 'The Sun\'s Yearly Path', 'Observe that sunrise direction changes; introduce the ecliptic.'),
            ('axial-tilt-and-seasons', 'Axial Tilt and the Seasons', 'Demonstrate with torch+globe why we have summer and winter.'),
            ('two-courses', 'Uttarāyaṇa and Dakshiṇāyana', 'Identify the dates and direction of each.'),
            ('equinoxes', 'Equinoxes — Viṣuva', 'Identify spring and autumn equinoxes (day = night).'),
            ('twelve-rashis', 'Twelve Rāśis', 'Name the 12 rāśis in Sanskrit and pair with Greek zodiac names.'),
            ('sankranti-moments', 'Saṁkrānti Moments', 'Identify Makara, Karka, and other saṁkrāntis on the calendar.'),
            ('sayana-vs-nirayana', 'Sāyana vs Nirayana', 'Distinguish tropical and sidereal zodiacs; introduce ayanāṁśa.'),
            ('precession-of-equinoxes', 'Precession of the Equinoxes', 'Explain why Indian and Western zodiac dates differ today.'),
            ('cross-cultural', 'Cross-Cultural Solar Calendars', 'Compare with Egyptian, Roman, Gregorian.'),
            ('final-share', 'Final Share and Assessment', 'Project share + summative quiz.'),
        ],
        'activity': {
            'slug': 'sunrise-direction-tracking',
            'title': 'Sunrise Direction Tracking',
            'duration': 30,
            'materials': 'compass app, classroom window, notebook',
            'description': (
                'Over 5 days, students note the compass bearing of sunrise '
                'each morning (from the same window). They graph the bearing '
                'and predict how it will change in 3 months.'
            ),
        },
        'project': {
            'slug': 'personal-solar-calendar',
            'title': 'Personal Solar Calendar',
            'description': (
                'Make a one-page solar calendar for the current year: '
                'mark the two solstices, two equinoxes, all 12 saṁkrānti '
                'dates, plus your own birthday with its rāśi.'
            ),
        },
        'parent_note': (
            "**Safety:** never look directly at the Sun. For any sun "
            "observation, use projection or proper solar filters. Your "
            "child can do sunrise-direction tracking safely from a window."
        ),
    },

    'module-13-indic-ecology': {
        'title': 'Indic Ecology — Vasudhaiva Kuṭumbakam',
        'sanskrit': 'Vasudhaiva Kuṭumbakam',
        'subtitle': '"The world is one family" — Indian ecological frameworks',
        'description': (
            "*Vasudhaiva Kuṭumbakam* — \"the world is one family\" — "
            "from the Mahā Upaniṣad (6.71–73) anchors the Indian "
            "ecological tradition. Combined with the Pṛthivī Sūkta "
            "(Atharva Veda 12.1), Iṣopaniṣad mantra 1, and Bhagavad "
            "Gītā 3.10–14 on *yajña* as ecological cycle, students "
            "encounter classical frameworks and apply them to modern "
            "climate and sustainability challenges."
        ),
        'nep': [
            '§4.6 — Integration of Indian Knowledge Systems',
            '§4.23 — Experiential learning (local-ecology mapping)',
            '§11.8 — Holistic, multidisciplinary (ethics + ecology + climate)',
        ],
        'key_terms': [
            ('Vasudhaiva Kuṭumbakam', 'Vasudhaiva Kuṭumbakam', '"the world is one family" — Mahā Upaniṣad 6.71'),
            ('yajña', 'yajña', 'cycle of giving and receiving (BG 3.10–14)'),
            ('ahiṁsā', 'ahiṁsā', 'non-violence; extended to non-human life'),
            ('devarakāḍu', 'devarakāḍu', 'sacred grove (Karnataka, S. India)'),
            ('sthāvara-jaṅgama', 'sthāvara-jaṅgama', 'immobile (plants, rocks) and mobile (animals) life'),
        ],
        'sources': [
            'Mahā Upaniṣad 6.71–73 — vasudhaiva kuṭumbakam',
            'Atharva Veda 12.1 — Pṛthivī Sūkta',
            'Bhagavad Gītā 3.10–14 — yajña as cycle',
            'Iṣopaniṣad mantra 1 — *īśāvāsyam idaṁ sarvam*',
            'Madhav Gadgil & Ramachandra Guha, *This Fissured Land: An Ecological History of India* (1992)',
            'IPCC Sixth Assessment Report (2021–2023)',
        ],
        'days': [
            ('vasudhaiva-kutumbakam', 'Vasudhaiva Kuṭumbakam', 'Identify the source verse and explain the principle.'),
            ('five-elements-as-frame', 'Five Elements as Ecological Frame', 'Link Module 2 pañcabhūta to ecology — interconnection.'),
            ('rivers-as-sacred', 'Rivers as Sacred', 'Discuss the ecological function of river-worship traditions.'),
            ('sacred-groves', 'Sacred Groves', 'Identify devarakāḍu and similar groves as biodiversity reserves.'),
            ('yajna-cycle', 'Yajña — The Ecological Cycle', 'Read BG 3.10–14; map yajña to natural-cycle reciprocity.'),
            ('prthivi-sukta', 'Pṛthivī Sūkta (AV 12.1)', 'Read the Earth-mother hymn and discuss imagery.'),
            ('isopanishad-mantra', 'Iṣopaniṣad — Non-Greed Ethic', 'Translate *īśāvāsyam idaṁ sarvam* and discuss its ecological implication.'),
            ('climate-change-context', 'Climate Change — The Crisis', 'Summarise key IPCC findings; what is changing and why.'),
            ('from-ancient-to-action', 'From Ancient to Action', 'Design one local environmental project applying an Indic-ecology principle.'),
            ('project-pitch', 'Project Pitch and Assessment', 'Present project pitches; summative quiz.'),
        ],
        'activity': {
            'slug': 'sacred-grove-mapping',
            'title': 'Sacred Grove (or Local Ecology) Mapping',
            'duration': 30,
            'materials': 'large paper, coloured markers, optional photos',
            'description': (
                'Identify one sacred grove, river-bank, or biodiversity site '
                'in your region. Map it with notes on flora, fauna, traditional '
                'protection practices, and current threats.'
            ),
        },
        'project': {
            'slug': 'local-ecology-action',
            'title': 'Local Ecology Action Plan',
            'description': (
                'Design and pitch one practical environmental project for '
                'your school or neighbourhood (e.g. plant-a-tree drive, water-'
                'audit, waste-sorting station). Pitch must reference one Indic '
                'principle (vasudhaiva kuṭumbakam, yajña, sacred-grove model).'
            ),
        },
        'parent_note': (
            "This module connects classical ecological wisdom with the "
            "current climate crisis. Talk with your child about local "
            "environmental concerns — water, waste, trees in your area — "
            "and how your family already practices small acts of conservation."
        ),
    },

    'module-14-magic-squares': {
        'title': 'Magic Squares — Bhadragaṇita',
        'sanskrit': 'Bhadra-gaṇita',
        'subtitle': 'Nārāyaṇa Paṇḍita\'s Gaṇita-kaumudī and the art of magic squares',
        'description': (
            "A magic square is an n×n grid of distinct integers where "
            "every row, column, and main diagonal sums to the same "
            "constant. Nārāyaṇa Paṇḍita's *Gaṇita-kaumudī* (1356 CE), "
            "Book 14 (*Bhadra-gaṇita*), gives the most systematic pre-"
            "modern Indian treatment, including the stair-step (kothumi) "
            "method for odd-order squares. Cross-cultural comparison with "
            "Lo Shu (China) and Dürer (Europe) shows the universality of "
            "the puzzle and the Indian contribution to its mathematical "
            "systematisation."
        ),
        'nep': [
            '§4.6 — Integration of Indian Knowledge Systems',
            '§4.23 — Experiential learning (constructive puzzling)',
            '§11.8 — Holistic, multidisciplinary (math + history + cross-cultural)',
        ],
        'key_terms': [
            ('bhadra-gaṇita', 'bhadra-gaṇita', '"auspicious arithmetic" — the Indian term for magic squares'),
            ('magic constant', 'siddhāṅka (modern coinage)', 'the common sum of all rows/columns/diagonals'),
            ('stair-step method', 'kothumi vidhi', 'Nārāyaṇa\'s algorithm for odd-order squares'),
        ],
        'sources': [
            'Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī* (1356 CE), Book 14 (Bhadra-gaṇita)',
            'Kim Plofker, *Mathematics in India* (Princeton, 2009), ch. 5',
            'Khajuraho temple inscription (~10th–11th c. CE) — 4×4 panel-magic square',
            'NCERT Mathematics Class VII, ch. 2 (Fractions and Decimals) — related grid arithmetic',
        ],
        'days': [
            ('discover-3x3', 'Discover the 3×3', 'Build the unique 3×3 magic square with 1–9 by trial.'),
            ('magic-constant', 'The Magic Constant', 'Derive why 3×3 with 1–9 must sum to 15 per row.'),
            ('how-many-3x3', 'How Many 3×3 Magic Squares?', 'Count the equivalence classes (up to symmetry).'),
            ('stair-step-method', 'Stair-Step Method (Nārāyaṇa)', 'Apply Nārāyaṇa\'s algorithm to build a 5×5 square.'),
            ('practice-5x5', 'Practice — 5×5 and 7×7', 'Use the method on multiple odd-order squares.'),
            ('4x4-and-khajuraho', '4×4 and the Khajuraho Square', 'Examine the Khajuraho inscription and its panel-magic property.'),
            ('historical-context', 'Historical Context — Nārāyaṇa and Predecessors', 'Place *Gaṇita-kaumudī* in 14th c. Indian math.'),
            ('cross-cultural', 'Cross-Cultural — Lo Shu and Dürer', 'Compare Indian, Chinese (Lo Shu), and European (Dürer 1514) magic squares.'),
            ('design-your-own', 'Design Your Own', 'Create a personalised 4×4 or 5×5 magic square as visual art.'),
            ('final-share', 'Final Share and Assessment', 'Present design + summative quiz.'),
        ],
        'activity': {
            'slug': 'class-3x3-tournament',
            'title': 'Class 3×3 Magic-Square Tournament',
            'duration': 25,
            'materials': 'grids on paper, pencils, timer',
            'description': (
                'In pairs, students race to construct the 3×3 magic square '
                'with 1–9 from a starting 9-position permutation. First pair '
                'with correct sums wins.'
            ),
        },
        'project': {
            'slug': 'magic-square-art',
            'title': 'Magic Square as Visual Art',
            'description': (
                'Design a 4×4 or 5×5 magic square. Decorate it as a piece '
                'of visual art (mandala-style, calligraphic, geometric). '
                'Include the magic constant calculation on the back.'
            ),
        },
        'parent_note': (
            "Your child is learning to construct magic squares — grids "
            "where every row, column, and diagonal sums to the same number. "
            "It\'s a puzzle and a piece of cultural mathematics. Ask them to "
            "show you the 3×3 with 1–9 — it\'s the foundational case."
        ),
    },

    'module-15-project-implementation': {
        'title': 'Project Implementation — Capstone',
        'sanskrit': 'Anvayana — Synthesis',
        'subtitle': 'A 10-day applied project drawing on Modules 1–14',
        'description': (
            "The capstone module of the curriculum. Students choose from "
            "a menu of applied projects (or design their own) that draw "
            "on concepts from Modules 1–14. They scope, research, design, "
            "build, document, and present. Process discipline — daily "
            "journal, source citations, honest reflection — is part of "
            "the assessment."
        ),
        'nep': [
            '§4.6 — Integration of Indian Knowledge Systems',
            '§4.23 — Experiential / project-based learning',
            '§11.8 — Holistic, multidisciplinary',
        ],
        'key_terms': [
            ('anvayana', 'anvayana', 'integration / following-through; capstone synthesis'),
            ('pañcagavya', 'pañcagavya', 'five-cow-product preparation (substituted with fermented-foods study for school safety)'),
            ('siddhānta', 'siddhānta', 'concluded principle or doctrine'),
        ],
        'sources': [
            'All Modules 1–14 of this curriculum',
            'Project-Based Learning literature (Buck Institute, Edutopia)',
            'NCERT NEP 2020 §4.23 — experiential learning',
        ],
        'days': [
            ('overview-and-menu', 'Capstone Overview and Project Menu', 'Review the 10-option project menu; pick a project.'),
            ('scope-and-plan', 'Scope and Plan', 'Write a 1-page project plan: problem, sources, deliverable, deadline.'),
            ('research-1', 'Research — Day 1', 'Gather sources; cross-reference earlier modules.'),
            ('research-2', 'Research — Day 2', 'Continue research; sketch initial design.'),
            ('mid-project-critique', 'Mid-Project Critique', 'Pairs swap plans; offer one strength + one concern.'),
            ('build-1', 'Build / Make — Day 1', 'Start building the artefact (model, poster, deck, garden plot).'),
            ('build-2', 'Build / Make — Day 2', 'Continue building; daily journal entry.'),
            ('document', 'Document', 'Write up process, sources, reflections (~500 words for Senior).'),
            ('rehearse', 'Rehearse Presentation', 'Pair feedback on final presentation; refine.'),
            ('share-day', 'Project Share Day', 'Present project to peers + parents; complete self-assessment.'),
        ],
        'activity': {
            'slug': 'mid-project-critique',
            'title': 'Mid-Project Critique Circle',
            'duration': 30,
            'materials': 'student project plans, sticky notes',
            'description': (
                'Pairs swap project plans, read in 5 minutes, then offer '
                'one strength (one sticky note) and one concern (another '
                'sticky note). Pairs rotate twice. Refine plan based on '
                'feedback.'
            ),
        },
        'project': {
            'slug': 'capstone-project',
            'title': 'Capstone Project (Student Choice)',
            'description': (
                'Choose one of the 10-option project menu (see README.md) '
                'or pitch your own. Deliverables: 1-page plan, daily '
                'journal, final artefact, ~500-word reflection (Senior; '
                '~300 for Middle; oral share for Primary), 5-minute '
                'presentation. Safety: NO cow-urine ingestion for any '
                'pañcagavya project — pivot to fermented-foods comparative '
                'study instead.'
            ),
        },
        'parent_note': (
            "This is the capstone module — your child picks a project "
            "drawing on the whole curriculum. Encourage their choice "
            "(don\'t pick for them). Ask them about their progress each "
            "day. Attend the share day if you can. **Safety:** pañcagavya "
            "projects in school MUST use fermented-foods comparative study "
            "(curd, paneer, batter), NOT cow-urine ingestion."
        ),
    },
}


# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------


def render_readme(mod, band):
    bi = BAND_INFO[band]
    days_md = '\n'.join(
        f"- **Day {i+1}** — {d[1]}: {d[2]}"
        for i, d in enumerate(mod['days'])
    )
    terms_md = '\n'.join(
        f"- *{iast}* — {meaning}"
        for _, iast, meaning in mod['key_terms']
    )
    nep_md = '\n'.join(f"- {n}" for n in mod['nep'])

    return f"""# {mod['title']}

**Band:** {bi['label']} ({bi['grades']}) · **Sessions:** 10 × {bi['duration']} · **Sanskrit:** {mod['sanskrit']}

## Overview

{mod['description']}

## NEP 2020 alignment

{nep_md}

## Key terms (this module)

{terms_md}

## Prerequisites

Module 2 (Panchabhūta) is recommended before this module. Modules 5 (Bindu Paddhati / dot addition) and 7 (×11 Multiplication) are useful prerequisites for Module 9 and 11.

## Materials needed (across 10 days)

- Notebook + pencils per student
- Whiteboard / chart paper
- (See `lesson-plan.md` for per-day material lists)

## 10-day map

{days_md}

## Files in this pack

- `lesson-plan.md` — detailed 10-day arc
- `sources.md` — sources cited in this module
- `teacher-notes.md` — common misconceptions, differentiation
- `parent-guide.md` — what parents should know
- `days/day-NN-*.md` — 10 per-day lesson plans
- `quizzes/formative.md`, `quizzes/summative.md`
- `activities/activity-01-*.md`
- `assessments/rubric.md`, `assessments/project-brief.md`
- `student-workbook.md`
- `writing-prompts.md` (or `oral-recall.md` for Primary)
- `homework.md`
- `slides/deck.md`

## Voice

{bi['voice'].capitalize()}; {bi['sentence']}. Pitches the concept first, frames the tradition as historical context, and uses IAST for all Sanskrit terms.
"""


def render_lesson_plan(mod, band):
    bi = BAND_INFO[band]
    days_md = '\n\n'.join(
        f"### Day {i+1} — {d[1]}\n\n"
        f"**Objective:** {d[2]}\n\n"
        f"**Flow:** Warm-up (5 min) · Core ({_core_minutes(bi)} min) · Activity ({_activity_minutes(bi)} min) · Wrap-up (5 min)"
        for i, d in enumerate(mod['days'])
    )
    return f"""# Lesson Plan — {mod['title']} ({BAND_INFO[band]['label']})

10-day arc, {bi['duration']} per session.

{days_md}

## Pacing notes

- {BAND_INFO[band]['label']} sessions are {bi['duration']}. Adjust if your block is different.
- Days 5 and 9 are buffer days — use to reinforce weaker concepts or extend stronger ones.
- The summative project (see `assessments/project-brief.md`) runs in parallel from Day 6 onward.

## Differentiation

- **For advanced students:** see `teacher-notes.md` for extension prompts.
- **For students needing more support:** simplify activities, do more pair-work, allow oral instead of written responses.
"""


def render_sources(mod, band):
    sources_md = '\n'.join(f"- {s}" for s in mod['sources'])
    return f"""# Sources — {mod['title']} ({BAND_INFO[band]['label']})

## Primary and secondary sources

{sources_md}

## A note on citation discipline

Per the curriculum's style guide, citations must be verifiable. If a verse number, page, or attribution cannot be confirmed, the source is paraphrased without invented attribution. Where direct quotes appear in {BAND_INFO[band]['label']}-band day files, the source is identified in IAST + edition.

## For deeper reading

- The shared glossary at `curriculum/_shared/glossary.md` contains the IAST + meaning for every Sanskrit term used.
- Other modules in this curriculum that connect: see the module README's "Prerequisites" section.
"""


def render_teacher_notes(mod, band):
    bi = BAND_INFO[band]
    return f"""# Teacher Notes — {mod['title']} ({bi['label']})

## Common student misconceptions

- *"This is religious, not scientific."* — Frame the tradition as historical observation. Pañcabhūta-like classifications of matter exist in many cultures. Indian astronomy and math are documented, peer-reviewed historical fields.
- *"The Sanskrit terms are just jargon."* — Insist on the triple format (Sanskrit / IAST / meaning) once, then use the Sanskrit alone. The terms are precise; the discipline of using them properly is itself a learning outcome.
- *"If it's traditional, it must work."* — Distinguish empirical claims (testable) from ethical/aesthetic frames (which need separate justification). Encourage students to ask "how would I test this?".

## Differentiation strategies

- **Extension for advanced students:** offer one optional "deeper read" per day — usually a primary source or modern paper.
- **Support for students needing scaffolds:** more pair-work, allow oral responses, provide partial outlines for writing prompts.
- **Multilingual classrooms:** Sanskrit terms are universal; vernacular equivalents (Hindi, Tamil, Telugu, Bengali, Marathi etc.) should be welcomed.

## Safety

- Any activity involving food, plants, fire, or outdoor work needs explicit safety briefing.
- See the relevant day file for activity-specific safety notes.

## Honest framing

- Where modern science clearly extends or revises traditional claims, say so.
- Where the tradition's framing is best understood as ethical/aesthetic, present it as such (not as competing science).
- Where attribution is debated (e.g., the "Vedic" status of Tirthaji's mathematics), present the debate honestly.

## End-of-module reflection (for teachers)

- Which concepts landed well? Which didn't?
- Which students grew most? Which need a different approach next module?
- Add notes to `teacher-notes.md` for the next teacher who uses this pack.
"""


def render_parent_guide(mod, band):
    bi = BAND_INFO[band]
    return f"""# Parent Guide — {mod['title']} ({bi['label']})

## What is your child learning?

{mod['description']}

## Why this matters

This module is part of an Indian Knowledge Systems curriculum that introduces classical Indian frameworks alongside their modern-scientific parallels. Your child will learn to (a) name and use precise Sanskrit terms, (b) understand the observational basis for the classical framework, and (c) relate it to current scientific or scholarly understanding.

## What you can do at home

{mod.get('parent_note', 'Ask your child to teach you one concept from this module. Listen for whether they can explain it in their own words.')}

## Conversation prompts

Try one of these over a meal or walk:

1. *"What's one Sanskrit word you learned this week? What does it mean?"*
2. *"What did you find surprising in this module?"*
3. *"Is there anything you're not sure about? Let's look it up together."*
4. *"How would you explain this to your grandmother / grandfather?"*

## Questions parents often ask

**Q: Is this religious instruction?**
A: No. The module presents Indian classical frameworks (cosmology, mathematics, astronomy, ecology) as historical knowledge systems with their own logic and method. The framing is scholarly and comparative, not devotional.

**Q: Will my child be tested on Sanskrit?**
A: Sanskrit terms are introduced for precision, not for rote memorisation. The summative quiz asks students to *use* the terms — for example, "Which doṣa is dominant in the morning hours?" — rather than translate them.

**Q: How does this connect to NCERT / board syllabus?**
A: This module supplements (does not replace) NCERT content. NEP 2020 §4.6 calls for the integration of Indian Knowledge Systems. The pack's `README.md` lists the specific NEP principles each module advances.

## Reading further (for parents)

See `sources.md` in this pack for the full source list.
"""


def render_day(mod, band, day_idx):
    bi = BAND_INFO[band]
    slug, title, objective = mod['days'][day_idx]
    day_num = day_idx + 1
    duration = bi['duration']

    # Pick a key term for vocab (cycle through)
    if mod['key_terms']:
        key = mod['key_terms'][day_idx % len(mod['key_terms'])]
        sanskrit_name, iast, meaning = key
        vocab_md = f"- *{iast}* (IAST: {iast}; lit. \"{meaning}\")"
    else:
        vocab_md = "- (no new term this day; review previous terms)"

    primary_friendly = (band == 'primary')
    citation_block = ''
    if band == 'senior' and day_idx == 0 and mod['sources']:
        citation_block = f"\n### Primary source (today's reading)\n\nFrom *{mod['sources'][0].split(',')[0]}* — see `sources.md`.\n"

    activity_min = _activity_minutes(bi)
    core_min = _core_minutes(bi)
    activity_phrase = mod['activity']['title']

    if primary_friendly:
        return f"""# Day {day_num} — {title}

**Module:** {mod['title']} (Primary) · **Time:** {duration}

## Goal

{objective}

## Materials

- Notebook, pencils, drawing paper
- (See lesson-plan.md for any day-specific materials)

## The flow

### Settle + chant (3 min)

Daily chant or breathing exercise.

### Story recall (4 min)

Briefly recall yesterday's lesson by asking: *"What's one thing you remember from yesterday?"*

### Today's idea ({core_min - 5} min)

{vocab_md}

Introduce the concept gently using a story, a drawing, or a sensory example. The concept for today: **{title}**. Keep sentences short.

### Activity ({activity_min} min)

A simplified version of *{activity_phrase}* (see `activities/`). Draw, sing, or act it out.

### Wrap-up (3 min)

Each child shares one word that describes today.

## Homework

(See `homework.md`.)

## Teacher notes

- Citations belong in teacher notes only, not in student-facing material at this band.
- Keep new Sanskrit terms to one per lesson, repeated several times.
- If energy is low, swap the activity for free drawing.
"""

    return f"""# Day {day_num} — {title}

**Module:** {mod['title']} · **Band:** {bi['label']} · **Time:** {duration}

## Learning objective

By the end of this lesson, students will: {objective.lower() if objective[0].isupper() else objective}

## Materials

- Whiteboard / chart paper
- Notebook, pen per student
- (See lesson-plan.md for any day-specific materials)

## Vocabulary introduced today

{vocab_md}
{citation_block}

## Lesson flow

### Warm-up (5 min)

- Daily check-in: one-sentence response to *"What's one thing you remember about yesterday's lesson?"*
- Hook: introduce a phenomenon or question that motivates today's concept.

### Core ({core_min} min)

1. **State the observable phenomenon first.** Whatever the day's idea is — a number trick, a celestial pattern, a herb's identifying feature — start with the thing students can see, hear, or do.
2. **Introduce the Sanskrit term.** Once, in the triple format, then italicised only.
3. **Build the conceptual map.** Connect today's idea to prior modules (especially Module 2 if applicable) and prior days.
4. **Work an example** with the whole class on the board.
5. **Independent or paired practice** for ~5 minutes.

### Activity ({activity_min} min)

A scaled version of *{activity_phrase}* (see `activities/`). Today's slice: focus on the part of the activity that reinforces {title}.

### Wrap-up (5 min)

- One-sentence exit ticket: *"What's one thing you learned today?"*
- Preview tomorrow.

## Homework

(See `homework.md` for today's task.)

## Differentiation

- **Extension:** offer one open question or extra problem for fast finishers.
- **Support:** pair students who need scaffolds; offer partial outlines.

## Teacher notes

- Citations: { 'at least one paraphrase per module' if band == 'middle' else 'at least one quoted verse with citation per module' }. Day 1 already includes one if applicable; you may add more.
- Connect to prior modules where natural (especially Module 2 pañcabhūta).
"""


def render_quiz_formative(mod, band):
    bi = BAND_INFO[band]
    qs = [
        f"1. Name the three / four key terms introduced in this module so far. Give the IAST and one-line meaning of each.",
        f"2. State the central idea of {mod['title']} in one sentence.",
        f"3. (Multiple choice) Which day in this module focused on '{mod['days'][2][1]}'?  (a) Day 1  (b) Day 2  (c) Day 3  (d) Day 4",
        f"4. True / False — and explain in one sentence: *{mod['title']} is purely a religious concept and has no scientific framing.*",
        f"5. Connect {mod['title']} to **one** other module in this curriculum. Which module, and how?",
        f"6. List **two** sources cited so far in this module.",
        f"7. (Short answer) Why does the module distinguish '{mod['key_terms'][0][1] if mod['key_terms'] else 'the key term'}' from related concepts? Give one example.",
        f"8. (Short answer) In your own words, explain Day 3's concept.",
        f"9. Identify **one** common misconception about {mod['title']} and rebut it in one sentence.",
        f"10. Write **one** question you have about this module so far — something you want clarified before the summative.",
    ]
    return f"""# Formative Quiz — {mod['title']} ({bi['label']})

**When:** mid-module (after Day 5).
**Duration:** {20 if band == 'primary' else 25} minutes.
**Format:** mix of short answer, multiple choice, and reflection. {('Sticker self-assessment for Primary.' if band == 'primary' else '')}

## Questions

{chr(10).join(qs)}

## How this is used

This quiz is **formative** — it's a check-in to see what's landing, not a grade. Teacher reviews answers to adjust pacing for Days 6–10. Students may swap and self-mark.
"""


def render_quiz_summative(mod, band):
    bi = BAND_INFO[band]
    qs = []
    qs.append("**Part A — Vocabulary (~5 points)**")
    for i, kt in enumerate(mod['key_terms'][:5]):
        _, iast, meaning = kt
        qs.append(f"A{i+1}. Define *{iast}* in your own words.")
    qs.append("")
    qs.append("**Part B — Concepts (~10 points)**")
    qs.append(f"B1. Explain the central idea of {mod['title']} in your own words (3–4 sentences).")
    qs.append(f"B2. Describe the method or framework students used in Day 4 of this module.")
    qs.append(f"B3. Identify ONE source cited in this module and explain why it matters.")
    qs.append(f"B4. Compare {mod['title']} with a concept from another module (your choice). What\'s similar, what\'s different?")
    qs.append(f"B5. Identify ONE common misconception about this module and rebut it in 2–3 sentences.")
    qs.append("")
    qs.append("**Part C — Application (~5 points)**")
    qs.append(f"C1. Give an example of {mod['title']} from your own daily life.")
    qs.append(f"C2. Describe one way this module connects to a current real-world issue (or scientific question).")
    qs.append("")
    qs.append("**Part D — Reflection (~5 points; ungraded for content)**")
    qs.append("D1. What surprised you most in this module?")
    qs.append("D2. What\'s one question you still have?")

    if band == 'senior':
        qs.append("")
        qs.append("**Part E — Primary source (~5 points; Senior only)**")
        qs.append(f"E1. Quote or paraphrase one passage from a primary source cited in this module. Explain it in your own words.")

    return f"""# Summative Quiz — {mod['title']} ({bi['label']})

**When:** end of module (after Day 10).
**Duration:** {30 if band == 'primary' else 45} minutes.
**Total points:** {20 if band == 'primary' else 30}.

## Questions

{chr(10).join(qs)}

## Marking guidance

- Vocabulary: give credit for correct meaning, even if exact wording differs.
- Concepts: look for evidence of understanding, not memorisation.
- Application: any reasonable example accepted.
- Reflection: ungraded for content; awarded for thoughtfulness.

## Pass mark

A score of {12 if band == 'primary' else 18}/{20 if band == 'primary' else 30} indicates the student has met the module's learning objectives.
"""


def render_activity(mod, band):
    bi = BAND_INFO[band]
    a = mod['activity']
    return f"""# Activity 1 — {a['title']}

**Module:** {mod['title']} · **Band:** {bi['label']} · **Duration:** {a['duration']} min

## Purpose

Reinforce the day-by-day concepts of {mod['title']} through a hands-on activity. Aligned with NEP 2020 §4.23 (experiential learning).

## Materials

{a['materials']}

## What students do

{a['description']}

## Step-by-step

1. **Setup (5 min)** — gather materials; explain the task.
2. **Working phase ({a['duration'] - 10} min)** — students work individually or in pairs.
3. **Share (5 min)** — selected students share their results with the class.

## Differentiation

- **Extension:** ask advanced students to do an additional iteration or analysis.
- **Support:** pair students who need scaffolds; offer partial templates.

## Assessment

This activity is **formative**. The teacher observes participation, accuracy, and reflection quality. No grade is assigned.

## Safety

- General safety briefing before any materials are handled.
- If herbs, plants, or food are involved: kitchen-amount only, no ingestion of unknown preparations.
- Outdoor activities: stay in the designated area; supervised by the teacher.
"""


def render_rubric(mod, band):
    bi = BAND_INFO[band]
    if band == 'primary':
        levels = ['🌟 Strong understanding', '🌱 Growing', '🌧 Needs more practice']
        criteria = ['Knows the new word(s)', 'Joined in activities', 'Asked good questions', 'Drew / made something']
    else:
        levels = ['Exceeding (4)', 'Meeting (3)', 'Approaching (2)', 'Beginning (1)']
        criteria = [
            'Accuracy of concepts — uses Sanskrit terms correctly, gets the central idea right',
            'Source discipline — cites sources, distinguishes traditional framing from empirical claim',
            'Application — connects the module to other modules and to real-world examples',
            'Presentation — clear, organised, evidence-supported',
            'Reflection — honest, thoughtful, identifies what was learned and what remains uncertain',
        ]

    body = ''
    if band == 'primary':
        body = '\n'.join(f"- **{c}** — {levels[0]} / {levels[1]} / {levels[2]}" for c in criteria)
    else:
        body = ''
        for c in criteria:
            body += f"\n### {c}\n\n"
            body += f"- **{levels[0]}** — Exceptional; could teach this to another student.\n"
            body += f"- **{levels[1]}** — Solid; meets the learning objective.\n"
            body += f"- **{levels[2]}** — Partial; some elements present, others missing.\n"
            body += f"- **{levels[3]}** — Significant gaps; needs re-teaching.\n"

    return f"""# Assessment Rubric — {mod['title']} ({bi['label']})

This rubric applies to the project (see `project-brief.md`) and may also inform the summative quiz.

## Criteria

{body}

## How the teacher uses this rubric

1. After the project share, score each student on each criterion.
2. Convert to a band (4 = Exceeding, 3 = Meeting, etc.) for the report card.
3. Share at least one strength and one area for growth with each student.

## Self-assessment (Senior students)

Senior students complete a parallel self-assessment using the same rubric before the teacher\'s assessment. The teacher and student then meet to compare.
"""


def render_project_brief(mod, band):
    bi = BAND_INFO[band]
    p = mod['project']
    return f"""# Project Brief — {p['title']}

**Module:** {mod['title']} · **Band:** {bi['label']}

## What you will do

{p['description']}

## Why

This project asks you to apply concepts from this module to your own life or a real situation. It is graded on the rubric in `rubric.md`.

## Deliverables

- **One-page project plan** (Day 2 of the module): problem, sources, deliverable, timeline.
- **Daily journal entries** (one per day, starting Day 6): what you did, what worked, what didn\'t.
- **Final artefact** ({"a drawing / made object" if band == 'primary' else "a poster / model / digital deliverable"}).
- **Written reflection** ({ 'oral share' if band == 'primary' else '300 words (Middle)' if band == 'middle' else '500 words (Senior)'}): what you learned, what surprised you, what you\'re still uncertain about.
- **Presentation** ({3 if band == 'primary' else 5}-minute share with the class).

## Timeline

- **Day 1–2:** scope and plan.
- **Day 3–4:** research.
- **Day 5:** mid-project critique.
- **Day 6–7:** build / make.
- **Day 8:** document.
- **Day 9:** rehearse.
- **Day 10:** share day.

## Sources

You must cite at least { 1 if band == 'primary' else 2 if band == 'middle' else 3 } sources. Use the form: *Author, Title, year.* (See `../sources.md` for examples.)

## Safety

- Any project involving plants / food / outdoor work must be supervised.
- **No herbal medicine recommendations.** Modules 10 and 4 give awareness; therapeutic decisions belong to qualified practitioners.
- {("**Capstone safety:** if you choose a pañcagavya project, you MUST use the fermented-foods comparative-study substitution — cow-urine ingestion is NOT allowed." if mod.get('title','').startswith('Project') else '')}

## Grading

See `rubric.md`. The project is worth the same weight as the summative quiz.
"""


def render_writing_prompts(mod, band):
    bi = BAND_INFO[band]
    if band == 'primary':
        return f"""# Oral Recall Prompts — {mod['title']} (Primary)

Use one of these as the day's last activity. Children answer aloud or by drawing.

1. *"Tell me one new word you learned today."*
2. *"What was your favourite part of today's lesson?"*
3. *"Show me with your hands what {mod['key_terms'][0][1] if mod['key_terms'] else 'today\'s idea'} looks like."*
4. *"Draw one thing from today's lesson."*
5. *"Sing or hum what {mod['key_terms'][1][1] if len(mod['key_terms']) > 1 else 'this'} feels like."*
6. *"Tell your neighbour one thing you learned."*
7. *"What is something you want to ask your teacher tomorrow?"*
8. *"What would you tell your parent about today's lesson?"*
"""

    prompts = [
        f"In 3–4 sentences, explain {mod['title']} to a friend who hasn't taken this module.",
        f"Choose one Sanskrit term from this module. Define it, then describe one observation from your own life that matches.",
        f"Compare {mod['title']} with a similar concept from another module or from your science textbook. What's similar? Different?",
        f"Identify ONE claim in this module that you'd want to test. How would you test it?",
        f"What was the most surprising thing in this module? Why did it surprise you?",
        f"Pick one source cited in this module. Write 2 sentences explaining why it matters.",
        f"What is one common misconception about {mod['title']}? Rebut it in 2–3 sentences.",
        f"Imagine you are teaching this module to a younger student. What would you say first?",
    ]
    if band == 'senior':
        prompts.append("Read one primary-source passage cited in this module. Translate or paraphrase it; comment on what it adds to your understanding.")
        prompts.append("Identify a contemporary debate about the IKS framework presented here (e.g., is Tirthaji's mathematics genuinely Vedic? are doṣas a valid framework today?). Take a position with two pieces of evidence.")
    return f"""# Writing Prompts — {mod['title']} ({bi['label']})

Use these for in-class writing, homework, or assessment. Each prompt is suitable for a {200 if band == 'middle' else 300}-word response.

{chr(10).join(f"{i+1}. {p}" for i, p in enumerate(prompts))}

## How to use

- Pick **one** prompt per day for the writing-prompts homework.
- Or assign all of them across the module, alternating between in-class and home.
- Senior students may treat any prompt as a 500-word essay topic.
"""


def render_homework(mod, band):
    bi = BAND_INFO[band]
    items = []
    for i, d in enumerate(mod['days']):
        items.append(f"**Day {i+1} — {d[1]}** · {('Draw' if band == 'primary' else 'Write 2 sentences')} about today's concept. (~{5 if band == 'primary' else 10} min)")
    return f"""# Homework — {mod['title']} ({bi['label']})

Light daily tasks. Each takes {5 if band == 'primary' else 10}–{10 if band == 'primary' else 15} minutes.

{chr(10).join(f'{i+1}. ' + x for i, x in enumerate(items))}

## Notes

- Homework is intended to consolidate what was learned in class, not introduce new content.
- If a child struggles, the parent should consult the teacher rather than push.
- Capstone project days (Module 15) may have lighter daily homework so students can focus on the project.
"""


def render_student_workbook(mod, band):
    bi = BAND_INFO[band]
    sections = []
    sections.append(f"# Student Workbook — {mod['title']} ({bi['label']})\n")
    sections.append("This workbook is yours to write in. Use it for vocab, exercises, and reflection across all 10 days.\n")
    sections.append("## Vocabulary tracker\n")
    sections.append("Fill in as we go:\n")
    for _, iast, meaning in mod['key_terms']:
        sections.append(f"- *{iast}* — _________________________ ")
    sections.append("\n## Day-by-day notes\n")
    for i, d in enumerate(mod['days']):
        sections.append(f"### Day {i+1} — {d[1]}\n")
        sections.append(f"**What I learned:**\n\n_________________________________________________________\n\n_________________________________________________________\n")
        sections.append(f"**One question I have:**\n\n_________________________________________________________\n")
    sections.append("## Final reflection\n")
    sections.append("After Day 10, write a paragraph: what is the most important thing you learned in this module?\n")
    sections.append("_________________________________________________________\n\n_________________________________________________________\n")
    return '\n'.join(sections)


def render_slides_deck(mod, band):
    bi = BAND_INFO[band]
    slides = []
    slides.append('---\nmarp: true\ntheme: default\nclass: lead\npaginate: true\n---\n')
    slides.append(f'# {mod["title"]}\n## {mod["subtitle"]}\n### {bi["label"]} band — {bi["grades"]}\n')

    slides.append('---\n## What this module is about\n')
    slides.append(mod['description'])

    slides.append('---\n## NEP 2020 alignment\n')
    for n in mod['nep']:
        slides.append(f'- {n}')

    slides.append('---\n## Key Sanskrit terms\n')
    for _, iast, meaning in mod['key_terms']:
        slides.append(f'- *{iast}* — {meaning}')

    slides.append('---\n## 10-day arc')
    for i, d in enumerate(mod['days']):
        slides.append(f'\n---\n## Day {i+1} — {d[1]}\n\n{d[2]}')

    slides.append('---\n## Activity\n')
    slides.append(f'**{mod["activity"]["title"]}**\n')
    slides.append(mod['activity']['description'])

    slides.append('---\n## Project\n')
    slides.append(f'**{mod["project"]["title"]}**\n')
    slides.append(mod['project']['description'])

    slides.append('---\n## Sources')
    for s in mod['sources'][:4]:
        slides.append(f'- {s}')

    slides.append('---\n## Questions?\n')
    slides.append(f'See `README.md` in this pack and `_shared/glossary.md` for definitions.')

    return '\n\n'.join(slides)


def _core_minutes(bi):
    return 15 if '30' in bi['duration'] else 20


def _activity_minutes(bi):
    return 8 if '30' in bi['duration'] else 15


# ---------------------------------------------------------------------------
# File-writer
# ---------------------------------------------------------------------------

def write_if_missing(path: Path, content: str) -> bool:
    """Write content only if path doesn't exist. Returns True if written."""
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
    return True


def generate_pack(slug: str, mod: dict, band: str):
    """Generate a complete pack for one (slug, band). Skips existing files."""
    pack = CURRICULUM / band / slug
    written = 0
    skipped = 0

    files = {
        'README.md': render_readme(mod, band),
        'lesson-plan.md': render_lesson_plan(mod, band),
        'sources.md': render_sources(mod, band),
        'teacher-notes.md': render_teacher_notes(mod, band),
        'parent-guide.md': render_parent_guide(mod, band),
        'quizzes/formative.md': render_quiz_formative(mod, band),
        'quizzes/summative.md': render_quiz_summative(mod, band),
        f"activities/activity-01-{mod['activity']['slug']}.md": render_activity(mod, band),
        'assessments/rubric.md': render_rubric(mod, band),
        'assessments/project-brief.md': render_project_brief(mod, band),
        ('oral-recall.md' if band == 'primary' else 'writing-prompts.md'): render_writing_prompts(mod, band),
        'homework.md': render_homework(mod, band),
        'student-workbook.md': render_student_workbook(mod, band),
        'slides/deck.md': render_slides_deck(mod, band),
    }

    # Per-day files
    for i, d in enumerate(mod['days']):
        slug_d = d[0]
        files[f'days/day-{i+1:02d}-{slug_d}.md'] = render_day(mod, band, i)

    for rel, content in files.items():
        p = pack / rel
        if write_if_missing(p, content):
            written += 1
        else:
            skipped += 1

    return written, skipped


def main():
    total_written = 0
    total_skipped = 0
    only_bands = sys.argv[1:] if len(sys.argv) > 1 else ['primary', 'middle', 'senior']

    for slug, mod in MODULES.items():
        for band in only_bands:
            w, s = generate_pack(slug, mod, band)
            total_written += w
            total_skipped += s
            print(f"  {band:>7} / {slug:35} wrote {w:2d}, skipped {s:2d}")

    print(f"\nTotal written: {total_written}.  Skipped (already present): {total_skipped}.")


if __name__ == '__main__':
    main()
