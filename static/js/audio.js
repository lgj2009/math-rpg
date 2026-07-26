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

    bgmStart(station = 'calm') {
        if (this._bgmOn) return;
        this._init();
        if (this.ctx.state === 'suspended') this.ctx.resume();
        this._bgmOn = true;
        this._bgmNodes = [];

        this._bgmGain = this.ctx.createGain();
        this._bgmGain.gain.value = 0.25;
        this._bgmGain.connect(this.ctx.destination);

        // Station presets
        const presets = {
            calm: {
                chords: [[220,262,330,392],[294,349,440,523],[196,247,330,392],[262,330,392,494]],
                chordDur: 3.2, kickVol: 0.14, hatVol: 0.02, melVol: 0.05, tempo: 700,
                melody: [523,587,659,523,440,494,523,392,440,523,587,659],
                chordVol: [0.10, 0.05],
            },
            upbeat: {
                chords: [[262,330,392],[330,415,494],[392,494,587],[349,440,523],[294,392,494],[262,330,392]],
                chordDur: 2.0, kickVol: 0.22, hatVol: 0.03, melVol: 0.08, tempo: 400,
                melody: [523,659,784,659,523,440,587,659,784,880,784,659],
                chordVol: [0.12, 0.06],
            },
            lofi: {
                chords: [[196,247,330],[262,330,392],[294,349,440],[330,392,494],[220,262,330],[196,294,349]],
                chordDur: 3.8, kickVol: 0.10, hatVol: 0.015, melVol: 0.03, tempo: 900,
                melody: [440,494,523,440,392,330,392,440,494,523,587,523],
                chordVol: [0.08, 0.04],
            },
        };
        const p = presets[station] || presets.calm;

        const playChord = (idx) => {
            if (!this._bgmOn) return;
            const chord = p.chords[idx % p.chords.length];
            const t = this.ctx.currentTime;
            chord.forEach((freq, i) => {
                const osc = this.ctx.createOscillator();
                const g = this.ctx.createGain();
                osc.type = i === 0 ? 'sine' : 'triangle';
                osc.frequency.value = freq;
                osc.detune.value = (Math.random() - 0.5) * 10;
                g.gain.setValueAtTime(0, t);
                g.gain.linearRampToValueAtTime(p.chordVol[i] || 0.06, t + 0.8);
                g.gain.linearRampToValueAtTime((p.chordVol[i] || 0.06) * 0.7, t + p.chordDur - 0.3);
                g.gain.linearRampToValueAtTime(0, t + p.chordDur + 0.1);
                osc.connect(g); g.connect(this._bgmGain);
                osc.start(t); osc.stop(t + p.chordDur + 0.3);
                this._bgmNodes.push(osc, g);
            });
            if (idx % 2 === 0) {
                const kick = this.ctx.createOscillator();
                const kg = this.ctx.createGain();
                kick.type = 'sine'; kick.frequency.setValueAtTime(120, t);
                kick.frequency.exponentialRampToValueAtTime(35, t + 0.12);
                kg.gain.setValueAtTime(p.kickVol, t);
                kg.gain.exponentialRampToValueAtTime(0.001, t + 0.25);
                kick.connect(kg); kg.connect(this._bgmGain);
                kick.start(t); kick.stop(t + 0.3);
                this._bgmNodes.push(kick, kg);
            }
            for (let b = 0; b < 4; b++) {
                const ht = t + b * (p.chordDur / 4);
                const hh = this.ctx.createOscillator(); const hg = this.ctx.createGain();
                hh.type = 'square'; hh.frequency.value = 6000;
                hg.gain.setValueAtTime(p.hatVol, ht); hg.gain.exponentialRampToValueAtTime(0.001, ht + 0.03);
                hh.connect(hg); hg.connect(this._bgmGain);
                hh.start(ht); hh.stop(ht + 0.04);
                this._bgmNodes.push(hh, hg);
            }
            this._bgmChordTimer = setTimeout(() => playChord(idx + 1), p.chordDur * 1000 - 50);
        };

        const playMelody = (idx) => {
            if (!this._bgmOn) return;
            const freq = p.melody[idx % p.melody.length];
            const osc = this.ctx.createOscillator(); const g = this.ctx.createGain();
            osc.type = 'sine'; osc.frequency.value = freq;
            const t = this.ctx.currentTime; const dur = 0.5 + Math.random() * 0.3;
            g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(p.melVol, t + 0.3);
            g.gain.linearRampToValueAtTime(0, t + dur);
            osc.connect(g); g.connect(this._bgmGain);
            osc.start(t); osc.stop(t + dur + 0.05);
            this._bgmNodes.push(osc, g);
            this._bgmMelTimer = setTimeout(() => playMelody((idx + 1) % p.melody.length), p.tempo + Math.random() * 400);
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
