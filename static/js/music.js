"use strict";
const MusicPlayer = {
    _open: false,
    _audio: new Audio(),

    toggle() {
        this._open = !this._open;
        document.getElementById('music-panel').style.display = this._open ? 'block' : 'none';
        document.getElementById('music-toggle').textContent = this._open ? '✕' : '🎵';
    },

    play(songId, title) {
        this._audio.pause();
        // NetEase direct stream — no iframe, no cross-origin issues
        const url = `https://music.163.com/song/media/outer/url?id=${songId}.mp3`;
        this._audio.src = url;
        this._audio.volume = 0.5;
        this._audio.play().catch(() => {});
        document.getElementById('music-now').textContent = '🎶 ' + title;
        // Also pause BGM
        if (typeof Audio !== 'undefined' && Audio.bgmStop) Audio.bgmStop();
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
        if (action === 'pause') {
            if (this._audio.paused) this._audio.play().catch(()=>{});
            else this._audio.pause();
        } else if (action === 'stop') {
            this._audio.pause();
            this._audio.src = '';
            document.getElementById('music-now').textContent = '';
        }
    },

    setVolume(val) {
        this._audio.volume = val / 100;
    },
};
