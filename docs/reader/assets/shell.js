/* Reading shell — top bar, TOC drawer, Tools overlay, themes, Zen mode.
   Expects window.READER = {docKey, kind, ...} set inline by serve.py. */
(function () {
  'use strict';
  const R = window.READER || { kind: 'doc' };
  const H = document.documentElement;
  const SETTINGS_KEY = 'tolstoy_reader_settings';

  // ── Settings (theme/scale/measure applied early by the head snippet) ──
  function loadSettings() {
    try { return JSON.parse(localStorage.getItem(SETTINGS_KEY) || '{}'); }
    catch { return {}; }
  }
  function saveSettings(patch) {
    localStorage.setItem(SETTINGS_KEY, JSON.stringify(Object.assign(loadSettings(), patch)));
  }
  window.readerSettings = { load: loadSettings, save: saveSettings };

  const S = loadSettings();

  // ── Panels: one open at a time, Esc closes ──
  const toc = document.getElementById('toc-drawer');
  const tools = document.getElementById('tools-overlay');
  const notes = document.getElementById('notes-panel');
  const panels = [toc, tools, notes].filter(Boolean);

  function closePanels(except) {
    panels.forEach(p => { if (p !== except) p.classList.remove('open'); });
  }
  function toggle(panel) {
    const opening = !panel.classList.contains('open');
    closePanels(panel);
    panel.classList.toggle('open', opening);
    return opening;
  }
  window.readerPanels = { toggle, closePanels };

  bind('tb-contents', () => toggle(toc));
  bind('tb-tools', () => toggle(tools));
  bind('tb-notes', () => {
    if (toggle(notes)) document.dispatchEvent(new CustomEvent('notes-panel-open'));
  });
  document.querySelectorAll('.panel-close').forEach(btn =>
    btn.addEventListener('click', () => btn.closest('#toc-drawer,#tools-overlay,#notes-panel').classList.remove('open')));

  document.addEventListener('keydown', e => { if (e.key === 'Escape') closePanels(); });
  document.addEventListener('mousedown', e => {
    if (!e.target.closest('#toc-drawer,#tools-overlay,#notes-panel,#topbar')) closePanels();
  });

  function bind(id, fn) {
    const el = document.getElementById(id);
    if (el) el.addEventListener('click', fn);
  }

  // ── TOC from headings (h2 = section; ids assigned to match p-N-M numbering) ──
  (function buildToc() {
    if (!toc) return;
    const list = toc.querySelector('ol');
    const hs = document.querySelectorAll('main h2, main h3');
    let secN = 0;
    hs.forEach(h => {
      if (h.tagName === 'H2') { secN += 1; if (!h.id) h.id = 'sec-' + secN; }
      else if (!h.id) h.id = 'h3-' + Math.random().toString(36).slice(2, 7);
      const li = document.createElement('li');
      if (h.tagName === 'H3') li.className = 'toc-h3';
      const a = document.createElement('a');
      a.href = '#' + h.id;
      a.textContent = h.textContent;
      a.addEventListener('click', e => {
        e.preventDefault();
        h.scrollIntoView({ behavior: 'smooth', block: 'start' });
        history.replaceState(null, '', '#' + h.id);
        toc.classList.remove('open');
      });
      li.appendChild(a);
      list.appendChild(li);
    });
    if (!hs.length) {
      const onpage = toc.querySelector('h3.onpage');
      if (onpage) {                 // hub drawer: no in-page TOC, drop the label + list
        list.remove();
        onpage.remove();
      } else {
        const p = document.createElement('p');
        p.className = 'notes-empty';
        p.textContent = 'No sections in this document.';
        list.replaceWith(p);
      }
    }
  })();

  // ── Display controls ──
  function setScale(v) {
    v = Math.min(1.25, Math.max(0.8, Math.round(v * 100) / 100));
    H.style.setProperty('--font-scale', v);
    saveSettings({ fontScale: v });
  }
  function getScale() { return parseFloat(H.style.getPropertyValue('--font-scale')) || S.fontScale || 1; }
  bind('font-smaller', () => setScale(getScale() - 0.05));
  bind('font-larger', () => setScale(getScale() + 0.05));

  // Paint the fill left of a slider's knob (the track is a plain input).
  function paintSlider(el, colorVar) {
    const pct = ((el.value - el.min) / (el.max - el.min)) * 100;
    el.style.background = `linear-gradient(to right, var(${colorVar}) ${pct}%, var(--slider-track) ${pct}%)`;
  }
  window.paintSlider = paintSlider;

  const measure = document.getElementById('measure-range');
  const measureOut = document.getElementById('measure-out');
  if (measure) {
    measure.value = S.measure || 56;
    measureOut.value = measure.value + ' ch';
    paintSlider(measure, '--accent');
    measure.addEventListener('input', () => {
      H.style.setProperty('--measure', measure.value + 'ch');
      measureOut.value = measure.value + ' ch';
      paintSlider(measure, '--accent');
      saveSettings({ measure: +measure.value });
    });
  }

  document.querySelectorAll('[data-theme-pick]').forEach(btn => {
    btn.addEventListener('click', () => {
      const t = btn.dataset.themePick;
      H.dataset.theme = t;
      saveSettings({ theme: t });
      document.querySelectorAll('[data-theme-pick]').forEach(b =>
        b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'));
    });
    btn.setAttribute('aria-pressed', (H.dataset.theme || 'paper') === btn.dataset.themePick ? 'true' : 'false');
  });

  // ── Layers (works only) ──
  document.querySelectorAll('[data-layer]').forEach(cb => {
    const name = cb.dataset.layer;
    cb.checked = H.dataset['l' + name.charAt(0).toUpperCase() + name.slice(1)] === 'on';
    cb.addEventListener('change', () => {
      H.dataset['l' + name.charAt(0).toUpperCase() + name.slice(1)] = cb.checked ? 'on' : 'off';
      const layers = loadSettings().layers || {};
      layers[name] = cb.checked;
      saveSettings({ layers });
    });
  });

  // ── Version switch: carry the nearest paragraph (the cross-version coordinate) ──
  document.querySelectorAll('a.version-link:not(.current)').forEach(a => {
    a.addEventListener('click', () => {
      const paras = document.querySelectorAll('main [id^="p-"]');
      let target = null;
      for (const p of paras) {
        if (p.getBoundingClientRect().bottom > 80) { target = p; break; }
      }
      if (target) a.href = a.href.split('#')[0] + '#' + target.id;
    });
  });

  // ── Reading-position hairline ──
  const progressFill = document.querySelector('#progress .fill');
  function paintProgress() {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    progressFill.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + '%';
  }
  if (progressFill) {
    addEventListener('scroll', paintProgress, { passive: true });
    paintProgress();
  }

  // ── Zen (fullscreen; chrome fades when idle, returns on mouse-move) ──
  let idleTimer = null;
  function wakeChrome() {
    document.body.classList.add('chrome');
    clearTimeout(idleTimer);
    idleTimer = setTimeout(() => document.body.classList.remove('chrome'), 2500);
  }
  bind('tb-zen', () => {
    if (document.fullscreenElement) document.exitFullscreen();
    else document.documentElement.requestFullscreen().catch(() => {});
  });
  document.addEventListener('fullscreenchange', () => {
    const zen = !!document.fullscreenElement;
    document.body.classList.toggle('zen', zen);
    const icon = document.getElementById('zen-icon');
    if (icon) icon.setAttribute('href', zen ? '#i-min' : '#i-focus');
    if (zen) wakeChrome();
  });
  document.addEventListener('mousemove', () => {
    if (document.body.classList.contains('zen')) wakeChrome();
  });

  // ── Footnote popover (work notes render at the end; hover previews them) ──
  const tooltip = document.getElementById('ann-tooltip');
  document.querySelectorAll('a.noteref').forEach(ref => {
    const note = document.querySelector(ref.getAttribute('href'));
    if (!note || !tooltip) return;
    ref.addEventListener('mouseenter', e => {
      tooltip.textContent = note.textContent.trim();
      tooltip.style.display = 'block';
      tooltip.style.left = Math.min(e.clientX + 12, innerWidth - tooltip.offsetWidth - 12) + 'px';
      tooltip.style.top = Math.max(12, e.clientY - tooltip.offsetHeight - 12) + 'px';
    });
    ref.addEventListener('mouseleave', () => { tooltip.style.display = 'none'; });
  });
})();
