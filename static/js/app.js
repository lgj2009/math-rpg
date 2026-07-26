// app.js — SPA router, API helper, global state, toast, modal
"use strict";

const App = {
    state: { player: null },
    baseURL: '/api',
    _navigating: false,

    async api(method, path, body) {
        const opts = { method, headers: { 'Content-Type': 'application/json' } };
        const token = localStorage.getItem('authToken');
        if (token) opts.headers['Authorization'] = 'Bearer ' + token;
        if (body) opts.body = JSON.stringify(body);
        const res = await fetch(`${this.baseURL}${path}`, opts);
        if (!res.ok) {
            let detail;
            try { const err = await res.json(); detail = err.detail; } catch (_) { /* ignore */ }
            throw new Error(detail || `Request failed: ${res.status}`);
        }
        return res.json();
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
        if (this._navigating) return;
        // If not logged in, always show welcome
        if (!localStorage.getItem('authToken') && page !== 'settings') {
            showWelcome();
            this._navigating = false;
            return;
        }
        this._navigating = true;
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
        const target = document.getElementById(`page-${page}`);
        if (target) target.classList.add('active');
        const nav = document.querySelector(`[data-page="${page}"]`);
        if (nav) nav.classList.add('active');
        window.location.hash = page;
        this._navigating = false;
        // Auto-render page module
        const noPlayerPages = ['settings'];
        if (!this.state.player && !noPlayerPages.includes(page)) {
            target && (target.innerHTML = '<div class="empty-state"><p>⚠️ 请先创建角色</p></div>');
            return;
        }
        const renderers = { dashboard, tasks, learn, practice, mistakes, progress, guild, bank, season, achievements, settings };
        if (renderers[page] && typeof renderers[page].render === 'function') {
            renderers[page].render();
        }
        // Render KaTeX after page content loads (delay for async render)
        setTimeout(() => this.renderMath(), 200);
    },

    renderMath(el) {
        if (typeof katex === 'undefined') return;
        const target = el || document;
        // Simple approach: find ALL text nodes, process $...$ and bare LaTeX
        const walker = document.createTreeWalker(target, NodeFilter.SHOW_TEXT, null);
        const nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);

        for (const node of nodes) {
            const text = node.textContent;
            const parent = node.parentElement;
            if (!parent || parent.tagName === 'SCRIPT' || parent.tagName === 'STYLE' || parent.closest('.katex')) continue;

            let html = text;
            let changed = false;

            // Replace $$...$$ (display math) first, then $...$ (inline math)
            if (text.includes('$$')) {
                const displayRegex = /\$\$([^$]+)\$\$/g;
                let dm;
                while ((dm = displayRegex.exec(text)) !== null) {
                    try {
                        const rendered = katex.renderToString(dm[1].trim(), { throwOnError: false, displayMode: true });
                        html = html.replace(dm[0], rendered);
                        changed = true;
                    } catch(e) {}
                }
            }
            if (html.includes('$')) {
                const regex = /\$([^$]+)\$/g;
                let m;
                while ((m = regex.exec(html)) !== null) {
                    const latex = m[1].trim();
                    const bareCmds = /^\\(sin|cos|tan|cot|sec|csc|log|ln|lim|max|min|sup|inf|det|gcd|Pr|mathbb|mathbf|mathit|mathrm|textrm|text|vec|bar|hat|dot|ddot|widetilde|widehat|overline|underline|overrightarrow|overleftarrow)\s*$/;
                    if (bareCmds.test(latex)) {
                        html = html.replace(m[0], latex.replace(/\\/g, ''));
                        changed = true;
                        continue;
                    }
                    try {
                        const rendered = katex.renderToString(latex, { throwOnError: false });
                        html = html.replace(m[0], rendered);
                        changed = true;
                    } catch(e) {}
                }
            }

            // If no $ delimiters but has LaTeX commands, render whole thing
            if (!text.includes('$') && /\\[a-zA-Z]+/.test(text)) {
                try {
                    html = katex.renderToString(text, { throwOnError: false });
                    changed = true;
                } catch(e) {}
            }

            if (changed) {
                const span = document.createElement('span');
                span.innerHTML = html;
                parent.replaceChild(span, node);
            }
        }
    },

    async refreshPlayer() {
        if (!this.state.player) return;
        try {
            const p = await this.get(`/players/${this.state.player.id}`);
            this.state.player = p;
            this.updateSidebar();
        } catch (e) {
            this.toast('刷新玩家数据失败', 'error');
        }
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

    t(key) { return I18N.t(key); },
};

function showWelcome() {
    localStorage.removeItem('authToken');
    localStorage.removeItem('playerId');
    App.state.player = null;
    const dash = document.getElementById('page-dashboard');
    if (!dash) return;
    dash.classList.add('active');
    dash.innerHTML = `
        <div class="welcome-screen">
            <h1>⚔️ Math RPG</h1>
            <p>Turn study into battle</p>
            <div class="auth-tabs">
                <button class="auth-tab active" onclick="switchAuthTab('login')">Login</button>
                <button class="auth-tab" onclick="switchAuthTab('register')">Register</button>
            </div>
            <form id="auth-form" class="auth-form">
                <input id="auth-email" type="email" placeholder="Email" required>
                <input id="auth-username" type="text" placeholder="Username">
                <input id="auth-password" type="password" placeholder="Password" minlength="4" required>
                <button type="submit" id="auth-btn">Login</button>
            </form>
            <div id="auth-status"></div>
        </div>`;
    setupAuthForm('login');
}

function switchAuthTab(tab) {
    document.querySelectorAll('.auth-tab').forEach(t => t.classList.toggle('active', t.textContent.toLowerCase().includes(tab)));
    setupAuthForm(tab);
}

function setupAuthForm(mode) {
    const form = document.getElementById('auth-form');
    const btn = document.getElementById('auth-btn');
    const userInput = document.getElementById('auth-username');
    btn.textContent = mode === 'login' ? 'Login' : 'Register';
    userInput.style.display = mode === 'login' ? 'none' : 'block';
    userInput.required = mode !== 'login';
    form.onsubmit = async (e) => {
        e.preventDefault();
        const email = document.getElementById('auth-email').value.trim();
        const username = document.getElementById('auth-username').value.trim();
        const password = document.getElementById('auth-password').value;
        const status = document.getElementById('auth-status');
        btn.disabled = true; btn.textContent = '...'; status.textContent = '';
        try {
            const endpoint = mode === 'login' ? '/auth/login' : '/auth/register';
            const body = mode === 'login' ? { email, password } : { email, username, password };
            const result = await App.post(endpoint, body);
            localStorage.setItem('authToken', result.token);
            localStorage.setItem('playerId', String(result.player_id));
            App.state.player = result.player;
            App.updateSidebar();
            App.navigate('dashboard');
            if (typeof dashboard !== 'undefined' && dashboard.render) dashboard.render();
        } catch (err) {
            status.innerHTML = '<span style="color:var(--ruby)">' + (err.message || 'Failed') + '</span>';
            btn.disabled = false; btn.textContent = mode === 'login' ? 'Login' : 'Register';
        }
    };

    // Add forgot password link below form
    if (mode === 'login') {
        const forgot = document.createElement('div');
        forgot.style.cssText = 'text-align:center;margin-top:8px;font-size:12px;color:var(--text-muted);cursor:pointer';
        forgot.textContent = 'Forgot password?';
        forgot.onclick = () => {
            const email = document.getElementById('auth-email').value.trim();
            if (!email) { App.toast('Enter your email first', 'warning'); return; }
            App.post('/auth/forgot-password', { email }).then(r => {
                App.toast('Reset code: ' + r.reset_code, 'info');
                document.getElementById('auth-status').innerHTML = '<span style="color:var(--gold)">Reset code: <b>' + r.reset_code + '</b><br>Use this code as your new password to login</span>';
            }).catch(e => App.toast(e.message, 'error'));
        };
        form.appendChild(forgot);
    }
}

// Auto-start BGM on first user interaction (browser policy)
let _bgmStarted = false;
document.addEventListener('click', () => {
    if (!_bgmStarted) { Audio.bgmStart(); _bgmStarted = true; }
}, { once: true });

window.addEventListener('DOMContentLoaded', () => {
    I18N.applyAll();
    const page = window.location.hash.slice(1) || 'dashboard';
    const token = localStorage.getItem('authToken');

    if (token) {
        App.get('/auth/me').then(user => {
            if (user.player) {
                App.state.player = user.player;
                App.updateSidebar();
                App.navigate(page);
            } else {
                showWelcome();
            }
        }).catch(() => {
            showWelcome();
        });
    } else {
        showWelcome();
    }
});

window.addEventListener('hashchange', () => {
    const page = window.location.hash.slice(1) || 'dashboard';
    App.navigate(page);
    App.refreshPlayer();
});

// Nav clicks
document.getElementById('sidebar').addEventListener('click', (e) => {
    const nav = e.target.closest('.nav-item');
    if (!nav) return;
    e.preventDefault();
    App.navigate(nav.dataset.page);
});
