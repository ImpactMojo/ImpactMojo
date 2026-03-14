/**
 * ImpactMojo Course Progress Tracking System
 * Version 1.0.0 - March 2026
 *
 * Tracks quiz completion per module, persists progress to localStorage
 * and syncs to Supabase user_progress table for authenticated users.
 * When all modules are complete, progress_percentage hits 100% and
 * the existing DB trigger auto-issues a certificate.
 *
 * Usage: Add to any course page:
 *   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
 *   <script src="../../js/course-progress.js"></script>
 */

(function () {
    'use strict';

    // =========================================================
    // CONFIGURATION
    // =========================================================
    const SUPABASE_URL = 'https://ddyszmfffyedolkcugld.supabase.co';
    const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRkeXN6bWZmZnllZG9sa2N1Z2xkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjQ3MzMxMzEsImV4cCI6MjA4MDMwOTEzMX0.vPLlFkC3pqOBtofZ8B6_FBLbRfOKwlyv3DzLvJBS16w';

    const COURSE_NAMES = {
        mel: 'Monitoring, Evaluation & Learning',
        dataviz: 'Data Visualization for Impact',
        devai: 'AI for Development',
        devecon: 'Development Economics',
        gandhi: "Gandhi's Political Thought",
        law: 'Law & Development',
        media: 'Media, Communication & Development',
        SEL: 'Social & Emotional Learning',
        poa: 'Politics of Aspiration'
    };

    // =========================================================
    // DETECT COURSE ID FROM URL
    // =========================================================
    function detectCourseId() {
        const path = window.location.pathname;
        const match = path.match(/\/courses\/([^/]+)/);
        return match ? match[1] : null;
    }

    const courseId = detectCourseId();
    if (!courseId || !COURSE_NAMES[courseId]) return;

    const STORAGE_KEY = 'impactmojo_course_progress_' + courseId;

    // =========================================================
    // STATE
    // =========================================================
    let moduleData = {};    // { module1: { total: 4, correct: Set([0,1,2,3]) }, ... }
    let completedModules = new Set();
    let totalModules = 0;
    let supabaseClient = null;
    let syncTimeout = null;

    // =========================================================
    // INIT SUPABASE (lazy, only if lib loaded)
    // =========================================================
    function getSupabase() {
        if (supabaseClient) return supabaseClient;
        if (window.supabase && window.supabase.createClient) {
            supabaseClient = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
        }
        return supabaseClient;
    }

    // =========================================================
    // SCAN DOM FOR MODULES & QUIZZES
    // =========================================================
    function scanModules() {
        const moduleSections = document.querySelectorAll('section[id^="module"]');
        moduleSections.forEach(function (section) {
            const id = section.id;  // e.g. "module1"
            const gradedQuestions = section.querySelectorAll('.quiz-question[data-correct]');
            if (gradedQuestions.length > 0) {
                moduleData[id] = {
                    total: gradedQuestions.length,
                    correct: new Set(),
                    element: section
                };
            }
        });
        totalModules = Object.keys(moduleData).length;
    }

    // =========================================================
    // LOCALSTORAGE PERSISTENCE
    // =========================================================
    function loadProgress() {
        try {
            var saved = JSON.parse(localStorage.getItem(STORAGE_KEY));
            if (saved && saved.completed) {
                saved.completed.forEach(function (id) {
                    if (moduleData[id]) {
                        completedModules.add(id);
                        // Fill all correct answers so UI shows as done
                        var mod = moduleData[id];
                        for (var i = 0; i < mod.total; i++) {
                            mod.correct.add(i);
                        }
                    }
                });
            }
        } catch (e) { /* ignore parse errors */ }
    }

    function saveProgress() {
        try {
            localStorage.setItem(STORAGE_KEY, JSON.stringify({
                courseId: courseId,
                completed: Array.from(completedModules),
                totalModules: totalModules,
                percentage: Math.round((completedModules.size / totalModules) * 100),
                updatedAt: new Date().toISOString()
            }));
        } catch (e) { /* ignore storage errors */ }
    }

    // =========================================================
    // SUPABASE SYNC (debounced)
    // =========================================================
    function queueSync() {
        if (syncTimeout) clearTimeout(syncTimeout);
        syncTimeout = setTimeout(syncToSupabase, 3000);
    }

    async function syncToSupabase() {
        var sb = getSupabase();
        if (!sb) return;

        try {
            var { data: { user } } = await sb.auth.getUser();
            if (!user) return;

            var percentage = totalModules > 0
                ? Math.round((completedModules.size / totalModules) * 100)
                : 0;

            var isComplete = percentage >= 100;
            var now = new Date().toISOString();

            await sb.from('user_progress').upsert({
                user_id: user.id,
                course_id: courseId,
                course_name: COURSE_NAMES[courseId],
                progress_percentage: percentage,
                last_accessed_at: now,
                started_at: now,
                completed_at: isComplete ? now : null,
                current_section: Array.from(completedModules).sort().pop() || null
            }, {
                onConflict: 'user_id,course_id'
            });
        } catch (e) {
            // Silently fail — user can still track locally
        }
    }

    // =========================================================
    // UI: PROGRESS BAR
    // =========================================================
    function createProgressBar() {
        var bar = document.createElement('div');
        bar.id = 'course-progress-bar';
        bar.innerHTML =
            '<div class="cpb-inner">' +
                '<div class="cpb-label">' +
                    '<span class="cpb-icon">' +
                        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="16" height="16">' +
                            '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>' +
                        '</svg>' +
                    '</span>' +
                    '<span class="cpb-text">Module Progress</span>' +
                    '<span class="cpb-count">0 / ' + totalModules + '</span>' +
                '</div>' +
                '<div class="cpb-track">' +
                    '<div class="cpb-fill" style="width: 0%"></div>' +
                '</div>' +
            '</div>';

        // Insert after reading-progress bar or at top of main-content
        var readingBar = document.getElementById('reading-progress');
        if (readingBar && readingBar.parentNode) {
            readingBar.parentNode.insertBefore(bar, readingBar.nextSibling);
        } else {
            var main = document.querySelector('.main-content');
            if (main) main.insertBefore(bar, main.firstChild);
        }
    }

    function updateProgressBar() {
        var count = completedModules.size;
        var pct = totalModules > 0 ? Math.round((count / totalModules) * 100) : 0;

        var fill = document.querySelector('.cpb-fill');
        var countEl = document.querySelector('.cpb-count');

        if (fill) fill.style.width = pct + '%';
        if (countEl) countEl.textContent = count + ' / ' + totalModules + ' (' + pct + '%)';

        // Change color when complete
        if (pct >= 100) {
            var bar = document.getElementById('course-progress-bar');
            if (bar) bar.classList.add('cpb-complete');
        }
    }

    // =========================================================
    // UI: SIDEBAR CHECKMARKS
    // =========================================================
    function updateSidebarChecks() {
        completedModules.forEach(function (modId) {
            var link = document.querySelector('a.nav-link[href="#' + modId + '"]');
            if (link && !link.querySelector('.cpb-check')) {
                var check = document.createElement('span');
                check.className = 'cpb-check';
                check.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="14" height="14"><path d="M5 13l4 4L19 7"/></svg>';
                link.appendChild(check);
            }
        });
    }

    // =========================================================
    // UI: RESTORE QUIZ VISUAL STATE FOR COMPLETED MODULES
    // =========================================================
    function restoreQuizState() {
        completedModules.forEach(function (modId) {
            var section = document.getElementById(modId);
            if (!section) return;
            var questions = section.querySelectorAll('.quiz-question[data-correct]');
            questions.forEach(function (q) {
                var correct = q.dataset.correct;
                var options = q.querySelectorAll('.quiz-option');
                options.forEach(function (opt) {
                    if (opt.dataset.option === correct) {
                        opt.classList.add('correct');
                        var radio = opt.querySelector('input[type="radio"]');
                        if (radio) radio.checked = true;
                    }
                });
                var feedback = q.querySelector('.quiz-feedback');
                if (feedback) {
                    feedback.textContent = '\u2713 Correct! Well done.';
                    feedback.className = 'quiz-feedback show correct';
                }
                var btn = q.querySelector('.check-answer-btn');
                if (btn) {
                    btn.disabled = true;
                    btn.textContent = 'Completed';
                    btn.style.opacity = '0.6';
                }
            });
        });
    }

    // =========================================================
    // UI: TOAST NOTIFICATION
    // =========================================================
    function showToast(message, type) {
        var existing = document.getElementById('cpb-toast');
        if (existing) existing.remove();

        var toast = document.createElement('div');
        toast.id = 'cpb-toast';
        toast.className = 'cpb-toast' + (type === 'complete' ? ' cpb-toast-complete' : '');
        toast.innerHTML =
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="20" height="20">' +
                '<path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>' +
            '</svg>' +
            '<span>' + message + '</span>';

        document.body.appendChild(toast);

        // Trigger animation
        requestAnimationFrame(function () {
            toast.classList.add('cpb-toast-show');
        });

        setTimeout(function () {
            toast.classList.remove('cpb-toast-show');
            setTimeout(function () { toast.remove(); }, 400);
        }, 3500);
    }

    // =========================================================
    // UI: COMPLETION MODAL
    // =========================================================
    function showCompletionModal() {
        var overlay = document.createElement('div');
        overlay.id = 'cpb-completion-overlay';
        overlay.innerHTML =
            '<div class="cpb-completion-modal">' +
                '<div class="cpb-completion-icon">' +
                    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" width="64" height="64">' +
                        '<path d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5"/>' +
                    '</svg>' +
                '</div>' +
                '<h3>Course Complete!</h3>' +
                '<p>Congratulations! You\'ve completed all modules in <strong>' + COURSE_NAMES[courseId] + '</strong>.</p>' +
                '<p class="cpb-completion-sub">If you\'re logged in, your certificate will be issued automatically. Check your <a href="/account.html">account page</a> to view it.</p>' +
                '<button class="cpb-completion-btn" onclick="this.closest(\'#cpb-completion-overlay\').remove()">Continue</button>' +
            '</div>';

        document.body.appendChild(overlay);
        requestAnimationFrame(function () {
            overlay.classList.add('cpb-overlay-show');
        });
    }

    // =========================================================
    // CORE: HANDLE QUIZ ANSWER (called from enhanced checkAnswer)
    // =========================================================
    function onQuizAnswered(questionEl, isCorrect) {
        if (!isCorrect) return;

        // Find which module this question belongs to
        var section = questionEl.closest('section[id^="module"]');
        if (!section) return;

        var modId = section.id;
        var mod = moduleData[modId];
        if (!mod || completedModules.has(modId)) return;

        // Find index of this question within the module's graded questions
        var gradedQuestions = Array.from(section.querySelectorAll('.quiz-question[data-correct]'));
        var idx = gradedQuestions.indexOf(questionEl);
        if (idx === -1) return;

        mod.correct.add(idx);

        // Check if all questions in this module are correct
        if (mod.correct.size >= mod.total) {
            completedModules.add(modId);
            saveProgress();
            updateProgressBar();
            updateSidebarChecks();
            queueSync();

            var moduleNum = modId.replace('module', '');
            showToast('Module ' + moduleNum + ' complete!');

            // Check if entire course is done
            if (completedModules.size >= totalModules) {
                setTimeout(function () { showCompletionModal(); }, 1000);
            }
        }
    }

    // =========================================================
    // ENHANCE EXISTING checkAnswer FUNCTION
    // =========================================================
    function enhanceCheckAnswer() {
        var originalCheckAnswer = window.checkAnswer;

        window.checkAnswer = function (button) {
            var question = button.closest('.quiz-question');
            var correct = question ? question.dataset.correct : null;
            var selected = question ? question.querySelector('input[type="radio"]:checked') : null;

            // Call original function
            if (typeof originalCheckAnswer === 'function') {
                originalCheckAnswer(button);
            }

            // Notify progress system
            if (selected && correct && selected.value === correct) {
                onQuizAnswered(question, true);
            }
        };
    }

    // =========================================================
    // INJECT STYLES
    // =========================================================
    function injectStyles() {
        var style = document.createElement('style');
        style.textContent =
            /* Progress Bar */
            '#course-progress-bar {' +
                'position: fixed; top: 3px; left: 0; right: 0; z-index: 999;' +
                'padding: 8px 16px; background: rgba(15, 23, 42, 0.95);' +
                'border-bottom: 1px solid rgba(51, 65, 85, 0.5);' +
                'backdrop-filter: blur(12px); transition: all 0.3s ease;' +
            '}' +
            '.cpb-inner { max-width: 900px; margin: 0 auto; }' +
            '.cpb-label {' +
                'display: flex; align-items: center; gap: 8px;' +
                'margin-bottom: 6px; font-size: 0.75rem; color: #94A3B8;' +
            '}' +
            '.cpb-icon { display: flex; align-items: center; color: #0EA5E9; }' +
            '.cpb-text { flex: 1; font-weight: 500; }' +
            '.cpb-count { font-family: "JetBrains Mono", monospace; color: #0EA5E9; font-weight: 600; }' +
            '.cpb-track {' +
                'height: 4px; background: rgba(51, 65, 85, 0.8);' +
                'border-radius: 4px; overflow: hidden;' +
            '}' +
            '.cpb-fill {' +
                'height: 100%; border-radius: 4px;' +
                'background: linear-gradient(90deg, #0EA5E9, #6366F1);' +
                'transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);' +
            '}' +
            '#course-progress-bar.cpb-complete .cpb-fill {' +
                'background: linear-gradient(90deg, #10B981, #0EA5E9);' +
            '}' +
            '#course-progress-bar.cpb-complete .cpb-count { color: #10B981; }' +

            /* Light mode */
            '[data-theme="light"] #course-progress-bar {' +
                'background: rgba(255, 255, 255, 0.95);' +
                'border-bottom-color: rgba(226, 232, 240, 0.8);' +
            '}' +
            '[data-theme="light"] .cpb-label { color: #64748B; }' +
            '[data-theme="light"] .cpb-track { background: #E2E8F0; }' +

            /* Sidebar checkmarks */
            '.cpb-check {' +
                'display: inline-flex; align-items: center; margin-left: auto;' +
                'color: #10B981; flex-shrink: 0;' +
            '}' +

            /* Toast */
            '.cpb-toast {' +
                'position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%) translateY(80px);' +
                'display: flex; align-items: center; gap: 10px;' +
                'padding: 12px 24px; border-radius: 12px;' +
                'background: rgba(15, 23, 42, 0.95); color: #10B981;' +
                'font-size: 0.9rem; font-weight: 600;' +
                'border: 1px solid rgba(16, 185, 129, 0.3);' +
                'box-shadow: 0 8px 30px rgba(0,0,0,0.3);' +
                'backdrop-filter: blur(12px);' +
                'z-index: 10000; opacity: 0;' +
                'transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s ease;' +
            '}' +
            '.cpb-toast-show { transform: translateX(-50%) translateY(0); opacity: 1; }' +
            '.cpb-toast-complete { color: #F59E0B; border-color: rgba(245, 158, 11, 0.3); }' +
            '[data-theme="light"] .cpb-toast { background: rgba(255,255,255,0.95); box-shadow: 0 8px 30px rgba(0,0,0,0.1); }' +

            /* Completion modal */
            '#cpb-completion-overlay {' +
                'position: fixed; inset: 0; z-index: 10001;' +
                'display: flex; align-items: center; justify-content: center;' +
                'background: rgba(0,0,0,0.6); backdrop-filter: blur(8px);' +
                'opacity: 0; transition: opacity 0.4s ease;' +
            '}' +
            '#cpb-completion-overlay.cpb-overlay-show { opacity: 1; }' +
            '.cpb-completion-modal {' +
                'background: #1E293B; border: 1px solid #334155;' +
                'border-radius: 20px; padding: 40px; text-align: center;' +
                'max-width: 440px; width: 90%; box-shadow: 0 20px 60px rgba(0,0,0,0.5);' +
                'transform: scale(0.9); transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);' +
            '}' +
            '.cpb-overlay-show .cpb-completion-modal { transform: scale(1); }' +
            '.cpb-completion-icon { color: #F59E0B; margin-bottom: 16px; }' +
            '.cpb-completion-modal h3 {' +
                'font-size: 1.5rem; color: #F1F5F9; margin: 0 0 12px; font-family: "Poppins", sans-serif;' +
            '}' +
            '.cpb-completion-modal p { color: #94A3B8; line-height: 1.6; margin: 0 0 8px; }' +
            '.cpb-completion-sub { font-size: 0.85rem; color: #64748B; }' +
            '.cpb-completion-sub a { color: #0EA5E9; text-decoration: none; }' +
            '.cpb-completion-btn {' +
                'margin-top: 20px; padding: 10px 32px; border: none; border-radius: 10px;' +
                'background: linear-gradient(135deg, #0EA5E9, #6366F1);' +
                'color: white; font-weight: 600; font-size: 0.95rem;' +
                'cursor: pointer; transition: transform 0.2s ease;' +
            '}' +
            '.cpb-completion-btn:hover { transform: scale(1.05); }' +
            '[data-theme="light"] .cpb-completion-modal { background: #fff; border-color: #E2E8F0; }' +
            '[data-theme="light"] .cpb-completion-modal h3 { color: #1E293B; }' +
            '[data-theme="light"] .cpb-completion-modal p { color: #64748B; }' +

            /* Offset main content for progress bar */
            '.main-content { padding-top: 48px !important; }' +

            /* Responsive */
            '@media (max-width: 900px) {' +
                '#course-progress-bar { padding: 6px 12px; }' +
                '.cpb-label { font-size: 0.7rem; }' +
                '.cpb-track { height: 3px; }' +
            '}';

        document.head.appendChild(style);
    }

    // =========================================================
    // BOOT
    // =========================================================
    function init() {
        scanModules();
        if (totalModules === 0) return;

        injectStyles();
        loadProgress();
        createProgressBar();
        updateProgressBar();
        updateSidebarChecks();
        restoreQuizState();
        enhanceCheckAnswer();

        // Sync on load for authenticated users
        setTimeout(syncToSupabase, 2000);
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
