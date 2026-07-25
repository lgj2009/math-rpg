"use strict";
// mistakes.js — Mistake book, monster gallery, and due-today attack queue
const mistakes = {
    currentTab: 'list',

    async render() {
        const el = document.getElementById('page-mistakes');
        if (!el) return;
        el.innerHTML = `
            <div class="tab-bar">
                <button class="tab-btn active" data-tab="list">📝 错题列表</button>
                <button class="tab-btn" data-tab="gallery">🐉 怪物图鉴</button>
                <button class="tab-btn" data-tab="due">⚔️ 今日讨伐</button>
            </div>
            <div id="mistakes-content" class="mistakes-content"></div>`;

        // Tab switching
        el.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', () => this.switchTab(btn.dataset.tab));
        });

        // Load module mapping for human-readable names
        this._moduleMap = await this._fetchModuleMap();
        await this.switchTab('list');
    },

    async switchTab(tab) {
        this.currentTab = tab;
        document.querySelectorAll('.tab-btn').forEach(b =>
            b.classList.toggle('active', b.dataset.tab === tab));
        const content = document.getElementById('mistakes-content');
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
        try {
            const modules = await App.get('/modules');
            const map = {};
            modules.forEach(m => { map[m.id] = m; });
            return map;
        } catch (_) {
            return {};
        }
    },

    // ─── Tab 1: Mistake List ────────────────────────────────────────

    async renderMistakeList(container) {
        const pid = App.state.player.id;
        const mistakesData = await App.get(`/players/${pid}/mistakes`);

        if (!mistakesData || mistakesData.length === 0) {
            container.innerHTML = '<div class="empty-state">🎉 暂无错题记录</div>';
            return;
        }

        let html = '<div class="mistake-grid">';
        mistakesData.forEach(m => {
            const mod = this._moduleMap[m.module_id];
            const modName = mod ? `${mod.icon || ''} ${mod.name}` : `模块 #${m.module_id}`;
            const badge = this._errorTypeBadge(m.error_type);
            const statusText = m.mastered
                ? '<span class="mistake-status mastered">✅ 已掌握</span>'
                : `<span class="mistake-status pending">🔄 已重试 ${m.retry_count} 次</span>`;

            html += `
                <div class="mistake-card">
                    <div class="mistake-header">
                        <span class="mistake-module">${modName}</span>
                        ${badge}
                    </div>
                    <div class="mistake-question">${m.question}</div>
                    <div class="mistake-footer">
                        ${statusText}
                        <span class="mistake-date">${this._formatDate(m.created_date)}</span>
                    </div>
                    ${!m.mastered ? `<button class="btn-retry" onclick="mistakes.retryMistake(${m.id})">🔁 重做</button>` : ''}
                </div>`;
        });
        html += '</div>';
        container.innerHTML = html;
    },

    _errorTypeBadge(errorType) {
        const labels = {
            calculation: '计算错误',
            logic: '逻辑错误',
            knowledge_gap: '知识漏洞',
        };
        const label = labels[errorType] || errorType || '未知';
        return `<span class="error-badge error-${errorType || 'unknown'}">${label}</span>`;
    },

    _formatDate(dateStr) {
        if (!dateStr) return '';
        const d = new Date(dateStr);
        return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
    },

    // ─── Tab 2: Monster Gallery ─────────────────────────────────────

    async renderGallery(container) {
        const pid = App.state.player.id;
        const spots = await App.get(`/players/${pid}/blind-spots`);

        if (!spots || spots.length === 0) {
            container.innerHTML = '<div class="empty-state">🎉 暂无活跃怪物，继续刷题吧！</div>';
            return;
        }

        let html = '<div class="boss-grid">';
        spots.forEach(spot => {
            html += Components.bossCard(spot);
        });
        html += '</div>';
        container.innerHTML = html;
    },

    // ─── Tab 3: Due Today ───────────────────────────────────────────

    async renderDueToday(container) {
        const pid = App.state.player.id;
        const rounds = await App.get(`/players/${pid}/blind-spots/due-today`);

        if (!rounds || rounds.length === 0) {
            container.innerHTML = '<div class="empty-state">🎉 今日没有待讨伐的怪物，休息一下吧！</div>';
            return;
        }

        let html = '<div class="due-queue">';
        rounds.forEach(r => {
            const hpBar = r.hp_current > 0
                ? `<span class="due-hp">❤️ ${r.hp_current} HP</span>`
                : '<span class="due-hp slain">💀 已讨伐</span>';
            const status = r.spot_status === 'cleared'
                ? '<span class="due-status done">✅ 已完成</span>'
                : '<span class="due-status active">⚔️ 待讨伐</span>';

            html += `
                <div class="due-item" data-blind-spot-id="${r.blind_spot_id}" data-round="${r.round}">
                    <div class="due-header">
                        <span class="due-spot-name">${r.spot_name}</span>
                        ${hpBar}
                        ${status}
                    </div>
                    <div class="due-question">${r.question}</div>
                    <div class="due-action">
                        <input type="text" class="due-answer-input" placeholder="输入你的答案..." id="due-answer-${r.id}">
                        <button class="btn-attack" onclick="mistakes.submitDueAnswer(${r.id}, ${r.blind_spot_id}, ${r.round})">⚔️ 提交答案</button>
                    </div>
                </div>`;
        });
        html += '</div>';
        container.innerHTML = html;
    },

    async submitDueAnswer(roundId, blindSpotId, roundNumber) {
        const input = document.getElementById(`due-answer-${roundId}`);
        if (!input || !input.value.trim()) {
            App.toast('请输入答案', 'warning');
            return;
        }
        const answer = input.value.trim();
        input.disabled = true;

        try {
            const result = await App.post(
                `/players/${App.state.player.id}/blind-spots/${blindSpotId}/attack`,
                { answer, round_number: roundNumber }
            );
            App.toast(
                result.boss_killed
                    ? `🎉 讨伐成功！造成 ${result.damage} 伤害，BOSS已消灭！`
                    : `⚔️ 造成 ${result.damage} 伤害，剩余 ${result.hp_remaining} HP`,
                result.boss_killed ? 'success' : 'info'
            );
            if (result.xp_gained > 0) {
                App.toast(`+${result.xp_gained} XP`, 'success');
            }
            App.refreshPlayer();
            // Refresh the due-today view
            const content = document.getElementById('mistakes-content');
            await this.renderDueToday(content);
        } catch (e) {
            App.toast('攻击失败: ' + e.message, 'error');
            input.disabled = false;
        }
    },

    // ─── Boss Attack from Gallery ───────────────────────────────────

    async attackBoss(blindSpotId) {
        // Check if there are due-today rounds for this boss
        try {
            const pid = App.state.player.id;
            const rounds = await App.get(`/players/${pid}/blind-spots/due-today`);
            const pending = rounds.filter(r => r.blind_spot_id === blindSpotId);

            if (pending.length > 0) {
                // Navigate to due-today tab with context
                this.switchTab('due');
                App.toast('请先在今日讨伐中作答', 'info');
            } else {
                // No pending rounds — inform the user
                App.toast('当前怪物没有待讨伐的轮次，请等待下次复测日', 'warning');
            }
        } catch (e) {
            App.toast('查询失败: ' + e.message, 'error');
        }
    },

    async retryMistake(mistakeId) {
        // Open a modal for self-graded retry
        const answer = await Components.modal(
            '🔁 重做错题',
            '请重新解答这道题，提交后系统将自动判断掌握情况。',
            [{ label: '我答对了 ✅', value: 'correct' }, { label: '我还不会 ❌', value: 'wrong' }]
        );
        if (!answer) return;

        try {
            const result = await App.post(
                `/players/${App.state.player.id}/mistakes/${mistakeId}/retry`,
                { answer: answer === 'correct' ? 'correct' : 'wrong' }
            );
            if (result.mastered) {
                App.toast('🎉 太棒了！这道题你已经掌握了！', 'success');
            } else {
                App.toast(`已提交 (第 ${result.retry_count} 次重试)，继续努力！`, 'info');
            }
            if (result.xp_gained > 0) {
                App.toast(`+${result.xp_gained} XP`, 'success');
            }
            App.refreshPlayer();
            // Re-render the mistake list to update status
            const content = document.getElementById('mistakes-content');
            await this.renderMistakeList(content);
        } catch (e) {
            App.toast('提交失败: ' + e.message, 'error');
        }
    },
};
