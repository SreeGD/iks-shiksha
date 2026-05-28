/** Path modes — Adhyayana (full course) / Darśana (workshop) / unset.
 *
 * Persisted in localStorage under key `iks-path`. Set on <html data-path="..">
 * before paint so CSS rules and route choices can adapt without flash.
 *
 * - adhyayana = the 15-module × 10-day Full Course (existing default)
 * - darshana  = the 15-module × 1-hour Workshop tour (new)
 * - unset     = first visit; PathPicker modal is shown on the homepage
 */

export type PathMode = 'adhyayana' | 'darshana' | 'unset';

export const PATH_KEY = 'iks-path';

/** Inline script for <head>. Sets data-path on <html> before paint. */
export const PATH_BOOTSTRAP_SCRIPT = `
(function() {
  try {
    var v = localStorage.getItem('${PATH_KEY}') || 'unset';
    document.documentElement.setAttribute('data-path', v);
  } catch (e) {
    document.documentElement.setAttribute('data-path', 'unset');
  }
})();
`.trim();

/** Inline JS helper for buttons that need to set the path. Mirrors
 *  AUDIENCE_SET_SNIPPET. Components include this once per page. */
export const PATH_SET_SNIPPET = `
function setIksPath(value) {
  try { localStorage.setItem('${PATH_KEY}', value); } catch (e) {}
  document.documentElement.setAttribute('data-path', value);
  document.dispatchEvent(new CustomEvent('iks-path-change', { detail: value }));
}
`.trim();
