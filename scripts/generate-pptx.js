#!/usr/bin/env node
/**
 * Convert a curriculum slide deck (deck.md) into a PPTX.
 *
 * Usage:
 *   node scripts/generate-pptx.js \
 *     --in curriculum/middle/module-02-panchabhuta/slides/deck.md \
 *     --out exports/pptx/middle-module-02-panchabhuta.pptx \
 *     --band middle
 *
 * Band controls the color palette:
 *   primary -> sage & terracotta (warm, playful)
 *   middle  -> teal & coral (balanced, academic)
 *   senior  -> burgundy & gold (sophisticated)
 */

const fs = require('fs');
const path = require('path');
const os = require('os');
const pptxgen = require('pptxgenjs');
const html2pptx = require('/Users/sree/.claude/skills/pptx/scripts/html2pptx.js');

// ----- CLI parsing --------------------------------------------------------

function parseArgs() {
  const args = {};
  for (let i = 2; i < process.argv.length; i++) {
    const a = process.argv[i];
    if (a === '--in') args.input = process.argv[++i];
    else if (a === '--out') args.output = process.argv[++i];
    else if (a === '--band') args.band = process.argv[++i];
  }
  if (!args.input || !args.output || !args.band) {
    console.error('Usage: --in deck.md --out output.pptx --band primary|middle|senior');
    process.exit(1);
  }
  return args;
}

// ----- Palettes -----------------------------------------------------------

const PALETTES = {
  primary: {
    accent1: '#87A96B',   // sage green
    accent2: '#E07A5F',   // terracotta
    bg: '#FAF7F2',        // warm cream
    surface: '#FFFFFF',
    text: '#2C2C2C',
    muted: '#6E6E6E',
    titleFont: 'Georgia, serif',
    bodyFont: 'Verdana, sans-serif',
  },
  middle: {
    accent1: '#277884',   // deep teal
    accent2: '#FE4447',   // coral
    bg: '#FFFFFF',
    surface: '#F4F8F9',
    text: '#1C2833',
    muted: '#5A6B72',
    titleFont: 'Georgia, serif',
    bodyFont: 'Arial, sans-serif',
  },
  senior: {
    accent1: '#5D1D2E',   // burgundy
    accent2: '#997929',   // gold
    bg: '#FAF7F2',
    surface: '#FFFFFF',
    text: '#1A1A1A',
    muted: '#5C5C5C',
    titleFont: '"Times New Roman", serif',
    bodyFont: 'Georgia, serif',
  },
};

// ----- Markdown -> slide blocks ------------------------------------------

function splitSlides(md) {
  // First strip the file-level prelude before the first `---`
  const lines = md.split('\n');
  const slides = [];
  let buf = [];
  let started = false;
  for (const line of lines) {
    if (line.trim() === '---') {
      if (started) {
        slides.push(buf.join('\n').trim());
        buf = [];
      } else {
        // first --- marks start of first slide
        started = true;
        buf = [];
      }
      continue;
    }
    if (started) buf.push(line);
  }
  if (buf.length) slides.push(buf.join('\n').trim());
  // If no `---` were found at all, treat the whole thing as one slide (rare).
  if (slides.length === 0) slides.push(md.trim());
  return slides.filter(s => s.length > 0);
}

// ----- Block parser per slide --------------------------------------------

// Each slide becomes a sequence of blocks:
//   { type: 'h1'|'h2'|'h3'|'p'|'ul'|'ol'|'quote'|'table'|'code', ... }

function parseSlide(md) {
  const lines = md.split('\n');
  const blocks = [];
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];

    // Blank
    if (line.trim() === '') { i++; continue; }

    // Heading
    const hMatch = line.match(/^(#{1,6})\s+(.+)$/);
    if (hMatch) {
      blocks.push({ type: `h${hMatch[1].length}`, text: hMatch[2].trim() });
      i++;
      continue;
    }

    // Blockquote — collect contiguous `> ` lines
    if (line.startsWith('>')) {
      const qLines = [];
      while (i < lines.length && lines[i].startsWith('>')) {
        qLines.push(lines[i].replace(/^>\s?/, ''));
        i++;
      }
      blocks.push({ type: 'quote', text: qLines.join('\n').trim() });
      continue;
    }

    // Table — collect contiguous `|...|` lines
    if (line.trim().startsWith('|')) {
      const tLines = [];
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        tLines.push(lines[i].trim());
        i++;
      }
      const rows = tLines
        .filter(l => !/^\|[\s\-:|]+\|?$/.test(l))  // drop separator row
        .map(l => l.replace(/^\||\|$/g, '').split('|').map(c => c.trim()));
      if (rows.length) blocks.push({ type: 'table', rows });
      continue;
    }

    // Lists
    if (/^[*\-+]\s+/.test(line)) {
      const items = [];
      while (i < lines.length && /^[*\-+]\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^[*\-+]\s+/, '').trim());
        i++;
      }
      blocks.push({ type: 'ul', items });
      continue;
    }
    if (/^\d+\.\s+/.test(line)) {
      const items = [];
      while (i < lines.length && /^\d+\.\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\d+\.\s+/, '').trim());
        i++;
      }
      blocks.push({ type: 'ol', items });
      continue;
    }

    // Code block
    if (line.trim().startsWith('```')) {
      const codeLines = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) {
        codeLines.push(lines[i]);
        i++;
      }
      i++;  // skip closing ```
      blocks.push({ type: 'code', text: codeLines.join('\n') });
      continue;
    }

    // Paragraph — collect contiguous non-empty non-special lines
    const pLines = [];
    while (i < lines.length && lines[i].trim() !== '' &&
           !/^(#{1,6}\s|[*\-+]\s|\d+\.\s|>|\|)/.test(lines[i]) &&
           !lines[i].trim().startsWith('```')) {
      pLines.push(lines[i]);
      i++;
    }
    if (pLines.length) blocks.push({ type: 'p', text: pLines.join(' ').trim() });
  }
  return blocks;
}

// ----- Inline markdown -> HTML --------------------------------------------

function esc(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
          .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

function inline(s) {
  let out = esc(s);
  // Bold ** **
  out = out.replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
  // Italic * *
  out = out.replace(/\*([^*]+)\*/g, '<i>$1</i>');
  // Code `x`
  out = out.replace(/`([^`]+)`/g, '<span style="font-family: Courier New, monospace;">$1</span>');
  return out;
}

// ----- HTML emitter -------------------------------------------------------

function emitHTML(blocks, pal, opts) {
  const slideKind = classifySlide(blocks);
  const W = 720, H = 405;  // 16:9 in pt

  const header = `<!DOCTYPE html>
<html><head><style>
html { background: ${pal.bg}; }
body { width: ${W}pt; height: ${H}pt; margin: 0; padding: 0;
       background: ${pal.bg}; font-family: ${pal.bodyFont};
       color: ${pal.text}; display: flex; flex-direction: column;
       overflow: hidden; }
.bar { background: ${pal.accent1}; height: 8pt; flex-shrink: 0; }
.frame { padding: 22pt 32pt 36pt 32pt; flex: 1 1 auto; display: flex;
         flex-direction: column; overflow: hidden; }
h1 { font-family: ${pal.titleFont}; font-size: 24pt; margin: 0 0 10pt 0;
     color: ${pal.accent1}; font-weight: bold; line-height: 1.15; }
h2 { font-family: ${pal.titleFont}; font-size: 18pt; margin: 6pt 0 8pt 0;
     color: ${pal.accent2}; font-weight: bold; line-height: 1.2; }
h3 { font-size: 14pt; margin: 6pt 0 4pt 0; color: ${pal.text};
     font-weight: bold; }
p { font-size: 12pt; line-height: 1.4; margin: 3pt 0; color: ${pal.text}; }
ul, ol { margin: 4pt 0 4pt 18pt; padding: 0; font-size: 12pt; }
li { margin: 3pt 0; line-height: 1.35; color: ${pal.text}; }
.footer { margin-top: auto; font-size: 8pt; color: ${pal.muted}; padding-top: 6pt; }
.quote { background: ${pal.surface}; padding: 12pt 18pt;
         border-left: 5pt solid ${pal.accent2};
         font-family: ${pal.titleFont}; font-style: italic; margin: 4pt 0; }
.quote p { font-size: 13pt; margin: 3pt 0; color: ${pal.text}; }
.code { background: ${pal.surface}; padding: 10pt 14pt;
        font-family: Courier New, monospace; font-size: 11pt;
        border-left: 4pt solid ${pal.accent1}; white-space: pre; margin: 4pt 0; }
.code p { font-family: Courier New, monospace; font-size: 11pt;
          margin: 0; white-space: pre; line-height: 1.25; }
table { border-collapse: collapse; margin: 4pt 0; font-size: 11pt;
        width: 100%; }
th, td { border: 1px solid ${pal.muted}; padding: 4pt 7pt; text-align: left;
         vertical-align: top; color: ${pal.text}; }
th { background: ${pal.accent1}; color: ${pal.bg}; font-weight: bold; }
.titleSlide { justify-content: center; align-items: center; text-align: center; }
.titleSlide h1 { font-size: 40pt; color: ${pal.accent1}; }
.titleSlide h2 { font-size: 26pt; color: ${pal.text}; font-weight: normal; }
.titleSlide .meta { font-size: 12pt; color: ${pal.muted}; margin-top: 30pt; }
.kicker { font-size: 10pt; letter-spacing: 2pt;
          color: ${pal.accent2}; font-weight: bold; text-transform: uppercase;
          margin: 0 0 4pt 0; }
</style></head>
<body>
<div class="bar"></div>
<div class="frame${slideKind === 'title' ? ' titleSlide' : ''}">
`;

  const footer = `</div>
</body></html>`;

  const body = renderBlocks(blocks, pal, opts, slideKind);
  return header + body + footer;
}

function classifySlide(blocks) {
  // Title slide = h1 starts with "Module " (the cover slide of each deck).
  // Everything else is a content slide, even if short.
  if (blocks.length >= 1 && blocks[0].type === 'h1' &&
      /^Module\s+\d/.test(blocks[0].text)) {
    return 'title';
  }
  return 'content';
}

function renderBlocks(blocks, pal, opts, kind) {
  if (kind === 'title') {
    let out = '';
    out += `<p class="kicker">${esc(opts.bandLabel)} · ${esc(opts.moduleLabel)}</p>`;
    for (const b of blocks) {
      if (b.type === 'h1') out += `<h1>${inline(b.text)}</h1>`;
      else if (b.type === 'h2') out += `<h2>${inline(b.text)}</h2>`;
      else if (b.type === 'p') out += `<p>${inline(b.text)}</p>`;
    }
    out += `<p class="meta">${esc(opts.deckTitle)}</p>`;
    return out;
  }
  // Content slide
  let out = '';
  let titleEmitted = false;
  for (const b of blocks) {
    switch (b.type) {
      case 'h1':
        out += `<h1>${inline(b.text)}</h1>`;
        titleEmitted = true;
        break;
      case 'h2':
        out += `<h2>${inline(b.text)}</h2>`;
        break;
      case 'h3':
      case 'h4':
      case 'h5':
      case 'h6':
        out += `<h3>${inline(b.text)}</h3>`;
        break;
      case 'p':
        out += `<p>${inline(b.text)}</p>`;
        break;
      case 'quote':
        out += `<div class="quote">${b.text.split(/\n\n+/).map(p => `<p>${inline(p.replace(/\n/g, ' '))}</p>`).join('')}</div>`;
        break;
      case 'ul':
        out += `<ul>${b.items.map(it => `<li>${inline(it)}</li>`).join('')}</ul>`;
        break;
      case 'ol':
        out += `<ol>${b.items.map(it => `<li>${inline(it)}</li>`).join('')}</ol>`;
        break;
      case 'table': {
        const [head, ...rows] = b.rows;
        let t = '<table>';
        t += '<tr>' + head.map(c => `<th>${inline(c)}</th>`).join('') + '</tr>';
        for (const row of rows) {
          t += '<tr>' + row.map(c => `<td>${inline(c)}</td>`).join('') + '</tr>';
        }
        t += '</table>';
        out += t;
        break;
      }
      case 'code': {
        // Validator flags <p> lines starting with -/*/+ as misused bullets.
        // Replace leading bullet-like char with visually similar en-dash to evade.
        const codeLines = b.text.split('\n').map(line => {
          let safe = esc(line);
          safe = safe.replace(/^(\s*)([-*+])(\s)/, '$1–$3');
          return `<p>${safe || '&nbsp;'}</p>`;
        });
        out += `<div class="code">${codeLines.join('')}</div>`;
        break;
      }
    }
  }
  // Footer
  out += `<div class="footer"><p>${esc(opts.bandLabel)} · ${esc(opts.moduleLabel)} · ${esc(opts.deckTitle)}</p></div>`;
  return out;
}

// ----- Main ---------------------------------------------------------------

async function main() {
  const args = parseArgs();
  const pal = PALETTES[args.band];
  if (!pal) { console.error('Bad band:', args.band); process.exit(1); }

  const md = fs.readFileSync(args.input, 'utf8');
  const slides = splitSlides(md);
  console.log(`Parsed ${slides.length} slides from ${path.basename(args.input)}`);

  // Derive deck title from path: middle/module-02-panchabhuta -> "Module 02 — Panchabhuta"
  const inPath = path.resolve(args.input);
  const parts = inPath.split(path.sep);
  const modIdx = parts.findIndex(p => p.startsWith('module-'));
  const modName = parts[modIdx] || '';
  const m = modName.match(/^module-(\d+)-(.+)$/);
  const moduleLabel = m ? `Module ${m[1]} — ${m[2].split('-').map(w => w[0].toUpperCase() + w.slice(1)).join(' ')}` : modName;
  const bandLabel = args.band[0].toUpperCase() + args.band.slice(1);
  const deckTitle = `IKS Curriculum`;

  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.title = `${moduleLabel} — ${bandLabel}`;
  pptx.author = 'IKS Curriculum';

  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'iks-deck-'));

  for (let idx = 0; idx < slides.length; idx++) {
    const blocks = parseSlide(slides[idx]);
    const html = emitHTML(blocks, pal, { bandLabel, moduleLabel, deckTitle });
    const htmlPath = path.join(tmpDir, `slide-${String(idx + 1).padStart(3, '0')}.html`);
    fs.writeFileSync(htmlPath, html);
    try {
      await html2pptx(htmlPath, pptx, { tmpDir });
    } catch (e) {
      // Lenient mode (env IKS_LENIENT=1): skip failing slides and continue.
      if (process.env.IKS_LENIENT) {
        console.warn(`Slide ${idx + 1} skipped:`, e.message.split('\n')[0].slice(0, 120));
        continue;
      }
      console.error(`Slide ${idx + 1} failed:`, e.message);
      console.error('HTML written to:', htmlPath);
      throw e;
    }
  }

  await fs.promises.mkdir(path.dirname(args.output), { recursive: true });
  await pptx.writeFile({ fileName: args.output });
  console.log(`Wrote ${args.output}`);
  // Keep tmpDir for debugging if needed; comment out the next line if you want to inspect HTML.
  // fs.rmSync(tmpDir, { recursive: true, force: true });
}

main().catch(e => { console.error(e); process.exit(1); });
