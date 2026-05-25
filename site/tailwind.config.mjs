/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        // Semantic tokens — values come from CSS variables (set per band).
        bg: 'rgb(var(--color-bg) / <alpha-value>)',
        surface: 'rgb(var(--color-surface) / <alpha-value>)',
        text: { DEFAULT: 'rgb(var(--color-text) / <alpha-value>)', muted: 'rgb(var(--color-text-muted) / <alpha-value>)' },
        accent: { DEFAULT: 'rgb(var(--color-accent) / <alpha-value>)', 2: 'rgb(var(--color-accent-2) / <alpha-value>)' },
        border: 'rgb(var(--color-border) / <alpha-value>)',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
        display: ['Fraunces', 'Georgia', 'serif'],
        devanagari: ['Noto Sans Devanagari', 'sans-serif'],
        mono: ['JetBrains Mono', 'Courier New', 'monospace'],
      },
      maxWidth: {
        prose: '72ch',
        content: '880px',
      },
    },
  },
};
