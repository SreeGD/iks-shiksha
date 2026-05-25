import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import tailwind from '@astrojs/tailwind';
import icon from 'astro-icon';
import { rehypeGlossary } from './src/utils/rehype-glossary.ts';

// Public site URL — set IKS_SITE_URL in the deploy workflow.
const SITE = process.env.IKS_SITE_URL || 'https://sreegd.github.io';
// For project Pages (sreegd.github.io/iks-shiksha/) we need a base path.
// Set IKS_BASE_PATH=/iks-shiksha (with leading slash) in CI.
const BASE = process.env.IKS_BASE_PATH || '/';

export default defineConfig({
  site: SITE,
  base: BASE,
  trailingSlash: 'always',
  integrations: [
    mdx(),
    sitemap(),
    tailwind({ applyBaseStyles: false }),
    icon({ include: { lucide: ['*'] } }),
  ],
  markdown: {
    shikiConfig: { theme: 'github-light', wrap: true },
    rehypePlugins: [rehypeGlossary],
  },
  build: { format: 'directory' },
  vite: {
    resolve: {
      // Allow Astro to read content from the parent curriculum/ folder.
      alias: { '@curriculum': '/curriculum' },
    },
  },
});
