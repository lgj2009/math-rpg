"use strict";
// practice.js — Combat mode: one Q at a time, instant feedback, combos, boss HP
const practice = {
    _session: null,
    _questionStart: 0,
    _renderId: 0,

    // ─── Module Selector ────────────────────────────────────────────
    async render() {
        const rid = ++this._renderId;
        const p = App.state.player;
        if (!p) { document.getElementById('page-practice').innerHTML = '<div class="empty-state"><p>⚠️ 请先创建角色</p></div>'; return; }
        const main = document.getElementById('page-practice');
        main.innerHTML = '<h2>⚔️ 狩猎场</h2><div id="module-grid" class="module-grid"></div>';
        try {
            const modules = await App.get('/modules');
            if (rid !== this._renderId) return;
            const grid = document.getElementById('module-grid');
            if (!grid) return;
            modules.forEach(m => {
                const card = document.createElement('div');
                card.className = 'module-card';
                const modName = I18N.t('module_' + m.id) || m.name;
                card.innerHTML = `<span class="module-icon">${m.icon}</span>
                    <span class="module-name">${modName}</span>
                    <span class="module-weight">${m.weight}${I18N.t('weight_label')}</span>`;
                card.onclick = () => this.startCombat(m);
                grid.appendChild(card);
            });
        } catch (e) { App.toast('加载失败', 'error'); }
    },

    // ─── Start Combat ──────────────────────────────────────────────
    async startCombat(module) {
        this._renderId++; // cancel any stale module grid render
        const main = document.getElementById('page-practice');
        main.innerHTML = '<div class="loading">⚔️ 准备战斗...</div>';
        try {
            const session = await App.post('/combat/start', {
                player_id: App.state.player.id, module_id: module.id, count: 10, lang: I18N._lang
            });
            this._session = session;
            this._questionStart = Date.now();
            this._renderBoss(session.question, 1);
        } catch (e) { App.toast('该模块暂不可用', 'error'); this.render(); }
    },

    // ─── Boss Intro ────────────────────────────────────────────────
    _renderBoss(q, qNum) {
        const s = this._session;
        const main = document.getElementById('page-practice');
        const hpPct = Math.round((s.total_questions - qNum + 1) / s.total_questions * 100);

        let optionsHTML = '';
        if (q.options && q.options.length) {
            optionsHTML = q.options.map((opt, i) => `
                <label class="option-label" data-value="${String.fromCharCode(65+i)}">
                    <input type="radio" name="answer" value="${String.fromCharCode(65+i)}">
                    <span>${opt}</span>
                </label>`).join('');
        } else {
            optionsHTML = `<input type="text" id="answer-input" class="answer-input" placeholder="输入答案...">`;
        }

        main.innerHTML = `
            <div class="combat-screen">
                <div class="boss-header">
                    <span class="boss-name-display">${s.boss_name}</span>
                    <span class="boss-round">${qNum} / ${s.total_questions}</span>
                </div>
                <div class="boss-hp-bar-large">
                    <div class="boss-hp-fill-large" style="width:${hpPct}%;background:${hpPct>60?'var(--emerald)':hpPct>30?'var(--gold)':'var(--ruby)'}"></div>
                </div>
                <div class="combo-display" id="combo-display"></div>
                <div class="question-card" style="margin-top:16px">
                    ${q.source_ref ? `<div class="question-source">📋 ${q.source_ref}</div>` : ''}
                    <div class="question-content">${q.content}</div>
                    <div class="question-options" id="options-area">${optionsHTML}</div>
                </div>
                <div class="combat-actions">
                    <span class="crit-timer" id="crit-timer">⚡暴击: 15s</span>
                    <button class="btn-primary" onclick="practice._submitAnswer()">⚔️ 攻击</button>
                </div>
                <div id="feedback-area"></div>
            </div>`;
        App.renderMath(main);
        this._questionStart = Date.now();
        this._startCritTimer();

        // Enter key submits
        const inp = document.getElementById('answer-input');
        if (inp) inp.addEventListener('keydown', e => { if (e.key === 'Enter') this._submitAnswer(); });
        // Click on option label selects radio
        document.querySelectorAll('.option-label').forEach(l => {
            l.addEventListener('click', () => {
                const radio = l.querySelector('input[type="radio"]');
                if (radio) radio.checked = true;
            });
        });
    },

    _shareVictory(title, score, accuracy) {
        const text = `⚔️ ${title}！\n📊 得分: ${score} | 正确率: ${accuracy}\n🎮 Math RPG — 把数学变成RPG\n🔗 https://math-rpg-production.up.railway.app\n#高中数学 #游戏化学习`;
        if (navigator.clipboard) {
            navigator.clipboard.writeText(text).then(() => App.toast('已复制分享文案！去小红书/B站/朋友圈粘贴', 'success'));
        } else {
            App.toast(text, 'info');
        }
    },

    _startCritTimer() {
        const el = document.getElementById('crit-timer');
        if (!el) return;
        const update = () => {
            const elapsed = (Date.now() - this._questionStart) / 1000;
            const remaining = Math.max(0, 15 - elapsed);
            if (remaining > 0) {
                el.textContent = `⚡暴击: ${Math.ceil(remaining)}s`;
                el.style.color = 'var(--gold)';
                this._timerId = setTimeout(update, 200);
            } else {
                el.textContent = '⏰ 暴击失效';
                el.style.color = 'var(--text-muted)';
            }
        };
        update();
    },

    // ─── Submit Answer ──────────────────────────────────────────────
    async _submitAnswer() {
        if (this._submitting) return;
        let answer = '';
        const selected = document.querySelector('input[name="answer"]:checked');
        if (selected) { answer = selected.value; }
        else {
            const inp = document.getElementById('answer-input');
            if (inp) answer = inp.value.trim();
        }
        if (!answer) { App.toast('请选择或输入答案', 'warning'); return; }

        this._submitting = true;
        clearTimeout(this._timerId);
        const timeMs = Date.now() - this._questionStart;

        try {
            const result = await App.post('/combat/answer', {
                session_id: this._session.session_id, answer: answer, time_ms: timeMs
            });
            this._showFeedback(result);
        } catch (e) { App.toast('提交失败', 'error'); this._submitting = false; }
    },

    // ─── Feedback ───────────────────────────────────────────────────
    _showFeedback(result) {
        const fb = document.getElementById('feedback-area');
        const comboEl = document.getElementById('combo-display');

        if (result.is_correct) {
            fb.innerHTML = `<div class="fb-correct">
                <span class="fb-icon">✅</span>
                ${result.crit ? '<span class="fb-crit">⚡暴击!</span>' : ''}
                <span class="fb-xp">+${result.xp_gained} XP</span>
                ${result.combo >= 3 ? `<span class="fb-combo">🔥${result.combo}连击!</span>` : ''}
            </div>`;
            SFX.beep && SFX.beep(600, 0.08);
            if (result.crit) SFX.beep && SFX.beep(900, 0.12);
        } else {
            fb.innerHTML = `<div class="fb-wrong">
                <span class="fb-icon">❌</span>
                <span>正确答案: <b>${result.correct_answer}</b></span>
                ${result.solution ? `<div class="fb-solution">💡 ${result.solution}</div>` : ''}
            </div>`;
            SFX.beep && SFX.beep(200, 0.2);
        }
        App.renderMath(fb);

        // Update combo display
        if (result.combo >= 3) {
            comboEl.innerHTML = `<span class="combo-badge combo-${result.combo>=8?'max':result.combo>=5?'high':'mid'}">🔥 ${result.combo} 连击!</span>`;
        } else {
            comboEl.innerHTML = '';
        }

        App.refreshPlayer();

        if (result.finished) {
            // Combat over — show final screen
            setTimeout(() => this._showFinal(result), 1500);
        } else {
            // Next question after short delay
            this._submitting = false;
            setTimeout(() => {
                fb.innerHTML = '';
                this._renderBoss(result.next_question, result.question_number + 1);
                this._submitting = false;
            }, result.is_correct ? 800 : 1800);
        }
    },

    // ─── Final Screen ──────────────────────────────────────────────
    _showFinal(result) {
        const f = result.final;
        const main = document.getElementById('page-practice');
        const pct = Math.round(f.accuracy * 100);

        let reviewHTML = '<div class="review-section"><h3>📋 战斗记录</h3>';
        f.per_question.forEach((q, i) => {
            reviewHTML += `<div class="review-item ${q.is_correct ? 'review-correct' : 'review-wrong'}">
                <div class="review-header">
                    <span>${q.is_correct ? '✅' : '❌'} 第${i+1}题 ${q.crit ? '⚡暴击' : ''} ${q.combo >= 3 ? '🔥'+q.combo+'连击' : ''}</span>
                    <span class="review-diff">+${q.xp} XP</span>
                </div>
                <div class="review-content">${q.content}</div>
                ${!q.is_correct ? `<div class="review-solution">💡 ${q.solution || q.correct_answer}</div>` : ''}
            </div>`;
        });
        reviewHTML += '</div>';

        main.innerHTML = `
            <div class="result-screen">
                <h2>${f.title_emoji} ${f.title}</h2>
                <div style="font-size:48px;margin:12px 0">🐉</div>
                <div class="result-big-number" style="color:${pct>=80?'var(--emerald)':pct>=60?'var(--gold)':'var(--ruby)'}">${f.correct} / ${f.total}</div>
                <div class="result-accuracy">正确率 ${pct}%</div>
                <div style="margin:12px 0;color:var(--text-secondary)">
                    🔥 最大连击: ${f.max_combo} &nbsp;|&nbsp; ⚡ 暴击: ${f.crits}次 &nbsp;|&nbsp; +${f.xp_total} XP
                </div>
                ${f.mistakes_created > 0 ? `<div class="mistake-auto-notice">📝 ${f.mistakes_created}道错题已加入错题本</div>` : ''}
                ${f.tasks_auto_done > 0 ? `<div class="task-auto-notice">📋 ${f.tasks_auto_done}个任务自动完成</div>` : ''}
                <div id="gacha-container"></div>
                ${reviewHTML}
                <button class="btn-primary" onclick="practice.render()">返回狩猎场</button>
                <button class="btn-secondary" onclick="practice._shareVictory('${f.title_emoji} ${f.title}', '${f.correct}/${f.total}', '${pct}%')" style="margin-top:8px">📤 分享战绩</button>
            </div>`;
        App.renderMath(main);

        // Gacha reveal
        if (f.gacha_result) {
            setTimeout(() => {
                Components.gachaReveal(f.gacha_result, document.getElementById('gacha-container'));
            }, 500);
        }
        App.refreshPlayer();
        this._submitting = false;
    },
};
