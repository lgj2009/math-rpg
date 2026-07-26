"use strict";
const MusicPlayer = {
    _open: false,
    _videoId: null,

    _presets: [
        {id: 'BV1yJ4m1M7T1', name: '🎧 学习 lofi'},
        {id: 'BV1th4y1m7GJ', name: '🎹 安静钢琴'},
        {id: 'BV15N4y1U7qK', name: '☕ 爵士咖啡'},
        {id: 'BV1RM4y1U7Uh', name: '🌙 深夜自习'},
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
        // Bilibili embed — works in China
        container.innerHTML = `<iframe width="100%" height="200"
            src="https://player.bilibili.com/player.html?bvid=${videoId}&autoplay=1&danmaku=0&high_quality=1&volume=0.5"
            frameborder="0" allow="autoplay" scrolling="no">
        </iframe>`;
        if (typeof SFX !== 'undefined' && SFX.bgmStop) SFX.bgmStop();
    },

    playCustom() {
        const input = document.getElementById('music-id-input').value.trim();
        if (!input) return;
        let id = input;
        // Extract BV id
        const m = input.match(/BV[a-zA-Z0-9]+/);
        if (m) id = m[0];
        if (id.startsWith('BV') && id.length >= 10) {
            this.play(id, '自定义');
        } else {
            App.toast('请输入有效的 Bilibili BV 号或链接', 'warning');
        }
    },

    stop() {
        document.getElementById('music-embed-container').innerHTML = '';
        document.getElementById('music-now').textContent = '';
        this._videoId = null;
    },

    setVolume(val) {
        // Bilibili iframe volume — reload with new volume param
        if (this._videoId) {
            const container = document.getElementById('music-embed-container');
            const v = val / 100;
            container.innerHTML = `<iframe width="100%" height="200"
                src="https://player.bilibili.com/player.html?bvid=${this._videoId}&autoplay=0&danmaku=0&high_quality=1&volume=${v}"
                frameborder="0" allow="autoplay" scrolling="no">
            </iframe>`;
        }
    },
};
