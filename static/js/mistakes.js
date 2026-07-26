"use strict";
const mistakes = {
    currentTab: 'list',

    async render() {
        const p = App.state.player;
        if (!p) { document.getElementById('page-mistakes').innerHTML = '<div class="empty-state"><p>⚠️ 请先创建角色</p></div>'; return; }
        const el = document.getElementById('page-mistakes');
        if (!el) return;
        el.innerHTML = `
            <div class="tab-bar">
                <button class="tab-btn active" data-tab="list">📝 错题列表</button>
                <button class="tab-btn" data-tab="gallery">🐉 怪物图鉴</button>
                <button class="tab-btn" data-tab="due">⚔️ 今日讨伐</button>
            </div>
            <div id="mistakes-content" class="mistakes-content"></div>`;
        el.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', () => this.switchTab(btn.dataset.tab));
        });
        this._moduleMap = await this._fetchModuleMap();
        await this.switchTab('list');
    },

    async switchTab(tab) {
        this.currentTab = tab;
        document.querySelectorAll('.tab-btn').forEach(b =>
            b.classList.toggle('active', b.dataset.tab === tab));
        const content = document.getElementById('mistakes-content');
        if (!content) return;
        content.innerHTML = '<div class="loading">⏳ 加载中...</div>';
        try {
            if (tab === 'list') await this.renderMistakeList(content);
            else if (tab === 'gallery') await this.renderGallery(content);
            else if (tab === 'due') await this.renderDueToday(content);
        } catch (e) {
            content.innerHTML = `<div class="error">❌ 加载失败: ${e.message}</div>`;
        }
    },

    async _fetchModuleMap() {
        try { const mods = await App.get('/modules'); const m = {}; mods.forEach(x => { m[x.id] = x; }); return m; }
        catch (_) { return {}; }
    },

    // ═══════════ Tab 1: 错题列表 (三问法) ═══════════

    async renderMistakeList(container) {
        const pid = App.state.player.id;
        const data = await App.get(`/players/${pid}/mistakes`);
        if (!data || data.length === 0) {
            container.innerHTML = '<div class="empty-state">🎉 暂无错题记录</div>';
            return;
        }
        let html = '<div class="mistake-grid">';
        data.forEach(m => {
            const mod = this._moduleMap[m.module_id];
            const modName = mod ? `${mod.icon || ''} ${mod.name}` : `模块#${m.module_id}`;
            const badge = this._errorBadge(m.error_type);
            const dots = m.mastered ? '🟢 已掌握' : `🔄 ${m.retry_count}/2 次重试`;

            html += `<div class="mistake-card ${m.mastered ? 'mastered' : ''}">
                <div class="mc-header">
                    <span class="mc-module">${modName}</span>${badge}
                    <span class="mc-status">${dots}</span>
                </div>
                <div class="mc-question">${m.question}</div>
                <div class="mc-sections">
                    <div class="mc-field"><span class="mc-label">❌ 错在哪：</span>${m.wrong_step || '未记录'}</div>
                    <div class="mc-field"><span class="mc-label">✅ 正解：</span>${m.correct_thought || '未记录'}</div>
                    <div class="mc-field"><span class="mc-label">📌 考点：</span>${m.knowledge_point || '未标记'}</div>
                </div>
                <div class="mc-footer">
                    <span class="mc-date">${this._fmtDate(m.created_date)}</span>
                    ${!m.mastered ? `<button class="btn-retry" onclick="mistakes.startRetry(${m.id})">🔁 重做</button>` : ''}
                </div>
            </div>`;
        });
        html += '</div>';
        container.innerHTML = html;
        App.renderMath(container);
    },

    _errorBadge(type) {
        const m = { calculation: '🔢计算', logic: '🧠逻辑', knowledge_gap: '📖知识漏洞' };
        const c = { calculation: 'badge-calc', logic: 'badge-logic', knowledge_gap: 'badge-gap' };
        return `<span class="error-badge ${c[type] || ''}">${m[type] || type || '未知'}</span>`;
    },

    _fmtDate(d) { if (!d) return ''; const t = new Date(d); return `${t.getFullYear()}-${String(t.getMonth()+1).padStart(2,'0')}-${String(t.getDate()).padStart(2,'0')}`; },

    // ═══════════ Tab 2: 怪物图鉴 ═══════════

    async renderGallery(container) {
        const pid = App.state.player.id;
        const spots = await App.get(`/players/${pid}/blind-spots`);
        if (!spots || spots.length === 0) {
            container.innerHTML = '<div class="empty-state">🎉 暂无活跃怪物，继续刷题吧！</div>';
            return;
        }
        let html = '<div class="boss-grid">';
        spots.forEach(s => { html += Components.bossCard(s); });
        html += '</div>';
        container.innerHTML = html;
        App.renderMath(container);
    },

    // ═══════════ Tab 3: 今日讨伐 ═══════════

    async renderDueToday(container) {
        const pid = App.state.player.id;
        const rounds = await App.get(`/players/${pid}/blind-spots/due-today`);
        if (!rounds || rounds.length === 0) {
            container.innerHTML = '<div class="empty-state">🎉 今日没有待讨伐的怪物，休息一下吧！</div>';
            return;
        }
        let html = '<div class="due-queue">';
        rounds.forEach(r => {
            const roundLabel = {1:'第1轮·今日', 2:'第2轮·第2天', 3:'第3轮·第7天', 4:'第4轮·第21天'}[r.round] || `第${r.round}轮`;
            html += `<div class="due-item">
                <div class="due-header">
                    <span class="due-spot-name">🐉 ${r.spot_name}</span>
                    <span class="due-round">${roundLabel}</span>
                </div>
                <div class="due-question">${r.question}</div>
                <div class="due-action">
                    <input type="text" class="due-answer-input" placeholder="输入答案..." id="da-${r.id}">
                    <button class="btn-attack" onclick="mistakes.submitDueAnswer(${r.id},${r.blind_spot_id},${r.round})">⚔️ 攻击</button>
                </div>
            </div>`;
        });
        html += '</div>';
        container.innerHTML = html;
        App.renderMath(container);
    },

    async submitDueAnswer(roundId, blindSpotId, roundNumber) {
        const inp = document.getElementById(`da-${roundId}`);
        if (!inp || !inp.value.trim()) { App.toast('请输入答案', 'warning'); return; }
        inp.disabled = true;
        try {
            const result = await App.post(`/players/${App.state.player.id}/blind-spots/${blindSpotId}/attack`,
                { answer: inp.value.trim(), round_number: roundNumber });
            App.toast(result.boss_killed ? '🎉 Boss消灭！' : `⚔️ 造成${result.damage}伤害，HP剩余${result.hp_remaining}`, result.boss_killed ? 'success' : 'info');
            if (result.xp_gained) App.toast(`+${result.xp_gained} XP`, 'success');
            App.refreshPlayer();
            const c = document.getElementById('mistakes-content');
            if (this.currentTab === 'due') await this.renderDueToday(c);
        } catch (e) { App.toast('失败: ' + e.message, 'error'); inp.disabled = false; }
    },

    async attackBoss(blindSpotId) {
        try {
            const rounds = await App.get(`/players/${App.state.player.id}/blind-spots/due-today`);
            if (rounds.some(r => r.blind_spot_id === blindSpotId)) { this.switchTab('due'); App.toast('请在上方作答', 'info'); }
            else App.toast('暂无待讨伐轮次，等待复测日', 'warning');
        } catch (e) { App.toast('查询失败: ' + e.message, 'error'); }
    },

    // ═══════════ 重做错题 (真正答题) ═══════════

    startRetry(mistakeId) {
        // Fetch the mistake to get question text
        App.get(`/players/${App.state.player.id}/mistakes`).then(data => {
            const m = data.find(x => x.id === mistakeId);
            if (!m) { App.toast('错题未找到', 'error'); return; }
            const el = document.getElementById('page-mistakes');
            el.innerHTML = `
                <div class="retry-screen">
                    <h3>🔁 重做错题</h3>
                    <div class="retry-question">${m.question}</div>
                    <div class="retry-hint">
                        <span>❌ 上次错误：</span>${m.wrong_step || '未记录'}
                    </div>
                    <input type="text" id="retry-answer" class="answer-input" placeholder="输入你的答案..." autofocus>
                    <div class="retry-buttons">
                        <button class="btn-primary" onclick="mistakes.submitRetry(${mistakeId})">提交答案</button>
                        <button class="btn-secondary" onclick="mistakes.render()">返回</button>
                    </div>
                </div>`;
            document.getElementById('retry-answer').addEventListener('keydown', e => {
                if (e.key === 'Enter') this.submitRetry(mistakeId);
            });
        });
    },

    async submitRetry(mistakeId) {
        const inp = document.getElementById('retry-answer');
        if (!inp || !inp.value.trim()) { App.toast('请输入答案', 'warning'); return; }
        inp.disabled = true;
        try {
            const result = await App.post(`/players/${App.state.player.id}/mistakes/${mistakeId}/retry`,
                { answer: inp.value.trim() });
            if (result.mastered) {
                App.toast('🎉 连续答对！这道题已掌握！', 'success');
                Audio.bossKill && Audio.bossKill();
            } else {
                App.toast(`已记录 (第${result.retry_count}/2次重试)，继续加油！`, 'info');
            }
            if (result.xp_gained) App.toast(`+${result.xp_gained} XP`, 'success');
            App.refreshPlayer();
            this.render();
        } catch (e) { App.toast('提交失败: ' + e.message, 'error'); inp.disabled = false; }
    },
};
