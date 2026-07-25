"use strict";
// dashboard.js — adventure hall with ring chart, score estimate, module status list
const dashboard = {
    chart: null,

    async render() {
        const main = document.getElementById('page-dashboard');
        if (!main) return;

        const pid = App.state.player && App.state.player.id;
        if (!pid) {
            main.innerHTML = '<div class="loading">请先创建角色</div>';
            return;
        }

        main.innerHTML = '<div class="loading">加载冒险数据中...</div>';

        try {
            const data = await App.get(`/players/${pid}/dashboard`);
            this._build(main, data);
        } catch (e) {
            main.innerHTML = `<div class="error">加载失败: ${e.message}</div>`;
        }
    },

    _build(main, data) {
        const p = data.player;
        const totalPct = data.total_questions > 0
            ? Math.round((data.total_correct / data.total_questions) * 100)
            : 0;

        // ── Hero Row: estimated score + streak + totals ──────────────
        main.innerHTML = `
            <div class="dashboard-header">
                <h2>📊 冒险大厅</h2>
                <p class="dashboard-subtitle">${p.username} · Lv.${p.level} ${p.title}</p>
            </div>
            <div class="stat-tiles">
                <div class="stat-tile">
                    <div class="stat-value score-value">${data.estimated_score}</div>
                    <div class="stat-label">估算分数 / 150</div>
                </div>
                <div class="stat-tile">
                    <div class="stat-value">${data.streak_days}</div>
                    <div class="stat-label">连续打卡</div>
                </div>
                <div class="stat-tile">
                    <div class="stat-value">${data.total_questions}</div>
                    <div class="stat-label">总答题数</div>
                </div>
                <div class="stat-tile">
                    <div class="stat-value ${totalPct >= 80 ? 'text-correct' : totalPct >= 50 ? 'text-accent' : ''}">${totalPct}%</div>
                    <div class="stat-label">总正确率</div>
                </div>
            </div>

            <div class="dashboard-grid">
                <div class="card chart-card">
                    <h3 class="card-title">🏆 掌握度全景</h3>
                    <div class="chart-container">
                        <canvas id="ring-chart"></canvas>
                    </div>
                    <div class="legend-row" id="mastery-legend"></div>
                </div>
                <div class="card module-list-card">
                    <h3 class="card-title">📚 模块状态</h3>
                    <div id="module-status-list"></div>
                </div>
            </div>
        `;

        // ── Build ring chart ─────────────────────────────────────────
        this._renderRing(data);

        // ── Build module status list ─────────────────────────────────
        this._renderModuleList(data.module_masteries);
    },

    _renderRing(data) {
        const ctx = document.getElementById('ring-chart');
        if (!ctx) return;

        if (this.chart) {
            this.chart.destroy();
            this.chart = null;
        }

        // Count modules by status
        const counts = { mastered: 0, practicing: 0, learning: 0, new: 0 };
        data.module_masteries.forEach(m => {
            if (counts.hasOwnProperty(m.status)) counts[m.status]++;
        });

        const statusLabels = { mastered: '已掌握', practicing: '练习中', learning: '学习中', new: '未开始' };
        const statusColors = {
            mastered: '#22c55e',
            practicing: '#f59e0b',
            learning: '#8b5cf6',
            new: '#334155',
        };

        const labels = [];
        const values = [];
        const colors = [];
        const order = ['mastered', 'practicing', 'learning', 'new'];
        order.forEach(s => {
            if (counts[s] > 0) {
                labels.push(statusLabels[s]);
                values.push(counts[s]);
                colors.push(statusColors[s]);
            }
        });

        // If nothing at all, show single "new" segment
        if (values.length === 0) {
            labels.push(statusLabels.new);
            values.push(data.module_masteries.length || 1);
            colors.push(statusColors.new);
        }

        this.chart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels,
                datasets: [{
                    data: values,
                    backgroundColor: colors,
                    borderColor: '#0f172a',
                    borderWidth: 2,
                    hoverOffset: 8,
                }],
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                cutout: '68%',
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: '#1e293b',
                        titleColor: '#f1f5f9',
                        bodyColor: '#94a3b8',
                        borderColor: '#334155',
                        borderWidth: 1,
                        padding: 10,
                        cornerRadius: 8,
                    },
                },
            },
        });

        // Legend
        const legendEl = document.getElementById('mastery-legend');
        if (legendEl) {
            legendEl.innerHTML = labels.map((l, i) =>
                `<span class="legend-item"><span class="legend-dot" style="background:${colors[i]}"></span>${l} ${values[i]}</span>`
            ).join('');
        }
    },

    _renderModuleList(masteries) {
        const container = document.getElementById('module-status-list');
        if (!container) return;

        container.innerHTML = masteries.map(m => {
            const pct = Math.round(m.accuracy_avg * 100);
            const statusClass = m.status;
            const statusLabel = this._statusLabel(m.status);
            return `
                <div class="module-status-row">
                    <span class="module-status-icon">${m.icon}</span>
                    <div class="module-status-info">
                        <div class="module-status-name">${m.module_name}</div>
                        <div class="module-status-bar">
                            <div class="module-status-fill" style="width:${pct}%"></div>
                        </div>
                    </div>
                    <span class="module-status-badge ${statusClass}">${statusLabel}</span>
                </div>
            `;
        }).join('');
    },

    _statusLabel(status) {
        const map = { mastered: '已掌握', practicing: '练习中', learning: '学习中', new: '未开始' };
        return map[status] || status;
    },
};
