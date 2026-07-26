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
    },
};
