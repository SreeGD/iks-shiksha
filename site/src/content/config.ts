import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Pack overview / README — one entry per (band, module) pair.
const packs = defineCollection({
  loader: glob({
    pattern: '*/module-*/README.md',
    base: '../curriculum',
  }),
  schema: z.object({}).passthrough(),
});

// Lesson plans — one entry per day file per pack.
const lessons = defineCollection({
  loader: glob({
    pattern: '*/module-*/days/day-*.md',
    base: '../curriculum',
  }),
  schema: z.object({}).passthrough(),
});

// Quizzes, activities, assessments, and other per-pack docs.
const docs = defineCollection({
  loader: glob({
    pattern: [
      '*/module-*/lesson-plan.md',
      '*/module-*/teacher-notes.md',
      '*/module-*/sources.md',
      '*/module-*/parent-guide.md',
      '*/module-*/student-workbook.md',
      '*/module-*/writing-prompts.md',
      '*/module-*/homework.md',
      '*/module-*/quizzes/*.md',
      '*/module-*/activities/*.md',
      '*/module-*/assessments/*.md',
      '*/module-*/slides/deck.md',
    ],
    base: '../curriculum',
  }),
  schema: z.object({}).passthrough(),
});

// Shared docs (glossary, style guide).
const shared = defineCollection({
  loader: glob({
    pattern: '_shared/**/*.md',
    base: '../curriculum',
  }),
  schema: z.object({}).passthrough(),
});

export const collections = { packs, lessons, docs, shared };
