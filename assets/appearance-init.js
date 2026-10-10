/* Run before stylesheets to avoid a light flash. Stores appearance only. */
(function () {
  'use strict';
  const key = 'wholemind.appearance.v1';
  const parameter = 'appearance';
  const valid = value => ['auto', 'light', 'dark'].includes(value);
  const root = document.documentElement;
  const system = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
  function readStored() {
    try { const value = window.localStorage.getItem(key); return valid(value) ? value : 'auto'; }
    catch (_) { return 'auto'; }
  }
  function remember(value) {
    try {
      if (value === 'auto') window.localStorage.removeItem(key);
      else window.localStorage.setItem(key, value);
    } catch (_) { /* Appearance still works for this page when storage is blocked. */ }
  }
  let preference = readStored();
  try {
    const address = new URL(window.location.href);
    const incoming = address.searchParams.get(parameter);
    if (valid(incoming)) { preference = incoming; remember(incoming); }
    if (address.searchParams.has(parameter)) {
      address.searchParams.delete(parameter);
      window.history.replaceState(window.history.state, '', address.href);
    }
  } catch (_) { /* Sandboxed previews may not allow history changes. */ }
  function apply() {
    const effective = preference === 'auto' ? (system && system.matches ? 'dark' : 'light') : preference;
    root.dataset.appearance = preference;
    root.dataset.theme = effective;
    const browserColor = document.querySelector('meta[name="theme-color"]');
    if (browserColor) browserColor.content = effective === 'light' ? '#F7F3EB' :
      (root.dataset.brand === 'maxine' ? '#221C25' : '#15211E');
    window.dispatchEvent(new CustomEvent('wholemind:appearance', { detail: { preference, effective } }));
  }
  window.WholeMindAppearance = Object.freeze({
    get: () => preference,
    set(value) { if (!valid(value)) return; preference = value; remember(value); apply(); },
    refresh: apply
  });
  const systemChanged = () => { if (preference === 'auto') apply(); };
  if (system && system.addEventListener) system.addEventListener('change', systemChanged);
  else if (system && system.addListener) system.addListener(systemChanged);
  window.addEventListener('storage', event => {
    if (event.key === key || event.key === null) { preference = readStored(); apply(); }
  });
  window.addEventListener('pageshow', event => {
    if (event.persisted) { preference = readStored(); apply(); }
  });
  apply();
})();
