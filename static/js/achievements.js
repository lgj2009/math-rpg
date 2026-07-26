"use strict";
const achievements = {
    render() {
        const p = App.state.player;
        if (!p) { document.getElementById('page-achievements').innerHTML = '<div class="empty-state"><p>⚠️ 请先创建角色</p></div>'; return; }
        const el = document.getElementById('page-achievements');
        if (!el) return;
        el.innerHTML = '<h2>🏆 成就殿堂</h2><div class="empty-state"><p style="font-size:48px">🏗️</p><p>成就系统即将开放</p><p style="color:var(--text-dim)">解锁隐藏成就，获取稀有奖励</p></div>';
    },
};
