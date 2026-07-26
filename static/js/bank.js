"use strict";
// bank.js — Question bank browser with full answers and solutions
const bank = {
    _filters: { module_id: '', difficulty: '', source: '', keyword: '' },
    _page: 1,

    async render() {
        const el = document.getElementById('page-bank');
        if (!el) return;
        await this._loadModules();
        el.innerHTML = `
            <h2>📚 题库</h2>
            <div class="bank-filters">
                <select id="bf-module" onchange="bank._filter()">
                    <option value="">全部模块</option>
                </select>
                <select id="bf-diff" onchange="bank._filter()">
                    <option value="">全部难度</option>
                    <option value="1">⭐ 基础</option>
                    <option value="2">⭐⭐ 中档</option>
                    <option value="3">⭐⭐⭐ 难题</option>
                </select>
                <select id="bf-source" onchange="bank._filter()">
                    <option value="">全部来源</option>
                    <option value="real_exam">🏛️ 高考真题</option>
                    <option value="curated">📝 精选模拟</option>
                    <option value="generated">🤖 AI生成</option>
                </select>
                <input id="bf-keyword" type="text" placeholder="搜索题目..." oninput="bank._filter()">
            </div>
            <div id="bank-results"></div>
            <div id="bank-pager"></div>`;
        this._page = 1;
        this._loadModules();
        this._fetch();
    },

    async _loadModules() {
        try {
            const mods = await App.get('/bank/modules');
            const sel = document.getElementById('bf-module');
            if (!sel) return;
            mods.forEach(m => {
                const opt = document.createElement('option');
                opt.value = m.id;
                opt.textContent = `${m.icon || ''} ${m.name}`;
                sel.appendChild(opt);
            });
        } catch (_) {}
    },

    _filter() {
        this._filters.module_id = document.getElementById('bf-module')?.value || '';
        this._filters.difficulty = document.getElementById('bf-diff')?.value || '';
        this._filters.source = document.getElementById('bf-source')?.value || '';
        this._filters.keyword = document.getElementById('bf-keyword')?.value || '';
        this._page = 1;
        this._fetch();
    },

    async _fetch() {
        const f = this._filters;
        const params = new URLSearchParams({ page: this._page, page_size: 15 });
        if (f.module_id) params.set('module_id', f.module_id);
        if (f.difficulty) params.set('difficulty', f.difficulty);
        if (f.source) params.set('source', f.source);
        if (f.keyword) params.set('keyword', f.keyword);

        const res = document.getElementById('bank-results');
        const pager = document.getElementById('bank-pager');
        res.innerHTML = '<div class="loading">⏳ 加载中...</div>';

        try {
            const data = await App.get(`/bank?${params.toString()}`);
            let html = `<div class="bank-count">共 ${data.total} 题</div>`;

            data.questions.forEach(q => {
                const diffStars = {1:'⭐',2:'⭐⭐',3:'⭐⭐⭐'}[q.difficulty] || '⭐';
                const typeLabel = {choice:'选择题',fill:'填空题',answer:'解答题'}[q.type] || q.type;
                const sourceLabel = q.source_type === 'real_exam' ? '🏛️ 真题' :
                                    q.source_type === 'curated' ? '📝 精选' : '🤖 生成';
                let optionsHTML = '';
                if (q.options && q.options.length) {
                    optionsHTML = `<div class="bq-options">${q.options.map(o => `<span class="bq-opt">${o}</span>`).join('')}</div>`;
                }

                html += `<div class="bank-question" onclick="this.classList.toggle('expanded')">
                    <div class="bq-header">
                        <span class="bq-module">${q.module_icon || ''} ${q.module_name || 'M'+q.module_id}</span>
                        <span class="bq-badges">
                            <span class="bq-type">${typeLabel}</span>
                            <span class="bq-diff">${diffStars}</span>
                            <span class="bq-source">${sourceLabel}</span>
                            ${q.source_ref ? `<span class="bq-ref">${q.source_ref}</span>` : ''}
                        </span>
                    </div>
                    <div class="bq-content">${q.content}</div>
                    ${optionsHTML}
                    <div class="bq-answer-panel">
                        <div class="bq-answer"><span class="bq-label">✅ 答案：</span>${q.answer}</div>
                        ${q.solution ? `<div class="bq-solution"><span class="bq-label">💡 解析：</span>${q.solution}</div>` : ''}
                    </div>
                </div>`;
            });

            res.innerHTML = html;
            App.renderMath(res);

            // Pager
            let ph = '';
            if (data.total_pages > 1) {
                ph += `<button class="btn-secondary" ${this._page<=1?'disabled':''} onclick="bank._goPage(${this._page-1})">◀ 上一页</button>`;
                ph += `<span style="margin:0 12px;color:var(--text-secondary);font-size:13px">${this._page} / ${data.total_pages}</span>`;
                ph += `<button class="btn-secondary" ${this._page>=data.total_pages?'disabled':''} onclick="bank._goPage(${this._page+1})">下一页 ▶</button>`;
            }
            pager.innerHTML = ph;
        } catch (e) {
            res.innerHTML = `<div class="error">❌ 加载失败: ${e.message}</div>`;
        }
    },

    _goPage(n) { this._page = n; this._fetch(); window.scrollTo(0, 0); },
};
