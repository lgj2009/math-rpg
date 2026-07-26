"use strict";
const MusicPlayer = {
    _open: false,
    _playerEl: null,

    _getPlayer() {
        if (!this._playerEl) {
            this._playerEl = document.getElementById('music-iframe');
        }
        return this._playerEl;
    },

    toggle() {
        this._open = !this._open;
        document.getElementById('music-panel').style.display = this._open ? 'block' : 'none';
        document.getElementById('music-toggle').textContent = this._open ? '✕' : '🎵';
    },

    play(songId, title) {
        const iframe = this._getPlayer();
        // Official NetEase embed — this works reliably
        iframe.src = `https://music.163.com/outchain/player?type=2&id=${songId}&auto=1&height=66`;
        document.getElementById('music-now').textContent = '🎶 ' + title;
        if (typeof SFX !== 'undefined' && SFX.bgmStop) SFX.bgmStop();
    },

    playCustom() {
        const input = document.getElementById('music-id-input').value.trim();
        if (!input) return;
        let id = input;
        const match = input.match(/id=(\d+)/);
        if (match) id = match[1];
        if (!/^\d+$/.test(id)) { App.toast('请输入有效的歌曲ID或网易云链接', 'warning'); return; }
        this.play(id, '自定义歌曲');
    },

    control(action) {
        const iframe = this._getPlayer();
        if (action === 'pause' || action === 'stop') {
            iframe.src = '';
            document.getElementById('music-now').textContent = '';
        }
    },

    setVolume(val) {
        // Volume for embedded iframe is limited
        const iframe = this._getPlayer();
        if (val < 10) { iframe.src = ''; }
    },
};
