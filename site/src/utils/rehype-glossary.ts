/**
 * Rehype plugin that auto-wraps Sanskrit glossary terms in <a class="glossary-term">.
 *
 * Each wrap links to /glossary/{slug}/ and carries data-meaning for a hover
 * tooltip styled in global.css. Only wraps the FIRST occurrence per text node
 * so paragraphs don't become a sea of underlines.
 *
 * Skipped contexts: <a>, <code>, <pre>, <h1>-<h6>, and ancestors thereof.
 */
// Minimal HAST types so we don't depend on @types/hast or unist-util-visit.
type HastNode = { type: string; [k: string]: any };
type Parent = HastNode & { children?: HastNode[] };
type Element = HastNode & { type: 'element'; tagName: string; properties?: any; children?: HastNode[] };
type Text = HastNode & { type: 'text'; value: string };
type Root = Parent;

import { loadGlossary, type GlossaryTerm } from './glossary';

const SKIP_TAGS = new Set(['a', 'code', 'pre', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']);

function escapeRegex(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

let cachedTerms: GlossaryTerm[] | null = null;
let cachedPattern: { regex: RegExp; map: Map<string, GlossaryTerm> } | null = null;

function getPattern() {
  if (cachedPattern) return cachedPattern;
  if (!cachedTerms) cachedTerms = loadGlossary();
  const map = new Map<string, GlossaryTerm>();
  for (const t of cachedTerms) {
    map.set(t.term, t);
    for (const alt of t.alternates) map.set(alt, t);
  }
  // Longest first so multi-word forms beat single-word substrings.
  const keys = Array.from(map.keys()).sort((a, b) => b.length - a.length);
  // Word-boundary on both sides; case-insensitive for ASCII alternates.
  // We use a Unicode-aware boundary via lookarounds to handle diacritics.
  const pattern = '(?<![\\p{L}])(' + keys.map(escapeRegex).join('|') + ')(?![\\p{L}])';
  const regex = new RegExp(pattern, 'giu');
  cachedPattern = { regex, map };
  return cachedPattern;
}

export function rehypeGlossary() {
  return (tree: Root) => {
    const { regex, map } = getPattern();

    function walk(node: Parent, ancestors: string[] = []) {
      if (!node.children) return;
      for (let i = 0; i < node.children.length; i++) {
        const child = node.children[i];
        if ((child as Element).type === 'element') {
          const el = child as Element;
          if (SKIP_TAGS.has(el.tagName)) continue;
          walk(el, [...ancestors, el.tagName]);
        } else if ((child as Text).type === 'text') {
          const text = (child as Text).value;
          // Quick skip if no possible match
          regex.lastIndex = 0;
          if (!regex.test(text)) continue;
          regex.lastIndex = 0;

          // Build new nodes from matches
          const newChildren: (Element | Text)[] = [];
          let lastIdx = 0;
          let firstOnly = true;
          let m: RegExpExecArray | null;
          while ((m = regex.exec(text))) {
            if (!firstOnly) break; // wrap only first occurrence per text node
            firstOnly = false;
            const matchText = m[0];
            const start = m.index;
            const end = start + matchText.length;
            const term = map.get(matchText) ?? map.get(matchText.toLowerCase());
            if (!term) continue;
            if (start > lastIdx) {
              newChildren.push({ type: 'text', value: text.slice(lastIdx, start) });
            }
            newChildren.push({
              type: 'element',
              tagName: 'a',
              properties: {
                href: `/glossary/${term.slug}/`,
                className: ['glossary-term'],
                'data-iast': term.term,
                'data-meaning': term.definition || term.literal || '',
                title: `${term.term} — ${term.definition || term.literal || ''}`,
              },
              children: [{ type: 'text', value: matchText }],
            } as Element);
            lastIdx = end;
          }
          if (lastIdx > 0) {
            if (lastIdx < text.length) {
              newChildren.push({ type: 'text', value: text.slice(lastIdx) });
            }
            node.children.splice(i, 1, ...newChildren);
            i += newChildren.length - 1;
          }
        }
      }
    }

    walk(tree as unknown as Parent);
  };
}
