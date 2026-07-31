/* ============================================================
   Django admin drag-to-reorder for TrainingAudience changelist.
   Requires list_editable to include the 'order' field so the
   hidden number inputs exist in each row. On drop, the inputs
   are updated; the user then clicks Save to persist.
   ============================================================ */

(function () {
    'use strict';

    document.addEventListener('DOMContentLoaded', function () {
        var tbody = document.querySelector('#result_list tbody');
        if (!tbody) return;

        /* ---- inject drag handles & make rows draggable ---- */
        var rows = Array.from(tbody.querySelectorAll('tr'));
        if (!rows.length) return;

        rows.forEach(function (row) {
            /* prepend a handle cell */
            var td = document.createElement('td');
            td.className = 'sortable-handle';
            td.setAttribute('title', 'Drag to reorder');
            td.innerHTML =
                '<span style="cursor:grab;font-size:18px;color:#A63EC5;' +
                'line-height:1;user-select:none;padding:0 8px;" ' +
                'aria-hidden="true">⠿</span>';
            row.insertBefore(td, row.firstChild);
            row.setAttribute('draggable', 'true');
        });

        /* ---- also add a header cell so columns line up ---- */
        var thead = document.querySelector('#result_list thead tr');
        if (thead) {
            var th = document.createElement('th');
            th.scope = 'col';
            th.style.width = '36px';
            thead.insertBefore(th, thead.firstChild);
        }

        /* ---- drag state ---- */
        var dragSrc = null;

        tbody.addEventListener('dragstart', function (e) {
            dragSrc = e.target.closest('tr');
            if (!dragSrc) return;
            e.dataTransfer.effectAllowed = 'move';
            dragSrc.style.opacity = '0.45';
        });

        tbody.addEventListener('dragover', function (e) {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
            var target = e.target.closest('tr');
            clearHighlight();
            if (target && target !== dragSrc) {
                target.style.borderTop = '3px solid #A63EC5';
            }
        });

        tbody.addEventListener('dragleave', function (e) {
            /* only clear when truly leaving tbody */
            if (!tbody.contains(e.relatedTarget)) {
                clearHighlight();
            }
        });

        tbody.addEventListener('drop', function (e) {
            e.preventDefault();
            e.stopPropagation();
            clearHighlight();
            var target = e.target.closest('tr');
            if (!target || target === dragSrc) return;

            /* insert dragged row before the drop target */
            tbody.insertBefore(dragSrc, target);
            syncOrderInputs();
        });

        tbody.addEventListener('dragend', function () {
            clearHighlight();
            if (dragSrc) {
                dragSrc.style.opacity = '';
                dragSrc = null;
            }
        });

        /* ---- helpers ---- */

        function clearHighlight() {
            Array.from(tbody.querySelectorAll('tr')).forEach(function (r) {
                r.style.borderTop = '';
            });
        }

        function syncOrderInputs() {
            /* Assign order values 10, 20, 30 … based on visual position.
               The input name ends with "-order"; list_editable keeps the
               input attached to its original row even after DOM reorder. */
            Array.from(tbody.querySelectorAll('tr')).forEach(function (row, i) {
                var input = row.querySelector('input[name$="-order"]');
                if (input) {
                    input.value = (i + 1) * 10;
                }
            });

            /* Flash a subtle reminder to save */
            flashSaveReminder();
        }

        function flashSaveReminder() {
            var banner = document.getElementById('sp-save-reminder');
            if (!banner) {
                banner = document.createElement('p');
                banner.id = 'sp-save-reminder';
                banner.style.cssText =
                    'background:#fff3cd;border:1px solid #D4AF37;border-radius:6px;' +
                    'padding:8px 16px;margin:12px 0;font-size:13px;font-weight:600;' +
                    'color:#856404;display:none;';
                banner.textContent = 'Order updated — click Save to apply.';
                var table = document.querySelector('#result_list');
                if (table && table.parentNode) {
                    table.parentNode.insertBefore(banner, table);
                }
            }
            banner.style.display = 'block';
        }
    });
})();
