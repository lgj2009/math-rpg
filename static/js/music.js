"use strict";
const MusicPlayer = {
    _open: false,
    _videoId: null,
    _loading: false,

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
        // Check network before attempting to load
        if (!navigator.onLine) {
            App.toast('⚠️ 网络未连接，无法播放音乐', 'warning');
            return;
        }
        this._loading = true;
        this._videoId = videoId;
        document.getElementById('music-now').textContent = '⏳ 加载中...';
        const container = document.getElementById('music-embed-container');

        // Bilibili embed — lazy-load with error handling
        const iframe = document.createElement('iframe');
        iframe.width = '100%';
        iframe.height = '200';
        iframe.frameBorder = '0';
        iframe.allow = 'autoplay';
        iframe.scrolling = 'no';
        iframe.src = `https://player.bilibili.com/player.html?bvid=${videoId}&autoplay=1&danmaku=0&high_quality=1&volume=0.5`;
        iframe.style.borderRadius = '6px';
        iframe.style.background = '#0a0e1a';

        // Handle load success / failure
        iframe.onload = () => {
            this._loading = false;
            document.getElementById('music-now').textContent = '🎶 ' + title;
        };
        iframe.onerror = () => {
            this._loading = false;
            document.getElementById('music-now').textContent = '❌ 加载失败';
            App.toast('⚠️ 音乐加载失败，请检查网络', 'warning');
        };

        container.innerHTML = '';
        container.appendChild(iframe);

        // Timeout: if it doesn't load in 15s, show warning
        clearTimeout(this._loadTimer);
        this._loadTimer = setTimeout(() => {
            if (this._loading) {
                this._loading = false;
                document.getElementById('music-now').textContent = '⏰ 加载超时，请检查网络';
            }
        }, 15000);

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
        clearTimeout(this._loadTimer);
        this._loading = false;
        const container = document.getElementById('music-embed-container');
        container.innerHTML = '';
        document.getElementById('music-now').textContent = '';
        this._videoId = null;
    },

    setVolume(val) {
        // Bilibili iframe volume — reload with new volume param
        if (this._videoId && navigator.onLine) {
            const container = document.getElementById('music-embed-container');
            const v = val / 100;
            const iframe = document.createElement('iframe');
            iframe.width = '100%';
            iframe.height = '200';
            iframe.frameBorder = '0';
            iframe.allow = 'autoplay';
            iframe.scrolling = 'no';
            iframe.src = `https://player.bilibili.com/player.html?bvid=${this._videoId}&autoplay=0&danmaku=0&high_quality=1&volume=${v}`;
            iframe.style.borderRadius = '6px';
            container.innerHTML = '';
            container.appendChild(iframe);
        }
    },
};

// Listen for network changes
window.addEventListener('online', () => {
    if (MusicPlayer._videoId && !MusicPlayer._loading) {
        document.getElementById('music-now').textContent = '🔁 网络已恢复，可重新播放';
    }
});
window.addEventListener('offline', () => {
    if (MusicPlayer._videoId) {
        document.getElementById('music-now').textContent = '⚠️ 网络已断开';
    }
});
