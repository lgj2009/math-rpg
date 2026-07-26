"use strict";
const season = {
    render() {
        const p = App.state.player;
        if (!p) { document.getElementById('page-season').innerHTML = '<div class="empty-state"><p>⚠️ 请先创建角色</p></div>'; return; }
        const el = document.getElementById('page-season');
        if (!el) return;
        el.innerHTML = '<h2>🏁 赛季通行证</h2><div class="empty-state"><p style="font-size:48px">🏗️</p><p>赛季系统即将开放</p><p style="color:var(--text-dim)">完成挑战，解锁绝版奖励</p></div>';
    },
};
