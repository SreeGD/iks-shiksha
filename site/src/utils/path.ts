/**
 * Path helper that respects Astro's `base` configuration.
 *
 * Astro's BASE_URL ends with a trailing slash, e.g. "/iks-shiksha/" when
 * deployed under a project Pages path. This helper joins the base with any
 * route, so callers can write `withBase('/middle/')` regardless of host config.
 *
 * Usage in .astro: `<a href={withBase('/middle/')}>...</a>`
 */
export const BASE = import.meta.env.BASE_URL; // ends with '/'

export function withBase(path: string): string {
  if (!path) return BASE;
  return BASE + path.replace(/^\//, '');
}
