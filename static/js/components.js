// components.js — shared UI widgets
"use strict";

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
        const hpPct = spot.hp_total > 0 ? (spot.hp_current / spot.hp_total) * 100 : 0;
        const hpColor = hpPct > 50 ? 'var(--correct)' : hpPct > 25 ? 'var(--accent)' : 'var(--wrong)';
        return `<div class="boss-card boss-${spot.boss_type || 'normal'}">
            <div class="boss-icon">🐉</div>
            <div class="boss-name">${spot.name}</div>
            <div class="boss-hp-bar"><div class="boss-hp-fill" style="width:${hpPct}%;background:${hpColor}"></div></div>
            <div class="boss-hp-text">HP: ${spot.hp_current}/${spot.hp_total}</div>
            <div class="boss-defeats">🏆 同类击败: ${spot.defeat_count || 0}</div>
            <button class="btn-attack" onclick="mistakes.attackBoss(${spot.id})">⚔️ 攻击</button>
        </div>`;
    },

    gachaReveal(item, container) {
        // 1.5s flip animation: card spins, then reveals rarity with colored glow
        container.innerHTML = `
            <div class="gacha-card gacha-${item.rarity}">
                <div class="gacha-spinner">🎴</div>
                <div class="gacha-result" style="display:none">
                    <div class="gacha-rarity">${item.rarity.toUpperCase()}</div>
                    <div class="gacha-item">${item.item_name}</div>
                </div>
            </div>`;
        const spinner = container.querySelector('.gacha-spinner');
        const result = container.querySelector('.gacha-result');
        Audio.gachaFlip();
        // 1.5s suspense animation
        setTimeout(() => {
            spinner.style.display = 'none';
            result.style.display = 'block';
            Audio.gachaRare(item.rarity);
        }, 1500);
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
