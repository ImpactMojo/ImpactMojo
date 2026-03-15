/**
 * ImpactMojo — Interactive Assessment Component
 * Reusable assessment system for flagship courses.
 *
 * Depends on: ASSESSMENT_DATA (from assessment-data.js)
 *
 * Usage:
 *   <div id="assessment-root" data-course="mel"></div>
 *   <script src="../../js/assessment-data.js"></script>
 *   <script src="../../js/assessments.js"></script>
 */

(function () {
    'use strict';

    /* -------------------------------------------------------
       CONSTANTS
    ------------------------------------------------------- */
    const LS_PREFIX = 'impactmojo_assessment_';

    /* -------------------------------------------------------
       HELPERS
    ------------------------------------------------------- */
    function getStorageKey(courseId) {
        return LS_PREFIX + courseId;
    }

    function loadProgress(courseId) {
        try {
            const raw = localStorage.getItem(getStorageKey(courseId));
            return raw ? JSON.parse(raw) : null;
        } catch (_) {
            return null;
        }
    }

    function saveProgress(courseId, data) {
        try {
            localStorage.setItem(getStorageKey(courseId), JSON.stringify(data));
        } catch (_) { /* quota exceeded — fail silently */ }
    }

    function clearProgress(courseId) {
        try { localStorage.removeItem(getStorageKey(courseId)); } catch (_) {}
    }

    /* -------------------------------------------------------
       INJECT STYLES (once)
    ------------------------------------------------------- */
    function injectStyles() {
        if (document.getElementById('impactmojo-assessment-styles')) return;
        const style = document.createElement('style');
        style.id = 'impactmojo-assessment-styles';
        style.textContent = `
/* ============================================
   ImpactMojo Assessment Component Styles
   ============================================ */

/* -- Modal overlay -- */
.assessment-overlay {
    position: fixed;
    inset: 0;
    z-index: 9999;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(6px);
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease, visibility 0.3s ease;
}
.assessment-overlay.open {
    opacity: 1;
    visibility: visible;
}

/* -- Modal container -- */
.assessment-modal {
    background: var(--secondary-bg, #1E293B);
    border: 1px solid var(--border-color, #334155);
    border-radius: 16px;
    width: 94%;
    max-width: 720px;
    max-height: 90vh;
    overflow-y: auto;
    padding: 2rem 2.25rem;
    position: relative;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
    transform: translateY(20px);
    transition: transform 0.3s ease;
}
.assessment-overlay.open .assessment-modal {
    transform: translateY(0);
}

/* Scrollbar styling */
.assessment-modal::-webkit-scrollbar { width: 6px; }
.assessment-modal::-webkit-scrollbar-track { background: transparent; }
.assessment-modal::-webkit-scrollbar-thumb {
    background: var(--border-color, #334155);
    border-radius: 3px;
}

/* -- Close button -- */
.assessment-close {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: none;
    border: none;
    color: var(--text-secondary, #94A3B8);
    font-size: 1.5rem;
    cursor: pointer;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    transition: background 0.2s, color 0.2s;
}
.assessment-close:hover {
    background: var(--hover-bg, #334155);
    color: var(--text-primary, #F1F5F9);
}

/* -- Header -- */
.assessment-header {
    margin-bottom: 1.5rem;
    padding-right: 2rem;
}
.assessment-header h2 {
    font-family: var(--font-heading, 'Poppins', sans-serif);
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-primary, #F1F5F9);
    margin: 0 0 0.5rem;
}
.assessment-header p {
    color: var(--text-secondary, #94A3B8);
    font-size: 0.95rem;
    margin: 0;
    line-height: 1.5;
}

/* -- Progress bar -- */
.assessment-progress {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 1.75rem;
}
.assessment-progress-bar {
    flex: 1;
    height: 6px;
    background: var(--border-color, #334155);
    border-radius: 3px;
    overflow: hidden;
}
.assessment-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #0EA5E9, #6366F1);
    border-radius: 3px;
    transition: width 0.4s ease;
}
.assessment-progress-text {
    font-size: 0.85rem;
    color: var(--text-muted, #64748B);
    white-space: nowrap;
    font-family: var(--font-mono, monospace);
}

/* -- Question -- */
.assessment-question-block {
    animation: assessFadeIn 0.35s ease;
}
@keyframes assessFadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}
.assessment-question-text {
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-primary, #F1F5F9);
    margin-bottom: 1.25rem;
    line-height: 1.55;
}
.assessment-question-type {
    display: inline-block;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
    background: rgba(14, 165, 233, 0.15);
    color: #0EA5E9;
    margin-bottom: 0.75rem;
    font-weight: 600;
}

/* -- Options -- */
.assessment-options {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
    margin-bottom: 1.5rem;
}
.assessment-option {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    padding: 0.85rem 1rem;
    border: 1px solid var(--border-color, #334155);
    border-radius: 10px;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s;
    background: transparent;
    user-select: none;
}
.assessment-option:hover {
    border-color: #0EA5E9;
    background: rgba(14, 165, 233, 0.06);
}
.assessment-option.selected {
    border-color: #0EA5E9;
    background: rgba(14, 165, 233, 0.1);
}
.assessment-option.correct-answer {
    border-color: #10B981;
    background: rgba(16, 185, 129, 0.1);
}
.assessment-option.incorrect-answer {
    border-color: #EF4444;
    background: rgba(239, 68, 68, 0.1);
}
.assessment-option.disabled {
    pointer-events: none;
    opacity: 0.85;
}
.assessment-option input[type="radio"],
.assessment-option input[type="checkbox"] {
    appearance: none;
    -webkit-appearance: none;
    width: 20px;
    height: 20px;
    min-width: 20px;
    border: 2px solid var(--border-color, #334155);
    border-radius: 50%;
    margin-top: 2px;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s;
    position: relative;
}
.assessment-option input[type="checkbox"] {
    border-radius: 4px;
}
.assessment-option input:checked {
    border-color: #0EA5E9;
    background: #0EA5E9;
}
.assessment-option input:checked::after {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 6px;
    height: 6px;
    background: white;
    border-radius: 50%;
    transform: translate(-50%, -50%);
}
.assessment-option input[type="checkbox"]:checked::after {
    width: 10px;
    height: 6px;
    background: transparent;
    border-left: 2px solid white;
    border-bottom: 2px solid white;
    border-radius: 0;
    transform: translate(-50%, -60%) rotate(-45deg);
}
.assessment-option-label {
    font-size: 0.95rem;
    color: var(--text-primary, #F1F5F9);
    line-height: 1.5;
}

/* -- Feedback -- */
.assessment-feedback {
    padding: 1rem 1.25rem;
    border-radius: 10px;
    margin-bottom: 1.5rem;
    font-size: 0.9rem;
    line-height: 1.55;
    display: none;
}
.assessment-feedback.show { display: block; animation: assessFadeIn 0.3s ease; }
.assessment-feedback.correct {
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.3);
    color: #6EE7B7;
}
.assessment-feedback.incorrect {
    background: rgba(239, 68, 68, 0.1);
    border: 1px solid rgba(239, 68, 68, 0.3);
    color: #FCA5A5;
}
.assessment-feedback strong {
    display: block;
    margin-bottom: 0.35rem;
    font-size: 0.95rem;
}

/* -- Action buttons -- */
.assessment-actions {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
}
.assessment-btn {
    font-family: var(--font-sans, 'Inter', sans-serif);
    font-size: 0.9rem;
    font-weight: 600;
    padding: 0.7rem 1.5rem;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    transition: background 0.2s, transform 0.15s;
}
.assessment-btn:active { transform: scale(0.97); }
.assessment-btn-primary {
    background: linear-gradient(135deg, #0EA5E9, #6366F1);
    color: white;
}
.assessment-btn-primary:hover { background: linear-gradient(135deg, #0284C7, #4F46E5); }
.assessment-btn-primary:disabled {
    opacity: 0.4;
    cursor: not-allowed;
}
.assessment-btn-secondary {
    background: var(--hover-bg, #334155);
    color: var(--text-primary, #F1F5F9);
}
.assessment-btn-secondary:hover { background: var(--border-color, #475569); }

/* -- Summary / Results -- */
.assessment-summary {
    text-align: center;
    animation: assessFadeIn 0.4s ease;
}
.assessment-score-ring {
    width: 140px;
    height: 140px;
    margin: 0 auto 1.5rem;
    position: relative;
}
.assessment-score-ring svg {
    transform: rotate(-90deg);
    width: 140px;
    height: 140px;
}
.assessment-score-ring circle {
    fill: none;
    stroke-width: 8;
    cx: 70;
    cy: 70;
    r: 60;
}
.assessment-score-ring .ring-bg {
    stroke: var(--border-color, #334155);
}
.assessment-score-ring .ring-fill {
    stroke-linecap: round;
    transition: stroke-dashoffset 1.2s ease;
}
.assessment-score-value {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    font-weight: 800;
    font-family: var(--font-heading, 'Poppins', sans-serif);
    color: var(--text-primary, #F1F5F9);
}
.assessment-summary h3 {
    font-family: var(--font-heading, 'Poppins', sans-serif);
    font-size: 1.35rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
    color: var(--text-primary, #F1F5F9);
}
.assessment-summary p {
    color: var(--text-secondary, #94A3B8);
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
    line-height: 1.5;
}
.assessment-summary-stats {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 2rem;
}
.assessment-stat {
    text-align: center;
}
.assessment-stat-value {
    font-size: 1.5rem;
    font-weight: 700;
    font-family: var(--font-heading, 'Poppins', sans-serif);
}
.assessment-stat-value.stat-correct { color: #10B981; }
.assessment-stat-value.stat-incorrect { color: #EF4444; }
.assessment-stat-value.stat-total { color: #0EA5E9; }
.assessment-stat-label {
    font-size: 0.8rem;
    color: var(--text-muted, #64748B);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* -- CTA button in course page -- */
.assessment-cta {
    padding: 2.5rem 2rem;
    text-align: center;
}
.assessment-cta h3 {
    font-family: var(--font-heading, 'Poppins', sans-serif);
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--text-primary, #F1F5F9);
    margin-bottom: 0.5rem;
}
.assessment-cta p {
    color: var(--text-secondary, #94A3B8);
    font-size: 0.95rem;
    max-width: 480px;
    margin: 0 auto 1.25rem;
    line-height: 1.5;
}
.assessment-launch-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: var(--font-sans, 'Inter', sans-serif);
    font-size: 1rem;
    font-weight: 600;
    padding: 0.85rem 2rem;
    border: none;
    border-radius: 10px;
    background: linear-gradient(135deg, #0EA5E9, #6366F1);
    color: white;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 4px 15px rgba(14, 165, 233, 0.3);
}
.assessment-launch-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(14, 165, 233, 0.4);
}
.assessment-launch-btn svg {
    width: 20px;
    height: 20px;
    stroke: currentColor;
    stroke-width: 2;
    fill: none;
}
.assessment-resume-note {
    display: block;
    font-size: 0.8rem;
    color: var(--text-muted, #64748B);
    margin-top: 0.75rem;
}

/* -- Responsive -- */
@media (max-width: 640px) {
    .assessment-modal {
        padding: 1.5rem 1.25rem;
        border-radius: 12px;
        max-height: 95vh;
    }
    .assessment-header h2 { font-size: 1.25rem; }
    .assessment-question-text { font-size: 1rem; }
    .assessment-summary-stats { gap: 1.25rem; }
}
`;
        document.head.appendChild(style);
    }

    /* -------------------------------------------------------
       ASSESSMENT ENGINE
    ------------------------------------------------------- */
    function Assessment(courseId) {
        const data = ASSESSMENT_DATA[courseId];
        if (!data) {
            console.warn('[Assessment] No data for course:', courseId);
            return;
        }

        this.courseId = courseId;
        this.data = data;
        this.questions = data.questions;
        this.total = this.questions.length;
        this.currentIndex = 0;
        this.answers = {};      // { questionId: userAnswer }
        this.results = {};      // { questionId: boolean }
        this.submitted = {};    // { questionId: true } — tracks which have been submitted
        this.finished = false;

        // Restore progress
        const saved = loadProgress(courseId);
        if (saved) {
            this.currentIndex = saved.currentIndex || 0;
            this.answers = saved.answers || {};
            this.results = saved.results || {};
            this.submitted = saved.submitted || {};
            this.finished = saved.finished || false;
        }

        // Build UI
        this.overlay = null;
        this.modal = null;
        this._buildOverlay();
    }

    Assessment.prototype.persist = function () {
        saveProgress(this.courseId, {
            currentIndex: this.currentIndex,
            answers: this.answers,
            results: this.results,
            submitted: this.submitted,
            finished: this.finished
        });
    };

    Assessment.prototype.open = function () {
        this.overlay.classList.add('open');
        document.body.style.overflow = 'hidden';
        if (this.finished) {
            this._renderSummary();
        } else {
            this._renderQuestion();
        }
    };

    Assessment.prototype.close = function () {
        this.overlay.classList.remove('open');
        document.body.style.overflow = '';
    };

    Assessment.prototype.restart = function () {
        this.currentIndex = 0;
        this.answers = {};
        this.results = {};
        this.submitted = {};
        this.finished = false;
        clearProgress(this.courseId);
        this._renderQuestion();
    };

    /* -- Build overlay / modal skeleton -- */
    Assessment.prototype._buildOverlay = function () {
        var self = this;

        this.overlay = document.createElement('div');
        this.overlay.className = 'assessment-overlay';
        this.overlay.setAttribute('role', 'dialog');
        this.overlay.setAttribute('aria-modal', 'true');
        this.overlay.setAttribute('aria-label', this.data.title);

        this.modal = document.createElement('div');
        this.modal.className = 'assessment-modal';

        // Close button
        var closeBtn = document.createElement('button');
        closeBtn.className = 'assessment-close';
        closeBtn.setAttribute('aria-label', 'Close assessment');
        closeBtn.innerHTML = '&times;';
        closeBtn.addEventListener('click', function () { self.close(); });

        this.modal.appendChild(closeBtn);

        // Body container
        this.body = document.createElement('div');
        this.body.className = 'assessment-body';
        this.modal.appendChild(this.body);

        this.overlay.appendChild(this.modal);

        // Close on overlay click
        this.overlay.addEventListener('click', function (e) {
            if (e.target === self.overlay) self.close();
        });

        // Esc key
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && self.overlay.classList.contains('open')) {
                self.close();
            }
        });

        document.body.appendChild(this.overlay);
    };

    /* -- Render current question -- */
    Assessment.prototype._renderQuestion = function () {
        var self = this;
        var q = this.questions[this.currentIndex];
        var isSubmitted = !!this.submitted[q.id];

        var html = '';

        // Header
        html += '<div class="assessment-header">';
        html += '<h2>' + escHtml(this.data.title) + '</h2>';
        html += '</div>';

        // Progress
        var pct = Math.round(((this.currentIndex) / this.total) * 100);
        html += '<div class="assessment-progress">';
        html += '  <div class="assessment-progress-bar"><div class="assessment-progress-fill" style="width:' + pct + '%"></div></div>';
        html += '  <span class="assessment-progress-text">' + (this.currentIndex + 1) + '/' + this.total + '</span>';
        html += '</div>';

        // Question
        html += '<div class="assessment-question-block">';

        var typeLabel = q.type === 'tf' ? 'True / False' : q.type === 'multi' ? 'Multiple Select' : 'Multiple Choice';
        html += '<span class="assessment-question-type">' + typeLabel + '</span>';
        html += '<div class="assessment-question-text">' + escHtml(q.question) + '</div>';

        // Options
        var inputType = q.type === 'multi' ? 'checkbox' : 'radio';
        html += '<div class="assessment-options">';
        q.options.forEach(function (opt) {
            var isSelected = false;
            if (q.type === 'multi') {
                isSelected = Array.isArray(self.answers[q.id]) && self.answers[q.id].indexOf(opt.value) !== -1;
            } else {
                isSelected = self.answers[q.id] === opt.value;
            }

            var optClasses = 'assessment-option';
            if (isSelected) optClasses += ' selected';
            if (isSubmitted) {
                optClasses += ' disabled';
                var isCorrectOpt = q.type === 'multi'
                    ? q.correct.indexOf(opt.value) !== -1
                    : q.correct === opt.value;
                if (isCorrectOpt) {
                    optClasses += ' correct-answer';
                } else if (isSelected && !isCorrectOpt) {
                    optClasses += ' incorrect-answer';
                }
            }

            html += '<label class="' + optClasses + '" data-value="' + opt.value + '">';
            html += '  <input type="' + inputType + '" name="assess-q-' + q.id + '" value="' + opt.value + '"'
                + (isSelected ? ' checked' : '') + (isSubmitted ? ' disabled' : '') + '>';
            html += '  <span class="assessment-option-label">' + escHtml(opt.label) + '</span>';
            html += '</label>';
        });
        html += '</div>';

        // Feedback
        if (isSubmitted) {
            var isCorrect = this.results[q.id];
            html += '<div class="assessment-feedback show ' + (isCorrect ? 'correct' : 'incorrect') + '">';
            html += '<strong>' + (isCorrect ? 'Correct!' : 'Incorrect') + '</strong>';
            html += escHtml(q.explanation);
            html += '</div>';
        } else {
            html += '<div class="assessment-feedback"></div>';
        }

        html += '</div>'; // /question-block

        // Actions
        html += '<div class="assessment-actions">';
        if (!isSubmitted) {
            html += '<button class="assessment-btn assessment-btn-primary" id="assess-submit-btn">Submit Answer</button>';
        } else if (this.currentIndex < this.total - 1) {
            html += '<button class="assessment-btn assessment-btn-primary" id="assess-next-btn">Next Question</button>';
        } else {
            html += '<button class="assessment-btn assessment-btn-primary" id="assess-finish-btn">View Results</button>';
        }
        if (this.currentIndex > 0 && !isSubmitted) {
            html += '<button class="assessment-btn assessment-btn-secondary" id="assess-prev-btn">Back</button>';
        }
        html += '</div>';

        this.body.innerHTML = html;

        // Bind events
        if (!isSubmitted) {
            // Option selection
            var optionEls = this.body.querySelectorAll('.assessment-option');
            optionEls.forEach(function (el) {
                el.addEventListener('click', function () {
                    var val = el.dataset.value;
                    if (q.type === 'multi') {
                        var arr = self.answers[q.id] || [];
                        var idx = arr.indexOf(val);
                        if (idx === -1) { arr.push(val); } else { arr.splice(idx, 1); }
                        self.answers[q.id] = arr;
                    } else {
                        self.answers[q.id] = val;
                    }
                    self.persist();
                    self._renderQuestion(); // re-render to update selection state
                });
            });

            // Submit
            var submitBtn = this.body.querySelector('#assess-submit-btn');
            if (submitBtn) {
                submitBtn.addEventListener('click', function () {
                    self._submitCurrent();
                });
            }

            // Back
            var prevBtn = this.body.querySelector('#assess-prev-btn');
            if (prevBtn) {
                prevBtn.addEventListener('click', function () {
                    self.currentIndex--;
                    self.persist();
                    self._renderQuestion();
                });
            }
        } else {
            // Next
            var nextBtn = this.body.querySelector('#assess-next-btn');
            if (nextBtn) {
                nextBtn.addEventListener('click', function () {
                    self.currentIndex++;
                    self.persist();
                    self._renderQuestion();
                });
            }
            // Finish
            var finishBtn = this.body.querySelector('#assess-finish-btn');
            if (finishBtn) {
                finishBtn.addEventListener('click', function () {
                    self.finished = true;
                    self.persist();
                    self._renderSummary();
                });
            }
        }
    };

    /* -- Submit current answer -- */
    Assessment.prototype._submitCurrent = function () {
        var q = this.questions[this.currentIndex];
        var answer = this.answers[q.id];

        // Validate: ensure something is selected
        if (answer === undefined || answer === null || (Array.isArray(answer) && answer.length === 0)) {
            var fb = this.body.querySelector('.assessment-feedback');
            if (fb) {
                fb.className = 'assessment-feedback show incorrect';
                fb.innerHTML = '<strong>Please select an answer.</strong>';
            }
            return;
        }

        // Check correctness
        var correct;
        if (q.type === 'multi') {
            var sorted = answer.slice().sort();
            var expected = q.correct.slice().sort();
            correct = sorted.length === expected.length && sorted.every(function (v, i) { return v === expected[i]; });
        } else {
            correct = answer === q.correct;
        }

        this.results[q.id] = correct;
        this.submitted[q.id] = true;
        this.persist();
        this._renderQuestion();
    };

    /* -- Render summary -- */
    Assessment.prototype._renderSummary = function () {
        var self = this;
        var correctCount = 0;
        this.questions.forEach(function (q) {
            if (self.results[q.id]) correctCount++;
        });
        var incorrect = this.total - correctCount;
        var pct = Math.round((correctCount / this.total) * 100);
        var passed = pct >= this.data.passingScore;

        var circumference = 2 * Math.PI * 60; // r=60
        var offset = circumference - (pct / 100) * circumference;
        var ringColor = passed ? '#10B981' : '#EF4444';

        var html = '';
        html += '<div class="assessment-summary">';

        // Score ring
        html += '<div class="assessment-score-ring">';
        html += '  <svg viewBox="0 0 140 140">';
        html += '    <circle class="ring-bg" />';
        html += '    <circle class="ring-fill" style="stroke:' + ringColor + '; stroke-dasharray:' + circumference + '; stroke-dashoffset:' + circumference + ';" />';
        html += '  </svg>';
        html += '  <div class="assessment-score-value">' + pct + '%</div>';
        html += '</div>';

        // Message
        if (passed) {
            html += '<h3 style="color:#10B981;">Assessment Passed</h3>';
            html += '<p>Congratulations! You scored ' + pct + '% and met the passing threshold of ' + this.data.passingScore + '%.</p>';
        } else {
            html += '<h3 style="color:#EF4444;">Keep Practising</h3>';
            html += '<p>You scored ' + pct + '%. The passing threshold is ' + this.data.passingScore + '%. Review the course material and try again.</p>';
        }

        // Stats
        html += '<div class="assessment-summary-stats">';
        html += '  <div class="assessment-stat"><div class="assessment-stat-value stat-correct">' + correctCount + '</div><div class="assessment-stat-label">Correct</div></div>';
        html += '  <div class="assessment-stat"><div class="assessment-stat-value stat-incorrect">' + incorrect + '</div><div class="assessment-stat-label">Incorrect</div></div>';
        html += '  <div class="assessment-stat"><div class="assessment-stat-value stat-total">' + this.total + '</div><div class="assessment-stat-label">Total</div></div>';
        html += '</div>';

        // Actions
        html += '<div class="assessment-actions" style="justify-content:center;">';
        html += '  <button class="assessment-btn assessment-btn-primary" id="assess-restart-btn">Retake Assessment</button>';
        html += '  <button class="assessment-btn assessment-btn-secondary" id="assess-close-btn">Close</button>';
        html += '</div>';

        html += '</div>';

        this.body.innerHTML = html;

        // Animate ring
        requestAnimationFrame(function () {
            var ring = self.body.querySelector('.ring-fill');
            if (ring) ring.style.strokeDashoffset = offset;
        });

        // Bind
        var restartBtn = this.body.querySelector('#assess-restart-btn');
        if (restartBtn) restartBtn.addEventListener('click', function () { self.restart(); });
        var closeBtn = this.body.querySelector('#assess-close-btn');
        if (closeBtn) closeBtn.addEventListener('click', function () { self.close(); });
    };

    /* -- Utility -- */
    function escHtml(str) {
        var div = document.createElement('div');
        div.appendChild(document.createTextNode(str));
        return div.innerHTML;
    }

    /* -------------------------------------------------------
       INITIALISE
    ------------------------------------------------------- */
    function init() {
        injectStyles();

        var roots = document.querySelectorAll('[data-course-assessment]');
        roots.forEach(function (root) {
            var courseId = root.getAttribute('data-course-assessment');
            if (!ASSESSMENT_DATA[courseId]) return;

            var assessment = new Assessment(courseId);
            var data = ASSESSMENT_DATA[courseId];
            var saved = loadProgress(courseId);

            // Build CTA
            var cta = document.createElement('div');
            cta.className = 'assessment-cta';

            var btnLabel = 'Start Assessment';
            var resumeNote = '';
            if (saved && saved.finished) {
                var correctCount = 0;
                data.questions.forEach(function (q) {
                    if (saved.results && saved.results[q.id]) correctCount++;
                });
                var prevPct = Math.round((correctCount / data.questions.length) * 100);
                btnLabel = 'View Results';
                resumeNote = 'Last score: ' + prevPct + '% — You can retake the assessment.';
            } else if (saved && saved.currentIndex > 0) {
                btnLabel = 'Resume Assessment';
                resumeNote = 'Progress saved — ' + (saved.currentIndex) + ' of ' + data.questions.length + ' answered.';
            }

            cta.innerHTML =
                '<h3>Course Assessment</h3>' +
                '<p>' + escHtml(data.description) + '</p>' +
                '<button class="assessment-launch-btn">' +
                '  <svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>' +
                '  ' + escHtml(btnLabel) +
                '</button>' +
                (resumeNote ? '<span class="assessment-resume-note">' + escHtml(resumeNote) + '</span>' : '');

            root.appendChild(cta);

            // Bind launch
            var launchBtn = cta.querySelector('.assessment-launch-btn');
            launchBtn.addEventListener('click', function () {
                assessment.open();
            });
        });
    }

    // Run on DOMContentLoaded or immediately if already loaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
