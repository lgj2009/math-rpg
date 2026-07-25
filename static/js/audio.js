// audio.js — Web Audio API sound effects (no external files)
"use strict";

const Audio = {
    ctx: null,
    _init() { if (!this.ctx) this.ctx = new (window.AudioContext || window.webkitAudioContext)(); },
    beep(freq, dur, type='square') {
        this._init();
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = type; osc.frequency.value = freq;
        gain.gain.value = 0.1;
        osc.connect(gain); gain.connect(this.ctx.destination);
        osc.start(); osc.stop(this.ctx.currentTime + dur);
    },
    levelUp() { this.beep(523, 0.1); setTimeout(() => this.beep(659, 0.1), 100); setTimeout(() => this.beep(784, 0.2), 200); },
    gachaFlip() { this.beep(200, 0.3, 'triangle'); },
    gachaRare(level) { const f = {rare: 440, epic: 550, legendary: 660, mythic: 880}[level] || 440; this.beep(f, 0.5, 'sine'); },
    bossKill() { for (let i = 0; i < 5; i++) setTimeout(() => this.beep(300 + i*100, 0.1), i*80); },
    click() { this.beep(800, 0.05); },
};
