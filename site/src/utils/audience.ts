/** Audience modes — teacher / parent / student / unset.
 *
 * Persisted in localStorage under key `iks-audience` so user choice survives
 * across page loads. The chosen mode is also set on <html data-audience="..">
 * so CSS rules can conditionally show/hide content.
 */

export type Audience = 'teacher' | 'parent' | 'student' | 'unset';

export const AUDIENCE_KEY = 'iks-audience';

/** Inline script that reads localStorage and sets data-audience on <html>.
 *  Inject into <head> so the attribute is set before paint.
 */
export const AUDIENCE_BOOTSTRAP_SCRIPT = `
(function() {
  try {
    var v = localStorage.getItem('${AUDIENCE_KEY}') || 'unset';
    document.documentElement.setAttribute('data-audience', v);
  } catch (e) {
    document.documentElement.setAttribute('data-audience', 'unset');
  }
})();
`.trim();

/** Inline script for any element that needs to set the audience.
 *  Used by audience-picker buttons and the header dropdown.
 */
export const AUDIENCE_SET_SNIPPET = `
function setIksAudience(value) {
  try { localStorage.setItem('${AUDIENCE_KEY}', value); } catch (e) {}
  document.documentElement.setAttribute('data-audience', value);
  // Tell any listening components on the page to re-render their state.
  document.dispatchEvent(new CustomEvent('iks-audience-change', { detail: value }));
}
`.trim();
