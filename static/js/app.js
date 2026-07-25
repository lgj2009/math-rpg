// app.js — SPA router, API helper, global state, toast, modal
const App = {
    state: { player: null },
    baseURL: '/api',

    async api(method, path, body) {
        const opts = { method, headers: { 'Content-Type': 'application/json' } };
        if (body) opts.body = JSON.stringify(body);
        const res = await fetch(`${this.baseURL}${path}`, opts);
        const data = await res.json();
        if (!res.ok) throw new Error(data.detail || 'Request failed');
        return data;
    },

    get(path) { return this.api('GET', path); },
    post(path, body) { return this.api('POST', path, body); },

    toast(msg, type='info') {
        const el = document.createElement('div');
        el.className = `toast toast-${type}`;
        el.textContent = msg;
        document.getElementById('toast-container').appendChild(el);
        setTimeout(() => el.remove(), 3000);
    },

    navigate(page) {
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
        const target = document.getElementById(`page-${page}`);
        if (target) target.classList.add('active');
        const nav = document.querySelector(`[data-page="${page}"]`);
        if (nav) nav.classList.add('active');
        window.location.hash = page;
    },

    async refreshPlayer() {
        if (!this.state.player) return;
        const p = await this.get(`/players/${this.state.player.id}`);
        this.state.player = p;
        this.updateSidebar();
    },

    updateSidebar() {
        const p = this.state.player;
        if (!p) return;
        document.getElementById('sidebar-name').textContent = p.username;
        document.getElementById('sidebar-level').textContent = `Lv.${p.level} ${p.title}`;
        document.getElementById('sidebar-streak').textContent = p.streak_days;
        document.getElementById('sidebar-energy').textContent = p.focus_energy;
        const xpBar = document.getElementById('sidebar-xp-bar');
        if (xpBar) xpBar.innerHTML = Components.xpBar(p);
    },
};

window.addEventListener('DOMContentLoaded', () => {
    const page = window.location.hash.slice(1) || 'dashboard';
    // Check for existing player (localStorage playerId)
    const pid = localStorage.getItem('playerId');
    if (pid) {
        App.get(`/players/${pid}`).then(p => {
            App.state.player = p;
            App.updateSidebar();
        }).catch(() => localStorage.removeItem('playerId'));
    }
    App.navigate(page);
    // If no player, show welcome/create modal
    if (!pid) {
        document.getElementById('page-dashboard').innerHTML = `
            <div class="welcome-screen">
                <h1>⚔️ 数学冒险</h1>
                <p>把刷题变成打怪升级</p>
                <form id="create-player-form">
                    <input id="username-input" placeholder="输入你的冒险者名字" required>
                    <button type="submit">开始冒险</button>
                </form>
            </div>`;
        document.getElementById('create-player-form').onsubmit = async (e) => {
            e.preventDefault();
            const username = document.getElementById('username-input').value;
            const p = await App.post('/players', { username });
            App.state.player = p;
            App.updateSidebar();
            localStorage.setItem('playerId', p.id);
            App.navigate('dashboard');
            if (typeof dashboard !== 'undefined') dashboard.render();
        };
    }
});

window.addEventListener('hashchange', () => {
    const page = window.location.hash.slice(1) || 'dashboard';
    App.navigate(page);
});

// Nav clicks
document.getElementById('sidebar').addEventListener('click', (e) => {
    const nav = e.target.closest('.nav-item');
    if (!nav) return;
    e.preventDefault();
    App.navigate(nav.dataset.page);
});
