"use strict";
// Visual Novel Engine — dialog, characters, typewriter, choices
const VN = {
    _el: null, _script: null, _lineIdx: 0, _charTimer: null, _callback: null,
    _chars: {
        sage: { name: '欧拉导师', emoji: '🧙', color: '#a78bfa' },
        player: { name: '你', emoji: '⚔️', color: '#f59e0b' },
        system: { name: '', emoji: '📜', color: '#8896ab' },
    },

    // Main entry: start a visual novel script
    start(script, container, onFinish) {
        this._script = script;
        this._lineIdx = 0;
        this._callback = onFinish;
        this._el = container;
        this._el.innerHTML = `<div class="vn-stage" id="vn-stage">
            <div class="vn-char-left" id="vn-char-left"></div>
            <div class="vn-char-right" id="vn-char-right"></div>
            <div class="vn-dialog-box" id="vn-dialog">
                <div class="vn-speaker" id="vn-speaker"></div>
                <div class="vn-text" id="vn-text"></div>
                <div class="vn-choices" id="vn-choices"></div>
                <div class="vn-indicator">▼ 点击继续</div>
            </div>
        </div>`;
        this._el.onclick = () => this._advance();
        this._advance();
    },

    _advance() {
        if (this._charTimer) { clearInterval(this._charTimer); this._charTimer = null; }
        if (this._lineIdx >= this._script.length) {
            this._finish();
            return;
        }
        const line = this._script[this._lineIdx++];
        this._render(line);
    },

    _render(line) {
        const speaker = this._chars[line.char] || this._chars.system;
        const dialog = document.getElementById('vn-dialog');
        const speakerEl = document.getElementById('vn-speaker');
        const textEl = document.getElementById('vn-text');
        const choicesEl = document.getElementById('vn-choices');
        const leftEl = document.getElementById('vn-char-left');
        const rightEl = document.getElementById('vn-char-right');
        const indicator = document.querySelector('.vn-indicator');

        // Set speaker
        speakerEl.textContent = speaker.emoji + ' ' + (speaker.name || '');
        speakerEl.style.color = speaker.color;

        // Position characters
        if (line.char === 'sage') {
            leftEl.innerHTML = `<div class="vn-sprite"><div class="vn-sprite-emoji">🧙</div><div class="vn-sprite-name">欧拉导师</div></div>`;
            leftEl.classList.add('active');
            rightEl.classList.remove('active');
        } else if (line.char === 'player') {
            rightEl.innerHTML = `<div class="vn-sprite"><div class="vn-sprite-emoji">⚔️</div><div class="vn-sprite-name">你</div></div>`;
            rightEl.classList.add('active');
            leftEl.classList.remove('active');
        }

        // Expression override
        if (line.expression) {
            const sprite = document.querySelector('.vn-sprite-emoji');
            if (sprite) sprite.textContent = line.expression;
        }

        // Choices or text
        if (line.choices) {
            indicator.style.display = 'none';
            textEl.textContent = line.text || '';
            choicesEl.innerHTML = line.choices.map((c, i) =>
                `<button class="vn-choice" onclick="event.stopPropagation();VN._choose(${i})">${c.label}</button>`
            ).join('');
            this._el.onclick = null; // disable click-to-advance during choices
        } else {
            indicator.style.display = 'block';
            choicesEl.innerHTML = '';
            this._el.onclick = () => this._advance();
            // Typewriter effect
            this._typewrite(textEl, line.text || '');
        }

        // Background mood
        if (line.bg) {
            document.getElementById('vn-stage').dataset.bg = line.bg;
        }

        // Custom HTML (for embedded canvas etc)
        if (line.html) {
            textEl.innerHTML = line.html;
        }
    },

    _typewrite(el, text) {
        let i = 0;
        el.textContent = '';
        this._charTimer = setInterval(() => {
            if (i < text.length) {
                el.textContent += text[i];
                i++;
            } else {
                clearInterval(this._charTimer);
                this._charTimer = null;
            }
        }, 35);
    },

    _choose(idx) {
        const line = this._script[this._lineIdx - 1]; // current line with choices
        const choice = line.choices[idx];
        // Jump to the labeled section
        if (choice.jump !== undefined) {
            this._lineIdx = choice.jump;
        }
        this._el.onclick = () => this._advance();
        this._advance();
    },

    _finish() {
        this._el.innerHTML = '';
        if (this._callback) this._callback();
    },
};
