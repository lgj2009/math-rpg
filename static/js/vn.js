"use strict";
// Visual Novel Engine v2 — music, canvas integration, quizzes, rich choices
const VN = {
    _el: null, _script: null, _lineIdx: 0, _charTimer: null, _callback: null,
    _music: null, // current music mood
    _chars: {
        sage:   { name: '欧拉导师', emoji: '🧙', color: '#a78bfa' },
        player: { name: '你',       emoji: '⚔️', color: '#f59e0b' },
        system: { name: '',         emoji: '📜', color: '#8896ab' },
    },

    start(script, container, onFinish) {
        this._script = script;
        this._lineIdx = 0; this._callback = onFinish;
        this._el = container;
        this._el.innerHTML = `<div class="vn-stage" id="vn-stage">
            <div class="vn-char-area">
                <div class="vn-char-slot" id="vn-char-left"></div>
                <div class="vn-char-slot" id="vn-char-right"></div>
            </div>
            <div class="vn-canvas-embed" id="vn-canvas-embed" style="display:none"></div>
            <div class="vn-dialog-box" id="vn-dialog">
                <div class="vn-speaker" id="vn-speaker"></div>
                <div class="vn-text" id="vn-text"></div>
                <div class="vn-choices" id="vn-choices"></div>
                <div class="vn-quiz" id="vn-quiz" style="display:none"></div>
                <div class="vn-indicator">▼ 点击继续</div>
            </div>
        </div>`;
        this._el.onclick = (e) => {
            if (e.target.closest('.vn-choice') || e.target.closest('.vn-quiz-btn') || e.target.closest('#vn-canvas-embed')) return;
            this._advance();
        };
        this._advance();
    },

    _advance() {
        if (this._charTimer) { clearInterval(this._charTimer); this._charTimer = null; }
        if (this._lineIdx >= this._script.length) { this._finish(); return; }
        const line = this._script[this._lineIdx++];
        this._render(line);
    },

    _render(line) {
        const speaker = this._chars[line.char] || this._chars.system;
        const speakerEl = document.getElementById('vn-speaker');
        const textEl = document.getElementById('vn-text');
        const choicesEl = document.getElementById('vn-choices');
        const quizEl = document.getElementById('vn-quiz');
        const leftEl = document.getElementById('vn-char-left');
        const rightEl = document.getElementById('vn-char-right');
        const canvasEmbed = document.getElementById('vn-canvas-embed');
        const indicator = document.querySelector('.vn-indicator');

        // Music mood
        if (line.music && Audio.bgmStart) {
            // Just set a mood — the BGM system handles smooth transitions
            this._music = line.music;
        }

        // Speaker
        speakerEl.textContent = speaker.emoji + ' ' + (speaker.name || '');
        speakerEl.style.color = speaker.color;

        // Character display (safe area above dialog — never blocks clicks)
        const leftEl = document.getElementById('vn-char-left');
        const rightEl = document.getElementById('vn-char-right');
        if (leftEl) leftEl.innerHTML = '';
        if (rightEl) rightEl.innerHTML = '';
        if (line.char === 'sage') {
            if (leftEl) leftEl.innerHTML = `<div class="vn-sprite"><div class="vn-sprite-emoji">${line.expression || speaker.emoji}</div><div class="vn-sprite-name">${speaker.name}</div></div>`;
        } else if (line.char === 'player') {
            if (rightEl) rightEl.innerHTML = `<div class="vn-sprite"><div class="vn-sprite-emoji">${line.expression || speaker.emoji}</div><div class="vn-sprite-name">${speaker.name}</div></div>`;
        }

        // Background
        if (line.bg) document.getElementById('vn-stage').dataset.bg = line.bg;
        if (line.music && Audio.bgmStart) Audio.bgmStart(line.music);

        // Embedded canvas
        if (line.canvas) {
            canvasEmbed.style.display = 'block';
            canvasEmbed.innerHTML = line.canvas;
            // If it's the secant-to-tangent canvas, init it
            if (line.canvas.includes('visual-canvas')) {
                setTimeout(() => { if (typeof learn !== 'undefined' && learn._startSecantCanvas) learn._startSecantCanvas(); }, 200);
            }
        } else {
            canvasEmbed.style.display = 'none';
        }

        // Quiz mode
        if (line.quiz) {
            indicator.style.display = 'none';
            textEl.textContent = line.text || '';
            choicesEl.innerHTML = '';
            quizEl.style.display = 'block';
            const q = line.quiz;
            quizEl.innerHTML = `
                <div class="vn-quiz-q">${q.question}</div>
                <input id="vn-quiz-input" type="text" class="vn-quiz-input" placeholder="${q.placeholder || '输入答案...'}">
                <div class="vn-quiz-btn" id="vn-quiz-submit">确认</div>
                <div id="vn-quiz-feedback"></div>`;
            const quizBtn = document.getElementById('vn-quiz-submit');
            if (quizBtn) {
                quizBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    this._checkQuiz();
                });
            }
            this._quizAnswer = q.answer;
            this._quizCorrectJump = q.correct_jump;
            this._quizWrongJump = q.wrong_jump;
            this._el.onclick = null;
            return;
        }
        quizEl.style.display = 'none';

        // Choices
        if (line.choices) {
            indicator.style.display = 'none';
            textEl.textContent = line.text || '';
            choicesEl.innerHTML = '';
            line.choices.forEach((c, i) => {
                const btn = document.createElement('div');
                btn.className = 'vn-choice';
                btn.textContent = c.label;
                btn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    e.preventDefault();
                    this._choose(i);
                });
                choicesEl.appendChild(btn);
            });
            this._el.onclick = null;
        } else {
            indicator.style.display = 'block';
            choicesEl.innerHTML = '';
            this._el.onclick = (e) => {
                if (e.target.closest('.vn-choice') || e.target.closest('.vn-quiz-btn') || e.target.closest('#vn-canvas-embed')) return;
                this._advance();
            };
            if (line.html) textEl.innerHTML = line.html;
            else this._typewrite(textEl, line.text || '');
        }
    },

    _checkQuiz() {
        const input = document.getElementById('vn-quiz-input');
        const fb = document.getElementById('vn-quiz-feedback');
        const answer = input.value.trim();
        if (this._quizAnswer.split(',').some(a => a.trim().toLowerCase() === answer.toLowerCase())) {
            fb.innerHTML = '<span style="color:var(--emerald);font-weight:700">✅ 正确！</span>';
            setTimeout(() => {
                if (this._quizCorrectJump !== undefined) this._lineIdx = this._quizCorrectJump;
                this._el.onclick = () => this._advance();
                this._advance();
            }, 1200);
        } else {
            fb.innerHTML = `<span style="color:var(--ruby)">❌ 不对。答案是 ${this._quizAnswer.split(',')[0]}</span>`;
            setTimeout(() => {
                if (this._quizWrongJump !== undefined) this._lineIdx = this._quizWrongJump;
                this._el.onclick = () => this._advance();
                this._advance();
            }, 1800);
        }
    },

    _typewrite(el, text) {
        let i = 0; el.textContent = '';
        this._charTimer = setInterval(() => { if (i < text.length) { el.textContent += text[i]; i++; } else clearInterval(this._charTimer); }, 30);
    },

    _choose(idx) {
        const line = this._script[this._lineIdx - 1];
        const choice = line.choices[idx];
        if (choice.jump !== undefined) this._lineIdx = choice.jump;
        this._el.onclick = (e) => {
            if (e.target.closest('.vn-choice') || e.target.closest('.vn-quiz-btn') || e.target.closest('#vn-canvas-embed')) return;
            this._advance();
        };
        this._advance();
    },

    _finish() {
        this._el.innerHTML = '';
        if (this._callback) this._callback();
    },
};
window.VN = VN;
