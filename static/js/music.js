"use strict";
const MusicPlayer = {
    _open: false,
    _widget: null,
    _videoId: null,

    // Known working lo-fi study music YouTube IDs
    _presets: [
        {id: 'jfKfPfyJRdk', name: '🎧 lofi hip hop radio'},
        {id: '5qap5aO4i9A', name: '🌙 lofi sleep & study'},
        {id: 'DWcJFNfaw9c', name: '☕ jazz & coffee'},
        {id: 'lTRiuFIWV54', name: '🎹 calm piano'},
    ],

    toggle() {
        this._open = !this._open;
        document.getElementById('music-panel').style.display = this._open ? 'block' : 'none';
        document.getElementById('music-toggle').textContent = this._open ? '✕' : '🎵';
    },

    play(videoId, title) {
        this._videoId = videoId;
        document.getElementById('music-now').textContent = '🎶 ' + title;
        const container = document.getElementById('music-embed-container');
        container.innerHTML = `<iframe width="100%" height="166"
            src="https://www.youtube.com/embed/${videoId}?autoplay=1&controls=0&loop=1"
            frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
        </iframe>`;
        if (typeof SFX !== 'undefined' && SFX.bgmStop) SFX.bgmStop();
    },

    playCustom() {
        const input = document.getElementById('music-id-input').value.trim();
        if (!input) return;
        // Extract YouTube video ID from URL or use raw input
        let id = input;
        const patterns = [
            /[?&]v=([^&]+)/,
            /youtu\.be\/([^?&]+)/,
            /embed\/([^/?]+)/,
        ];
        for (const p of patterns) {
            const m = input.match(p);
            if (m) { id = m[1]; break; }
        }
        if (id.length === 11) {
            this.play(id, '自定义');
        } else {
            App.toast('请输入有效的 YouTube 链接或视频 ID', 'warning');
        }
    },

    stop() {
        document.getElementById('music-embed-container').innerHTML = '';
        document.getElementById('music-now').textContent = '';
        this._videoId = null;
    },
};
