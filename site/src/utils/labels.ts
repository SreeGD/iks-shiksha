/** Pretty-name helpers shared across pages. */

export const BAND_LABELS: Record<string, string> = {
  primary: 'Primary',
  middle: 'Middle',
  senior: 'Senior',
};

export const BAND_GRADES: Record<string, string> = {
  primary: 'Grades 3–5',
  middle: 'Grades 6–8',
  senior: 'Grades 9–12',
};

export const BAND_BLURBS: Record<string, string> = {
  primary:
    'Story-led, drawing-heavy, 30-minute sessions. Sticker assessments. Sanskrit terms learned through a daily chant.',
  middle:
    '45-minute sessions. Balanced text + hands-on activity. Project-based assessment with rubric. Sanskrit terms with transliteration and meaning; verses cited from primary sources.',
  senior:
    'Primary-source reading in IAST. Argumentative writing. Structured debate. Research-synthesis papers.',
};

export const MODULE_TITLES: Record<string, string> = {
  'module-01-what-is-iks': 'What is IKS?',
  'module-02-panchabhuta': 'Panchabhūta (Five Elements)',
  'module-03-ayurveda-good-health': 'Ayurveda and Good Health',
  'module-05-dot-addition': 'Bindu Paddhati (Dot Method)',
  'module-08-yoga': 'Yoga and the Body',
};

export const MODULE_BLURBS: Record<string, string> = {
  'module-01-what-is-iks':
    'The map of Indian Knowledge Systems — Vedas, Vedangas, Upavedas, named achievements with dates.',
  'module-02-panchabhuta':
    'The Sāṅkhya cosmology of earth, water, fire, air, space — taught alongside states of matter.',
  'module-03-ayurveda-good-health':
    'Tridosha, dinacharya, ahāra. Lifestyle medicine + honest modern evidence framing.',
  'module-05-dot-addition':
    'The 20th-century mental-arithmetic technique for fast column addition.',
  'module-08-yoga':
    "Patañjali's eight limbs + safe āsana practice + breath physiology.",
};

export function prettyFileName(filename: string): string {
  const stem = filename.replace(/\.md$/, '').replace(/\.html$/, '');
  const labels: Record<string, string> = {
    README: 'Overview',
    'lesson-plan': '10-Day Lesson Plan',
    'teacher-notes': 'Teacher Notes',
    sources: 'Sources',
    'parent-guide': 'Parent Guide',
    'writing-prompts': 'Writing Prompts',
    homework: 'Homework',
    'student-workbook': 'Student Workbook',
    rubric: 'Rubric',
    'project-brief': 'Project Brief',
    formative: 'Formative Quiz',
    summative: 'Summative Quiz',
    'oral-recall': 'Oral Recall',
    deck: 'Slide Deck (source)',
  };
  if (labels[stem]) return labels[stem];

  const dayMatch = stem.match(/^day-(\d+)-(.+)$/);
  if (dayMatch) {
    const n = parseInt(dayMatch[1], 10);
    const slug = dayMatch[2].replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());
    return `Day ${n} — ${slug}`;
  }

  const actMatch = stem.match(/^activity-(\d+)-(.+)$/);
  if (actMatch) {
    const n = parseInt(actMatch[1], 10);
    const slug = actMatch[2].replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());
    return `Activity ${n} — ${slug}`;
  }

  return stem.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());
}
