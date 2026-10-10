/* Progressive enhancement. No analytics or worksheet storage/network requests.
   appearance-init.js stores only a visitor's light/dark appearance preference. */
(function () {
  'use strict';
  const boundFields = new WeakSet();
  const boundButtons = new WeakSet();
  function syncWorksheets(root = document) {
    root.querySelectorAll('[data-worksheet]').forEach(field => {
      const output = field.parentElement.querySelector('.print-response');
      if (output) output.textContent = field.value;
    });
  }
  function initializeWorksheets(root = document) {
    const fields = [...root.querySelectorAll('[data-worksheet]')];
    fields.forEach(field => {
      if (boundFields.has(field)) return;
      field.addEventListener('input', () => syncWorksheets(root));
      boundFields.add(field);
    });
    root.querySelectorAll('[data-print]').forEach(button => {
      button.hidden = false;
      if (boundButtons.has(button)) return;
      button.addEventListener('click', () => { syncWorksheets(root); window.print(); });
      boundButtons.add(button);
    });
    root.querySelectorAll('[data-clear]').forEach(button => {
      button.hidden = fields.length === 0;
      if (boundButtons.has(button)) return;
      button.addEventListener('click', () => {
        if (fields.some(field => field.value) && !window.confirm('Clear the responses on this page? This cannot be undone.')) return;
        fields.forEach(field => { field.value = ''; });
        syncWorksheets(root);
        const status = root.querySelector('#worksheet-status');
        if (status) status.textContent = 'The worksheet responses have been cleared.';
      });
      boundButtons.add(button);
    });
  }
  function syncAppearance(root = document) {
    const appearance = window.WholeMindAppearance;
    if (!appearance) return;
    const value = appearance.get();
    root.querySelectorAll('fieldset[data-appearance] input[type="radio"]').forEach(input => {
      input.checked = input.value === value;
    });
    root.querySelectorAll('a[data-brand-link]').forEach(link => {
      const original = link.dataset.appearanceHref || link.getAttribute('href');
      // The standalone review switches both brands within a single document.
      if (!original || original.startsWith('#/')) return;
      link.dataset.appearanceHref = original;
      try {
        const target = new URL(original, document.baseURI);
        if (!['https:', 'http:', 'file:'].includes(target.protocol)) return;
        target.searchParams.set('appearance', value);
        link.href = target.href;
      } catch (_) { /* Preserve the original link if a preview has no valid base URL. */ }
    });
  }
  function initializeAppearance(root = document) {
    if (!window.WholeMindAppearance) return;
    root.querySelectorAll('fieldset[data-appearance]').forEach(control => {
      control.hidden = false;
      if (control.dataset.appearanceBound) return;
      control.dataset.appearanceBound = 'true';
      control.addEventListener('change', event => {
        if (event.target.matches('input[type="radio"]')) window.WholeMindAppearance.set(event.target.value);
      });
    });
    syncAppearance(root);
  }
  window.addEventListener('beforeprint', () => syncWorksheets());
  window.addEventListener('wholemind:appearance', () => syncAppearance());
  window.initializeWholeMindWorksheets = initializeWorksheets;
  window.initializeWholeMindAppearance = initializeAppearance;
  initializeWorksheets();
  initializeAppearance();
})();
