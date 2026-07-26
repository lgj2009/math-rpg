"use strict";
const season = {
    async render() {
        const p = App.state.player;
        if (!p) { document.getElementById('page-season').innerHTML = '<div class="empty-state"><p>Please login first</p></div>'; return; }
        const el = document.getElementById('page-season');
        el.innerHTML = '<div class="loading">Loading season...</div>';
        try {
            const data = await App.get(`/season/${p.id}`);
            const pct = Math.round(data.player_xp / (data.tiers[data.total_tiers - 1]?.xp || 4000) * 100);
            const nextTier = data.tiers.find(t => !t.unlocked);

            let tiersHTML = data.tiers.map((t, i) => {
                const lineY = 20 + i * 60;
                return `<div class="st-wrapper" style="top:${lineY}px">
                    <div class="st-node ${t.unlocked ? 'unlocked' : 'locked'} ${t.claimed ? 'claimed' : ''}">
                        <span>${t.icon || '⭐'}</span>
                    </div>
                    <div class="st-label">
                        <span style="font-weight:700;font-size:13px">Tier ${t.tier}</span>
                        <span style="font-size:11px;color:var(--text-muted)">${t.xp} XP</span>
                    </div>
                    <div class="st-rewards">
                        <span class="st-reward free">🎁 ${t.free.name}</span>
                        <span class="st-reward premium">💎 ${t.premium.name}</span>
                    </div>
                    ${t.unlocked && !t.claimed ? `<button class="btn-retry" onclick="season._claim(${t.tier})" style="font-size:11px;padding:4px 10px">领取</button>` : t.claimed ? '<span style="color:var(--emerald);font-size:11px">✅</span>' : ''}
                </div>`;
            }).join('');

            el.innerHTML = `
                <h2>🏁 ${data.name}</h2>
                <div style="color:var(--text-secondary);margin-bottom:16px">
                    ⏰ ${data.days_left} 天剩余 &nbsp;|&nbsp; 📊 ${data.player_xp} / ${data.tiers[data.total_tiers-1]?.xp || '?'} XP &nbsp;|&nbsp; Tier ${data.current_tier}/${data.total_tiers}
                </div>
                <div class="xp-bar" style="margin-bottom:24px"><div class="xp-fill" style="width:${Math.min(100,pct)}%"></div></div>
                <div class="st-container">${tiersHTML}</div>
                <div style="margin-top:16px;font-size:12px;color:var(--text-muted)">
                    🎁 免费奖励 &nbsp;|&nbsp; 💎 付费奖励
                </div>`;
        } catch (e) { el.innerHTML = '<div class="error">Failed to load season</div>'; }
    },

    async _claim(tier) {
        try {
            const result = await App.post('/season/claim', { player_id: App.state.player.id, tier });
            App.toast(`领取成功: ${result.reward.name}`, 'success');
            this.render();
        } catch (e) { App.toast(e.message, 'error'); }
    },
};
