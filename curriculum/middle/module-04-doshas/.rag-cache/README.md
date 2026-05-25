# RAG cache — Module 4 Doshas (Middle)

RAG queries were attempted via `scripts/query-vk-rag.py` against the vidya-karana ChromaDB. The local Python environment did not have `chromadb` installed at build time, so the cache below records the **intended** queries and the **anchor sources** the lessons cite. When chromadb becomes available, run:

```bash
CHROMADB_PATH=/Users/sree/Projects/vidya-karana/chromadb \
  python3 /Users/sree/Projects/indianknowledgesystem/scripts/query-vk-rag.py \
  "vata pitta kapha definition Caraka"
```

and similar for the four queries below; save outputs as `query-NN.json`.

## Intended queries

1. `"vata pitta kapha definition Caraka"`
2. `"tridosha balance prakriti constitution"`
3. `"dosha vikriti imbalance symptoms"`
4. `"Caraka Samhita sutra sthana definition tridosha"`

## Anchor sources used in lessons (independently verified, not from RAG)

| Citation | Used in | Content |
|----------|---------|---------|
| **Caraka Saṁhitā, Sūtrasthāna 1.57** | Day 2, Day 7 | Defines *vāta, pitta, śleṣman* (=kapha) as the three *doṣa*s of the body; their natural state preserves the body, vitiated state harms it. |
| **Caraka Saṁhitā, Sūtrasthāna 1.59** | Day 2 | *vāyuḥ pittaṁ kaphaścoktaḥ śārīro doṣasaṅgrahaḥ* — "Vāyu, pitta, and kapha are declared the summary of bodily *doṣa*s." |
| **Aṣṭāṅga Hṛdaya, Sūtrasthāna 1.6–7** | Day 2, Day 6 | Vāgbhaṭa's compact statement of the *doṣa-dhātu-mala* framework: three *doṣa*s, seven *dhātu*s (tissues), three *mala*s (wastes) together constitute the body. |
| **Aṣṭāṅga Hṛdaya, Sūtrasthāna 1.8** | Day 7 | *roga-rogo-vidhijñānaṁ* — the science of disease and its remedy rests on knowing the *doṣa*s in their normal and vitiated states. |
| **Caraka Saṁhitā, Vimānasthāna 8.95–99** | Day 7 (Senior cross-reference) | Classical description of *prakṛti* (constitutional types) determined at conception. |

## Why these citations are safe

Caraka Saṁhitā and Aṣṭāṅga Hṛdaya are the two most-edited primary sources in the classical Ayurvedic corpus. The verse numbers above appear in the standard editions used by Indian Ayurvedic colleges (Trikamji's Caraka, Kunte's Aṣṭāṅga Hṛdaya). They are paraphrased — not directly quoted at length — in this module, except for the short Caraka 1.59 *pratīka* used at Senior band.
