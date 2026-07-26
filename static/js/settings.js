"use strict";
const settings = {
    _toggleBGM() {
        const on = Audio.bgmToggle();
        const btn = document.getElementById('bgm-btn');
        if (btn) btn.textContent = on ? '🔊 开启' : '🔇 关闭';
    },

    render() {
        const el = document.getElementById('page-settings');
        if (!el) return;
        const t = App.t;
        el.innerHTML = `<h2>${t('settings_title')}</h2>
            <div class="settings-panel">
                <div class="setting-item"><span>${t('settings_theme')}</span><span>${t('settings_theme_val')}</span></div>
                <div class="setting-item">
                    <span>${t('settings_sound')}</span>
                    <button class="btn-retry" onclick="settings._toggleBGM()" id="bgm-btn">${Audio.bgmIsOn() ? '🔊 开启' : '🔇 关闭'}</button>
                </div>
                <div class="setting-item"><span>${t('settings_count')}</span><span>${t('settings_count_val')}</span></div>
                <div class="setting-item">
                    <span>${t('settings_lang')}</span>
                    <select onchange="settings._switchLang(this.value)" style="padding:6px 10px;border:1px solid rgba(255,255,255,0.1);border-radius:var(--radius);background:var(--bg-field);color:var(--text-primary);font-size:13px;outline:none">
                        <option value="zh" ${I18N._lang==='zh'?'selected':''}>🇨🇳 中文</option>
                        <option value="en" ${I18N._lang==='en'?'selected':''}>🇬🇧 English</option>
                        <option value="vi" ${I18N._lang==='vi'?'selected':''}>🇻🇳 Tiếng Việt</option>
                    </select>
                </div>
                <div class="setting-item"><span>${t('settings_reset')}</span><button class="btn-danger" onclick="if(confirm('${t('settings_reset_confirm')}')){localStorage.clear();location.reload();}">${t('settings_reset_btn')}</button></div>
            </div>

            <h2 style="margin-top:32px">${t('settings_feedback')}</h2>
            <div class="settings-panel" style="margin-top:12px">
                <div class="feedback-form">
                    <select id="fb-category" class="fb-select">
                        <option value="bug">${t('settings_fb_bug')}</option>
                        <option value="feature">${t('settings_fb_feature')}</option>
                        <option value="question">${t('settings_fb_question')}</option>
                        <option value="general" selected>${t('settings_fb_other')}</option>
                    </select>
                    <textarea id="fb-message" class="fb-textarea" placeholder="${t('settings_fb_placeholder')}" rows="4" maxlength="5000"></textarea>
                    <div class="fb-footer">
                        <span id="fb-status"></span>
                        <button class="btn-primary" onclick="settings.submitFeedback()">${t('settings_fb_send')}</button>
                    </div>
                </div>
            </div>`;
    },

    _switchLang(lang) {
        I18N.setLang(lang);
        I18N.applyAll();
        App.toast({zh:'语言已切换',en:'Language changed',vi:'Đã đổi ngôn ngữ'}[lang] || 'OK', 'success');
    },

    async submitFeedback() {
        const t = App.t;
        const message = document.getElementById('fb-message').value.trim();
        if (!message) { App.toast('Please enter feedback', 'warning'); return; }
        const status = document.getElementById('fb-status');
        status.textContent = t('settings_fb_sending');
        const btn = document.querySelector('.btn-primary');
        if (btn) btn.disabled = true;
        try {
            const p = App.state.player;
            const result = await App.post('/feedback', {
                player_id: p ? p.id : null, username: p ? p.username : 'Anonymous',
                category: document.getElementById('fb-category').value,
                message: message, page: window.location.hash.slice(1) || 'dashboard',
            });
            status.textContent = result.email_sent ? t('settings_fb_ok') : t('settings_fb_saved');
            document.getElementById('fb-message').value = '';
            App.toast('Feedback sent!', 'success');
        } catch (e) {
            status.textContent = t('settings_fb_fail') + ': ' + (e.message || '');
        }
        if (btn) btn.disabled = false;
    },
};
