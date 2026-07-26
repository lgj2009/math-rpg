"use strict";
const achievements = {
    async render() {
        const p = App.state.player;
        if (!p) { document.getElementById('page-achievements').innerHTML = '<div class="empty-state"><p>Please login first</p></div>'; return; }
        const el = document.getElementById('page-achievements');
        el.innerHTML = '<div class="loading">Loading achievements...</div>';
        try {
            const data = await App.get(`/achievements/${p.id}?lang=${I18N._lang}`);
            const unlocked = data.filter(a => a.unlocked).length;
            const total = data.length;
            const cats = { combat: '⚔️ 战斗', learning: '📖 学习', streak: '🔥 坚持', social: '🏰 社交', hidden: '🌙 隐藏' };

            let html = `<h2>🏆 成就殿堂</h2>
                <div style="margin-bottom:20px;color:var(--text-secondary)">
                    已解锁 <b style="color:var(--gold)">${unlocked}</b> / ${total} 成就
                    <div class="xp-bar" style="margin-top:8px"><div class="xp-fill" style="width:${Math.round(unlocked/total*100)}%"></div></div>
                </div>`;

            Object.entries(cats).forEach(([cat, label]) => {
                const items = data.filter(a => a.category === cat);
                if (items.length === 0) return;
                html += `<h3 style="margin-top:24px;margin-bottom:12px">${label}</h3><div class="achieve-grid">`;
                items.forEach(a => {
                    const rarityColors = { common: 'var(--text-secondary)', rare: 'var(--sapphire)', epic: 'var(--purple)', legendary: 'var(--gold)' };
                    html += `<div class="achieve-card ${a.unlocked ? 'unlocked' : 'locked'}">
                        <div class="achieve-icon">${a.unlocked ? a.icon : '🔒'}</div>
                        <div class="achieve-name" style="color:${a.unlocked ? rarityColors[a.rarity] || 'var(--text-dim)' : 'var(--text-muted)'}">${a.name}</div>
                        <div class="achieve-desc">${a.unlocked ? a.desc : '???'}</div>
                        <div class="achieve-rarity" style="color:${rarityColors[a.rarity] || 'var(--text-muted)'}">${a.rarity.toUpperCase()}</div>
                    </div>`;
                });
                html += '</div>';
            });

            el.innerHTML = html;
        } catch (e) { el.innerHTML = '<div class="error">Failed to load achievements</div>'; }
    },
};
