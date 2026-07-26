"use strict";
const SFX = {
    ctx: null, _bgmOn: false, _bgmNodes: [], _bgmGain: null,

    _init() { if (!this.ctx) this.ctx = new (window.AudioContext || window.webkitAudioContext)(); },

    // ── SFX ────────────────────────────────────────────────────────
    beep(freq, dur, type='square', vol=0.1) {
        this._init();
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = type; osc.frequency.value = freq;
        gain.gain.value = vol;
        osc.connect(gain); gain.connect(this.ctx.destination);
        osc.start(); osc.stop(this.ctx.currentTime + dur);
    },
    levelUp() { this.beep(523, 0.1, 'square', 0.1); setTimeout(() => this.beep(659, 0.1, 'square', 0.1), 100); setTimeout(() => this.beep(784, 0.2, 'square', 0.1), 200); },
    gachaFlip() { this.beep(200, 0.3, 'triangle', 0.08); },
    gachaRare(level) { const f = {rare: 440, epic: 550, legendary: 660, mythic: 880}[level] || 440; this.beep(f, 0.5, 'sine', 0.12); },
    bossKill() { for (let i = 0; i < 5; i++) setTimeout(() => this.beep(300 + i*100, 0.1, 'square', 0.1), i*80); },
    click() { this.beep(800, 0.05, 'square', 0.05); },

    // ── Lo-fi Background Music ──────────────────────────────────────
    bgmToggle() {
        this._init();
        if (this._bgmOn) { this.bgmStop(); return false; }
        else { this.bgmStart(); return true; }
    },

    bgmStart() {
        if (this._bgmOn) return;
        this._init();
        if (this.ctx.state === 'suspended') this.ctx.resume();
        this._bgmOn = true;
        this._bgmNodes = [];

        this._bgmGain = this.ctx.createGain();
        this._bgmGain.gain.value = 0.30;
        this._bgmGain.connect(this.ctx.destination);

        // Jazzy 7th chords — lo-fi progression
        const chords = [
            [220, 262, 330, 392],  // Am7
            [294, 349, 440, 523],  // Dm7
            [196, 247, 330, 392],  // G7
            [262, 330, 392, 494],  // Cmaj7
        ];
        const chordDur = 3.0;

        const playChord = (idx) => {
            if (!this._bgmOn) return;
            const chord = chords[idx % chords.length];
            const t = this.ctx.currentTime;

            chord.forEach((freq, i) => {
                const osc = this.ctx.createOscillator();
                const g = this.ctx.createGain();
                osc.type = i === 0 ? 'sine' : 'triangle';
                osc.frequency.value = freq;
                osc.detune.value = (Math.random() - 0.5) * 10;
                g.gain.setValueAtTime(0, t);
                g.gain.linearRampToValueAtTime(i === 0 ? 0.12 : 0.06, t + 0.8);
                g.gain.linearRampToValueAtTime(i === 0 ? 0.08 : 0.04, t + chordDur - 0.3);
                g.gain.linearRampToValueAtTime(0, t + chordDur + 0.1);
                osc.connect(g); g.connect(this._bgmGain);
                osc.start(t); osc.stop(t + chordDur + 0.3);
                this._bgmNodes.push(osc, g);
            });

            // Lo-fi kick every other chord
            if (idx % 2 === 0) {
                const kick = this.ctx.createOscillator();
                const kg = this.ctx.createGain();
                kick.type = 'sine'; kick.frequency.setValueAtTime(120, t);
                kick.frequency.exponentialRampToValueAtTime(35, t + 0.12);
                kg.gain.setValueAtTime(0.18, t);
                kg.gain.exponentialRampToValueAtTime(0.001, t + 0.25);
                kick.connect(kg); kg.connect(this._bgmGain);
                kick.start(t); kick.stop(t + 0.3);
                this._bgmNodes.push(kick, kg);
            }

            // Hi-hat ticks
            for (let b = 0; b < 4; b++) {
                const ht = t + b * (chordDur / 4);
                const hh = this.ctx.createOscillator();
                const hg = this.ctx.createGain();
                hh.type = 'square'; hh.frequency.value = 6000;
                hg.gain.setValueAtTime(0.025, ht);
                hg.gain.exponentialRampToValueAtTime(0.001, ht + 0.03);
                hh.connect(hg); hg.connect(this._bgmGain);
                hh.start(ht); hh.stop(ht + 0.04);
                this._bgmNodes.push(hh, hg);
            }

            this._bgmChordTimer = setTimeout(() => playChord(idx + 1), chordDur * 1000 - 50);
        };

        // Simple gentle melody
        const melNotes = [523, 587, 659, 523, 440, 494, 523, 392, 440, 523, 587, 659];
        const playMelody = (idx) => {
            if (!this._bgmOn) return;
            const freq = melNotes[idx % melNotes.length];
            const osc = this.ctx.createOscillator();
            const g = this.ctx.createGain();
            osc.type = 'sine';
            osc.frequency.value = freq;
            const t = this.ctx.currentTime;
            const dur = 0.5 + Math.random() * 0.3;
            g.gain.setValueAtTime(0, t);
            g.gain.linearRampToValueAtTime(0.06, t + 0.3);
            g.gain.linearRampToValueAtTime(0, t + dur);
            osc.connect(g); g.connect(this._bgmGain);
            osc.start(t); osc.stop(t + dur + 0.05);
            this._bgmNodes.push(osc, g);
            const nextDelay = 700 + Math.random() * 600;
            this._bgmMelTimer = setTimeout(() => playMelody((idx + 1) % melNotes.length), nextDelay);
        };

        playChord(0);
        setTimeout(() => playMelody(0), 1200);
    },

    bgmStop() {
        this._bgmOn = false;
        clearTimeout(this._bgmChordTimer);
        clearTimeout(this._bgmMelTimer);
        if (this._bgmGain) {
            this._bgmGain.gain.linearRampToValueAtTime(0, this.ctx.currentTime + 0.5);
        }
        setTimeout(() => {
            this._bgmNodes.forEach(n => { try { n.stop(); n.disconnect(); } catch(e){} });
            this._bgmNodes = [];
        }, 600);
    },

    bgmIsOn() { return this._bgmOn; },
};
