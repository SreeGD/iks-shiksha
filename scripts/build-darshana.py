#!/usr/bin/env python3
"""Generate 45 Darśana workshop markdown files (15 modules × 3 bands).

Each workshop is a 60-minute condensed lesson per module per band, structured:
  - Opening hook (5 min)
  - Core idea (15 min)
  - Demonstration (10 min)
  - Source moment (5 min) — quoted verse (Senior) / paraphrase (Middle) / story (Primary)
  - Hands-on activity (15 min)
  - Reflection + take-home (10 min)

Followed by a "Go deeper into Adhyayana" sidebar listing the 10 days the
student is skipping if they only do the workshop.

Output: curriculum/{band}/module-NN-{slug}/darshana.md
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURRICULUM = ROOT / 'curriculum'


BAND_DURATION_HINT = {
    'primary': '60 min (works as 45 min if needed — see notes)',
    'middle': '60 min',
    'senior': '60 min',
}


# Each module: title, sanskrit name, subtitle, hook/core/demo/source/activity/reflection
# Each of those is a dict keyed by band.

WORKSHOPS = {

    'module-01-what-is-iks': {
        'title': 'What is IKS?',
        'sanskrit': 'Bhāratīya Jñāna-Paramparā',
        'subtitle': 'The map of Indian Knowledge Systems',
        'hook': {
            'primary': '*"What\'s the longest poem you\'ve heard?"* (a song? a story? the Hanumān Cālīsā?) Now imagine 100,000 verses kept alive only by memory — that\'s the Mahābhārata.',
            'middle': 'Project the *Lothal dockyard* (Indus Valley, ~2500 BCE). *"What does this tell you about Indian engineering 4500 years ago?"* — pause for guesses. India\'s knowledge traditions are old, varied, and documented.',
            'senior': 'Show side-by-side: Āryabhaṭa\'s value of π (3.1416, c. 499 CE) and Aryabhata-I\'s heliocentric hint. Ask: *"Which two of these are not in your science textbook? Why might that be?"*',
        },
        'core': {
            'primary': """**IKS is a name for Indian ways of knowing.** It includes math, medicine, astronomy, dance, music, building, language, and yoga.

Three big groups (write on board):
- **Vedāṅgas** — six "limbs of the Veda" — śikṣā (pronunciation), kalpa (ritual procedure), vyākaraṇa (grammar), nirukta (etymology), chandas (metre), jyotiṣa (astronomy)
- **Upavedas** — applied sciences — Āyurveda (medicine), Dhanurveda (martial), Gandharvaveda (arts), Sthāpatya (architecture)
- **Itihāsa-purāṇa** — history-and-story texts

Pick ONE limb together; the class brainstorms what we still use from it today.""",
            'middle': """**IKS = the documented knowledge traditions of the Indian subcontinent.** Three frameworks:

1. **Vedāṅgas (six limbs of the Veda)** — śikṣā, kalpa, vyākaraṇa, nirukta, chandas, jyotiṣa. The "supporting sciences" of Vedic studies.
2. **Upavedas (applied sciences)** — Āyurveda (medicine), Dhanurveda (martial science), Gandharvaveda (music/dance/drama), Sthāpatya-veda (architecture).
3. **Six Darśanas** (philosophical schools): Nyāya, Vaiśeṣika, Sāṅkhya, Yoga, Mīmāṁsā, Vedānta — each is a coherent argument structure, not a religion.

The point: this is a documented intellectual tradition with internal disagreement, evidence rules, and reform — much like Western philosophy. Treat it that way.""",
            'senior': """**IKS = the documented Indian knowledge traditions, from the Saraswati-Sindhu civilisation (~3000 BCE) through the colonial period.**

Three useful framings:

1. **The Vedāṅga / Upaveda / Darśana taxonomy** (canonical) — six Vedic limbs, four applied sciences, six philosophical schools.
2. **The science-vs-religion problem.** Some of IKS (jyotiṣa-as-astronomy, Āyurveda-as-medicine) maps onto empirical disciplines. Some (mantras-as-ritual, kāla-as-cosmology) does not. Distinguish carefully.
3. **The historical question.** Documented dates and authors: Pāṇini (~500 BCE, grammar), Caraka (~200 BCE, medicine), Āryabhaṭa (499 CE, astronomy), Bhāskara II (1150 CE, math). These are real scholars with verifiable corpora.

Honest framing: IKS is neither uniformly ancient nor uniformly scientific. It is a documented intellectual tradition with reform, debate, and dates.""",
        },
        'demo': {
            'primary': """**The Memory Game.** Read out 5 Sanskrit words slowly: *jala, agni, vāyu, pṛthivī, ākāśa* (water, fire, air, earth, space). Say them again. A third time. Now ask children to repeat — most will get all 5.

*"Did you know — long ago, students learned 100,000 verses this way? That\'s how the Mahābhārata survived."*""",
            'middle': """**Compare two timelines** on the board:
- Pāṇini\'s *Aṣṭādhyāyī* — grammar with ~4000 rules, c. 500 BCE
- The first European systematic grammar (Robert Lowth) — 1762 CE

Difference: ~2200 years. Discussion: *"What does this tell us about (a) the depth of Indian linguistics, (b) why Pāṇini\'s framework is still studied at MIT linguistics programs?"*""",
            'senior': """**Project Āryabhaṭa\'s sine table** (rough chart, 24 entries, c. 499 CE) and Madhava\'s infinite series for π (~1400 CE, 250 years before Leibniz).

Show the Mādhava formula:
$$\\pi = 4 \\left(1 - \\frac{1}{3} + \\frac{1}{5} - \\frac{1}{7} + \\cdots\\right)$$

Discussion: *"This is the Leibniz series, attested in Kerala 250 years before Leibniz. Why isn\'t this in your maths textbook? What does its absence tell us about the politics of mathematical history?"*""",
        },
        'source': {
            'primary': 'Tell the story of Pāṇini, the boy from Gandhāra who looked up at the stars one night and decided to write down ALL the rules of Sanskrit. *"He took 12 years. The book is called Aṣṭādhyāyī — eight chapters. People still study it today!"*',
            'middle': 'Read aloud: *"vidyā dadāti vinayaṁ vinayād yāti pātratām"* — "Learning brings humility; from humility comes worthiness." (Subhāṣita, traditional.) The traditional epistemology values intellectual humility — a useful framing for any source-checking practice.',
            'senior': 'Read aloud Āryabhaṭīya, *Gaṇitapāda* 1: *"brahmā kṛtaṁ paramaṁ rāhuṁ ca śaśinaṁ ravim..."* (the invocation), followed by Āryabhaṭa\'s heliocentric hint in *Gola-pāda* — *"the apparent westward motion of stars at the equator is due to the earth itself moving eastward."* Read alongside the matching paragraph from a 21st-c. NCERT physics textbook on Earth\'s rotation.',
        },
        'activity': {
            'primary': """**Vedic Memory Olympics.** Pair students. Each pair learns 4 Sanskrit words from one of the upavedas: e.g.,
- Āyurveda group: *vāta, pitta, kapha, prakṛti*
- Yoga group: *āsana, prāṇāyāma, dhyāna, samādhi*
- Music group: *rāga, tāla, svara, śruti*

Each pair "performs" their 4 words for the class. Repeat in chorus together. End with applause.""",
            'middle': """**Map an Upaveda.** Divide class into 4 groups (Āyurveda, Dhanurveda, Gandharvaveda, Sthāpatya). Each group has 12 minutes to:
1. Look up one famous practitioner of that field (Caraka, Suśruta, Bharata\'s Nāṭyaśāstra, Viśvakarmā tradition).
2. Find one modern-day descendant institution (AIIMS Ayurveda program, ICCR for arts, IIT-Roorkee architecture history).
3. Draw a one-page connection diagram: ancient → medieval → modern.

Each group presents 2 minutes.""",
            'senior': """**Source-criticism exercise.** Distribute 4 short paragraphs (cut from popular media articles claiming "ancient Indian science discovered X"). Pairs evaluate each:

1. Is the claim verifiable? (Author? Date? Manuscript?)
2. What is the manuscript evidence?
3. Is the modern parallel accurate, exaggerated, or invented?

Each pair classifies the 4 claims as: *real (documented)*, *partially exaggerated*, *anachronistic*, *fabricated*. Class discusses.""",
        },
        'reflection': {
            'primary': 'Each child shares ONE Sanskrit word they remembered from today\'s lesson. Round of applause for each.',
            'middle': '*"What\'s one thing about IKS you want to learn more about? Why?"* — written in 3 sentences. Pairs swap and respond.',
            'senior': '*"Distinguish three things: (1) what\'s ancient AND scientifically valid, (2) what\'s ancient AND historically interesting BUT no longer scientifically used, (3) what\'s claimed as ancient BUT is actually a modern reconstruction. Give one example of each from your prior knowledge."*',
        },
        'go_deeper_days': [
            ('day-01', 'Why IKS now? The mapping problem'),
            ('day-02', 'Vedas and Vedāṅgas: the six supporting sciences'),
            ('day-03', 'Upavedas: applied disciplines'),
            ('day-04', 'Itihāsa and Purāṇas: history-as-story'),
            ('day-05', 'Six Darśanas: the philosophical schools'),
            ('day-06', 'Named figures: Pāṇini to Āryabhaṭa'),
            ('day-07', 'Source discipline: what we can verify'),
            ('day-08', 'IKS meets modern science: bridges and tensions'),
            ('day-09', 'NEP 2020 and IKS integration'),
            ('day-10', 'Synthesis project: your map of IKS'),
        ],
    },

    'module-02-panchabhuta': {
        'title': 'Panchabhūta — The Five Elements',
        'sanskrit': 'Pañcabhūta',
        'subtitle': 'The classical Indian classification of matter',
        'hook': {
            'primary': 'Hold a glass of water. *"What can water do?"* (Flow, splash, freeze, evaporate.) Now an ice cube. *"Still water?"* (Yes — different form.) *"In India long ago, people said matter has FIVE basic forms — like five friends. Today we meet them."*',
            'middle': 'Project a candle being lit. *"What just happened? Wax (earth-like solid) → fire (heat) → air (gas, you can feel it) → space (the room\'s air carries the heat). One simple act involves four of the five elements."*',
            'senior': 'On the board: "Matter exists in solid, liquid, gas, plasma, and vacuum." Below: "The Sāṅkhya school of ~6th c. BCE Indian philosophy proposed: *pṛthvī, ap, tejas, vāyu, ākāśa* — the same five categories, derived from observation. The classification is empirical. The cosmological wrapping is philosophical."',
        },
        'core': {
            'primary': """**Meet the five friends:**
- **Pṛthvī (पृथ्वी)** — Earth. *Solid stuff.* Rocks, mountains, bones.
- **Ap (अप्)** — Water. *Liquid stuff.* Rivers, blood, juice.
- **Tejas (तेजस्)** — Fire. *Warm stuff.* Sun, candles, body warmth.
- **Vāyu (वायु)** — Air. *Moving stuff.* Wind, breath, the smell of food.
- **Ākāśa (आकाश)** — Space. *Where everything fits.* The room, the sky, the gap between hands.

Make a hand sign for each friend. Practice 3 times.""",
            'middle': """**The five elements:**

| Sanskrit | Modern parallel | Observable property |
|----------|----------------|---------------------|
| Pṛthvī (पृथ्वी) | Solid | Hardness, density |
| Ap (अप्) | Liquid | Cohesion, flow |
| Tejas (तेजस्) | Plasma / energy | Heat, light |
| Vāyu (वायु) | Gas | Mobility, expansion |
| Ākāśa (आकाश) | Vacuum / space | Containment |

**Key idea:** Sāṅkhya philosophy treats these as five categories of phenomena, not separate substances. Modern physics likewise: solid, liquid, gas, plasma, and... space (the vacuum is a thing, with Higgs field and zero-point energy).

The mapping is not perfect — but the categorisation is empirically reasonable.""",
            'senior': """**The Sāṅkhya derivation.** Sāṅkhya (Kapila, ~6th c. BCE) derives the *pañcabhūta* from the *tanmātras* (subtle qualities):

| Element | Tanmātra | Sense |
|---------|----------|-------|
| Ākāśa | śabda (sound) | hearing |
| Vāyu | sparśa (touch) | touch |
| Tejas | rūpa (form/colour) | sight |
| Ap | rasa (taste) | taste |
| Pṛthvī | gandha (smell) | smell |

**Critical pattern:** earth carries all five qualities (you can hear it, touch it, see it, taste it, smell it). Air carries only two (sound, touch). The taxonomy is a sense-perception hierarchy disguised as a matter classification.

**Modern bridge:** the five states of matter (solid, liquid, gas, plasma, vacuum/space) are observationally similar but conceptually distinct. The Sāṅkhya scheme is a *sensory taxonomy*; the modern scheme is a *thermodynamic taxonomy*. Both are valid descriptive frameworks at their level of abstraction.""",
        },
        'demo': {
            'primary': '**Element walk.** Stand in a line. The teacher names one element; children mime it:\n- Pṛthvī → stand strong like a mountain\n- Ap → wave arms like water\n- Tejas → flicker like a flame\n- Vāyu → blow softly\n- Ākāśa → spread arms wide and breathe deep\n\nRepeat 3 times, faster each time. Cheer at the end.',
            'middle': '**State-change demo.** With one ice cube, one candle flame, and one cup of water: observe ice (pṛthvī-like) → water (ap-like) → steam (vāyu-like) → diffuses (ākāśa-like). The candle flame stays *tejas*.\n\nDraw the cycle on the board. *"This is the Indian classification of matter — observable, testable, with one observation: ākāśa is what allows the transitions, the medium that everything else moves through."*',
            'senior': '**Multi-sense identification challenge.** Place 5 covered samples (rock, water, candle [unlit], a paper fan, an empty box). Pairs identify each by:\n- Sight only (lift cover briefly)\n- Touch only (with gloves to mute sense)\n- Hearing only (tap the sample, listen)\n\nDiscussion: *"Which element was easiest to identify by which sense? Map your findings to the Sāṅkhya tanmātra scheme. Does the ancient categorisation match your modern empirical experience?"*',
        },
        'source': {
            'primary': 'Tell the story of *Pañcabhūta* as five family members of Earth. *"They each have a job. Pṛthvī gives us food. Ap gives us drinks. Tejas warms us. Vāyu brings us smells and breath. Ākāśa makes room for everyone."*',
            'middle': 'Paraphrase from Śrīmad-Bhāgavatam 3.26.49: *"From the five subtle elements (tanmātras), the five gross elements (pañcabhūta) emerge — earth, water, fire, air, and space. These pervade the entire physical world."*',
            'senior': '**Direct verse (Senior).** Śrīmad-Bhāgavatam 3.26.36, with Sāṅkhya commentary:\n\n> *mṛdutvaṁ kaṭhinatvaṁ ca śaityam uṣṇatvam eva ca /*\n> *etat sparśasya sparśatvaṁ tanmātratvaṁ nabhasvataḥ //*\n\n"Softness, hardness, cold, and heat — these qualities of touch (*sparśa*) are the subtle attributes (*tanmātra*) of air (*nabhasvat*)."\n\nNote the sophistication: temperature is folded into *touch* as a quality of *vāyu*. This is consistent with classical Indian physiology, which treats temperature perception as a tactile sensation, not a separate sense.',
        },
        'activity': {
            'primary': '**Five-friends drawing.** Each child folds a paper into 5 sections. In each section, draw something for that element (sun for tejas, balloon for vāyu, river for ap, mountain for pṛthvī, sky for ākāśa). Decorate. Share.',
            'middle': '**Element census of your classroom.** Pairs walk around the room and identify ONE item for each element. List them on a worksheet. Compare with another pair. Discussion: *"Which element was hardest to find? Why?"* (Often ākāśa — students struggle to think of "empty space" as an element. That\'s the pedagogical point.)',
            'senior': '**Critical-categorisation exercise.** Each student picks one modern phenomenon (laser, magnet, sound wave, gas pressure, plasma TV screen). They argue: *"Which element of the pañcabhūta best maps onto this phenomenon? Where does the mapping break down?"*\n\nPair-share. Class discussion focuses on the boundary cases — where ancient categories help vs where they constrain.',
        },
        'reflection': {
            'primary': 'Each child names their favourite element and why. Group hug at the end (representing ākāśa connecting everyone).',
            'middle': '*"Which element is most overlooked in modern thinking? Why might ancient frameworks have foregrounded it more?"* — 3 sentences.',
            'senior': '*"Sāṅkhya organises matter by sensory access. Modern physics organises by thermodynamic state. Both are descriptive frameworks; neither is universal truth. Argue for which framework is more useful for which questions, and where each falls short."*',
        },
        'go_deeper_days': [
            ('day-01', 'Five friends — meeting the elements'),
            ('day-02', 'Earth and water — solid and liquid'),
            ('day-03', 'Five qualities, five senses (tanmātras)'),
            ('day-04', 'Fire and air — energy and motion'),
            ('day-05', 'Ākāśa — the fifth element'),
            ('day-06', 'Modern parallels — states of matter'),
            ('day-07', 'Pañcabhūta in Āyurveda — bridge to Module 4'),
            ('day-08', 'Pañcabhūta in cuisine — six tastes'),
            ('day-09', 'Pañcabhūta in nature — local examples'),
            ('day-10', 'Synthesis project: build a pañcabhūta poster'),
        ],
    },

    'module-03-ayurveda-good-health': {
        'title': 'Āyurveda and Good Health',
        'sanskrit': 'Āyurveda',
        'subtitle': 'The science of life — daily routine, diet, and well-being',
        'hook': {
            'primary': '*"What time did you wake up today? Did you eat? What did you drink? Did you move?"* Quick show-of-hands. *"Āyurveda is just a name for: noticing these things and choosing well. Today we\'ll learn the BIG rules people in India have followed for thousands of years."*',
            'middle': 'Project two side-by-side photos: (a) a modern busy office worker on a couch, (b) a person doing morning yoga at sunrise. *"Both are valid lives. But the second is closer to what Āyurveda recommends. Why?"* Brief discussion: rhythms, food, sleep, movement.',
            'senior': '*"Modern medicine is reactive — you go when something is wrong. Āyurveda is preventive — you live so that things don\'t go wrong. Today we examine the framework: dinacharya (daily routine), ahāra (diet), and tridoṣa (the three constitutional types). All as wellness lens — NOT diagnosis."*',
        },
        'core': {
            'primary': """**Four big rules from Āyurveda:**

1. **Wake with the sun.** Sunrise = wake-up bell.
2. **Eat warm meals.** Cold food shocks the tummy.
3. **Sip water through the day.** Not ice-cold.
4. **Sleep when it\'s dark.** No screens before bed.

Each rule has a Sanskrit name (write on board):
- *dinacarya* (daily routine)
- *ahāra* (food)
- *nidrā* (sleep)
- *praheli* (water — drink slow)

Sing-chant: *"Wake. Eat. Sip. Sleep."*""",
            'middle': """**Āyurveda framework, three pillars:**

1. **Dinacarya** (daily routine) — sleep, wake, food times. Aligning with sun/circadian rhythm.
2. **Ahāra** (diet) — the *ṣaḍ-rasa* (six tastes): sweet, sour, salty, pungent, bitter, astringent. Each meal should include several tastes; not just sweet.
3. **Tridoṣa** (three constitutions) — *vāta* (motion), *pitta* (transformation), *kapha* (structure). Everyone has all three; the ratio differs. **THIS IS A WELLNESS LENS, NOT DIAGNOSIS.**

Modern parallel: circadian rhythm research (Nobel 2017, Hall/Rosbash/Young) validates dinacarya logic.""",
            'senior': """**Āyurveda as Indian preventive medicine.**

1. **Dinacarya** (daily routine, codified in Aṣṭāṅga Hṛdaya, *Sūtrasthāna* 2). Sleep, wake, food, exercise, elimination — each at appropriate time. Modern: circadian biology shows ~85% of human physiology has circadian rhythm. Misalignment correlates with metabolic and cognitive impairment.

2. **Ahāra** (diet, *Sūtrasthāna* 5). The six tastes (*ṣaḍ-rasa*) — each meal should ideally include several. Sweet alone (modern diet) is the most common modern misalignment. *Ṛtucharya* (seasonal eating) — light and bitter in summer (pitta-rich), warm and oily in winter (vāta-rich).

3. **Tridoṣa** (Caraka *Sūtrasthāna* 1.57). *Prakṛti* (innate constitution) vs *vikṛti* (current state). Self-knowledge as the first step of self-care.

**CRITICAL CAVEAT, REPEATED:** this is a wellness lens, NOT a diagnostic system. For health concerns, see a doctor.""",
        },
        'demo': {
            'primary': '**Six-taste tasting.** Set out (or describe) 6 small samples — honey (sweet), lemon (sour), salt water (salty), ginger (pungent), bitter gourd skin (bitter), banana peel water (astringent). Children sniff/taste tiny amounts. Match the Sanskrit name to each taste.',
            'middle': '**24-hour clock activity.** Each student sketches their actual daily schedule (sleep, eat, school, exercise) on a circular 24-hour clock. Compare with the Āyurveda-recommended schedule. Identify 2 mismatches.',
            'senior': '**Source-text reading.** Read aloud Aṣṭāṅga Hṛdaya, *Sūtrasthāna* 2.1–5 (a brief stanza on dinacarya). Discuss: how much of this is *empirical* (testable by modern science), how much is *prescriptive* (a values judgment), how much is *symbolic* (cultural-religious framing).',
        },
        'source': {
            'primary': 'Tell the story of Caraka, the wandering physician who walked from village to village teaching people: *"Wake up when birds wake up. Eat warm food. Be kind to your body."*',
            'middle': 'Paraphrase Caraka Saṁhitā, *Sūtrasthāna* 1.41: *"The purpose of this Āyurveda is to maintain the health of the healthy and to relieve the disorders of the diseased."* The order matters — prevention first, treatment second.',
            'senior': '**Quoted verse.** Caraka Saṁhitā, *Sūtrasthāna* 1.41:\n\n> *prayojanaṁ ca asya svastha-svāsthya-rakṣaṇam āturasya vikāra-praśamanaṁ ca*\n\n"The purpose of this is the preservation of health in the healthy AND the alleviation of disorders in the diseased."\n\nNote the syntactic priority: *svastha-svāsthya-rakṣaṇam* (healthy-people\'s-health-preservation) comes FIRST. The discipline is fundamentally preventive.',
        },
        'activity': {
            'primary': '**Make a healthy day card.** Each child draws their ideal day: sunrise wake, warm breakfast, school, lunch with vegetables, play, dinner, bedtime story, sleep. Add Sanskrit labels for what they know.',
            'middle': '**Six-taste meal design.** Pairs design ONE meal that includes 4 of the 6 tastes. Use Indian ingredients. Present to class — explain which taste each ingredient brings.',
            'senior': '**One-week dinacarya self-audit.** Each student logs their actual sleep/wake/food times for ONE typical week (or recalls last week). Identify 2 misalignments with Āyurveda recommendations. Propose ONE specific change to test for 2 weeks. Honest reflection: *"What\'s preventing me from making this change?"*',
        },
        'reflection': {
            'primary': 'Each child says one Āyurveda rule they\'ll try this week. Cheer for each commitment.',
            'middle': '*"What\'s ONE thing about your daily routine you\'d change after this lesson? Why? What might get in the way?"*',
            'senior': '*"Āyurveda articulates a wellness framework. Modern medicine articulates a disease framework. Argue: which framework does our society currently OVER-prioritise? Which is UNDER-prioritised? What would balanced integration look like?"*',
        },
        'go_deeper_days': [
            ('day-01', 'What is Āyurveda? Definition + scope'),
            ('day-02', 'Tridoṣa — vāta, pitta, kapha'),
            ('day-03', 'Dinacarya — daily routine'),
            ('day-04', 'Ahāra — food + the six tastes'),
            ('day-05', 'Ṛtucarya — seasonal eating'),
            ('day-06', 'Sleep, exercise, elimination'),
            ('day-07', 'Caraka, Suśruta, Vāgbhaṭa — the three Āyurveda authors'),
            ('day-08', 'Bridge to modern science — circadian, microbiome'),
            ('day-09', 'Critical reading — Āyurveda claims vs evidence'),
            ('day-10', 'Synthesis: personal wellness plan + class share'),
        ],
    },

    'module-04-doshas': {
        'title': 'Doshas — Vāta, Pitta, Kapha',
        'sanskrit': 'Tri-doṣa',
        'subtitle': 'Three biological rhythms in Āyurvedic thought',
        'hook': {
            'primary': 'Three children — quick one, focused one, steady one. *"All three are good! Different is good!"* Tell a story of three friends, each with a different way of being in the world.',
            'middle': '*"Describe three students you know — without naming them — one sentence each, focusing on their energy and pace."* Pair-share. Most descriptions cluster around: quick, focused, steady. These are the doṣas.',
            'senior': '*"Modern personality psychology has ~6 big frameworks (Big Five, MBTI, RIASEC, etc.). Āyurveda has had ONE for ~2500 years: tridoṣa. What does that say about (a) the durability of the framework and (b) the limits of pre-modern psychology?"*',
        },
        'core': {
            'primary': """**Three friends inside everyone:**
- **Wiggle (vāta)** — quick like wind, dry, light
- **Spark (pitta)** — warm, sharp, focused
- **Cozy (kapha)** — slow, soft, steady

All three live inside us. Today\'s mood = who\'s "loudest" today. We can have a Wiggle morning and a Cozy afternoon — that\'s normal!""",
            'middle': """**Three doṣas:**

| Doṣa | Element pair | Quality | Style |
|------|-------------|---------|-------|
| Vāta | ākāśa + vāyu | mobile, dry, cold | quick, changeable |
| Pitta | tejas + ap | hot, sharp, intense | focused, transformative |
| Kapha | ap + pṛthvī | heavy, cool, stable | steady, calm |

**Critical:** *prakṛti* (innate ratio, lifelong) vs *vikṛti* (current state, fluctuates). Self-observation, NOT diagnosis. Refer health concerns to a doctor.""",
            'senior': """**Tridoṣa as biological-rhythm framework.**

1. **Vāta (motion).** Modern parallels: autonomic nervous system arousal, peristaltic + circulatory rhythms.
2. **Pitta (transformation).** Modern: metabolic rate, thermoregulation, inflammatory response.
3. **Kapha (structure).** Modern: anabolic/structural metabolism, parasympathetic dominance.

The mapping is not 1:1, but the empirical observations behind each doṣa are well-attested (Caraka *Sūtrasthāna* 12).

**Honest critique:** Tridoṣa is not a clinical-diagnostic tool by modern medical standards. It IS a useful self-observation framework. Most users err by reading it as diagnostic — that\'s a category mistake.""",
        },
        'demo': {
            'primary': 'Three friend pictures: a windy figure (Wiggle), a fiery figure (Spark), a cosy figure (Cozy). Each child picks one they feel most like today. Show your friend to a partner.',
            'middle': '**Doṣa-style observation.** Pairs swap notes for 5 minutes. Each describes the other: pace of speech, body type, sleep pattern, food preferences. Then each labels themself with the doṣa ratio that best fits.',
            'senior': '**The 30-question prakṛti survey.** Distribute the Aṣṭāṅga Hṛdaya *Sūtrasthāna* 1-derived survey. Students fill in 10 minutes. Most score as *dvi-doṣa* (mixed) — that\'s the expected result. Discussion: why is mono-doṣa rare?',
        },
        'source': {
            'primary': 'Tell the story of the three friends Wiggle, Spark, Cozy meeting a wise woman who said: *"You\'re all my favourites — different is wonderful."*',
            'middle': 'Paraphrase Caraka *Sūtrasthāna* 1.57: *"The three doṣas — vāta, pitta, kapha — are the foundation of all bodily processes."*',
            'senior': '**Quoted verse.** Caraka Saṁhitā, *Sūtrasthāna* 1.57:\n\n> *vāyuḥ pittaṁ kaphaścoktaḥ śārīro doṣa-saṅgrahaḥ*\n\n"Wind, bile, and phlegm — this is the summary of the bodily doṣas."\n\nNote: this verse does NOT say "diseases." It says "doṣas" — functional principles. Treating them AS diseases is a modern misreading. The translation "humour" or "principle" is more accurate.',
        },
        'activity': {
            'primary': 'Each child draws their three friends. Decorate. Make a class wall: three big drawings of Wiggle, Spark, Cozy; small drawings stuck around each one.',
            'middle': '**Personal doṣa-rhythm clock.** Each student marks the kapha (morning), pitta (noon), vāta (evening) hours on a 24-hour circle. Annotate when YOU feel each doṣa dominant. Share with a partner.',
            'senior': '**Doṣa critical-reading exercise.** Distribute 3 short pop-Āyurveda blog excerpts. Pairs evaluate: is the claim (a) traditional, (b) empirically testable, (c) overreach? Develop a scoring rubric together.',
        },
        'reflection': {
            'primary': 'Three-friend chant: *"Wiggle, Spark, Cozy — three friends inside!"* Repeat 3 times.',
            'middle': '*"After this workshop, what\'s ONE doṣa-aware change you might try? What might get in the way?"*',
            'senior': '*"Distinguish: where IS tridoṣa empirically defensible? Where is it culturally meaningful but empirically weak? Where would treating it as diagnosis cause harm?"* — 3 paragraphs.',
        },
        'go_deeper_days': [
            ('day-01', 'Three doṣas — introduction'),
            ('day-02', 'Vāta — the motion principle'),
            ('day-03', 'Pitta — the transformation principle'),
            ('day-04', 'Kapha — the structure principle'),
            ('day-05', 'Mapping doṣas to the five elements (Module 2)'),
            ('day-06', 'Prakṛti self-assessment'),
            ('day-07', 'Daily doṣa rhythms (kapha morning, pitta noon, vāta evening)'),
            ('day-08', 'Seasonal doṣa rhythms'),
            ('day-09', 'Balance vs imbalance (sāmya vs vaiṣamya)'),
            ('day-10', 'Synthesis + 7-day self-observation project'),
        ],
    },

    'module-05-dot-addition': {
        'title': 'Bindu Paddhati — Dot Addition',
        'sanskrit': 'Bindu Paddhati',
        'subtitle': 'A 20th-century mental-arithmetic technique for column addition',
        'hook': {
            'primary': 'Write 8 + 7 on the board. Solve traditionally. Now do it with dots: 8 dots ●●●●●●●● + 7 dots ●●●●●●● = 15 dots ●●●●●●●●●●●●●●●. *"That\'s the idea. Today we use this trick for much bigger sums."*',
            'middle': 'Show the column 9 + 8 + 7 + 6 = ?. Most students will sum top-to-bottom. *"What if there\'s a faster way? A 20th-century Indian arithmetic technique called Bindu Paddhati (dot method) gives one. Today we learn it."*',
            'senior': 'Project the problem: 47 + 38 + 26 + 91 + 53 = ? Time the class. Most: ~30-45 seconds. *"There\'s a faster method, documented in 20th-century Indian textbooks. It\'s called Bindu Paddhati. Today we learn it AND examine its honest historical claim."*',
        },
        'core': {
            'primary': """**The dot method:** when you add and get 10 or more, put a DOT next to the number above.

Example: 6 + 7 in a column.
6
7 → 6 + 7 = 13. Write 3, put a DOT.

Each dot = 10. So at the end: count dots × 10, add the remainder.

Practice: 8 + 9 in a column.""",
            'middle': """**Bindu Paddhati for column addition.**

For each column (units, tens, hundreds):
1. Add running total downwards.
2. Whenever you reach 10 or more, mark a DOT (•) next to that digit and continue with the remainder.
3. At the end of the column, write the remainder. Count the dots — that\'s your carry.

Example: 9 + 8 + 6 + 4 = ?
- 9 + 8 = 17 → mark • by 8, remainder 7
- 7 + 6 = 13 → mark • by 6, remainder 3
- 3 + 4 = 7 → final
- Total: 2 dots + 7 = 27. ✓

**Speed:** much faster than mental running-total for long columns.""",
            'senior': """**Bindu Paddhati — modern reconstruction.**

The method as taught is well-documented in 20th-century Indian mental-arithmetic primers (e.g., Bharati Krishna Tirthaji\'s *Vedic Mathematics*, 1965; later popularizations).

**Honest historical framing:**
- The DOT NOTATION as such is a modern (20th-c.) pedagogical convention.
- The PLACE-VALUE ARITHMETIC behind it is much older (Brahmi numerals, ~3rd c. BCE; place value formalised ~Āryabhaṭa, 499 CE).
- The CLAIM that this is "Vedic" is contested (S.G. Dani, *Frontline* 1993). It\'s a 20th-c. arithmetic synthesis that uses Sanskrit names.

**Method itself:** sound. **Historical claim:** modern, not ancient.

Both can be true. Use the method; teach the honest history.""",
        },
        'demo': {
            'primary': 'On the board, do 7 + 8 with the dot. Then 9 + 6. Then 8 + 4 + 5. Children call out the dots together. Cheer for each correct answer.',
            'middle': 'Live calculation race. Same column (47 + 38 + 26 + 91 + 53), two methods:\n- Traditional: ~25 seconds for most students\n- Bindu Paddhati: with practice, ~12-15 seconds\n\nClass observes the time difference.',
            'senior': '**Source comparison.** Project two passages: (a) Tirthaji 1965 description of *Bindu Paddhati*, (b) a Sanskrit excerpt claimed to be the "original" but actually a 20th-c. Sanskrit composition. Students compare: where does the documentary evidence lie? What\'s the honest dating?',
        },
        'source': {
            'primary': 'Story of an Indian teacher in the 1960s who saw children struggling with long column addition and said: *"What if we used a dot to mean ten?"* The trick spread to schools all over India.',
            'middle': 'Paraphrase Tirthaji 1965: *"The Bindu Paddhati removes the need to carry, by using a dot as a visual marker of 10."* Modern: dot-counting in computer arithmetic uses the same principle (binary carry-saving adders).',
            'senior': '**Quoted reference.** Tirthaji, *Vedic Mathematics* (1965, posthumous), in the chapter on column addition:\n\n> "The dot above the digit signifies ten. The student need not carry mentally; the dot does the carrying."\n\nReal source, real date. **Note:** Tirthaji\'s book itself is contested as "Vedic." Use the technique honestly: it\'s a 20th-c. mental-arithmetic system, not a Vedic-period text.',
        },
        'activity': {
            'primary': 'Practice worksheet: 8 column-addition problems using the dot method. Pairs check each other.',
            'middle': '**Method race.** Each student does 10 column-addition problems using Bindu Paddhati. Time themselves. Then do another 10 using traditional method. Compare times — celebrate any improvement.',
            'senior': '**Critical historical-mathematics essay.** Each student writes 200 words: *"The Bindu Paddhati is empirically useful but its claimed antiquity is unprovable. How should educators present such methods honestly? What is lost by overclaiming antiquity? What is lost by dismissing the method as not-really-ancient?"*',
        },
        'reflection': {
            'primary': 'Each child shows one problem they solved with the dot method. Round of applause.',
            'middle': '*"You now know two methods for column addition. When would you use which? Why?"*',
            'senior': '*"This module taught you a technique AND a historical critique of its claimed origin. How will you teach this honestly to a younger student?"*',
        },
        'go_deeper_days': [
            ('day-01', 'Why mental arithmetic? The setup'),
            ('day-02', 'Single-digit + single-digit with the dot'),
            ('day-03', 'Two-digit column addition'),
            ('day-04', 'Three- and four-digit columns'),
            ('day-05', 'Speed practice — Bindu Paddhati vs traditional'),
            ('day-06', 'Why it works — place value + carry'),
            ('day-07', 'Honest history — Tirthaji 1965, Dani 1993 critique'),
            ('day-08', 'Bridge to computer arithmetic — carry-save addition'),
            ('day-09', 'Mixed problem set'),
            ('day-10', 'Project — design your own mental-math poster'),
        ],
    },

    'module-06-moon-phases-tithi': {
        'title': 'Moon Phases and Tithi',
        'sanskrit': 'Candra-pakṣa, Tithi',
        'subtitle': 'The moon\'s monthly cycle and the Indian lunar calendar',
        'hook': {
            'primary': 'Show a chart of moon phases. *"Did you see the moon last night? Was it round, half, or thin? Today we learn why it changes shape!"*',
            'middle': 'Project a year-long animation of moon phases. *"~29.5 days from full moon to full moon. Indian astronomy divides this into 30 lunar days called tithis. Why 30 and not 29 or 30 sometimes? Today we find out."*',
            'senior': 'Show side-by-side: (a) NASA\'s lunar phase diagram for the current month, (b) a panchanga page for the same month. Same astronomy, two frameworks. *"How do they correspond? Where do they diverge?"*',
        },
        'core': {
            'primary': """**The moon changes shape because it goes around Earth.**

Two halves of the moon-month:
- **Śukla pakṣa** (शुक्ल पक्ष) — bright half — moon grows from tiny to full
- **Kṛṣṇa pakṣa** (कृष्ण पक्ष) — dark half — moon shrinks from full to tiny

Each day in each half has a number (tithi 1 to 15). Sing-chant the numbers.""",
            'middle': """**Moon-month framework:**

- **Synodic month:** ~29.5 days from one full moon to the next.
- **Tithi:** 1/30th of synodic month — NOT a 24-hour day. Tithi length varies (~20-26 hours).
- **Pakṣa:** half-month, 15 tithis. *Śukla* (bright/waxing) or *Kṛṣṇa* (dark/waning).
- **Pañcāṅga:** the five-limbed Indian calendar with tithi, vāra (weekday), nakṣatra, yoga, karaṇa.

**Why eclipses?** Solar eclipse only on amāvasyā (new moon). Lunar eclipse only on pūrṇimā (full moon). Both require alignment of Sun-Moon-Earth.""",
            'senior': """**Lunisolar astronomy + Indian calendar.**

1. **Synodic month** (~29.530589 days, modern measurement). Indian astronomy: same value within ~0.001 days, established by Sūrya-siddhānta and refined by Bhāskara II.

2. **Tithi computation.** True tithi = elongation of Moon-Sun angle / 12°. Varies because moon\'s orbital speed varies (Kepler\'s 2nd law).

3. **Pañcāṅga five limbs.** Tithi (lunar day), vāra (weekday), nakṣatra (27 lunar mansions), yoga (Sun-Moon longitudinal sum), karaṇa (half-tithi). Each is a precise astronomical computation.

4. **Eclipse geometry.** Why solar eclipses only at new moon: Moon must be between Sun and Earth, occurring only at conjunction. Why not every new moon: lunar orbit tilted ~5.14° from ecliptic; eclipse requires near-node passage.""",
        },
        'demo': {
            'primary': 'Use a lamp (Sun), a tennis ball (moon), and a child\'s head (Earth) — walk the moon around Earth, watching which side is lit. Children take turns being Moon.',
            'middle': 'Live computation: pick today\'s date, look up the lunar elongation (in degrees) from any pañcāṅga app. Compute the tithi by dividing by 12°. Compare with the published pañcāṅga.',
            'senior': '**Critical reading.** Compare Sūrya-siddhānta\'s tithi calculation with the modern Drik Pañcāṅga (web). Both use the same underlying astronomy. Discussion: where do they differ in conventions (sidereal vs tropical reference frames)?',
        },
        'source': {
            'primary': 'Tell the moon-grandmother story: the moon visits 30 friends each month (tithis), splitting her time between bright friends (śukla pakṣa) and shadow friends (kṛṣṇa pakṣa).',
            'middle': 'Paraphrase Sūrya-siddhānta, ch. 2: *"The tithi is the time required for the Moon to gain 12° of longitudinal separation from the Sun. There are 30 tithis in a synodic month."*',
            'senior': '**Direct verse.** Sūrya-siddhānta 2.66:\n\n> *bhāgāḥ ṣaṣṭi-guṇāḥ proktās tithayo dvi-guṇās tathā*\n\n"Sixty divisions are stated; thus the tithis are twice that (× 60 / 12 = 30)."\n\nThe verse encodes the 12°-per-tithi rule that defines the lunar day.',
        },
        'activity': {
            'primary': 'Each child draws today\'s moon and the moon for tomorrow (predicted). Compare with classmates. Send home with a prompt to observe tonight.',
            'middle': '**Build a class tithi calendar** for the current month. Each student fills in 2-3 dates with tithi, pakṣa, and one cultural festival or saint\'s day if any.',
            'senior': '**Eclipse prediction exercise.** Using a published table, identify the next 3 solar and lunar eclipses visible from your region. Predict which months / tithis. Discuss: how does ancient and modern eclipse-prediction differ in precision?',
        },
        'reflection': {
            'primary': 'Each child says one thing they learned about the moon. Cheer.',
            'middle': '*"Why does India use two calendars (lunar pañcāṅga + Gregorian solar) in daily life? What does each handle better?"*',
            'senior': '*"Indian classical astronomy achieved ~99.9% precision on synodic month calculation by ~500 CE. What does this tell us about (a) the empirical sophistication of pre-modern Indian science, (b) the limits of attempting modern claims from this evidence?"*',
        },
        'go_deeper_days': [
            ('day-01', 'The moon\'s shape — why it changes'),
            ('day-02', 'Pakṣa — bright and dark fortnights'),
            ('day-03', '15 tithis — names and computation'),
            ('day-04', 'Building a tithi calendar'),
            ('day-05', 'Lunar months and festivals'),
            ('day-06', 'Pañcāṅga — the five limbs'),
            ('day-07', 'Eclipse geometry'),
            ('day-08', 'Modern lunar science — phases, libration, tides'),
            ('day-09', 'Cross-cultural calendars — Hijri, Chinese, Hebrew'),
            ('day-10', 'Synthesis quiz + moon diary share'),
        ],
    },

    'module-07-eleven-multiplication': {
        'title': '×11 Multiplication',
        'sanskrit': 'Ekādhikena Pūrveṇa',
        'subtitle': 'Mental multiplication by 11 from 20th-century Indian arithmetic',
        'hook': {
            'primary': 'Write 23 × 11 on the board. Pause. *"Anyone solve it in 3 seconds?"* (Pause.) *"Today\'s magic trick: split the digits, add them, put the sum in middle. 23 → 2_3 → 2_(2+3)_3 → 253. Magic!"*',
            'middle': 'Show 87 × 11 mentally. Most students reach for long multiplication. *"Or — split, add, with carry. Today\'s lesson: ×11 mental method, with the carry case included."*',
            'senior': 'Project: 234 × 11 = ? Pause. *"Long multiplication takes ~30 seconds. The Vedic Mathematics method takes ~5 seconds. Today we learn the method AND examine its honest historical claim — manuscript date 1911-1918, published 1965."*',
        },
        'core': {
            'primary': """**The trick for ×11:**

For any 2-digit number, split the digits and put their sum in the middle.

24 → 2_4 → 2_(2+4)_4 → 264.
35 → 3_5 → 3_(3+5)_5 → 385.
71 → 7_1 → 7_(7+1)_1 → 781.

Chant: *"Split, add, put in middle!"*""",
            'middle': """**×11 method:**

For (10a + b) × 11 = 100a + 10(a+b) + b.

Procedure:
1. Split the 2 digits: a _ b
2. Add them: a+b
3. Put the sum in the middle: a (a+b) b

**Carry case:** if a+b ≥ 10, carry the tens digit to the first slot.
- 87 × 11 = 8_(8+7)_7 = 8_15_7 → carry: (8+1) 5 7 = 957.

**Extension:** 3-digit × 11: abc → a (a+b) (b+c) c.""",
            'senior': """**×11 mental method (Vedic Mathematics by Bharati Krishna Tirthaji, 1965).**

Algebraic identity: (10a + b)(10 + 1) = 100a + 10(a+b) + b.

**Procedure:**
1. Split 2-digit number into a and b.
2. Cross-add: a + b.
3. Place: a, (a+b), b. Carry if needed.

**Extension to 3-digit:** abc × 11 = a, (a+b), (b+c), c.

**Honest historical caveats:**
- Tirthaji\'s manuscript: 1911-1918.
- Published posthumously: 1965.
- Claimed source: a Parisistha of the Atharvaveda. **This manuscript has never been independently verified.**
- Mathematician S.G. Dani (1993) critique: the methods are 20th-century arithmetic, not Vedic.

Use the method; teach the honest history.""",
        },
        'demo': {
            'primary': 'Practice in chorus: 12 × 11, 21 × 11, 34 × 11, 56 × 11. Chant the answers together.',
            'middle': 'Live speed race: every student solves 5 problems mentally. Time it. Average ~3 seconds per problem with practice. Compare with the long-multiplication time for the same problems.',
            'senior': '**Algebra explainer + carry-case worked example.** Derive (10a + b) × 11 = 100a + 10(a+b) + b on the board with the carry rule. Then demo 99 × 11 = 1089 (the most carry-heavy case). Discuss generalization to 3-digit.',
        },
        'source': {
            'primary': 'Tell the story of a wise teacher who said: *"Numbers like games. The ×11 game has a simple rule. Today we play."*',
            'middle': 'Paraphrase Tirthaji 1965: *"Ekādhikena Pūrveṇa — \'by one more than the previous.\' The sūtra-name for the ×11 (and related) methods."*',
            'senior': '**Quoted reference.** Tirthaji, *Vedic Mathematics* (1965), Sūtra 1 — *Ekādhikena Pūrveṇa*:\n\n> "By one more than the previous one."\n\nThis is one of 16 sūtras. The phrase itself does not appear in extant Atharvaveda manuscripts. Treat as 20th-century synthesis.',
        },
        'activity': {
            'primary': 'Each child solves 5 ×11 problems on a worksheet. Pairs check. Cheer for completed worksheets.',
            'middle': '**Mental-math sprint.** Each student does 20 ×11 problems in 3 minutes. Best score wins.',
            'senior': '**Historical-method critique.** Each student writes 250 words on: *"Tirthaji\'s ×11 method works. Its claimed Vedic origin is unverified. How would you teach this honestly to (a) a curious child, (b) a sceptical adult?"*',
        },
        'reflection': {
            'primary': 'Each child says one ×11 problem they solved. Cheer for each.',
            'middle': '*"When is ×11 mental method faster than the long method? When is it slower? Why?"*',
            'senior': '*"This module taught you a technique and its honest historical context. How does separating method from origin claims serve mathematical education?"*',
        },
        'go_deeper_days': [
            ('day-01', 'The ×11 hook — what is the trick?'),
            ('day-02', 'The carry case'),
            ('day-03', 'Why it works — the algebra'),
            ('day-04', '3-digit ×11'),
            ('day-05', 'Speed day'),
            ('day-06', 'Anurūpyena extension to ×12-19'),
            ('day-07', 'Limits of the method'),
            ('day-08', 'Tirthaji 1965 and the historical claim'),
            ('day-09', 'Mixed practice'),
            ('day-10', 'Final assessment'),
        ],
    },

    'module-08-yoga': {
        'title': 'Yoga and the Body',
        'sanskrit': 'Yoga',
        'subtitle': 'Patañjali\'s eight limbs and safe āsana practice',
        'hook': {
            'primary': 'All stand. *"Reach up high! Bring hands together. Now bow slow."* *"That\'s sūrya namaskāra — a yoga sequence. Today we learn what YOGA really means in India."*',
            'middle': 'Ask: *"What do you think yoga is?"* (Likely answer: stretching.) Project Patañjali\'s definition: *"Yogaḥ citta-vṛtti-nirodhaḥ"* — Yoga is the stilling of the mind\'s fluctuations. (Yogasūtra 1.2). *"Stretching is one of EIGHT limbs of yoga. Today we map all eight."*',
            'senior': 'Project Patañjali\'s Yogasūtra (~200 BCE-200 CE). 196 sūtras. Project the Aṣṭāṅga (eight-limbs) chapter — *Sādhana-pāda*, sūtras 28-29. *"Modern global yoga = āsana + prāṇāyāma. Two of eight limbs. Today we see the full architecture."*',
        },
        'core': {
            'primary': """**Yoga is more than just stretching. It\'s a way to feel good in your body and your mind.**

Eight parts of yoga:
1. Yama — be kind to others
2. Niyama — be kind to yourself
3. Āsana — body poses
4. Prāṇāyāma — breath
5. Pratyāhāra — turn senses inward
6. Dhāraṇā — focus
7. Dhyāna — meditation
8. Samādhi — deep peace

Today: try a little of each!""",
            'middle': """**Patañjali\'s eight limbs of yoga:**

| Limb | Sanskrit | Modern translation |
|------|----------|-------------------|
| 1 | Yama | Ethical restraints (5: non-violence, truthfulness, non-stealing, sexual restraint, non-greed) |
| 2 | Niyama | Personal observances (5: purity, contentment, austerity, study, surrender) |
| 3 | Āsana | Posture |
| 4 | Prāṇāyāma | Breath regulation |
| 5 | Pratyāhāra | Withdrawal of senses |
| 6 | Dhāraṇā | Concentration |
| 7 | Dhyāna | Meditation |
| 8 | Samādhi | Absorbed awareness |

Modern yoga in the West = mostly limbs 3 + 4. The full system is much wider.""",
            'senior': """**Patañjali\'s Aṣṭāṅga Yoga — Yogasūtra (c. 200 BCE-200 CE).**

1. **Yamas** (Sūtra 2.30): *ahiṁsā, satya, asteya, brahmacarya, aparigraha*. Universal ethics.
2. **Niyamas** (Sūtra 2.32): *śauca, santoṣa, tapas, svādhyāya, īśvarapraṇidhāna*. Personal observances.
3. **Āsana** (Sūtra 2.46): *sthira-sukham āsanam* — "steady and comfortable seat." NOT primarily about flexibility.
4. **Prāṇāyāma** (Sūtra 2.49-53): breath regulation, modern parallel to autonomic-system entrainment.
5-8. **Pratyāhāra → Samādhi**: progressive meditative absorption.

**Critical:** Patañjali says āsana is "steady-comfortable seat" — for meditation. The modern flexibility-focused practice (e.g., Iyengar lineage) is a 20th-century reformation, not the original system. Honest framing matters.""",
        },
        'demo': {
            'primary': 'Lead a gentle 3-pose sequence: stand tall (tāḍāsana), bend forward (uttānāsana), stretch arms up (ūrdhva hastāsana). Each held for 3 breaths.',
            'middle': '**Eight-limb tasting.** Brief experience of each limb: 1 minute of *ahiṁsā* (mental check: anyone you\'re angry at?), 1 minute of *santoṣa* (gratitude breath), 2 minutes of *āsana* (one pose), 2 minutes of *prāṇāyāma* (alternate-nostril breathing), 1 minute of *pratyāhāra* (eyes closed), 1 minute of *dhyāna* (silent sit).',
            'senior': '**Source-text close read.** Project Yogasūtra 2.46-48 (āsana definition). Compare with Iyengar\'s *Light on Yoga* (1966) introduction. Discussion: what stayed same? What evolved?',
        },
        'source': {
            'primary': 'Tell the story of Patañjali, a wise teacher who said: *"Yoga is not just bending your body. It\'s being kind, breathing well, focusing your mind, and being at peace."*',
            'middle': 'Paraphrase Yogasūtra 1.2: *"Yogaḥ citta-vṛtti-nirodhaḥ"* — "Yoga is the stilling of the mind\'s fluctuations." The whole system is in service of mental clarity.',
            'senior': '**Direct verse.** Yogasūtra 1.2:\n\n> *yogaḥ citta-vṛtti-nirodhaḥ*\n\n"Yoga is the cessation of the modifications of the mind-stuff."\n\nThe entire eight-limb scaffolding is methodology for ONE goal: the *citta-vṛtti-nirodha*. Modern wellness-yoga has largely lost this framing.',
        },
        'activity': {
            'primary': 'Design a 3-minute "kind-yoga" sequence: one ethical commitment (yama/niyama), one pose, one breath. Each child shares.',
            'middle': '**Eight-limb personal mapping.** Each student picks ONE limb they want to practice for one week, with one daily action. Pair-share.',
            'senior': '**Compare three yoga traditions.** Pairs research one: Patañjali Yogasūtra, Bhagavad Gītā ch. 6 (Dhyāna-Yoga), and the Haṭha Yoga Pradīpikā (~15th c. CE). Compare on: scope of practice, theological framing, treatment of the body.',
        },
        'reflection': {
            'primary': 'Each child says one limb they liked. Cheer for each.',
            'middle': '*"Modern yoga focuses on āsana. What\'s lost by ignoring the other 7 limbs? What might you incorporate?"*',
            'senior': '*"Yoga has been globalised, adapted, and commercialised since ~1960. What\'s preserved? What\'s lost? What\'s added that wasn\'t in the original?"*',
        },
        'go_deeper_days': [
            ('day-01', 'Yoga in your life — what is it really?'),
            ('day-02', 'Yamas — five ethical restraints'),
            ('day-03', 'Niyamas — five personal observances'),
            ('day-04', 'Āsana — what Patañjali actually said'),
            ('day-05', 'Prāṇāyāma — breath physiology'),
            ('day-06', 'Pratyāhāra and Dhāraṇā — turning inward, focusing'),
            ('day-07', 'Dhyāna — meditation as method'),
            ('day-08', 'Samādhi — the goal'),
            ('day-09', 'Modern yoga — what changed, what stayed'),
            ('day-10', 'Personal practice plan + share'),
        ],
    },

    'module-09-subtraction-nikhilam': {
        'title': 'Subtraction by Nikhilam',
        'sanskrit': 'Nikhilaṁ Navataścaramaṁ Daśataḥ',
        'subtitle': '"All from 9, last from 10" — a complement method for subtraction',
        'hook': {
            'primary': 'Write 100 − 7 on the board. *"Quick — say the answer!"* (93.) *"What about 100 − 37?"* (Slower.) *"Today: a trick that makes 100 − ANYTHING fast."*',
            'middle': 'Project: 1000 − 437 = ? Long subtraction has many borrows. *"Or — Nikhilam: all from 9, last from 10. → 999 − 437 = 562, then +1 = 563. Today\'s lesson."*',
            'senior': 'Project: 10000 − 1547. Long subtraction takes ~30 seconds. *"Nikhilam takes ~5 seconds. Today: the method + its bridge to TWO\'S COMPLEMENT in modern computing."*',
        },
        'core': {
            'primary': """**The trick: "All from 9, last from 10"**

For 100 − 37:
- The "9 column" digit (3): 9 − 3 = 6
- The "10 column" digit (7): 10 − 7 = 3
- Answer: 63!

Chant: *"All from 9, last from 10!"*""",
            'middle': """**Nikhilam method for subtraction from powers of 10:**

For 10ⁿ − N:
1. Subtract each digit of N from 9 EXCEPT the last digit.
2. Subtract the LAST digit from 10.
3. Concatenate.

Example: 1000 − 437.
- 4 → 9 − 4 = 5
- 3 → 9 − 3 = 6
- 7 → 10 − 7 = 3
- Answer: 563.

**Algebraic identity:** 10ⁿ − N = (10ⁿ − 1) − N + 1 = "all 9s minus N, plus 1." The procedure encodes this.""",
            'senior': """**Nikhilam complement method (Tirthaji, 1965, Sūtra 2).**

For B − N (where B is 10ⁿ):
- Identity: B − N = (B − 1) − N + 1
- Procedure: "all from 9" gives (B − 1) − N digit-wise (no borrows because every digit of (B − 1) is 9)
- "+1" gives the last-digit-from-10 correction

**Modern parallel: two\'s complement in binary computing.**

To compute A − B in binary, computers don\'t have a subtraction circuit. Instead:
1. Invert (one\'s complement) every bit of B.
2. Add 1 (two\'s complement).
3. Add A.

Same identity, in base 2. **Nikhilam = two\'s complement, in base 10.** The principle is the same.

This is a genuine insight, not a forced parallel.""",
        },
        'demo': {
            'primary': 'Chorus through 5 problems: 100 − 25, 100 − 47, 100 − 89, 100 − 91, 100 − 56. Children call out the answers.',
            'middle': '**Live computation.** Compute 10000 − 4783 by both methods. Time it. Discuss why Nikhilam is faster (no borrowing cascade).',
            'senior': '**Binary bridge.** On the board, compute 9 − 5 in binary using two\'s complement. Then compute 10 − 7 in decimal using Nikhilam. Highlight: same identity, two bases.',
        },
        'source': {
            'primary': 'Tell the story: *"All from 9, last from 10!"* This little rule helps subtract big numbers fast.',
            'middle': 'Paraphrase Tirthaji 1965, Sūtra 2: *"Nikhilaṁ Navataścaramaṁ Daśataḥ — all from 9 and the last from 10. The complement method."*',
            'senior': '**Quoted reference.** Tirthaji, *Vedic Mathematics* (1965), Sūtra 2:\n\n> *Nikhilaṁ Navataścaramaṁ Daśataḥ*\n\n"All-from-nine and last-from-ten."\n\nThe sūtra name is Sanskrit. The technique it labels is the decimal complement, which is well-attested across pre-modern arithmetic traditions (Chinese, Arabic, European). Tirthaji\'s contribution: organising under Sanskrit sūtra-names.',
        },
        'activity': {
            'primary': 'Worksheet: 10 problems of (100 − X), where X is 2-digit. Pairs check. Stars for completion.',
            'middle': '**Speed race.** 20 problems mixing subtraction from 100, 1000, 10000. Each student records their time + accuracy.',
            'senior': '**Computer-subtraction explainer poster.** Each student designs a poster showing: (a) Nikhilam decimal subtraction with one example, (b) two\'s complement binary subtraction with the same number in binary. Display side-by-side.',
        },
        'reflection': {
            'primary': 'Each child does one Nikhilam problem aloud. Cheer.',
            'middle': '*"What surprised you most about the connection between Nikhilam and computers?"*',
            'senior': '*"Argue: which deserves more curriculum time — the Nikhilam method or its connection to two\'s complement computer arithmetic? Defend your answer."*',
        },
        'go_deeper_days': [
            ('day-01', 'The sūtra — all from 9, last from 10'),
            ('day-02', 'Complement to 1000'),
            ('day-03', 'Subtract from a power of 10'),
            ('day-04', 'General subtraction'),
            ('day-05', 'The algebra — why it works'),
            ('day-06', 'Bar model proof'),
            ('day-07', 'Two\'s complement in binary'),
            ('day-08', 'Speed practice'),
            ('day-09', 'Mixed practice'),
            ('day-10', 'Final assessment + computer-subtraction poster'),
        ],
    },

    'module-10-herbs-aushadhi': {
        'title': 'Herbs — Auṣadhi',
        'sanskrit': 'Auṣadhi',
        'subtitle': 'Six kitchen-and-garden healing plants',
        'hook': {
            'primary': 'Hold up tulsī, then a piece of ginger, then turmeric. *"What do these have in common?"* (They\'re plants. They\'re in your kitchen. They help you when you\'re a bit unwell.) *"Today: meet six healer-plants of India."*',
            'middle': 'Pass around small samples of tulsī, neem, turmeric, ginger, ajwain, mint. *"Sniff each one. Which has the sharpest smell? What\'s in your kitchen? Today: six plants of Āyurveda, with traditional uses AND modern active compounds."*',
            'senior': 'Project Caraka Saṁhitā, *Sūtrasthāna* 1: *"There is no plant in the world that is not medicine."* Pair with a modern phytochemistry paper title from *Journal of Ethnopharmacology*. *"Today: six well-studied Āyurveda herbs with their traditional uses, modern active compounds, AND honest safety warnings."*',
        },
        'core': {
            'primary': """**Six healer-plants of India:**

1. **Tulsī (तुलसी)** — holy basil — for colds
2. **Nimba (निम्ब)** — neem — bitter, for skin
3. **Haridrā (हरिद्रा)** — turmeric — golden, for wounds
4. **Ārdraka (आर्द्रक)** — ginger — warm, for tummy
5. **Yavānī (यवानी)** — ajwain — for digestion
6. **Pudīnā (पुदीना)** — mint — cool, for breath

Always check with a grown-up before using any plant as medicine.""",
            'middle': """**Six common Āyurveda herbs:**

| Sanskrit | Common name | Active compound | Use |
|----------|-------------|-----------------|-----|
| Tulasī | Holy basil | Eugenol | Colds, immunity |
| Nimba | Neem | Azadirachtin | Skin (external) |
| Haridrā | Turmeric | Curcumin | Anti-inflammatory |
| Ārdraka | Ginger | Gingerol | Digestion, nausea |
| Yavānī | Ajwain | Thymol | Digestion |
| Pudīnā | Mint | Menthol | Coolant, freshness |

**Safety:** kitchen amounts (cooking) are safe for most. Therapeutic doses require a qualified practitioner. Neem oil orally has documented hepatotoxicity at high doses — NEVER ingest neem oil.""",
            'senior': """**Six Āyurveda herbs — traditional uses + modern pharmacology + safety.**

| Sanskrit | Species | Active compound | Modern evidence |
|----------|---------|-----------------|-----------------|
| Tulasī | *Ocimum tenuiflorum* | Eugenol | Adaptogenic claims partially supported; clinical evidence moderate |
| Nimba | *Azadirachta indica* | Azadirachtin | Strong antimicrobial; HEPATOTOXIC at high oral doses |
| Haridrā | *Curcuma longa* | Curcumin | Anti-inflammatory supported; bioavailability poor without piperine |
| Ārdraka | *Zingiber officinale* | Gingerol | Anti-nausea well-supported (clinical trials) |
| Yavānī | *Trachyspermum ammi* | Thymol | Carminative effect; thymol antimicrobial |
| Pudīnā | *Mentha* spp. | Menthol | Mild GI relaxant; topical analgesic |

**Critical safety:** therapeutic dosing belongs to qualified practitioners. Self-prescription based on Sanskrit names alone is dangerous. **Always consult a doctor.**""",
        },
        'demo': {
            'primary': '**Smell-test parade.** Each child smells each of 6 samples (covered, blind). Try to identify. Reveal. Cheer.',
            'middle': '**Two-herb deep dive.** Pair students — each pair takes one herb (rotation through the 6). 5 minutes to identify: leaf, smell, active compound, one traditional use. Quick presentation.',
            'senior': '**Source comparison.** Distribute one page of Caraka *Sūtrasthāna* 1 (on herbs) + one abstract of a modern phytochemistry review for turmeric/curcumin. Compare: claims, evidence, framing. Where do they agree? Diverge?',
        },
        'source': {
            'primary': 'Tell the story of the wise plant-finder of Bharat who tasted plants for centuries and wrote down which ones helped: *"This one for colds. This one for tummy. This one for the skin."*',
            'middle': 'Paraphrase Atharva Veda 8.7.4: *"The herbs grew before the heavens, three ages before the gods."* (A poetic way of saying plants long predate human medicine.)',
            'senior': '**Direct verse.** Atharva Veda 8.7.4:\n\n> *yā oṣadhīr pūrvā jātā devebhyas tri-yugaṁ purā*\n\n"The herbs that were born before the gods, by three ages."\n\nThe verse establishes the antiquity-claim for herbal medicine in the Indian tradition. Modern: phylogenetic evidence supports that flowering plants predate human evolution by ~100 million years. The poetic claim has empirical resonance.',
        },
        'activity': {
            'primary': '**Herb-friend deck.** Each child draws one herb on a card with its name. Combine into a class deck. Take home for a parent show.',
            'middle': '**Six-herb identification deck.** Each pair builds a deck: 6 cards, each with the plant, Sanskrit name, active compound, one traditional use, one safety warning.',
            'senior': '**Critical-pharmacology project pitch.** Each student picks ONE of the 6 herbs and proposes a 1-page research summary: traditional use, active compound, modern clinical evidence (or absence), safety profile. Pitch to class for critique.',
        },
        'reflection': {
            'primary': 'Each child says one herb they\'ll remember. Cheer.',
            'middle': '*"Which herb surprised you most? Why?"*',
            'senior': '*"What\'s the right way to teach Āyurveda herbs in modern schools? Where\'s the line between cultural literacy and medical recommendation?"*',
        },
        'go_deeper_days': [
            ('day-01', 'What is auṣadhi?'),
            ('day-02', 'Tulsī — holy basil'),
            ('day-03', 'Neem — bitter healer'),
            ('day-04', 'Turmeric — golden root'),
            ('day-05', 'Ginger — warming root'),
            ('day-06', 'Ajwain — carom seed'),
            ('day-07', 'Mint — cooling leaf'),
            ('day-08', 'Herbs and the doṣas (link to Module 4)'),
            ('day-09', 'Build the class herb deck'),
            ('day-10', 'Final share + assessment'),
        ],
    },

    'module-11-multiplication-near-base': {
        'title': 'Multiplication Near a Power of 10',
        'sanskrit': 'Nikhilam',
        'subtitle': 'Fast multiplication when numbers are near 10, 100, or 1000',
        'hook': {
            'primary': 'Write 9 × 8 on the board. *"Quick answer? 72."* Now write 99 × 98. *"That\'s harder. Today: a trick."*',
            'middle': 'Project 97 × 96 = ? *"Hard to do in your head — usually. But there\'s a trick: cross-subtract and multiply deficits. 97 × 96 = 9312. Today\'s method: Nikhilam for multiplication."*',
            'senior': 'Project 998 × 997 = ? *"Long multiplication takes ~60 seconds. Nikhilam takes ~5 seconds. Today: the method, the algebra, and when (NOT) to use it."*',
        },
        'core': {
            'primary': """**For numbers JUST BELOW 100, use this trick:**

99 × 98:
- 99 is 100 − 1 (deficit 1)
- 98 is 100 − 2 (deficit 2)
- Cross-subtract: 99 − 2 = 97. (Same as 98 − 1 = 97.)
- Multiply deficits: 1 × 2 = 2.
- Answer: 9702!

Chant: *"Cross-subtract, multiply deficits!"*""",
            'middle': """**Nikhilam multiplication for numbers near a power of 10:**

For (B − a)(B − b), where B is a power of 10:
1. Compute deficits: a, b.
2. Cross-subtract: (B − a) − b OR (B − b) − a (same answer).
3. Multiply deficits: a × b.
4. Result: [cross-subtract] [multiply], with appropriate padding.

Example: 97 × 96.
- Deficits: 3, 4.
- Cross-subtract: 97 − 4 = 93. Or 96 − 3 = 93.
- Multiply deficits: 3 × 4 = 12.
- Answer: 9312.

**Numbers above base:** 103 × 104 — excesses 3, 4; cross-add → 107; multiply → 12; answer 10712.""",
            'senior': """**Nikhilam multiplication — the algebra.**

Identity: (B − a)(B − b) = B² − B(a + b) + ab = B[B − (a + b)] + ab = B[(B − a) − b] + ab.

So:
- Cross-subtract = (B − a) − b OR (B − b) − a (both give B − a − b)
- Multiply = ab

Padding: the "multiply" part must have as many digits as the base has zeros (e.g., for B = 100, pad to 2 digits).

**Algebraic derivation FOR THE STUDENT** (don\'t just give them the rule):
(100 − 3)(100 − 4) = 10000 − 400 − 300 + 12 = 10000 − 700 + 12 = 9300 + 12 = 9312.

**When it\'s faster:** both factors WITHIN 5-10% of the same base.
**When it\'s slower:** factors far from any base.""",
        },
        'demo': {
            'primary': 'Practice in chorus: 9 × 8, 8 × 7, 7 × 6 (single digit deficits from 10). Then 99 × 98, 98 × 97 (deficits from 100).',
            'middle': 'Live speed: 5 problems near 100 (e.g., 96 × 93, 88 × 89). Each student solves mentally. Time it.',
            'senior': '**Algebra-on-the-board demo + edge cases.** Derive identity. Then demo: 999 × 998 (deficits 1, 2 → 997 | 002 → 997002). Then show a mixed case: 102 × 98 (excess + deficit → cross-subtract → 100, multiply 2 × 2 = 4 → answer 9996, but pad: 102 × 98 = 100² − 4 = 9996). Discuss.',
        },
        'source': {
            'primary': 'Tell the story of an old number-trick from India that lets you multiply BIG numbers if they are close to 100.',
            'middle': 'Paraphrase Tirthaji 1965, Sūtra 2 (same as Module 9, applied to multiplication): *"Nikhilaṁ — all from 9, last from 10 — gives the deficits, which then drive the multiplication."*',
            'senior': '**Quoted reference.** Tirthaji, *Vedic Mathematics* (1965), Sūtra 2 application to multiplication:\n\n> "When two numbers are both close to the same power of 10, use the deficits (or excesses) to compute the product."\n\nSūtra 2 (*Nikhilam*) is used for BOTH subtraction (Module 9) and multiplication (this module). Same algebra, two applications.',
        },
        'activity': {
            'primary': 'Worksheet: 8 problems of NN × NN where both numbers are 91-99. Pairs check.',
            'middle': '**Mental-math sprint.** 15 problems of near-100 multiplication. Each student records time + accuracy. Pair-share strategies.',
            'senior': '**Decision-tree poster.** Each student designs a one-page flowchart: *"Given a multiplication problem, which method do I use? Long, ×11, Nikhilam, near-base Nikhilam, or other?"* Defend the boundaries.',
        },
        'reflection': {
            'primary': 'Each child does one near-100 problem aloud. Cheer.',
            'middle': '*"For what % of multiplication problems would Nikhilam help? When does it NOT help?"*',
            'senior': '*"This module taught a special-case mental method. What\'s the right balance in a curriculum between general algorithms and special-case tricks?"*',
        },
        'go_deeper_days': [
            ('day-01', 'Finger-trick prelude'),
            ('day-02', '97 × 96 — two below base'),
            ('day-03', '103 × 104 — two above base'),
            ('day-04', 'Mixed cases'),
            ('day-05', '3-digit near 1000'),
            ('day-06', 'Algebra proof'),
            ('day-07', 'When to use'),
            ('day-08', 'Speed sprints'),
            ('day-09', 'Mixed practice — combining ×11 and Nikhilam'),
            ('day-10', 'Final assessment'),
        ],
    },

    'module-12-movement-of-sun': {
        'title': 'Movement of the Sun',
        'sanskrit': 'Sūrya-gati',
        'subtitle': 'Solar year, solstices, equinoxes, and the 12 rāśis',
        'hook': {
            'primary': '*"Where did the sun rise today? Where will it set?"* Point. *"Did you know the sunrise direction CHANGES through the year? Today we learn why."*',
            'middle': 'Project a sunrise-direction composite (12 photos, one per month, same location). *"The sunrise drifts north and south through the year. Why?"* (Earth\'s axial tilt.) *"Today: the Indian framework — uttarāyaṇa, dakṣiṇāyana, and the 12 rāśis."*',
            'senior': 'Project: (a) Earth\'s axial tilt diagram, (b) the 12 rāśis (sidereal zodiac), (c) the modern tropical zodiac. *"Three frameworks, two ancient and one modern. They drift apart over millennia. Today: why."*',
        },
        'core': {
            'primary': """**The Sun moves on a big yearly path:**

- **Uttarāyaṇa (उत्तरायण)** — northward course — Dec to June — days get longer
- **Dakṣiṇāyana (दक्षिणायन)** — southward course — June to Dec — days get shorter

Two special days:
- **Solstice** — sun is at its farthest north (June) or south (Dec)
- **Equinox** — day = night (March 21, Sept 22)

12 zodiac signs (rāśis) for 12 months: chant them — Meṣa, Vṛṣabha, Mithuna, Karkaṭa, Siṁha, Kanyā, Tulā, Vṛścika, Dhanus, Makara, Kumbha, Mīna.""",
            'middle': """**The Sun\'s annual journey:**

1. **Axial tilt** (23.5°) → Sun\'s apparent path drifts north/south.
2. **Uttarāyaṇa** (Dec 21 → June 21): Sun rises further north each day.
3. **Dakṣiṇāyana** (June 21 → Dec 21): Sun rises further south each day.
4. **Solstices:** June 21 (Sun farthest north), Dec 21 (farthest south).
5. **Equinoxes:** March 21, Sept 22 (Sun crosses the equator, day = night everywhere).
6. **12 rāśis:** the ecliptic divided into 12 × 30° segments. Sun travels through ~1 rāśi per month.
7. **Saṅkrānti:** the day Sun moves from one rāśi to the next. Makara Saṅkrānti (Sun enters Capricorn) ~ Jan 14.""",
            'senior': """**Earth-Sun astronomy + Indian framework.**

1. **Earth\'s axial tilt** (~23.4°) → annual variation of Sun\'s declination → seasons.
2. **Uttarāyaṇa** in Indian tradition: starts at Dec solstice (modern view) OR Makara Saṅkrānti (~Jan 14, traditional view). The ~24-day gap is the *ayanāṁśa* — the precession-of-equinoxes difference between sāyana (tropical) and nirayana (sidereal) reference frames.

3. **Precession:** Earth\'s axis wobbles with ~26,000-year period. Discovered ~130 BCE by Hipparchus. Independently computed by Indian astronomers (Bhāskara II, ~1150 CE). Today\'s *ayanāṁśa* ~24°.

4. **12 rāśis** — sidereal zodiac, anchored to fixed stars. Tropical zodiac anchored to equinox. Drift apart by ~1° per 72 years.

**Honest framing:** the Indian framework (sidereal) and modern Western framework (tropical) are both valid astronomical conventions. They serve different purposes (Indian tradition: long-term star-anchored; modern: season-anchored).""",
        },
        'demo': {
            'primary': 'In a sunny window: mark today\'s sunrise direction. Compare with a marked sunrise direction from 3 months ago (or imagine). Show the chant: *"Uttarāyaṇa! Dakṣiṇāyana!"*',
            'middle': 'Globe + torch demo: tilt the globe, walk torch around. Show how axial tilt creates seasons. Compute today\'s ayanāṁśa (use a panchanga app).',
            'senior': '**Sidereal vs tropical comparison.** Use a sky-map app (Stellarium). Show where the Sun ACTUALLY is on March 21 vs where the tropical zodiac says Aries begins. Quantify the gap.',
        },
        'source': {
            'primary': 'Tell the story of how the Sun visits 12 houses (rāśis) each year, taking one month at each — like a friend visiting 12 cousins.',
            'middle': 'Paraphrase Sūrya-siddhānta, ch. 14: *"The Sun travels along the ecliptic. In one year it completes one revolution through the 12 rāśis."*',
            'senior': '**Direct verse.** Sūrya-siddhānta 14.1:\n\n> *bhānor varṣa-gatiḥ rāśi-dvādaśakaṁ kālaḥ sāyanam*\n\n"The Sun\'s annual motion is twelve rāśis — this is the sāyana (with-ayana) year."\n\nNote the technical precision: *sāyana* specifies the reference frame. Indian astronomy distinguished sidereal and tropical conventions explicitly.',
        },
        'activity': {
            'primary': 'Each child marks 4 special days on a year-circle (Mar 21, Jun 21, Sep 22, Dec 21) and labels them. Decorate.',
            'middle': '**Personal solar calendar.** Mark current month, ayanāṁśa, current rāśi, next saṅkrānti. Predict your birthday\'s rāśi (use a panchanga). Compare with classmates.',
            'senior': '**Precession project pitch.** Each student researches one named historical observation of precession (Hipparchus 130 BCE, Bhāskara II 1150 CE, Newton 1687). Present: who? where? what did they observe?',
        },
        'reflection': {
            'primary': 'Each child says one thing they learned about the Sun. Cheer.',
            'middle': '*"Why does Makara Saṅkrānti (Jan 14) not match the December solstice exactly? What does the gap tell us?"*',
            'senior': '*"Which is more useful in modern times — sāyana or nirayana? For which purpose? Defend with evidence."*',
        },
        'go_deeper_days': [
            ('day-01', 'Sun\'s yearly path'),
            ('day-02', 'Axial tilt and seasons'),
            ('day-03', 'Uttarāyaṇa and Dakṣiṇāyana'),
            ('day-04', 'Equinoxes — viṣuva'),
            ('day-05', '12 rāśis'),
            ('day-06', 'Saṅkrānti moments'),
            ('day-07', 'Sāyana vs nirayana — the ayanāṁśa'),
            ('day-08', 'Precession of equinoxes'),
            ('day-09', 'Cross-cultural calendars — solar systems'),
            ('day-10', 'Final share + personal calendar'),
        ],
    },

    'module-13-indic-ecology': {
        'title': 'Indic Ecology — Vasudhaiva Kuṭumbakam',
        'sanskrit': 'Vasudhaiva Kuṭumbakam',
        'subtitle': '"The world is one family" — Indian ecological frameworks',
        'hook': {
            'primary': 'Show a picture of Earth from space. *"Look. One Earth. One family. Today: an old Sanskrit phrase that says exactly this."*',
            'middle': 'Project the verse: *"vasudhaiva kuṭumbakam"* — *"the Earth itself is one family."* (Mahā Upaniṣad 6.71-73.) *"This is the framework. Today we look at the practices — sacred groves, yajña, ahiṁsā — that came from it."*',
            'senior': 'Project: (a) Mahā Upaniṣad 6.71-73, (b) IPCC AR6 climate-emergency declaration. *"2500 years separate them, yet they ask the same questions: how do humans relate to the non-human? Today\'s workshop reads classical Indian ecology against modern climate ethics."*',
        },
        'core': {
            'primary': """**The Earth is one family.**

Old wisdom from India:
- **Vasudhaiva Kuṭumbakam (वसुधैव कुटुम्बकम्)** — "the Earth is one family"
- All people, animals, plants, mountains, rivers — one family.

Old practices:
- **Sacred groves** — small forests where people don\'t cut trees
- **Rivers worshipped** — Ganga, Yamuna, Saraswati
- **Yajña (यज्ञ)** — give back what you take

Today: small acts to care for our family.""",
            'middle': """**Indic ecology framework:**

1. **Vasudhaiva Kuṭumbakam** (Mahā Upaniṣad 6.71-73): the Earth is one family. Universal moral inclusion.

2. **Sacred groves (devarakāḍu, sarpa-kāvu):** community-protected forests, ~13,000 documented across India. Biodiversity hotspots, water-table protection.

3. **Yajña (Bhagavad Gītā 3.10-14):** the ecological cycle — every taking is part of a give-and-take with the larger system.

4. **Ahiṁsā:** non-harming, extended to non-human life.

5. **Five elements (pañcabhūta):** ecological substrate — air, water, fire, earth, space. Pollution = imbalance.

**Climate context:** these are frameworks. Practice was uneven. Don\'t romanticise.""",
            'senior': """**Indic ecology — frameworks and the climate present.**

1. **Vasudhaiva Kuṭumbakam** (Mahā Upaniṣad 6.71-73). Origin verse for "Earth as family" framing. Used today in Indian foreign policy, environmental rhetoric.

2. **Atharva Veda Pṛthivī Sūkta (12.1):** 63-verse hymn to Earth as goddess and substrate. Read alongside Lovelock\'s Gaia hypothesis (1979).

3. **Iṣopaniṣad 1:** *īśāvāsyam idaṁ sarvam* — "all this is to be inhabited by the divine." Foundational sustainability ethic.

4. **Bhagavad Gītā 3.10-14:** yajña cycle. Modern parallel: ecological reciprocity in indigenous-knowledge frameworks (Robin Wall Kimmerer, *Braiding Sweetgrass*).

5. **Sacred groves:** ~13,000 in India (Gadgil & Vartak 1981). Biodiversity = species/area significantly higher than non-protected.

**Honest framing:** ancient practice was imperfect. Soil erosion, hunting pressures, caste-restricted access existed. Use the FRAMEWORKS to inspire modern practice; don\'t mythologise pre-modern practice.""",
        },
        'demo': {
            'primary': 'Each child draws "one family of Earth" — themselves, their family, one animal, one plant, one river. Decorate.',
            'middle': '**Local sacred-grove research.** Pairs research one named sacred grove (e.g., Mawphlang in Meghalaya, Sarguja in Chhattisgarh, Karnataka coast devarakāḍu). 5 minutes. Quick presentation.',
            'senior': '**Source-critical reading.** Project (a) Mahā Upaniṣad 6.71-73, (b) IPCC AR6 SPM excerpt. Pairs identify: where do the ethical claims overlap? Where do they diverge? Where does one fill a gap the other has?',
        },
        'source': {
            'primary': 'Tell the story of an old wise woman who looked at the Earth and said: *"vasudhaiva kuṭumbakam"* — "the Earth is our family."',
            'middle': 'Paraphrase Mahā Upaniṣad 6.71-73: *"The narrow-minded ask \'is this mine or yours?\' For the noble-minded, the whole Earth is one family."*',
            'senior': '**Direct verse.** Mahā Upaniṣad 6.71-73:\n\n> *ayaṁ nijaḥ paro veti gaṇanā laghu-cetasām /*\n> *udāra-caritānāṁ tu vasudhaiva kuṭumbakam //*\n\n"The reckoning of \'this is mine, that is another\'s\' belongs to the narrow-minded. To the noble-hearted, the Earth itself is one family."\n\nNote: NOT "all humans" — *vasudhā* (Earth) includes all life, all elements. The moral scope is the entire biosphere.',
        },
        'activity': {
            'primary': 'Class decision: ONE small action together this week (water saving, no plastic, tree care). Each child commits.',
            'middle': '**Local environmental project pitch.** Pairs design one local environmental action: tree planting, river cleanup, school waste reduction. Present.',
            'senior': '**Climate-ethics essay.** Each student writes 400 words: *"Indic ecology and modern climate ethics both ask: how should humans treat the non-human? Compare ONE specific principle from each tradition. Where do they agree? Diverge?"*',
        },
        'reflection': {
            'primary': 'Each child commits one small Earth-care action for this week. Cheer.',
            'middle': '*"Which Indic framework most surprises you? Which would you adapt to your daily life?"*',
            'senior': '*"India is the world\'s 3rd-largest CO2 emitter (2024). Its tradition includes vasudhaiva kuṭumbakam. Discuss the gap. What\'s needed to close it?"*',
        },
        'go_deeper_days': [
            ('day-01', 'Vasudhaiva kuṭumbakam — the founding verse'),
            ('day-02', 'Five elements as ecological frame'),
            ('day-03', 'Rivers as sacred'),
            ('day-04', 'Sacred groves'),
            ('day-05', 'Yajña cycle — Gītā 3.10-14'),
            ('day-06', 'Pṛthivī Sūkta — Atharva Veda 12.1'),
            ('day-07', 'Iṣopaniṣad mantra 1'),
            ('day-08', 'Climate change context'),
            ('day-09', 'From ancient to action'),
            ('day-10', 'Project pitch + assessment'),
        ],
    },

    'module-14-magic-squares': {
        'title': 'Magic Squares — Bhadragaṇita',
        'sanskrit': 'Bhadragaṇita',
        'subtitle': 'Nārāyaṇa Paṇḍita\'s 1356 CE magic-square algorithms',
        'hook': {
            'primary': 'Show a 3×3 grid with numbers 1-9. *"All rows, all columns, both diagonals add to 15! Magic!"*',
            'middle': 'Challenge: place 1-9 in a 3×3 grid so every row/column/diagonal sums to 15. Pause for tries. Reveal the answer. *"This is a magic square. Today: how to make one for ANY odd size."*',
            'senior': 'Project the Khajuraho 4×4 magic square (~10th c. CE) and Dürer\'s Melencolia I 4×4 (1514). *"Same combinatorial object. Today: Nārāyaṇa Paṇḍita\'s 1356 CE algorithm — most rigorous pre-modern treatment of magic squares."*',
        },
        'core': {
            'primary': """**A magic square: numbers in a grid where rows, columns, diagonals all add to the same.**

The 3×3 with 1-9:
```
2 7 6
9 5 1
4 3 8
```
All rows = 15. All columns = 15. Diagonals too!

The middle number is ALWAYS 5. (Try shifting numbers around.)""",
            'middle': """**Magic squares:**

For an n × n square using 1 to n²:
- Magic constant M = n(n² + 1) / 2.
- 3 × 3 with 1-9: M = 15.
- 4 × 4 with 1-16: M = 34.
- 5 × 5 with 1-25: M = 65.

**Stair-step method (odd n):**
1. Place 1 in the top-middle.
2. From any cell, move up-right (wrap if off-grid).
3. If cell is occupied, move down instead.

Nārāyaṇa Paṇḍita\'s *Gaṇita-kaumudī* (1356 CE) systematised this for any odd n.""",
            'senior': """**Magic squares — combinatorics + history.**

**Algebra:**
- Magic constant M = n(n² + 1) / 2.
- For n = 3: 15. For n = 4: 34. For n = 5: 65.
- Number of essentially distinct 3 × 3 magic squares (using 1-9, up to symmetry): EXACTLY 1.
- 4 × 4: 880 (Frenicle de Bessy, 1693).
- 5 × 5: 275,305,224.

**Nārāyaṇa Paṇḍita\'s 1356 stair-step algorithm:**
- Place 1 in top-middle (or any specified start).
- Move up-right; wrap with toroidal topology.
- If destination occupied, move down instead.

**Honest historical framing:**
- Lo Shu (China, ~9th c. BCE): earliest known 3 × 3 magic square.
- Khajuraho (~10th c. CE): pan-diagonal 4 × 4 — sophisticated combinatorial property.
- Gaṇita-kaumudī (1356 CE): rigorous algorithmic treatment.
- Dürer (1514): European 4 × 4.

The mathematics is universal; the algorithmic systematisation by Nārāyaṇa is a genuine contribution to combinatorics.""",
        },
        'demo': {
            'primary': 'Show the 3 × 3 magic square. Children find the rows that add to 15, the columns, the diagonals. Cheer for each find.',
            'middle': '**Build a 5 × 5 using stair-step.** Live on board: place 1 top-middle. Move up-right. Wrap if needed. Build through 25. Verify M = 65.',
            'senior': '**Compare three magic squares.** Khajuraho (4 × 4, pan-diagonal), Dürer (4 × 4, "ordinary"), and a stair-step 5 × 5. Identify what makes Khajuraho special.',
        },
        'source': {
            'primary': 'Tell the story of Nārāyaṇa Paṇḍita, who in 1356 wrote a book full of number puzzles, called *Gaṇita-kaumudī* — "Moonlight of Numbers."',
            'middle': 'Paraphrase Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī* (1356 CE), ch. 14 *Bhadragaṇita*: *"For any odd n, place 1 in the top-middle; move up-right; if the cell is occupied, move down. Continue until n² is placed."*',
            'senior': '**Quoted reference.** Nārāyaṇa Paṇḍita, *Gaṇita-kaumudī* (1356 CE), *Bhadragaṇita* chapter. The treatise systematises magic-square construction for any odd order. Translated and analysed by Kim Plofker in *Mathematics in India* (2009). Predates the most rigorous European treatments (Stifel 1544, Fermat 1640) by ~200 years.',
        },
        'activity': {
            'primary': '**Decorate the 3 × 3 magic square.** Each child draws the square with colours, frames, and animals around the numbers.',
            'middle': '**Build YOUR 5 × 5.** Using stair-step. Verify M = 65. Pair-check.',
            'senior': '**Pan-diagonal 4 × 4 challenge.** Construct a 4 × 4 magic square where ALL diagonals (including "broken" diagonals that wrap around) sum to 34. (Hint: the Khajuraho square is one such.) Time it.',
        },
        'reflection': {
            'primary': 'Each child shows their decorated 3 × 3. Cheer.',
            'middle': '*"What makes a magic square \'magic\'? What\'s the math behind it?"*',
            'senior': '*"Nārāyaṇa\'s 1356 work predates Stifel by ~200 years. Why is it absent from most Western histories of mathematics? Discuss the politics of mathematical historiography."*',
        },
        'go_deeper_days': [
            ('day-01', 'Discover the 3 × 3'),
            ('day-02', 'Magic constant'),
            ('day-03', 'How many 3 × 3 magic squares?'),
            ('day-04', 'Stair-step method'),
            ('day-05', 'Practice — 5 × 5 and 7 × 7'),
            ('day-06', '4 × 4 and the Khajuraho square'),
            ('day-07', 'Historical context — Nārāyaṇa Paṇḍita'),
            ('day-08', 'Cross-cultural — Lo Shu, Dürer, Indian'),
            ('day-09', 'Design your own magic square'),
            ('day-10', 'Final share + assessment'),
        ],
    },

    'module-15-project-implementation': {
        'title': 'Project Implementation — Capstone',
        'sanskrit': 'Pañcagavya (and other capstones)',
        'subtitle': '10-day applied project drawing on Modules 1-14',
        'hook': {
            'primary': 'Show the 14 module pictures. *"You\'ve learned 14 things! Today: pick ONE and make a project!"*',
            'middle': 'Show the 10-option capstone menu. *"You\'ve learned the frameworks. Today: pick ONE and apply it. The capstone is your work."*',
            'senior': 'Project: "Knowledge without application is incomplete." *"You\'ve seen 14 modules. The capstone asks: where will you take this beyond the classroom? Today: project menu, scoping, and the safety floor."*',
        },
        'core': {
            'primary': """**You can make a project!**

Pick from this menu:
1. Make a 5-element collage (Module 2)
2. Build a doṣa-friend deck (Module 4)
3. Make a herb-friend deck (Module 10)
4. Draw a moon calendar (Module 6)
5. Build a sun calendar (Module 12)
6. Make a magic-square decoration (Module 14)
7. Design a kind-yoga sequence (Module 8)
8. Plant a tree (Module 13)

Or invent your own from a module you loved!""",
            'middle': """**Capstone menu (pick one):**

1. **Doṣa self-observation week** (Module 4) — track your sleep/food/mood for 7 days
2. **Herb identification deck** (Module 10) — 6 cards with Sanskrit, common name, active compound, use, safety
3. **Tithi/festival calendar** (Module 6) — current month\'s lunar calendar with festivals
4. **Sun-path tracker** (Module 12) — sunrise direction for 5 days, mapped on a year-circle
5. **Magic-square art** (Module 14) — design + decorate a 4 × 4 or 5 × 5
6. **Yoga sequence design** (Module 8) — 10-min sequence with limbs 1-4 mapped
7. **Sustainability audit of school** (Module 13) — water, waste, biodiversity
8. **Mental-math toolkit** (Modules 5, 7, 9, 11) — one-page reference card
9. **Pañcabhūta cuisine** (Module 2 + 3) — design a meal touching all 5 elements / 6 tastes
10. **Pañcagavya kitchen-science** — SAFE substitute: fermented foods (curd, paneer, batter) — NOT cow-urine ingestion.

**Safety floor:** food projects use familiar safe ingredients. Yoga avoids extreme poses. Outdoor projects require supervision.""",
            'senior': """**Capstone menu — 10 options + 1 open-design:**

1-9 as above. Plus:
- **Critical-history essay** (any module) — 1000 words on the honest dating + historiography of one IKS claim.
- **Open-design** — propose your own project that draws on at least 2 modules. Pitch to teacher for approval.

**Project requirements:**
- Daily journal (10 days, minimum 100 words/day)
- Source citations (minimum 5 sources, verifiable)
- Reflection (500 words at end: what you did, what worked, what you\'d change)
- Class presentation (5 minutes)

**Safety floor (repeated):**
- NO cow-urine ingestion for pañcagavya — use fermented-foods comparative study
- NO unsupervised herbal medicine experiments
- NO extreme yoga poses without instructor

**Assessment:** teacher rubric (60%) + self-assessment (20%) + peer feedback (20%).""",
        },
        'demo': {
            'primary': 'Show 3 sample projects (previous classes\' work, if any, or teacher mock-ups). Children pick their favourite to inspire.',
            'middle': 'Walk through one project end-to-end: e.g., "doṣa-rhythm clock" (Module 4) — scope → research → design → build → present. 10-min overview.',
            'senior': '**Project-scoping workshop.** Pairs swap project ideas. Each pair gives the other (a) one strength, (b) one concern, (c) one suggested narrowing or expansion. Then each student writes their final scope.',
        },
        'source': {
            'primary': 'Tell a story about a child who made a great project — and what made it great: choosing carefully, doing the work, showing pride.',
            'middle': 'Paraphrase Bhagavad Gītā 2.47: *"Your right is to action alone, never to its fruits."* (Modern translation: focus on the WORK, not the outcome.)',
            'senior': '**Direct verse.** Bhagavad Gītā 2.47:\n\n> *karmaṇy-evādhikāras te mā phaleṣu kadācana /*\n> *mā karma-phala-hetur bhūr mā te saṅgo \'stv akarmaṇi //*\n\n"You have a right to action, never to its fruits. Let not the fruits of action be your motive; nor be attached to inaction."\n\nA capstone project is an exercise in *karma-yoga* — focused, disciplined work without obsessing over the outcome.',
        },
        'activity': {
            'primary': 'Each child writes (or draws) their project plan: WHAT they\'ll make, what they need, who will help. Submit to teacher.',
            'middle': '**Project scoping.** 30 minutes silent work: write a 1-page project plan with scope, sources, timeline (10 days), assessment criteria.',
            'senior': '**Project scoping + critique.** 40 minutes individual + 10 minutes pair-critique. Submit plan for teacher approval.',
        },
        'reflection': {
            'primary': 'Each child shares their project choice and why. Cheer for each commitment.',
            'middle': '*"Why is THIS project the right one for you? What will you learn that you couldn\'t learn in class?"*',
            'senior': '*"How does THIS capstone challenge your assumptions about IKS? What\'s the riskiest part of your project — and why is the risk worth taking?"*',
        },
        'go_deeper_days': [
            ('day-01', 'Overview + project menu'),
            ('day-02', 'Scope + plan'),
            ('day-03', 'Research day 1'),
            ('day-04', 'Research day 2'),
            ('day-05', 'Mid-project critique'),
            ('day-06', 'Build day 1'),
            ('day-07', 'Build day 2'),
            ('day-08', 'Document'),
            ('day-09', 'Rehearse'),
            ('day-10', 'Share day'),
        ],
    },
}


# =============================================================================
# Renderer
# =============================================================================

def render_workshop(slug: str, mod: dict, band: str) -> str:
    """Render a single workshop markdown file."""
    title = mod['title']
    sanskrit = mod['sanskrit']
    subtitle = mod['subtitle']
    hook = mod['hook'][band]
    core = mod['core'][band]
    demo = mod['demo'][band]
    source = mod['source'][band]
    activity = mod['activity'][band]
    reflection = mod['reflection'][band]
    days = mod['go_deeper_days']

    # Determine the module number from slug (e.g. 'module-04-doshas' → 4)
    mod_num = int(slug.split('-')[1])

    band_label = {'primary': 'Primary (3-5)', 'middle': 'Middle (6-8)', 'senior': 'Senior (9-12)'}[band]
    days_list = '\n'.join(f"- **{d[0].replace('day-', 'Day ').lstrip('0')}** — {d[1]}" for d in days)

    return f"""# Module {mod_num} — {title} (Darśana)

**Sanskrit:** *{sanskrit}* · **Band:** {band_label} · **Duration:** 60 min · **Path:** Darśana (Workshop)

{subtitle}.

> **Darśana note.** This workshop condenses Module {mod_num}\'s full 10-day arc into one hour. For the deeper version — daily lesson plans, quizzes, assessments, slide decks — switch to **[Adhyayana](../)** (the Full Course path).

---

## Opening hook · 5 min

{hook}

---

## Core idea · 15 min

{core}

---

## Demonstration · 10 min

{demo}

---

## Source moment · 5 min

{source}

---

## Hands-on activity · 15 min

{activity}

---

## Reflection + take-home · 10 min

{reflection}

---

## Go deeper into Adhyayana

The 10 days you\'re skipping if you only do this workshop:

{days_list}

→ **[Open the Adhyayana track for this module](../)** to access all 10 days, the 4-audience PDFs, the slide deck, the quizzes, and the project rubric.
"""


def main():
    written = 0
    for slug, mod in WORKSHOPS.items():
        for band in ('primary', 'middle', 'senior'):
            path = CURRICULUM / band / slug / 'darshana.md'
            path.parent.mkdir(parents=True, exist_ok=True)
            content = render_workshop(slug, mod, band)
            path.write_text(content, encoding='utf-8')
            written += 1
    print(f"Wrote {written} darshana.md files.")


if __name__ == '__main__':
    main()
