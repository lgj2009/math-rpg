"use strict";
// progress.js — radar chart + module detail view
const progress = {
    chart: null,
    _modules: [],

    async render() {
        const main = document.getElementById('page-progress');
        if (!main) return;

        const pid = App.state.player && App.state.player.id;
        if (!pid) {
            main.innerHTML = '<div class="loading">请先创建角色</div>';
            return;
        }

        main.innerHTML = '<div class="loading">加载修炼数据中...</div>';

        try {
            const data = await App.get(`/players/${pid}/progress`);
            this._modules = data.modules || [];
            this._build(main, data);
        } catch (e) {
            main.innerHTML = `<div class="error">加载失败: ${e.message}</div>`;
        }
    },

    _build(main, data) {
        const overallPct = Math.round(data.overall_accuracy * 100);

        main.innerHTML = `
            <div class="dashboard-header">
                <h2>📈 修炼进度</h2>
                <p class="dashboard-subtitle">${data.username} · 总正确率 ${overallPct}% · 共 ${data.total_questions} 题</p>
            </div>

            <div class="dashboard-grid">
                <div class="card chart-card">
                    <h3 class="card-title">🎯 五维能力雷达</h3>
                    <div class="chart-container">
                        <canvas id="radar-chart"></canvas>
                    </div>
                </div>
                <div class="card module-detail-card">
                    <h3 class="card-title">📖 模块明细</h3>
                    <div id="module-selector" class="module-tabs"></div>
                    <div id="module-detail-panel"></div>
                </div>
            </div>

            <div class="card" style="margin-top:20px">
                <h3 class="card-title">📊 全部模块一览</h3>
                <div id="module-table"></div>
            </div>
        `;

        this._renderRadar(data);
        this._renderModuleTabs();
        // Select first module by default
        if (this._modules.length > 0) {
            this._showModuleDetail(this._modules[0].module_id);
        }
        this._renderTable(data);
    },

    _renderRadar(data) {
        const ctx = document.getElementById('radar-chart');
        if (!ctx) return;

        if (this.chart) {
            this.chart.destroy();
            this.chart = null;
        }

        // Compute average scores across all modules for the overall radar
        const modules = data.modules || [];
        const dimKeys = ['accuracy_avg', 'speed_qualify', 'retention_score', 'mistake_clear_rate', 'stability_score'];
        const dimLabels = ['正确率', '速度达标', '保留率', '错题清除', '稳定性'];

        const averages = dimKeys.map(key => {
            const vals = modules.map(m => m[key]).filter(v => v !== undefined);
            return vals.length > 0 ? vals.reduce((a, b) => a + b, 0) / vals.length : 0;
        });

        // Also compute per-module colors using a subset of categorical slots
        const colors = [
            '#3987e5', // blue
            '#d95926', // orange
            '#199e70', // aqua
            '#c98500', // yellow
            '#d55181', // magenta
            '#008300', // green
            '#9085e9', // violet
            '#e66767', // red
        ];

        const datasets = [{
            label: '整体平均',
            data: dimKeys.map((key, i) => {
                // Mix numeric scales: speed_qualify is 0/1, accuracy is 0-1
                const avg = averages[i];
                // For speed_qualify (boolean), scale it like everything else (0-1)
                return Math.round(avg * 100);
            }),
            backgroundColor: 'rgba(245, 158, 11, 0.15)',
            borderColor: '#f59e0b',
            borderWidth: 2,
            pointBackgroundColor: '#f59e0b',
            pointBorderColor: '#0f172a',
            pointBorderWidth: 2,
            pointRadius: 4,
            hoverRadius: 6,
        }];

        // Add per-module lines (up to 8, one per color slot)
        modules.slice(0, 8).forEach((m, i) => {
            datasets.push({
                label: m.module_name,
                data: dimKeys.map(key => {
                    const val = m[key];
                    return typeof val === 'number' ? Math.round(val * 100) : (val ? 100 : 0);
                }),
                backgroundColor: 'transparent',
                borderColor: colors[i % colors.length],
                borderWidth: 1.5,
                borderDash: [4, 3],
                pointBackgroundColor: colors[i % colors.length],
                pointBorderColor: '#0f172a',
                pointBorderWidth: 1.5,
                pointRadius: 3,
                hoverRadius: 5,
            });
        });

        this.chart = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: dimLabels,
                datasets,
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                scales: {
                    r: {
                        min: 0,
                        max: 100,
                        ticks: {
                            display: false,
                            stepSize: 25,
                        },
                        pointLabels: {
                            color: '#f1f5f9',
                            font: { size: 13, weight: '500' },
                        },
                        grid: {
                            color: '#334155',
                            lineWidth: 1,
                        },
                        angleLines: {
                            color: '#334155',
                            lineWidth: 1,
                        },
                        backgroundColor: 'rgba(30, 41, 59, 0.3)',
                    },
                },
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: '#94a3b8',
                            boxWidth: 12,
                            padding: 12,
                            font: { size: 12 },
                            usePointStyle: true,
                        },
                    },
                    tooltip: {
                        backgroundColor: '#1e293b',
                        titleColor: '#f1f5f9',
                        bodyColor: '#94a3b8',
                        borderColor: '#334155',
                        borderWidth: 1,
                        padding: 10,
                        cornerRadius: 8,
                        callbacks: {
                            label: function (ctx) {
                                return ctx.dataset.label + ': ' + ctx.parsed.r + '%';
                            },
                        },
                    },
                },
            },
        });
    },

    _renderModuleTabs() {
        const container = document.getElementById('module-selector');
        if (!container) return;

        container.innerHTML = this._modules.map(m =>
            `<button class="tab-btn" data-module-id="${m.module_id}" onclick="progress._showModuleDetail(${m.module_id})">
                ${m.icon} ${m.module_name}
            </button>`
        ).join('');

        // Activate first
        const first = container.querySelector('.tab-btn');
        if (first) first.classList.add('active');
    },

    _showModuleDetail(moduleId) {
        // Update tab active state
        document.querySelectorAll('#module-selector .tab-btn').forEach(btn => {
            btn.classList.toggle('active', parseInt(btn.dataset.moduleId) === moduleId);
        });

        const m = this._modules.find(mod => mod.module_id === moduleId);
        if (!m) return;

        const panel = document.getElementById('module-detail-panel');
        if (!panel) return;

        const statusLabel = this._statusLabel(m.status);
        const accPct = Math.round(m.accuracy_avg * 100);
        const retPct = Math.round(m.retention_score * 100);
        const misPct = Math.round(m.mistake_clear_rate * 100);
        const stabPct = Math.round(m.stability_score * 100);

        panel.innerHTML = `
            <div class="module-detail-header">
                <span class="module-detail-icon">${m.icon}</span>
                <div>
                    <div class="module-detail-name">${m.module_name}</div>
                    <span class="module-status-badge ${m.status}">${statusLabel}</span>
                </div>
                <span class="module-detail-weight">权重 ${m.weight}分</span>
            </div>
            <div class="module-detail-scores">
                <div class="detail-score-row">
                    <span class="detail-score-label">🎯 正确率</span>
                    <div class="detail-score-bar"><div class="detail-score-fill" style="width:${accPct}%"></div></div>
                    <span class="detail-score-val">${accPct}%</span>
                </div>
                <div class="detail-score-row">
                    <span class="detail-score-label">⚡ 速度达标</span>
                    <div class="detail-score-bar"><div class="detail-score-fill ${m.speed_qualify ? 'fill-correct' : 'fill-dim'}" style="width:${m.speed_qualify ? 100 : 0}%"></div></div>
                    <span class="detail-score-val">${m.speed_qualify ? '✓' : '✗'}</span>
                </div>
                <div class="detail-score-row">
                    <span class="detail-score-label">🔄 保留率</span>
                    <div class="detail-score-bar"><div class="detail-score-fill" style="width:${retPct}%"></div></div>
                    <span class="detail-score-val">${retPct}%</span>
                </div>
                <div class="detail-score-row">
                    <span class="detail-score-label">🧹 盲点清除</span>
                    <div class="detail-score-bar"><div class="detail-score-fill" style="width:${misPct}%"></div></div>
                    <span class="detail-score-val">${misPct}%</span>
                </div>
                <div class="detail-score-row">
                    <span class="detail-score-label">📊 稳定性</span>
                    <div class="detail-score-bar"><div class="detail-score-fill" style="width:${stabPct}%"></div></div>
                    <span class="detail-score-val">${stabPct}%</span>
                </div>
            </div>
        `;
    },

    _renderTable(data) {
        const container = document.getElementById('module-table');
        if (!container) return;

        const modules = data.modules || [];

        container.innerHTML = `
            <table class="progress-table">
                <thead>
                    <tr>
                        <th></th>
                        <th>模块</th>
                        <th>正确率</th>
                        <th>速度</th>
                        <th>保留率</th>
                        <th>盲点清除</th>
                        <th>稳定性</th>
                        <th>状态</th>
                    </tr>
                </thead>
                <tbody>
                    ${modules.map(m => {
                        const statusLabel = this._statusLabel(m.status);
                        const acc = Math.round(m.accuracy_avg * 100);
                        const ret = Math.round(m.retention_score * 100);
                        const mis = Math.round(m.mistake_clear_rate * 100);
                        const stab = Math.round(m.stability_score * 100);
                        return `<tr>
                            <td>${m.icon}</td>
                            <td>${m.module_name}</td>
                            <td>${acc}%</td>
                            <td>${m.speed_qualify ? '✓' : '✗'}</td>
                            <td>${ret}%</td>
                            <td>${mis}%</td>
                            <td>${stab}%</td>
                            <td><span class="module-status-badge ${m.status}">${statusLabel}</span></td>
                        </tr>`;
                    }).join('')}
                </tbody>
            </table>
        `;
    },

    _statusLabel(status) {
        const map = { mastered: '已掌握', practicing: '练习中', learning: '学习中', new: '未开始' };
        return map[status] || status;
    },
};
