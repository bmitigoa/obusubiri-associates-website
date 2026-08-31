/* ============================================================
   STICKY PANELS  — accordion + sticky image crossfade
   No external dependencies. Vanilla JS.
   ============================================================ */

(function () {
    'use strict';

    function initStickyPanels(section) {
        var panels   = Array.from(section.querySelectorAll('.sp-panel'));
        var imgs     = Array.from(section.querySelectorAll('.sp-img'));
        var badge    = section.querySelector('.sp-badge-title');

        if (!panels.length) return;

        /* ---- helpers ---- */

        function setActiveImage(index) {
            imgs.forEach(function (img, i) {
                img.classList.toggle('is-active', i === index);
            });
            if (badge) {
                var panel = panels[index];
                var title = panel ? panel.querySelector('.sp-panel-title') : null;
                badge.textContent = title ? title.textContent : '';
            }
        }

        function openPanel(panel, index) {
            panel.classList.add('is-open');
            panel.querySelector('.sp-toggle').setAttribute('aria-expanded', 'true');
            setActiveImage(index);
        }

        function closePanel(panel) {
            panel.classList.remove('is-open');
            panel.querySelector('.sp-toggle').setAttribute('aria-expanded', 'false');
        }

        /* ---- accordion click ---- */

        panels.forEach(function (panel, index) {
            var btn = panel.querySelector('.sp-toggle');
            if (!btn) return;

            btn.addEventListener('click', function () {
                var isOpen = panel.classList.contains('is-open');

                // Close all
                panels.forEach(function (p) { closePanel(p); });

                // Toggle clicked — open if it was closed, keep image synced if it was already open
                if (!isOpen) {
                    openPanel(panel, index);
                } else {
                    setActiveImage(index);
                }
            });
        });

        /* ---- Open first panel by default ---- */
        openPanel(panels[0], 0);
    }

    /* ---- Boot all instances on the page ---- */

    function boot() {
        var sections = document.querySelectorAll('.sp-section[data-sticky-panels]');
        sections.forEach(function (section) {
            initStickyPanels(section);
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', boot);
    } else {
        boot();
    }

})();
