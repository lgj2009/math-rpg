"use strict";
// NetEase Cloud Music mini player
const MusicPlayer = {
    _open: false,
    _currentId: null,
    _currentTitle: '',

    toggle() {
        this._open = !this._open;
        document.getElementById('music-panel').style.display = this._open ? 'block' : 'none';
        document.getElementById('music-toggle').textContent = this._open ? '✕' : '🎵';
    },

    play(songId, title) {
        this._currentId = songId;
        this._currentTitle = title;
        document.getElementById('music-now').textContent = '🎶 ' + title;
        // NetEase iframe player
        const iframe = document.getElementById('music-iframe');
        iframe.style.display = 'block';
        iframe.style.width = '0'; iframe.style.height = '0';
        iframe.src = `https://music.163.com/outchain/player?type=2&id=${songId}&auto=1&height=32`;
        document.getElementById('music-volume').value = 50;
    },

    playCustom() {
        const input = document.getElementById('music-id-input').value.trim();
        if (!input) return;
        // Extract song ID from URL or use raw input
        let id = input;
        const match = input.match(/id=(\d+)/);
        if (match) id = match[1];
        if (!/^\d+$/.test(id)) { App.toast('请输入有效的歌曲ID或网易云链接', 'warning'); return; }
        this.play(id, '自定义歌曲');
    },

    control(action) {
        if (!this._currentId) return;
        const iframe = document.getElementById('music-iframe');
        if (action === 'pause') {
            iframe.src = iframe.src.replace('auto=1', 'auto=0');
        } else if (action === 'stop') {
            iframe.src = '';
            iframe.style.display = 'none';
            document.getElementById('music-now').textContent = '';
            this._currentId = null;
        }
    },

    setVolume(val) {
        // Volume for iframe is limited — this is best-effort
        const iframe = document.getElementById('music-iframe');
        if (val < 30) iframe.style.display = 'none'; // Can't really control iframe volume
        else iframe.style.display = 'block';
    },
};
