"use strict";
const guild = {
    _data: null, _tab: 'overview',

    t(k) { return I18N.t(k); },

    async render() {
        const p = App.state.player;
        if (!p) { document.getElementById('page-guild').innerHTML = '<div class="empty-state"><p>Please login first</p></div>'; return; }
        const el = document.getElementById('page-guild');
        if (!el) return;
        let myGuild = null;
        try {
            const list = await App.get('/guild/list');
            for (const g of list) {
                const detail = await App.get(`/guild/${g.id}`);
                if (detail.is_member) { myGuild = detail; break; }
            }
        } catch (e) {}
        if (myGuild) { this._data = myGuild; this._renderGuild(el); }
        else this._renderDiscovery(el);
    },

    async _renderDiscovery(el) {
        const t = this.t.bind(this);
        let listHTML = '<div class="loading">Loading...</div>';
        try {
            const list = await App.get('/guild/list');
            if (list.length === 0) listHTML = `<div class="empty-state">${t('guild_no_guilds')}</div>`;
            else listHTML = list.map(g => `<div class="guild-card">
                <div class="guild-card-header"><span class="guild-card-name">🏰 ${g.name}</span><span class="guild-card-members">👥 ${g.member_count}</span></div>
                <div class="guild-card-desc">${g.description || t('guild_desc_default')}</div>
                <div class="guild-card-stats"><span>📊 ${t('guild_weekly_xp')}: ${g.weekly_xp}</span><span>🐉 Boss HP: ${g.boss_hp}/${g.boss_max_hp}</span></div>
                <button class="btn-primary" onclick="guild._join(${g.id})">${t('guild_join')}</button></div>`).join('');
        } catch(e) { listHTML = `<div class="error">${t('guild_load_fail')}</div>`; }
        el.innerHTML = `<h2>${t('guild_title')}</h2>
            <div style="margin-bottom:20px"><h3>${t('guild_create_title')}</h3>
                <div class="guild-create-form">
                    <input id="gc-name" placeholder="${t('guild_name_ph')}" maxlength="30" style="padding:10px;border:1px solid rgba(255,255,255,0.1);border-radius:var(--radius);background:var(--bg-field);color:var(--text-primary);font-size:14px;outline:none;flex:1">
                    <input id="gc-desc" placeholder="${t('guild_desc_ph')}" maxlength="100" style="padding:10px;border:1px solid rgba(255,255,255,0.1);border-radius:var(--radius);background:var(--bg-field);color:var(--text-primary);font-size:14px;outline:none;flex:1">
                    <button class="btn-primary" onclick="guild._create()">${t('guild_create_btn')}</button></div>
                <div id="gc-status"></div></div>
            <h3>${t('guild_discover')}</h3><div class="guild-list">${listHTML}</div>`;
    },

    async _create() {
        const t=this.t.bind(this); const name=document.getElementById('gc-name').value.trim(); const desc=document.getElementById('gc-desc').value.trim();
        if(!name){App.toast(t('guild_name_ph'),'warning');return;}
        try{await App.post('/guild/create',{name,description:desc});App.toast(t('guild_create_ok'),'success');this.render();}
        catch(e){document.getElementById('gc-status').innerHTML='<span style="color:var(--ruby)">'+e.message+'</span>';}
    },
    async _join(gid){const t=this.t.bind(this);try{await App.post('/guild/join',{guild_id:gid});App.toast(t('guild_joined_ok'),'success');this.render();}catch(e){App.toast(e.message,'error');}},

    _renderGuild(el) {
        const t=this.t.bind(this); const g=this._data;
        el.innerHTML = `<div class="guild-tabs">
            <button class="tab-btn ${this._tab==='overview'?'active':''}" onclick="guild._switchTab('overview')">${t('guild_tab_overview')}</button>
            <button class="tab-btn ${this._tab==='chat'?'active':''}" onclick="guild._switchTab('chat')">${t('guild_tab_chat')}</button>
            <button class="tab-btn ${this._tab==='boss'?'active':''}" onclick="guild._switchTab('boss')">${t('guild_tab_boss')}</button>
            <button class="tab-btn ${this._tab==='feed'?'active':''}" onclick="guild._switchTab('feed')">${t('guild_tab_feed')}</button></div>
            <div id="guild-tab-content"></div>`;
        this._switchTab(this._tab);
    },

    async _switchTab(tab) {
        this._tab=tab; const t=this.t.bind(this);
        document.querySelectorAll('.guild-tabs .tab-btn').forEach(b=>{
            const txt=b.textContent; const key={'overview':'guild_tab_overview','chat':'guild_tab_chat','boss':'guild_tab_boss','feed':'guild_tab_feed'}[tab];
            b.classList.toggle('active',txt.includes(t(key).replace(/^[^ ]+ /,'')));
        });
        const content=document.getElementById('guild-tab-content'); if(!content)return; const g=this._data;
        if(tab==='overview'){
            const membersHTML=(g.members||[]).map(m=>`<div class="gm-row"><span>${m.role==='owner'?'👑':'⚔️'} <b>${m.username}</b> · Lv.${m.level} · ${m.title}</span><span>📊 ${m.weekly_xp} XP</span></div>`).join('');
            content.innerHTML=`<div class="guild-overview"><h3>🏰 ${g.name}</h3><p style="color:var(--text-secondary);margin-bottom:16px">${g.description||t('guild_on_quest')}</p>
                <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:20px">
                    <div class="stat-tile"><div class="stat-value">${g.member_count}</div><div class="stat-label">${t('guild_members_label')}</div></div>
                    <div class="stat-tile"><div class="stat-value">${g.weekly_xp}</div><div class="stat-label">${t('guild_weekly_xp')}</div></div>
                    <div class="stat-tile"><div class="stat-value">${g.daily_xp}</div><div class="stat-label">${t('guild_daily_xp')}</div></div></div>
                <h4>👥 ${t('guild_members_label')}</h4>${membersHTML}
                ${!g.is_owner?`<button class="btn-danger" style="margin-top:16px" onclick="guild._leave()">${t('guild_leave')}</button>`:''}</div>`;
        }else if(tab==='chat'){
            content.innerHTML=`<div class="guild-chat"><div id="chat-messages" class="chat-messages"><div class="loading">Loading...</div></div>
                <div class="chat-input-row"><input id="chat-input" placeholder="${t('guild_chat_ph')}" maxlength="500" onkeydown="if(event.key==='Enter')guild._sendMessage()">
                <button class="btn-primary" onclick="guild._sendMessage()">${t('guild_chat_send')}</button></div></div>`;
            this._loadMessages();
        }else if(tab==='boss'){
            const hpPct=Math.round(g.boss_hp/g.boss_max_hp*100);
            content.innerHTML=`<div class="guild-boss"><div style="text-align:center;font-size:64px;margin-bottom:16px">🐉</div><h3>${t('guild_boss_title')}</h3>
                <div class="boss-hp-bar-large" style="margin:12px 0"><div class="boss-hp-fill-large" style="width:${hpPct}%;background:${hpPct>50?'var(--emerald)':hpPct>25?'var(--gold)':'var(--ruby)'}"></div></div>
                <div style="text-align:center;font-weight:700;font-size:16px">${g.boss_hp} / ${g.boss_max_hp} HP</div>
                <p style="color:var(--text-secondary);text-align:center;margin:12px 0">${t('guild_boss_hint')}</p>
                <div style="text-align:center"><button class="btn-primary" onclick="guild._attackBoss()">${t('guild_boss_atk')}</button></div>
                <div id="boss-result" style="text-align:center;margin-top:8px"></div></div>`;
        }else if(tab==='feed'){
            content.innerHTML='<div id="feed-list" class="feed-list"><div class="loading">Loading...</div></div>';
            this._loadFeed();
        }
    },

    async _loadMessages(){const t=this.t.bind(this);try{const msgs=await App.get(`/guild/${this._data.id}/messages`);const el=document.getElementById('chat-messages');if(!el)return;el.innerHTML=msgs.length===0?`<div class="empty-state">${t('guild_chat_empty')}</div>`:msgs.map(m=>`<div class="chat-msg"><span class="chat-user">${m.username}</span><span class="chat-text">${m.message}</span><span class="chat-time">${(m.created_at||'').slice(11,16)}</span></div>`).join('');el.scrollTop=el.scrollHeight;}catch(e){}},
    async _sendMessage(){const t=this.t.bind(this);const inp=document.getElementById('chat-input');if(!inp||!inp.value.trim())return;try{await App.post('/guild/messages',{guild_id:this._data.id,message:inp.value.trim()});inp.value='';this._loadMessages();}catch(e){App.toast(t('guild_send_fail'),'error');}},
    async _loadFeed(){const t=this.t.bind(this);try{const feed=await App.get(`/guild/${this._data.id}/activity`);const el=document.getElementById('feed-list');if(!el)return;el.innerHTML=feed.length===0?`<div class="empty-state">${t('guild_feed_empty')}</div>`:feed.map(f=>`<div class="feed-item"><span class="feed-icon">${f.action==='joined'?'👋':f.action==='boss_damage'?'⚔️':f.action==='boss_kill'?'🏆':'📝'}</span><span><b>${f.username}</b> ${f.action==='joined'?t('guild_feed_joined'):f.action==='boss_damage'?f.detail:f.action==='boss_kill'?t('guild_feed_boss_kill'):f.action}</span><span class="feed-time">${(f.created_at||'').slice(11,16)}</span></div>`).join('');}catch(e){}},
    async _attackBoss(){const t=this.t.bind(this);try{const result=await App.post('/guild/boss/attack',{guild_id:this._data.id,damage:50});document.getElementById('boss-result').innerHTML=result.killed?`<span style="color:var(--emerald);font-weight:700">${t('guild_boss_killed')}</span>`:`<span style="color:var(--gold)">${t('guild_boss_dmg')}${result.boss_hp}</span>`;this._data.boss_hp=result.boss_hp;this._data.boss_max_hp=result.boss_max_hp;}catch(e){App.toast(e.message,'error');}},
    async _leave(){const t=this.t.bind(this);if(!confirm(t('guild_leave_confirm')))return;try{await App.post('/guild/leave',{guild_id:this._data.id});App.toast(t('guild_left_ok'),'info');this.render();}catch(e){App.toast(e.message,'error');}},
};
