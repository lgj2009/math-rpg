"use strict";
const MusicPlayer = {
    _open: false,
    _station: 'calm',

    toggle() {
        this._open = !this._open;
        document.getElementById('music-panel').style.display = this._open ? 'block' : 'none';
        document.getElementById('music-toggle').textContent = this._open ? '✕' : '🎵';
    },

    switchStation(name, label) {
        this._station = name;
        document.getElementById('music-now').textContent = '🎶 ' + label;
        // Restart BGM with new parameters
        if (typeof SFX !== 'undefined' && SFX.bgmStart) {
            SFX.bgmStop();
            setTimeout(() => SFX.bgmStart(name), 200);
        }
    },

    stop() {
        if (typeof SFX !== 'undefined' && SFX.bgmStop) SFX.bgmStop();
        document.getElementById('music-now').textContent = '';
    },

    setVolume(val) {
        if (typeof SFX !== 'undefined' && SFX._bgmGain) {
            SFX._bgmGain.gain.value = val / 100 * 0.3;
        }
    },
};
