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
        // Visual Novel mode — highest priority
        if (l.vn_script) {
            el.innerHTML = '';
            const vnContainer = document.createElement('div');
            el.appendChild(vnContainer);
            VN.start(l.vn_script, vnContainer, () => {
                // After VN finishes, show the rest of the lesson
                this._showLessonContent(el, l);
            });
            return;
        }
        this._showLessonContent(el, l);
    },

    _showLessonContent(el, l) {
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
            // 5-layer progressive unlock
            const layers = [
                {id:1, title: l.layer1_title || '🌍 为什么要发明这个？', body: l.layer1, color: 'gold'},
                {id:2, title: l.layer2_title || '🔍 怎么发现的？', body: l.layer2, color: 'blue'},
                {id:3, title: l.layer3_title || '🧱 核心概念', body: l.layer3, color: 'purple'},
                {id:4, title: l.layer4_title || '🔗 在数学大厦中的位置', body: l.layer4, color: 'green'},
                {id:5, title: l.layer5_title || '🛠️ 怎么用？', body: l.layer5, color: 'red'},
            ];
            let layersHTML = layers.map((ly, i) => {
                const hint = i === 0 ? '点击解锁' : `需要先解锁上一层`;
                return `<div class="deep-layer layer-${ly.id} locked" id="deep-layer${ly.id}">
                    <div class="deep-layer-title" onclick="learn._unlockLayer(${ly.id})">
                        <span class="layer-lock">🔒</span> ${ly.title}
                        <span class="layer-hint">${hint}</span>
                    </div>
                    <div class="deep-layer-body" style="display:none">${hl(ly.body).replace(/\n/g, '<br>')}</div>
                </div>`;
            }).join('');

            el.innerHTML = `<div class="lesson lesson-deep">
                <div class="lesson-header-row">
                    ${l.textbook_ref ? `<span class="learn-ref">📖 ${l.textbook_ref}</span>` : ''}
                </div>
                ${layersHTML}
                ${l.formula ? `<div class="lesson-section"><h4>📐 公式</h4><div class="lesson-formula">$$${l.formula}$$</div></div>` : ''}
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
    _unlockLayer(id) {
        const layer = document.getElementById(`deep-layer${id}`);
        if (!layer) return;
        // Check prerequisite: previous layer must be unlocked first
        if (id > 1) {
            const prev = document.getElementById(`deep-layer${id-1}`);
            if (prev && prev.classList.contains('locked')) {
                App.toast('请先解锁上一层', 'warning');
                return;
            }
        }
        const body = layer.querySelector('.deep-layer-body');
        const lock = layer.querySelector('.layer-lock');
        const hint = layer.querySelector('.layer-hint');
        if (layer.classList.contains('locked')) {
            layer.classList.remove('locked');
            layer.classList.add('unlocked');
            if (body) body.style.display = 'block';
            if (lock) lock.textContent = '🔓';
            if (hint) hint.textContent = '已解锁';
            body.scrollIntoView({ behavior: 'smooth', block: 'center' });
            App.renderMath(body);
            // If this is layer 3, init the canvas
            if (id === 3) {
                setTimeout(() => this._animateSecantToTangent(), 400);
            }
        }
    },

    _startSecantCanvas() {
        if (!document.getElementById('visual-canvas')) return;
        const infoText = document.getElementById('visual-info');
        const txt = infoText ? infoText.textContent || '' : '';
        if (txt.includes('拖动三角形')) this._animateSineLaw();
        else if (txt.includes('拖动 d')) this._animateArithmeticSeq();
        else this._animateSecantToTangent();
    },

    // ── Sine Law: Circumcircle + Triangle ──────────────────────────
    _animateSineLaw() {
        const canvas = document.getElementById('visual-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const W = canvas.width, H = canvas.height;
        const info = document.getElementById('visual-info');
        let dragging = null;

        // Triangle vertices: A, B, C
        let pts = { A: {x: 120, y: 270}, B: {x: 400, y: 270}, C: {x: 200, y: 80} };

        const dist = (p, q) => Math.sqrt((p.x-q.x)**2 + (p.y-q.y)**2);
        const angle = (p, q, r) => {
            const a = dist(q, r), b = dist(p, r), c = dist(p, q);
            return Math.acos((b*b + c*c - a*a) / (2*b*c));
        };

        const circumcircle = () => {
            const A = pts.A, B = pts.B, C = pts.C;
            const d = 2*(A.x*(B.y-C.y) + B.x*(C.y-A.y) + C.x*(A.y-B.y));
            if (Math.abs(d) < 1) return {x: W/2, y: H/2, r: 150};
            const ux = ((A.x*A.x+A.y*A.y)*(B.y-C.y) + (B.x*B.x+B.y*B.y)*(C.y-A.y) + (C.x*C.x+C.y*C.y)*(A.y-B.y)) / d;
            const uy = ((A.x*A.x+A.y*A.y)*(C.x-B.x) + (B.x*B.x+B.y*B.y)*(A.x-C.x) + (C.x*C.x+C.y*C.y)*(B.x-A.x)) / d;
            return {x: ux, y: uy, r: dist({x:ux,y:uy}, A)};
        };

        const draw = () => {
            ctx.clearRect(0, 0, W, H);
            const A = pts.A, B = pts.B, C = pts.C;
            const a = dist(B, C), b = dist(A, C), c = dist(A, B);
            const angA = angle(B, A, C), angB = angle(A, B, C), angC = angle(A, C, B);
            const cc = circumcircle();
            const ratioA = (a / Math.sin(angA)).toFixed(1);
            const ratioB = (b / Math.sin(angB)).toFixed(1);
            const ratioC = (c / Math.sin(angC)).toFixed(1);
            const twoR = (2 * cc.r).toFixed(1);

            // Circumcircle
            ctx.strokeStyle = 'rgba(139,92,246,0.3)'; ctx.lineWidth = 2;
            ctx.beginPath(); ctx.arc(cc.x, cc.y, cc.r, 0, Math.PI*2); ctx.stroke();
            ctx.fillStyle = '#a78bfa'; ctx.beginPath(); ctx.arc(cc.x, cc.y, 3, 0, Math.PI*2); ctx.fill();

            // Triangle
            ctx.strokeStyle = 'rgba(255,255,255,0.3)'; ctx.lineWidth = 2;
            ctx.beginPath(); ctx.moveTo(A.x, A.y); ctx.lineTo(B.x, B.y); ctx.lineTo(C.x, C.y); ctx.closePath(); ctx.stroke();
            ctx.fillStyle = 'rgba(240,180,41,0.1)'; ctx.fill();

            // Vertices
            [{p: A, n: 'A'}, {p: B, n: 'B'}, {p: C, n: 'C'}].forEach(v => {
                ctx.fillStyle = '#f59e0b'; ctx.beginPath(); ctx.arc(v.p.x, v.p.y, 7, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = '#fff'; ctx.font = 'bold 14px system-ui'; ctx.fillText(v.n, v.p.x+10, v.p.y-8);
            });

            // Labels
            const mid = (p,q) => ({x:(p.x+q.x)/2, y:(p.y+q.y)/2});
            const ab = mid(A,B), bc = mid(B,C), ca = mid(C,A);
            ctx.fillStyle = '#fff'; ctx.font = '12px system-ui';
            ctx.fillText(`c=${c.toFixed(0)}`, ab.x, ab.y+16);
            ctx.fillText(`a=${a.toFixed(0)}`, bc.x-30, bc.y-6);
            ctx.fillText(`b=${b.toFixed(0)}`, ca.x+10, ca.y-6);

            // Angles
            ctx.fillStyle = '#f59e0b'; ctx.font = '11px system-ui';
            ctx.fillText(`A=${(angA*180/Math.PI).toFixed(0)}°`, A.x-60, A.y-8);
            ctx.fillText(`B=${(angB*180/Math.PI).toFixed(0)}°`, B.x+10, B.y-14);
            ctx.fillText(`C=${(angC*180/Math.PI).toFixed(0)}°`, C.x-60, C.y-14);

            // Info panel
            if (info) info.innerHTML = `
                a/sinA = ${ratioA} &nbsp;|&nbsp; b/sinB = ${ratioB} &nbsp;|&nbsp; c/sinC = ${ratioC} &nbsp;|&nbsp; 2R = ${twoR}
                <br><span style='font-size:11px;color:${ratioA===ratioB&&ratioB===ratioC?'var(--emerald)':'var(--ruby)'}'>
                ${ratioA===ratioB&&ratioB===ratioC?'✅ 三个比值相等！这就是正弦定理':'⚠️ 拖动顶点试试'}</span>`;
        };

        canvas.onmousedown = (e) => {
            const rect = canvas.getBoundingClientRect();
            const mx = (e.clientX-rect.left)*(W/rect.width);
            const my = (e.clientY-rect.top)*(H/rect.height);
            for (const [k, p] of Object.entries(pts)) {
                if (Math.hypot(mx-p.x, my-p.y) < 15) { dragging = k; canvas.style.cursor='grabbing'; break; }
            }
        };
        canvas.onmousemove = (e) => {
            if (dragging) {
                const rect = canvas.getBoundingClientRect();
                pts[dragging].x = (e.clientX-rect.left)*(W/rect.width);
                pts[dragging].y = (e.clientY-rect.top)*(H/rect.height);
                draw();
            }
        };
        canvas.onmouseup = () => { dragging = null; canvas.style.cursor='default'; };
        canvas.ontouchstart = (e) => {
            const rect = canvas.getBoundingClientRect();
            const mx = (e.touches[0].clientX-rect.left)*(W/rect.width);
            const my = (e.touches[0].clientY-rect.top)*(H/rect.height);
            for (const [k, p] of Object.entries(pts)) {
                if (Math.hypot(mx-p.x, my-p.y) < 25) { dragging = k; e.preventDefault(); break; }
            }
        };
        canvas.ontouchmove = (e) => {
            if (dragging) { const rect = canvas.getBoundingClientRect(); pts[dragging].x = (e.touches[0].clientX-rect.left)*(W/rect.width); pts[dragging].y = (e.touches[0].clientY-rect.top)*(H/rect.height); draw(); e.preventDefault(); }
        };
        canvas.ontouchend = () => { dragging = null; };

        draw();
    },

    _animateSecantToTangent() {
        const canvas = document.getElementById('visual-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const W = canvas.width, H = canvas.height;
        const info = document.getElementById('visual-info');
        let dragging = false, xB = 3.5, hasDragged = false;

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

        const xA = 1, yA = 1;
        const fromCanvasX = (cx) => (cx - 80) / 100;

        const draw = () => {
            ctx.clearRect(0,0,W,H);
            drawGrid(); drawCurve();
            const bx = toCanvasX(xB), by = toCanvasY(fx(xB));
            const dxB = xB - xA, slope = dxB > 0.005 ? (fx(xB)-1)/dxB : 2;

            // Point A
            ctx.fillStyle = '#f59e0b'; ctx.beginPath();
            ctx.arc(toCanvasX(xA), toCanvasY(yA), 7, 0, Math.PI*2); ctx.fill();
            ctx.fillStyle = '#f59e0b'; ctx.font = 'bold 13px system-ui';
            ctx.fillText('A(1,1)', toCanvasX(xA)+12, toCanvasY(yA)-10);

            // Point B — draggable
            ctx.fillStyle = '#3b82f6'; ctx.beginPath();
            ctx.arc(bx, by, 7, 0, Math.PI*2); ctx.fill();
            if (dxB > 0.12) {
                ctx.fillStyle = '#3b82f6'; ctx.font = 'bold 13px system-ui';
                ctx.fillText(`B(${xB.toFixed(2)},${fx(xB).toFixed(2)})`, bx+12, by-10);
            }
            ctx.strokeStyle = 'rgba(59,130,246,0.5)'; ctx.lineWidth = 2;
            ctx.beginPath(); ctx.arc(bx, by, 14, 0, Math.PI*2); ctx.stroke();

            // Secant / Tangent
            if (dxB > 0.005) {
                const yLeft = yA + slope * (-0.5), yRight = fx(xB) + slope * 0.5;
                ctx.strokeStyle = 'rgba(59,130,246,0.7)'; ctx.lineWidth = 2;
                ctx.setLineDash([6,3]); ctx.beginPath();
                ctx.moveTo(toCanvasX(xA-0.5), toCanvasY(yLeft));
                ctx.lineTo(toCanvasX(xB+0.5), toCanvasY(yRight)); ctx.stroke();
                ctx.setLineDash([]);
                ctx.fillStyle = '#3b82f6'; ctx.font = '12px system-ui';
                ctx.fillText(`割线斜率 = ${slope.toFixed(3)}`, toCanvasX(2), toCanvasY(fx(2))+30);
                ctx.fillText(`Δx = ${dxB.toFixed(3)}`, toCanvasX(2), toCanvasY(fx(2))+48);
            } else {
                const yLeft = 1 + 2*(-0.5), yRight = 1 + 2*3;
                ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 3; ctx.beginPath();
                ctx.moveTo(toCanvasX(xA-0.5), toCanvasY(yLeft));
                ctx.lineTo(toCanvasX(xA+3), toCanvasY(yRight)); ctx.stroke();
                ctx.fillStyle = '#ef4444'; ctx.font = 'bold 14px system-ui';
                ctx.fillText("切线斜率 = 2 = f'(1)", toCanvasX(1.5), toCanvasY(fx(2))+30);
            }

            if (!hasDragged) {
                ctx.fillStyle = 'rgba(255,255,255,0.6)'; ctx.font = '13px system-ui';
                ctx.fillText('👆 拖动蓝点', toCanvasX(1.5), H-16);
            }

            if (info) {
                if (dxB > 0.02) info.innerHTML = `<span style="color:#3b82f6">拖拽 B 点</span> — Δx=${dxB.toFixed(3)} — 割线斜率=${slope.toFixed(3)}`;
                else if (dxB > 0.003) info.innerHTML = `<span style="color:#f59e0b">越来越近！</span> 斜率 → ${slope.toFixed(3)}`;
                else info.innerHTML = `<span style="color:#ef4444">B=A！切线斜率 = <b>2</b></span> ← f'(1)`;
            }
        };

        canvas.onmousedown = (e) => {
            const rect = canvas.getBoundingClientRect();
            const mx = fromCanvasX((e.clientX-rect.left)*(W/rect.width));
            const my = (H-60-(e.clientY-rect.top)*(H/rect.height))/22;
            if (Math.abs(mx-xB) < 0.3 && Math.abs(my-fx(xB)) < 1.5) { dragging = true; hasDragged = true; canvas.style.cursor = 'grabbing'; }
        };
        canvas.onmousemove = (e) => {
            const rect = canvas.getBoundingClientRect();
            const mx = fromCanvasX((e.clientX-rect.left)*(W/rect.width));
            if (dragging) { xB = Math.max(1.001, Math.min(4, mx)); draw(); }
            else { const my = (H-60-(e.clientY-rect.top)*(H/rect.height))/22; canvas.style.cursor = Math.abs(mx-xB)<0.3&&Math.abs(my-fx(xB))<1.5?'grab':'default'; }
        };
        canvas.onmouseup = () => { dragging = false; };
        canvas.onmouseleave = () => { dragging = false; };
        canvas.ontouchstart = (e) => {
            const rect = canvas.getBoundingClientRect();
            const mx = fromCanvasX((e.touches[0].clientX-rect.left)*(W/rect.width));
            if (Math.abs(mx-xB) < 0.5) { dragging = true; hasDragged = true; e.preventDefault(); }
        };
        canvas.ontouchmove = (e) => {
            if (dragging) { const rect = canvas.getBoundingClientRect(); xB = Math.max(1.001, Math.min(4, fromCanvasX((e.touches[0].clientX-rect.left)*(W/rect.width)))); draw(); e.preventDefault(); }
        };
        canvas.ontouchend = () => { dragging = false; };

        draw();
    },

    _animateArithmeticSeq() {
        const canvas = document.getElementById('visual-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const W = canvas.width, H = canvas.height;
        const info = document.getElementById('visual-info');
        let a1 = 1, d = 3, draggingSlider = null;

        const draw = () => {
            ctx.clearRect(0, 0, W, H);
            ctx.strokeStyle = 'rgba(255,255,255,0.2)'; ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(40, H-80); ctx.lineTo(W-20, H-80); ctx.stroke();
            const terms = [];
            for (let i = 1; i <= 8; i++) terms.push(a1 + (i-1)*d);
            const xScale = (W-100) / Math.max(1, terms[7] - terms[0] + d*2);
            const xOffset = 50 - (terms[0] - d) * xScale;
            terms.forEach((val, i) => {
                const x = xOffset + val * xScale, y = H - 80;
                ctx.fillStyle = '#f59e0b'; ctx.beginPath(); ctx.arc(x, y, 6, 0, Math.PI*2); ctx.fill();
                ctx.fillStyle = '#fff'; ctx.font = 'bold 12px system-ui'; ctx.fillText(`a${i+1}=${val}`, x-18, y-16);
                if (i > 0) {
                    const px = xOffset + terms[i-1] * xScale;
                    ctx.strokeStyle = 'rgba(240,180,41,0.4)'; ctx.lineWidth = 2;
                    ctx.beginPath(); ctx.moveTo(px, y); ctx.lineTo(x, y); ctx.stroke();
                    ctx.fillStyle = 'rgba(255,255,255,0.4)'; ctx.font = '10px system-ui';
                    ctx.fillText(`+${d}`, (px+x)/2-8, y-6);
                }
            });
            ctx.fillStyle = '#3b82f6'; ctx.fillRect(40, H-40, 200, 6);
            const a1x = 40 + (a1 + 5) * (200/15);
            ctx.fillStyle = '#3b82f6'; ctx.beginPath(); ctx.arc(a1x, H-37, 10, 0, Math.PI*2); ctx.fill();
            ctx.fillStyle = '#fff'; ctx.font = '11px system-ui'; ctx.fillText(`a1 = ${a1}`, 40, H-50);
            ctx.fillStyle = '#ef4444'; ctx.fillRect(280, H-40, 180, 6);
            const dx = 280 + (d + 2) * (180/10);
            ctx.fillStyle = '#ef4444'; ctx.beginPath(); ctx.arc(dx, H-37, 10, 0, Math.PI*2); ctx.fill();
            ctx.fillStyle = '#fff'; ctx.fillText(`d = ${d}`, 280, H-50);
            if (info) info.innerHTML = `a1=${a1}, d=${d} → an = ${a1} + (n-1)×${d} | 通项: an = ${d}n + ${a1-d}`;
        };
        canvas.onmousedown = (e) => {
            const rect = canvas.getBoundingClientRect();
            const mx = (e.clientX-rect.left)*(W/rect.width), my = (e.clientY-rect.top)*(H/rect.height);
            if (my > H-55 && my < H-20) {
                if (mx > 40 && mx < 240) draggingSlider = 'a1';
                else if (mx > 280 && mx < 460) draggingSlider = 'd';
            }
        };
        canvas.onmousemove = (e) => {
            if (!draggingSlider) return;
            const rect = canvas.getBoundingClientRect();
            const mx = (e.clientX-rect.left)*(W/rect.width);
            if (draggingSlider === 'a1') a1 = Math.round(Math.max(-5, Math.min(10, (mx-40)*(15/200)-5)));
            else d = Math.round(Math.max(-2, Math.min(8, (mx-280)*(10/180)-2)));
            draw();
        };
        canvas.onmouseup = () => { draggingSlider = null; };
        canvas.ontouchstart = (e) => {
            const rect = canvas.getBoundingClientRect();
            const mx = (e.touches[0].clientX-rect.left)*(W/rect.width), my = (e.touches[0].clientY-rect.top)*(H/rect.height);
            if (my > H-55 && my < H-20) {
                if (mx > 40 && mx < 240) draggingSlider = 'a1';
                else if (mx > 280 && mx < 460) draggingSlider = 'd';
                e.preventDefault();
            }
        };
        canvas.ontouchmove = (e) => {
            if (!draggingSlider) return;
            const rect = canvas.getBoundingClientRect();
            const mx = (e.touches[0].clientX-rect.left)*(W/rect.width);
            if (draggingSlider === 'a1') a1 = Math.round(Math.max(-5, Math.min(10, (mx-40)*(15/200)-5)));
            else d = Math.round(Math.max(-2, Math.min(8, (mx-280)*(10/180)-2)));
            draw(); e.preventDefault();
        };
        canvas.ontouchend = () => { draggingSlider = null; };
        draw();
    },
};
