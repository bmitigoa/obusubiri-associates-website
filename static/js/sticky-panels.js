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

                // Toggle clicked
                if (!isOpen) {
                    openPanel(panel, index);
                } else {
                    // Reopened: keep image on current panel
                    setActiveImage(index);
                }
            });
        });

        /* ---- IntersectionObserver: update image as panels scroll into view ---- */

        var isMobile = function () { return window.innerWidth < 768; };

        var observer = new IntersectionObserver(function (entries) {
            if (isMobile()) return;

            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var idx = panels.indexOf(entry.target);
                    if (idx !== -1) {
                        // Only crossfade the image — don't auto-open the panel
                        setActiveImage(idx);
                    }
                }
            });
        }, {
            threshold: 0.45
        });

        panels.forEach(function (panel) { observer.observe(panel); });

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
