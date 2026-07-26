"use strict";
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
        // NetEase official embed — needs to be visible to play
        const container = document.getElementById('music-embed-container');
        container.innerHTML = `<iframe frameborder="no" border="0" marginwidth="0" marginheight="0"
            width="100%" height="52"
            src="https://music.163.com/outchain/player?type=2&id=${songId}&auto=1&height=32">
        </iframe>`;
        // Pause BGM
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

    stop() {
        document.getElementById('music-embed-container').innerHTML = '';
        document.getElementById('music-now').textContent = '';
        this._currentId = null;
    },
};
