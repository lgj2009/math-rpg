// components.js — shared UI widgets
const Components = {
    xpBar(player) {
        const thresholds = [0, 500, 1500, 3500, 7000, 12000, 20000];
        const levels = [1, 5, 10, 15, 20, 25, 30];
        let next = 20000, prev = 0;
        for (let i = 0; i < levels.length; i++) {
            if (player.level >= levels[i]) prev = thresholds[i];
            if (player.level < levels[i]) { next = thresholds[i]; break; }
        }
        if (player.level >= 30) { prev = 20000; next = 20000; }
        const pct = next > prev ? ((player.xp - prev) / (next - prev)) * 100 : 100;
        return `<div class="xp-bar"><div class="xp-fill" style="width:${Math.min(100, Math.max(0, pct))}%"></div></div>`;
    },

    bossCard(spot) {
        // Renders a blind_spot as a monster card with HP bar — placeholder
        return `<div class="boss-card">
            <div class="boss-name">${spot.question_type || 'Unknown'} Boss</div>
            <div class="boss-hp-bar"><div class="boss-hp-fill" style="width:${spot.hp_pct || 100}%"></div></div>
            <div class="boss-hp-text">${spot.hp || '???'} HP</div>
        </div>`;
    },

    gachaReveal(item) {
        // 1.5s flip animation overlay — placeholder
        return `<div class="gacha-reveal">
            <div class="gacha-card gacha-${item.rarity || 'common'}">
                <div class="gacha-front">?</div>
                <div class="gacha-back">${item.name || 'Item'}</div>
            </div>
        </div>`;
    },

    modal(title, content, buttons) {
        // Generic modal — returns Promise that resolves with clicked button value
        return new Promise((resolve) => {
            const overlay = document.getElementById('modal-overlay');
            overlay.style.display = 'flex';
            overlay.innerHTML = `
                <div class="modal-box">
                    <h2>${title}</h2>
                    ${content ? `<p>${content}</p>` : ''}
                    <div class="modal-buttons">
                        ${(buttons || [{label: '确定', value: 'ok'}]).map(b => `<button data-value="${b.value}">${b.label}</button>`).join('')}
                    </div>
                </div>`;
            overlay.querySelectorAll('.modal-buttons button').forEach(btn => {
                btn.addEventListener('click', () => {
                    overlay.style.display = 'none';
                    resolve(btn.dataset.value);
                });
            });
        });
    },
};
