"use strict";
const learn = {
    _modules: [],
    _activeModule: null,
    _activeConcept: null,
    _renderId: 0,

    // ─── Module Grid (like hunting ground) ──────────────────────────
    async render() {
        const rid = ++this._renderId;
        const el = document.getElementById('page-learn');
        if (!el) return;
        this._activeModule = null;
        this._activeConcept = null;
        el.innerHTML = '<h2>📖 学艺堂 — 选择模块</h2><div id="learn-module-grid" class="module-grid"></div>';
        try {
            const data = await App.get('/learn/modules');
            if (rid !== this._renderId) return;
            this._modules = data;
            const grid = document.getElementById('learn-module-grid');
            if (!grid) return;
            data.forEach(m => {
                const card = document.createElement('div');
                card.className = 'module-card';
                const modName = I18N.t('module_' + m.id) || m.name;
                card.innerHTML = `<span class="module-icon">${m.icon}</span>
                    <span class="module-name">${modName}</span>
                    <span class="module-weight">${m.concept_count}${I18N.t('concepts_label')}</span>`;
                card.onclick = () => this._showModule(m);
                grid.appendChild(card);
            });
        } catch (e) { App.toast('加载失败', 'error'); }
    },

    // ─── Concept List for a Module ──────────────────────────────────
    _showModule(m) {
        this._activeModule = m;
        this._activeConcept = null;
        const el = document.getElementById('page-learn');
        let conceptsHTML = '';
        if (m.concepts.length === 0) {
            conceptsHTML = '<div class="empty-state">该模块暂无学习内容，请先前往狩猎场练习</div>';
        } else {
            conceptsHTML = m.concepts.map(c => `
                <div class="learn-concept-card" onclick="learn._selectConcept('${c.name}')">
                    <span class="lcc-icon">${c.has_lesson ? '📘' : '📄'}</span>
                    <span class="lcc-name">${c.name}</span>
                    <span class="lcc-arrow">→</span>
                </div>`).join('');
        }
        el.innerHTML = `
            <div class="learn-header">
                <button class="btn-secondary" onclick="learn.render()">← 返回模块列表</button>
                <h2>${m.icon} ${m.name}</h2>
            </div>
            <div class="learn-concept-list">${conceptsHTML}</div>`;
    },

    // ─── Lesson Detail ──────────────────────────────────────────────
    async _selectConcept(name) {
        this._activeConcept = name;
        const el = document.getElementById('page-learn');
        el.innerHTML = `
            <div class="learn-header">
                <button class="btn-secondary" onclick="learn._showModule(learn._activeModule)">← 返回知识点</button>
                <h2>📘 ${name}</h2>
            </div>
            <div id="lesson-content" class="loading">加载中...</div>`;
        try {
            const l = await App.get(`/learn/concept/${encodeURIComponent(name)}`);
            this._renderLesson(l);
        } catch (e) {
            document.getElementById('lesson-content').innerHTML = `<div class="error">暂无教程</div>`;
        }
    },

    _renderLesson(l) {
        const el = document.getElementById('lesson-content');
        // Deep lessons have 5 layers (layer1-layer5)
        const isDeep = !!l.deep;
        const isRich = !!l.hook;
        let examplesHTML = '';
        if (l.examples && Array.isArray(l.examples)) {
            examplesHTML = l.examples.map((ex, i) => `
                <div class="lesson-example">
                    <div class="example-diff">${ex.difficulty}</div>
                    <div class="example-q"><b>题目：</b>${ex.q}</div>
                    <div class="example-s"><b>解答：</b>${ex.s.replace(/\n/g, '<br>')}</div>
                    <div class="example-a"><b>答案：</b>${ex.a}</div>
                </div>`).join('');
        } else if (l.example) {
            examplesHTML = `<div class="lesson-example">
                <div class="example-q"><b>题目：</b>${l.example.question}</div>
                <div class="example-s"><b>解答：</b>${l.example.solution.replace(/\n/g, '<br>')}</div>
                <div class="example-a"><b>答案：</b>${l.example.answer}</div>
            </div>`;
        }

        // Helper: convert **text** to <strong>text</strong> for highlighting
        const hl = (text) => text.replace(/\*\*(.+?)\*\*/g, '<strong class="hl">$1</strong>');

        if (isDeep) {
            // 5-layer deep learning format
            el.innerHTML = `<div class="lesson lesson-deep">
                <div class="lesson-header-row">
                    ${l.textbook_ref ? `<span class="learn-ref">📖 ${l.textbook_ref}</span>` : ''}
                </div>
                <div class="deep-layer layer-1" id="deep-layer1">
                    <div class="deep-layer-title">${l.layer1_title || '🌍 为什么要发明这个？'}</div>
                    <div class="deep-layer-body">${hl(l.layer1).replace(/\n/g, '<br>')}</div>
                </div>
                <div class="deep-layer layer-2" id="deep-layer2">
                    <div class="deep-layer-title">${l.layer2_title || '🔍 怎么发现的？'}</div>
                    <div class="deep-layer-body">${hl(l.layer2).replace(/\n/g, '<br>')}</div>
                </div>
                <div class="deep-layer layer-3" id="deep-layer3">
                    <div class="deep-layer-title">${l.layer3_title || '🧱 核心概念'}</div>
                    <div class="deep-layer-body">${hl(l.layer3).replace(/\n/g, '<br>')}</div>
                </div>
                ${l.formula ? `<div class="lesson-section"><h4>📐 公式</h4><div class="lesson-formula">$$${l.formula}$$</div></div>` : ''}
                ${l.visual ? `<div class="lesson-visual"><canvas id="visual-canvas" width="560" height="360"></canvas><div id="visual-info"></div></div>` : ''}
                <div class="deep-layer layer-4" id="deep-layer4">
                    <div class="deep-layer-title">${l.layer4_title || '🔗 在数学大厦中的位置'}</div>
                    <div class="deep-layer-body">${hl(l.layer4).replace(/\n/g, '<br>')}</div>
                </div>
                <div class="deep-layer layer-5" id="deep-layer5">
                    <div class="deep-layer-title">${l.layer5_title || '🛠️ 怎么用？'}</div>
                    <div class="deep-layer-body">${hl(l.layer5).replace(/\n/g, '<br>')}</div>
                </div>
                <div class="lesson-section"><h4>💡 例题</h4>${examplesHTML}</div>
                <div class="lesson-section"><h4>⚠️ 常见错误</h4>${l.traps.map(t => `<div class="lesson-trap">• ${t}</div>`).join('')}</div>
                ${l.children && l.children.length ? `<div class="lesson-section"><h4>📎 进阶</h4><div class="learn-children">${l.children.map(c => `<span class="learn-child-link" onclick="learn._selectConcept('${c}')">→ ${c}</span>`).join('')}</div></div>` : ''}
            </div>`;
        } else {
            el.innerHTML = `<div class="lesson">
                <div class="lesson-header-row">
                    ${l.textbook_ref ? `<span class="learn-ref">📖 ${l.textbook_ref}</span>` : ''}
                </div>
                ${isRich ? `
                    <div class="lesson-hook">💬 ${l.hook}</div>
                    <div class="lesson-intuition"><h4>🧠 直观理解</h4><div class="lesson-text">${l.intuition.replace(/\n/g, '<br>')}</div></div>
                ` : ''}
                <div class="lesson-summary">${l.summary}</div>
                ${isRich ? `<div class="lesson-section"><h4>📖 深入讲解</h4><div class="lesson-text">${l.core.replace(/\n/g, '<br>')}</div></div>` : ''}
                <div class="lesson-section">
                    <h4>📐 核心公式</h4>
                    <div class="lesson-formula">$$${l.formula}$$</div>
                </div>
                ${l.derivation ? `<div class="lesson-section"><h4>🔍 公式推导</h4><div class="lesson-text">${l.derivation.replace(/\n/g, '<br>')}</div></div>` : ''}
                ${!isRich && l.explanation ? `<div class="lesson-section"><h4>📝 详细说明</h4><div class="lesson-text">${l.explanation.replace(/\n/g, '<br>')}</div></div>` : ''}
                <div class="lesson-section"><h4>💡 例题</h4>${examplesHTML}</div>
                <div class="lesson-section"><h4>⚠️ 常见错误</h4>${l.traps.map(t => `<div class="lesson-trap">• ${t}</div>`).join('')}</div>
                ${l.connections ? `<div class="lesson-section"><h4>🔗 知识链接</h4><div class="lesson-text">${l.connections.replace(/\n/g, '<br>')}</div></div>` : ''}
                ${l.practice_hint ? `<div class="lesson-section"><h4>🎯 解题口诀</h4><div class="lesson-text" style="color:var(--gold)">${l.practice_hint.replace(/\n/g, '<br>')}</div></div>` : ''}
                ${l.children && l.children.length ? `<div class="lesson-section"><h4>📎 进阶</h4><div class="learn-children">${l.children.map(c => `<span class="learn-child-link" onclick="learn._selectConcept('${c}')">→ ${c}</span>`).join('')}</div></div>` : ''}
            </div>`;
        }
        App.renderMath(el);
        // Start visualization if present
        if (l.visual === 'secant_to_tangent') {
            setTimeout(() => this._animateSecantToTangent(), 300);
        }
    },

    // ── Secant → Tangent Animation ──────────────────────────────────
    _animateSecantToTangent() {
        const canvas = document.getElementById('visual-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const W = canvas.width, H = canvas.height;
        const info = document.getElementById('visual-info');
        let animId;

        // Curve: y = x², mapped to canvas coordinates
        const fx = (x) => x * x;
        const toCanvasX = (x) => 80 + x * 100;        // x range: -0.5 to 4.5
        const toCanvasY = (y) => H - 60 - y * 22;      // y range: 0 to 16 → invert for canvas

        // Draw grid
        const drawGrid = () => {
            ctx.strokeStyle = 'rgba(255,255,255,0.06)'; ctx.lineWidth = 1;
            for (let i = 0; i <= 4; i++) {
                const cx = toCanvasX(i);
                ctx.beginPath(); ctx.moveTo(cx, 30); ctx.lineTo(cx, H-40); ctx.stroke();
            }
            for (let j = 0; j <= 15; j+=2) {
                const cy = toCanvasY(j);
                ctx.beginPath(); ctx.moveTo(60, cy); ctx.lineTo(W-20, cy); ctx.stroke();
            }
            // Axes
            ctx.strokeStyle = 'rgba(255,255,255,0.3)'; ctx.lineWidth = 1.5;
            ctx.beginPath(); ctx.moveTo(60, toCanvasY(0)); ctx.lineTo(W-10, toCanvasY(0)); ctx.stroke(); // x-axis
            ctx.beginPath(); ctx.moveTo(toCanvasX(0), H-20); ctx.lineTo(toCanvasX(0), 20); ctx.stroke();   // y-axis
            // Labels
            ctx.fillStyle = '#8896ab'; ctx.font = '11px system-ui';
            for (let i = 1; i <= 4; i++) { ctx.fillText(i, toCanvasX(i)-4, toCanvasY(0)+16); }
            for (let j = 2; j <= 14; j+=4) { ctx.fillText(j, toCanvasX(0)-22, toCanvasY(j)+4); }
            ctx.fillText('x', W-15, toCanvasY(0)+16); ctx.fillText('y', toCanvasX(0)-14, 28);
        };

        // Draw curve
        const drawCurve = () => {
            ctx.strokeStyle = 'rgba(139,92,246,0.6)'; ctx.lineWidth = 2.5;
            ctx.beginPath();
            let first = true;
            for (let px = -0.2; px <= 4.2; px += 0.05) {
                const cx = toCanvasX(px), cy = toCanvasY(fx(px));
                if (first) { ctx.moveTo(cx, cy); first = false; }
                else ctx.lineTo(cx, cy);
            }
            ctx.stroke();
            ctx.fillStyle = '#a78bfa'; ctx.font = '13px system-ui';
            ctx.fillText('y = x²', toCanvasX(3.2), toCanvasY(fx(3.2))-10);
        };

        // Animation: B approaches A
        const xA = 1, yA = fx(1);
        let t = 0; // 0 → 1, where t=1 means B=A (full approach)

        const drawFrame = () => {
            ctx.clearRect(0, 0, W, H);
            drawGrid();
            drawCurve();

            // Point A (fixed)
            const ax = toCanvasX(xA), ay = toCanvasY(yA);
            ctx.fillStyle = '#f59e0b'; ctx.beginPath();
            ctx.arc(ax, ay, 6, 0, Math.PI*2); ctx.fill();
            ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 13px system-ui';
            ctx.fillText('A(1,1)', ax+10, ay-10);

            // Point B (approaches A as t increases)
            const xB = xA + 2.5 * (1 - t); // starts at x=3.5, ends at x=1
            const yB = fx(xB);
            const bx = toCanvasX(xB), by = toCanvasY(yB);
            const dxB = xB - xA;
            ctx.fillStyle = '#3b82f6'; ctx.beginPath();
            ctx.arc(bx, by, 5, 0, Math.PI*2); ctx.fill();
            // Only show B label when it's not too close to A
            if (dxB > 0.15) {
                ctx.fillStyle = '#3b82f6'; ctx.font = 'bold 13px system-ui';
                ctx.fillText(`B(${xB.toFixed(2)},${yB.toFixed(2)})`, bx+10, by-10);
            }

            // Secant line AB
            const dxB = xB - xA;
            if (dxB > 0.02) {
                // Extend secant line beyond A and B
                const extendLeft = toCanvasX(xA - 0.5);
                const extendRight = toCanvasX(xB + 0.5);
                const slope = (yB - yA) / dxB;
                const yLeft = yA + slope * (-0.5);
                const yRight = yB + slope * 0.5;
                ctx.strokeStyle = 'rgba(59,130,246,0.7)'; ctx.lineWidth = 2;
                ctx.setLineDash([6, 3]);
                ctx.beginPath();
                ctx.moveTo(toCanvasX(xA - 0.5), toCanvasY(yLeft));
                ctx.lineTo(toCanvasX(xB + 0.5), toCanvasY(yRight));
                ctx.stroke();
                ctx.setLineDash([]);
                // Slope label
                ctx.fillStyle = '#3b82f6'; ctx.font = '12px system-ui';
                const slopeText = `割线斜率 = ${slope.toFixed(2)}`;
                ctx.fillText(slopeText, toCanvasX(2), toCanvasY(fx(2))+30);
                const dxText = `Δx = ${dxB.toFixed(2)}`;
                ctx.fillText(dxText, toCanvasX(2), toCanvasY(fx(2))+48);
            } else {
                // Tangent line at A
                const slope = 2 * xA; // f'(1) = 2
                const yLeft = yA + slope * (-0.5);
                const yRight = yA + slope * 3;
                ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(toCanvasX(xA - 0.5), toCanvasY(yLeft));
                ctx.lineTo(toCanvasX(xA + 3), toCanvasY(yRight));
                ctx.stroke();
                ctx.fillStyle = '#ef4444'; ctx.font = 'bold 13px system-ui';
                ctx.fillText('切线斜率 = 2', toCanvasX(2), toCanvasY(fx(2))+30);
                ctx.fillText("这就是 f'(1)", toCanvasX(2), toCanvasY(fx(2))+50);
            }

            // Update info
            if (info) {
                if (dxB > 0.02) {
                    info.innerHTML = `<span style="color:#3b82f6">🔵 B 点向 A 点靠近中...</span> Δx = ${dxB.toFixed(3)} | 割线斜率 = ${((yB-yA)/dxB).toFixed(3)}`;
                } else {
                    info.innerHTML = `<span style="color:#ef4444">🔴 B 与 A 重合！</span> 割线变成了 <b>切线</b>，斜率 = <b>2</b> ← 这就是导数 f'(1)`;
                }
            }

            // Advance animation
            t += 0.005;
            if (t >= 1) t = 1;
            animId = requestAnimationFrame(drawFrame);
        };

        // Replay button
        const replay = () => { t = 0; };
        canvas.onclick = replay;
        if (info) info.style.cursor = 'pointer';
        if (info) info.onclick = replay;

        drawFrame();
        this._visualCleanup = () => cancelAnimationFrame(animId);
    },
};
