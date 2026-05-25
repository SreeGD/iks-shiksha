/**
 * Glossary parser — reads `curriculum/_shared/glossary.md` and extracts terms.
 *
 * The glossary is human-written markdown with sections (## Topic) and term
 * lines like:
 *   - **iast-term** (Devanāgarī; alternate) — "literal meaning." *Functional definition.*
 *
 * This parser walks line-by-line; cheap and predictable.
 */

import fs from 'node:fs';
import path from 'node:path';

export interface GlossaryTerm {
  /** URL-safe slug derived from the primary IAST term. */
  slug: string;
  /** Primary term (IAST). */
  term: string;
  /** Devanāgarī, if provided in parentheses. */
  devanagari?: string;
  /** Alternate spellings (English transliteration without diacritics). */
  alternates: string[];
  /** Literal/etymological meaning (text between quotes after the em-dash). */
  literal?: string;
  /** Functional definition (the italicised text after the literal). */
  definition: string;
  /** Section heading the term sat under. */
  section: string;
}

const GLOSSARY_PATH = path.resolve('../curriculum/_shared/glossary.md');

export function loadGlossary(): GlossaryTerm[] {
  if (!fs.existsSync(GLOSSARY_PATH)) return [];
  const raw = fs.readFileSync(GLOSSARY_PATH, 'utf8');
  const lines = raw.split('\n');

  const terms: GlossaryTerm[] = [];
  let section = 'General';

  for (const line of lines) {
    const sect = line.match(/^##\s+(.+)$/);
    if (sect) {
      section = sect[1].trim();
      continue;
    }

    // Term line: starts with "- **term**"
    // The definition may contain nested *italic* terms; greedy-match until end-of-line.
    const match = line.match(/^-\s+\*\*([^*]+)\*\*\s*(?:\(([^)]+)\))?\s*[—-]\s*(?:"([^"]+?)\.?")?\s*(?:\*(.+)\*\s*)?$/);
    if (!match) continue;
    const [, term, parenContent, literal, rawDefinition] = match;
    // Strip nested *…* markers from the definition so it renders cleanly.
    const definition = (rawDefinition ?? '').replace(/\*/g, '');

    // Parse Devanāgarī + alternates from parens
    let devanagari: string | undefined;
    const alternates: string[] = [];
    if (parenContent) {
      const parts = parenContent.split(';').map((p) => p.trim());
      for (const part of parts) {
        if (/[ऀ-ॿ]/.test(part)) {
          // Contains Devanāgarī code points
          devanagari = part;
        } else if (part.toLowerCase().startsWith('also ')) {
          alternates.push(part.replace(/^also\s+/i, '').trim());
        } else if (/[ऀ-ॿ]/.test(part) === false && !part.toLowerCase().startsWith('iast')) {
          // Catch-all for other annotations like "lit."; ignored
        }
      }
    }

    terms.push({
      slug: slugify(term.trim()),
      term: term.trim(),
      devanagari,
      alternates,
      literal: literal?.trim(),
      definition: definition?.trim() ?? '',
      section,
    });
  }

  return terms;
}

export function slugify(term: string): string {
  return term
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')   // strip diacritics
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}
