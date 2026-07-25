"use strict";
// practice.js — module selector, question flow, timer, gacha reveal
const practice = {
    currentSession: null,
    currentModule: null,
    currentIndex: 0,
    answers: [],
    timerInterval: null,
    startTime: null,

    async render() {
        const main = document.getElementById('page-practice');
        main.innerHTML = '<h2>⚔️ 狩猎场 — 选择模块</h2><div id="module-grid" class="module-grid"></div>';
        try {
            const modules = await App.get('/modules');
            const grid = document.getElementById('module-grid');
            modules.forEach(m => {
                const card = document.createElement('div');
                card.className = 'module-card';
                card.innerHTML = `<span class="module-icon">${m.icon}</span>
                    <span class="module-name">${m.name}</span>
                    <span class="module-weight">${m.weight}分</span>`;
                card.onclick = () => this.startModule(m);
                grid.appendChild(card);
            });
        } catch (e) {
            App.toast('加载模块列表失败', 'error');
        }
    },

    async startModule(module) {
        this.currentModule = module;
        const count = 10;
        try {
            const session = await App.get(`/modules/${module.id}/practice?player_id=${App.state.player.id}&count=${count}`);
            this.currentSession = session;
            this.currentIndex = 0;
            this.answers = [];
            this.totalStartTime = Date.now();
            this.renderQuestion();
        } catch (e) {
            App.toast('该模块暂无可用的题目', 'error');
        }
    },

    renderQuestion() {
        const q = this.currentSession.questions[this.currentIndex];
        const main = document.getElementById('page-practice');
        const total = this.currentSession.questions.length;
        const idx = this.currentIndex + 1;

        let optionsHTML = '';
        if (q.options) {
            optionsHTML = q.options.map((opt, i) => `
                <label class="option-label">
                    <input type="radio" name="answer" value="${String.fromCharCode(65 + i)}">
                    <span>${opt}</span>
                </label>`).join('');
        } else {
            optionsHTML = `<input type="text" id="answer-input" class="answer-input" placeholder="输入答案...">`;
        }

        main.innerHTML = `
            <div class="question-flow">
                <div class="question-header">
                    <span>${this.currentSession.module_name || ''}</span>
                    <span class="question-counter">${idx} / ${total}</span>
                    <span class="question-timer" id="question-timer">⏱ 0:00</span>
                </div>
                <div class="question-card">
                    <div class="question-content">${q.content}</div>
                    <div class="question-options">${optionsHTML}</div>
                </div>
                <button id="btn-next" class="btn-primary" onclick="practice.nextQuestion()">
                    ${idx === total ? '提交' : '下一题'}
                </button>
            </div>`;
        this.startTimer();
    },

    startTimer() {
        this.totalStartTime = this.totalStartTime || Date.now();
        clearInterval(this.timerInterval);
        this.timerInterval = setInterval(() => {
            const elapsed = Math.floor((Date.now() - this.totalStartTime) / 1000);
            const min = Math.floor(elapsed / 60);
            const sec = elapsed % 60;
            const el = document.getElementById('question-timer');
            if (el) el.textContent = `⏱ ${min}:${String(sec).padStart(2, '0')}`;
        }, 1000);
    },

    nextQuestion() {
        const q = this.currentSession.questions[this.currentIndex];
        let answer;
        if (q.options) {
            const selected = document.querySelector('input[name="answer"]:checked');
            if (!selected) { App.toast('请选择一个答案'); return; }
            answer = selected.value;
        } else {
            answer = document.getElementById('answer-input').value;
            if (!answer.trim()) { App.toast('请输入答案'); return; }
        }
        this.answers.push({ question_id: q.id, answer });

        this.currentIndex++;
        if (this.currentIndex >= this.currentSession.questions.length) {
            this.submit();
        } else {
            this.renderQuestion();
        }
    },

    async submit() {
        clearInterval(this.timerInterval);
        const timeUsed = Math.floor((Date.now() - this.totalStartTime) / 1000);
        try {
            const result = await App.post(`/players/${App.state.player.id}/practice`, {
                session_id: this.currentSession.session_id,
                module_id: this.currentSession.module_id,
                answers: this.answers,
                time_used_sec: timeUsed,
            });
            this.totalStartTime = null;
            this.showResult(result);
        } catch (e) {
            App.toast('提交失败，请重试', 'error');
        }
    },

    showResult(result) {
        const main = document.getElementById('page-practice');
        const pct = Math.round(result.accuracy * 100);
        const emoji = pct >= 90 ? '🎉' : pct >= 70 ? '👍' : '💪';

        main.innerHTML = `
            <div class="result-screen">
                <h2>${emoji} 练习完成</h2>
                <div class="result-big-number">${result.correct} / ${result.total}</div>
                <div class="result-accuracy">正确率 ${pct}%</div>
                <div class="result-xp">+${result.xp_gained} XP</div>
                <div id="gacha-container"></div>
                ${result.near_miss ? `<div class="near-miss-banner">
                    <p>差一点就完美了！三倍奖励等你拿！</p>
                    <button class="btn-primary" onclick="practice.startModule(practice.currentModule)">再来一套 (三倍奖励!)</button>
                </div>` : ''}
                <button class="btn-secondary" onclick="practice.render()">返回模块列表</button>
            </div>`;

        // Gacha reveal animation after a short delay
        setTimeout(() => {
            if (result.gacha_result) {
                Components.gachaReveal(result.gacha_result, document.getElementById('gacha-container'));
            }
        }, 500);
        App.refreshPlayer();
    },
};
