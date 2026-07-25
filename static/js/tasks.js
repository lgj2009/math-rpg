"use strict";
// tasks.js — Adventurer's Task Board (冒险者任务板)

const tasks = {
    async render() {
        const main = document.getElementById('page-tasks');
        if (!main) return;
        const today = new Date().toISOString().slice(0, 10);
        const p = App.state.player;
        if (!p) {
            main.innerHTML = '<div class="loading">加载中...</div>';
            return;
        }

        // Fetch today's tasks; auto-generate if none exist
        let taskList;
        try {
            taskList = await App.get(`/players/${p.id}/tasks?date=${today}`);
            if (taskList.length === 0) {
                await App.post(`/players/${p.id}/tasks/generate`);
                taskList = await App.get(`/players/${p.id}/tasks?date=${today}`);
            }
        } catch (e) {
            main.innerHTML = `<div class="error">❌ 加载任务失败: ${e.message}</div>`;
            return;
        }

        // Group by type
        const byType = { main: [], side: [], challenge: [] };
        taskList.forEach(t => byType[t.task_type].push(t));

        // Render sections
        main.innerHTML = `
            <h2>☀️ 今日任务板 <span class="streak-badge">🔥×${p.streak_days}</span></h2>
            <div class="quest-section">
                <h3>🗡️ 主线任务</h3>
                ${byType.main.map(t => this.questCard(t)).join('') || '<p class="empty-state">暂无主线任务</p>'}
            </div>
            <div class="quest-section">
                <h3>🧪 支线任务</h3>
                ${byType.side.map(t => this.questCard(t)).join('') || '<p class="empty-state">暂无支线任务</p>'}
            </div>
            <div class="quest-section">
                <h3>⚡ 每日挑战</h3>
                ${byType.challenge.map(t => this.questCard(t)).join('') || '<p class="empty-state">暂无挑战</p>'}
            </div>`;
    },

    questCard(task) {
        const done = task.completed;
        return `<div class="quest-card ${done ? 'quest-done' : ''}">
            <div class="quest-content">${task.content}</div>
            <div class="quest-reward">💰 ${task.xp_reward} XP</div>
            ${task.time_limit_min ? `<div class="quest-timer">⏱ ${task.time_limit_min}分钟</div>` : ''}
            ${!done
                ? `<button class="btn-complete" onclick="tasks.complete(${task.id})">完成</button>`
                : '<span class="quest-done-badge">✅ 已完成</span>'}
        </div>`;
    },

    async complete(taskId) {
        try {
            const result = await App.post(
                `/players/${App.state.player.id}/tasks/${taskId}/complete`,
                { actual_time_min: 0 }
            );
            Audio.levelUp();
            if (result.xp_gained) {
                App.toast(`任务完成! +${result.xp_gained} XP`, 'success');
            } else {
                App.toast('任务完成!', 'success');
            }
            await App.refreshPlayer();
            this.render();
        } catch (e) {
            App.toast(`完成任务失败: ${e.message}`, 'error');
        }
    },
};
