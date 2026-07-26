"use strict";
const season = {
    async render() {
        const p = App.state.player;
        if (!p) { document.getElementById('page-season').innerHTML = '<div class="empty-state"><p>Please login first</p></div>'; return; }
        const el = document.getElementById('page-season');
        el.innerHTML = '<div class="loading">Loading...</div>';
        try {
            const data = await App.get(`/season/${p.id}`);
            const maxXp = data.tiers[data.total_tiers - 1]?.xp || 4000;
            const pct = Math.min(100, Math.round(data.player_xp / maxXp * 100));
            const nextTier = data.tiers.find(t => !t.unlocked);

            // Build tier track
            let trackHTML = '';
            data.tiers.forEach((t, i) => {
                const isCurrent = t.unlocked && (i + 1 >= data.total_tiers || !data.tiers[i + 1].unlocked);
                const state = t.claimed ? 'claimed' : t.unlocked ? 'unlocked' : 'locked';
                const icon = state === 'locked' ? '🔒' : state === 'claimed' ? '✅' : '⭐';

                trackHTML += `
                <div class="sp-tier ${state} ${isCurrent ? 'current' : ''}">
                    <div class="sp-tier-node">
                        <div class="sp-tier-icon">${icon}</div>
                        <div class="sp-tier-num">${t.tier}</div>
                    </div>
                    <div class="sp-tier-card">
                        <div class="sp-tier-header">
                            <span class="sp-tier-label">Tier ${t.tier}</span>
                            <span class="sp-tier-xp">${t.xp} XP</span>
                        </div>
                        <div class="sp-rewards-row">
                            <div class="sp-reward-box free">
                                <span class="sp-reward-track">🎁 免费</span>
                                <span class="sp-reward-item">${t.free.icon} ${t.free.name}</span>
                            </div>
                            <div class="sp-reward-box premium">
                                <span class="sp-reward-track">💎 付费</span>
                                <span class="sp-reward-item">${t.premium.icon} ${t.premium.name}</span>
                            </div>
                        </div>
                        ${state === 'unlocked' ? `<button class="btn-primary" onclick="season._claim(${t.tier})" style="margin-top:8px;width:100%">领取奖励</button>` :
                          state === 'claimed' ? '<div class="sp-claimed-badge">✅ 已领取</div>' :
                          `<div class="sp-lock-info">🔒 还需 ${t.xp - data.player_xp} XP</div>`}
                    </div>
                </div>`;
            });

            el.innerHTML = `
                <div class="sp-header">
                    <div class="sp-header-top">
                        <h2>🏁 ${data.name}</h2>
                        <div class="sp-timer">⏰ ${data.days_left} 天</div>
                    </div>
                    <p class="sp-subtitle">完成练习、击败Boss、每日打卡来获取赛季经验</p>
                </div>

                <div class="sp-progress-bar">
                    <div class="sp-progress-fill" style="width:${pct}%"></div>
                    <div class="sp-progress-text">${data.player_xp} / ${maxXp} XP · Tier ${data.current_tier}/${data.total_tiers}</div>
                </div>

                ${nextTier ? `
                <div class="sp-next-tier">
                    🎯 下一级: Tier ${nextTier.tier} — 还需 <b>${nextTier.xp - data.player_xp} XP</b>
                </div>` : ''}

                <div class="sp-track-label">
                    <span>🎁 赛季奖励</span>
                    <span style="color:var(--text-muted);font-size:11px">Demo 模式 · 全部免费</span>
                </div>

                <div class="sp-track">${trackHTML}</div>

                <div class="sp-xp-sources">
                    <h4>📊 如何获得赛季经验</h4>
                    <div class="sp-source-grid">
                        <div class="sp-source">⚔️ 完成练习 <b>+50 XP</b></div>
                        <div class="sp-source">🐉 击败Boss <b>+100 XP</b></div>
                        <div class="sp-source">🔥 每日打卡 <b>+30 XP</b></div>
                        <div class="sp-source">📖 学习课程 <b>+20 XP</b></div>
                        <div class="sp-source">💬 公会发言 <b>+10 XP</b></div>
                        <div class="sp-source">🏆 解锁成就 <b>+80 XP</b></div>
                    </div>
                </div>`;
        } catch (e) { el.innerHTML = '<div class="error">Failed to load</div>'; }
    },

    async _claim(tier) {
        try {
            const r = await App.post('/season/claim', { player_id: App.state.player.id, tier });
            App.toast(`🎁 ${r.reward.name}`, 'success');
            this.render();
        } catch (e) { App.toast(e.message, 'error'); }
    },
};
