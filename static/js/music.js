"use strict";
const MusicPlayer = {
    _open: false,

    toggle() {
        this._open = !this._open;
        document.getElementById('music-panel').style.display = this._open ? 'block' : 'none';
        document.getElementById('music-toggle').textContent = this._open ? '✕' : '🎵';
    },

    play(trackId, title) {
        document.getElementById('music-now').textContent = '🎶 ' + title;
        // SoundCloud embed — designed for embedding, no cross-origin issues
        const url = `https://api.soundcloud.com/tracks/${trackId}`;
        const embedUrl = `https://w.soundcloud.com/player/?url=${encodeURIComponent(url)}&auto_play=true&visual=false&buying=false&sharing=false&download=false&show_artwork=false`;
        const container = document.getElementById('music-embed-container');
        container.innerHTML = `<iframe width="100%" height="60" scrolling="no" frameborder="no"
            src="${embedUrl}"></iframe>`;
        if (typeof SFX !== 'undefined' && SFX.bgmStop) SFX.bgmStop();
    },

    playCustom() {
        const input = document.getElementById('music-id-input').value.trim();
        if (!input) return;
        // Accept SoundCloud track ID or full URL
        let id = input;
        const match = input.match(/tracks\/(\d+)/);
        if (match) id = match[1];
        if (!/^\d+$/.test(id)) { App.toast('请输入有效的 SoundCloud 歌曲 ID 或链接', 'warning'); return; }
        this.play(id, '自定义歌曲');
    },

    stop() {
        document.getElementById('music-embed-container').innerHTML = '';
        document.getElementById('music-now').textContent = '';
    },
};
