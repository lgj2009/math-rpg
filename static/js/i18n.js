"use strict";
// i18n.js — Internationalization: zh (default), en, vi
const I18N = {
    _lang: localStorage.getItem('lang') || 'zh',
    _strings: {
        // Sidebar & Navigation
        sidebar_dashboard:  { zh: '📊 冒险大厅',  en: '📊 Adventure Hall', vi: '📊 Sảnh Mạo Hiểm' },
        sidebar_tasks:     { zh: '📋 任务板',    en: '📋 Quest Board',     vi: '📋 Bảng Nhiệm Vụ' },
        sidebar_learn:     { zh: '📖 学艺堂',    en: '📖 Academy',         vi: '📖 Học Viện' },
        sidebar_practice:  { zh: '⚔️ 狩猎场',    en: '⚔️ Hunting Grounds', vi: '⚔️ Săn Quái' },
        sidebar_mistakes:  { zh: '📝 错题本',    en: '📝 Mistake Log',     vi: '📝 Sổ Tay Lỗi' },
        sidebar_progress:  { zh: '📈 修炼进度',  en: '📈 Progress',        vi: '📈 Tiến Độ' },
        sidebar_bank:      { zh: '📚 题库',      en: '📚 Question Bank',   vi: '📚 Ngân Hàng Đề' },
        sidebar_guild:     { zh: '🏰 公会',      en: '🏰 Guild',           vi: '🏰 Bang Hội' },
        sidebar_season:    { zh: '🏁 赛季通行证', en: '🏁 Season Pass',     vi: '🏁 Mùa Giải' },
        sidebar_achievements: { zh: '🏆 成就殿堂', en: '🏆 Achievements',   vi: '🏆 Thành Tựu' },
        sidebar_settings:  { zh: '⚙️ 设置',      en: '⚙️ Settings',        vi: '⚙️ Cài Đặt' },

        // Player card
        player_level:      { zh: 'Lv.', en: 'Lv.', vi: 'Cấp' },
        player_streak:     { zh: '天',   en: 'd',   vi: 'ngày' },

        // Welcome
        welcome_title:     { zh: '⚔️ 数学冒险',      en: '⚔️ Math RPG',         vi: '⚔️ Phiêu Lưu Toán' },
        welcome_subtitle:  { zh: '把刷题变成打怪升级', en: 'Turn study into battle', vi: 'Biến học tập thành chiến đấu' },
        welcome_placeholder: { zh: '输入你的冒险者名字', en: 'Enter your hero name', vi: 'Nhập tên anh hùng' },
        welcome_btn:       { zh: '开始冒险', en: 'Start Adventure', vi: 'Bắt Đầu' },
        welcome_create_fail: { zh: '创建失败', en: 'Creation failed', vi: 'Tạo thất bại' },

        // Practice / Combat
        practice_title:    { zh: '⚔️ 狩猎场 — 选择模块', en: '⚔️ Hunting Grounds — Select Module', vi: '⚔️ Săn Quái — Chọn Môn' },
        practice_attack:   { zh: '⚔️ 攻击', en: '⚔️ Attack', vi: '⚔️ Tấn Công' },
        practice_next:     { zh: '下一题', en: 'Next', vi: 'Tiếp' },
        practice_submit:   { zh: '提交', en: 'Submit', vi: 'Nộp' },
        practice_crit_active:  { zh: '⚡暴击:', en: '⚡Crit:', vi: '⚡Chí Mạng:' },
        practice_crit_lost:    { zh: '⏰ 暴击失效', en: '⏰ Crit window closed', vi: '⏰ Hết chí mạng' },
        practice_no_questions: { zh: '该模块暂无可用的题目', en: 'No questions available', vi: 'Không có câu hỏi' },
        practice_load_fail:    { zh: '加载模块列表失败', en: 'Failed to load modules', vi: 'Tải danh sách thất bại' },
        practice_submit_fail:  { zh: '提交失败，请重试', en: 'Submit failed, retry', vi: 'Nộp thất bại, thử lại' },
        practice_answer_empty: { zh: '请选择或输入答案', en: 'Please select or enter an answer', vi: 'Vui lòng chọn hoặc nhập đáp án' },

        // Combat result
        combat_perfect:    { zh: '完美讨伐', en: 'Perfect Victory', vi: 'Chiến Thắng Hoàn Hảo' },
        combat_success:    { zh: '讨伐成功', en: 'Victory', vi: 'Chiến Thắng' },
        combat_pass:       { zh: '勉强过关', en: 'Barely Passed', vi: 'Vừa Đủ Qua' },
        combat_fail:       { zh: '讨伐失败', en: 'Defeated', vi: 'Thất Bại' },
        combat_accuracy:   { zh: '正确率', en: 'Accuracy', vi: 'Tỉ lệ đúng' },
        combat_max_combo:  { zh: '最大连击', en: 'Max Combo', vi: 'Combo tối đa' },
        combat_crits:      { zh: '暴击', en: 'Crits', vi: 'Chí mạng' },
        combat_mistakes_created: { zh: '道错题已加入错题本', en: 'mistakes added to log', vi: 'lỗi đã thêm vào sổ tay' },
        combat_tasks_done:  { zh: '个任务自动完成', en: 'tasks auto-completed', vi: 'nhiệm vụ hoàn thành' },
        combat_back:       { zh: '返回狩猎场', en: 'Back to Hunting Grounds', vi: 'Quay Lại Săn Quái' },
        combat_log:        { zh: '战斗记录', en: 'Battle Log', vi: 'Nhật Ký Chiến Đấu' },
        combat_prepare:    { zh: '⚔️ 准备战斗...', en: '⚔️ Preparing for battle...', vi: '⚔️ Chuẩn bị chiến đấu...' },

        // Mistakes
        mistakes_title:    { zh: '📝 错题本', en: '📝 Mistake Log', vi: '📝 Sổ Tay Lỗi' },
        mistakes_list_tab: { zh: '📝 错题列表', en: '📝 Mistake List', vi: '📝 Danh Sách Lỗi' },
        mistakes_gallery_tab: { zh: '🐉 怪物图鉴', en: '🐉 Monster Gallery', vi: '🐉 Bộ Sưu Tập Quái' },
        mistakes_due_tab:  { zh: '⚔️ 今日讨伐', en: '⚔️ Today\'s Hunt', vi: '⚔️ Săn Hôm Nay' },
        mistakes_none:     { zh: '🎉 暂无错题记录', en: '🎉 No mistakes yet', vi: '🎉 Chưa có lỗi nào' },
        mistakes_no_monsters: { zh: '🎉 暂无活跃怪物', en: '🎉 No active monsters', vi: '🎉 Không có quái vật' },
        mistakes_no_due:   { zh: '🎉 今日没有待讨伐的怪物', en: '🎉 No monsters due today', vi: '🎉 Hôm nay không có quái' },
        mistakes_retry:    { zh: '🔁 重做', en: '🔁 Retry', vi: '🔁 Làm Lại' },
        mistakes_mastered: { zh: '✅ 已掌握', en: '✅ Mastered', vi: '✅ Đã Thuộc' },
        mistakes_retries:  { zh: '次重试', en: ' retries', vi: ' lần thử lại' },
        mistakes_load_fail:{ zh: '❌ 加载失败', en: '❌ Load failed', vi: '❌ Tải thất bại' },
        mistakes_attack_fail: { zh: '攻击失败', en: 'Attack failed', vi: 'Tấn công thất bại' },

        // Tasks
        tasks_title:       { zh: '☀️ 今日任务板', en: '☀️ Today\'s Quest Board', vi: '☀️ Bảng Nhiệm Vụ Hôm Nay' },
        tasks_main:        { zh: '🗡️ 主线任务', en: '🗡️ Main Quest', vi: '🗡️ Nhiệm Vụ Chính' },
        tasks_side:        { zh: '🧪 支线任务', en: '🧪 Side Quest', vi: '🧪 Nhiệm Vụ Phụ' },
        tasks_challenge:   { zh: '⚡ 每日挑战', en: '⚡ Daily Challenge', vi: '⚡ Thử Thách' },
        tasks_complete_btn:{ zh: '完成', en: 'Complete', vi: 'Hoàn Thành' },
        tasks_done_badge:  { zh: '✅ 已完成', en: '✅ Done', vi: '✅ Xong' },

        // Bank
        bank_title:        { zh: '📚 题库', en: '📚 Question Bank', vi: '📚 Ngân Hàng Đề' },
        bank_search:       { zh: '搜索题目...', en: 'Search questions...', vi: 'Tìm kiếm...' },
        bank_all_modules:  { zh: '全部模块', en: 'All Modules', vi: 'Tất Cả' },
        bank_all_diff:     { zh: '全部难度', en: 'All Difficulty', vi: 'Tất Cả Độ Khó' },
        bank_all_source:   { zh: '全部来源', en: 'All Sources', vi: 'Tất Cả Nguồn' },
        bank_source_exam:  { zh: '🏛️ 高考真题', en: '🏛️ Gaokao Real', vi: '🏛️ Đề Thi Thật' },
        bank_source_curated: { zh: '📝 精选模拟', en: '📝 Curated', vi: '📝 Tuyển Chọn' },
        bank_source_ai:    { zh: '🤖 AI生成', en: '🤖 AI Generated', vi: '🤖 AI Tạo' },
        bank_diff_1:       { zh: '⭐ 基础', en: '⭐ Basic', vi: '⭐ Cơ Bản' },
        bank_diff_2:       { zh: '⭐⭐ 中档', en: '⭐⭐ Medium', vi: '⭐⭐ Trung Bình' },
        bank_diff_3:       { zh: '⭐⭐⭐ 难题', en: '⭐⭐⭐ Hard', vi: '⭐⭐⭐ Khó' },
        bank_answer:       { zh: '✅ 答案：', en: '✅ Answer: ', vi: '✅ Đáp Án: ' },
        bank_solution:     { zh: '💡 解析：', en: '💡 Solution: ', vi: '💡 Giải Thích: ' },
        bank_type_choice:  { zh: '选择题', en: 'Multiple Choice', vi: 'Trắc Nghiệm' },
        bank_type_fill:    { zh: '填空题', en: 'Fill in Blank', vi: 'Điền Khuyết' },
        bank_type_answer:  { zh: '解答题', en: 'Word Problem', vi: 'Tự Luận' },

        // Learn
        learn_title:       { zh: '📖 学艺堂 — 选择模块', en: '📖 Academy — Select Module', vi: '📖 Học Viện — Chọn Môn' },
        learn_back_modules:{ zh: '← 返回模块列表', en: '← Back to modules', vi: '← Quay lại' },
        learn_back_concepts:{ zh: '← 返回知识点', en: '← Back to concepts', vi: '← Quay lại' },
        learn_no_content:  { zh: '该模块暂无学习内容，请先前往狩猎场练习', en: 'No lessons yet. Try the Hunting Grounds first.', vi: 'Chưa có bài học. Hãy thử Săn Quái trước.' },
        learn_select_hint: { zh: '👈 选择一个知识点开始学习', en: '👈 Select a concept to learn', vi: '👈 Chọn một khái niệm để học' },

        // Dashboard
        dashboard_score:   { zh: '预估分数', en: 'Est. Score', vi: 'Điểm Dự Đoán' },
        dashboard_streak:  { zh: '连续打卡', en: 'Streak', vi: 'Chuỗi Ngày' },
        dashboard_questions: { zh: '累计刷题', en: 'Total Questions', vi: 'Tổng Số Câu' },
        dashboard_mastered:  { zh: '已掌握', en: 'Mastered', vi: 'Đã Thuộc' },

        // Progress
        progress_accuracy: { zh: '正确率', en: 'Accuracy', vi: 'Độ Chính Xác' },
        progress_speed:    { zh: '速度', en: 'Speed', vi: 'Tốc Độ' },
        progress_retention:{ zh: '记忆保持', en: 'Retention', vi: 'Ghi Nhớ' },
        progress_mistakes: { zh: '错题消灭', en: 'Mistake Clear', vi: 'Xóa Lỗi' },
        progress_stability:{ zh: '稳定性', en: 'Stability', vi: 'Ổn Định' },
        progress_mastered: { zh: '已掌握', en: 'Mastered', vi: 'Đã Thuộc' },
        progress_practicing:{ zh: '练习中', en: 'Practicing', vi: 'Đang Luyện' },
        progress_learning: { zh: '学习中', en: 'Learning', vi: 'Đang Học' },
        progress_new:      { zh: '未开始', en: 'New', vi: 'Mới' },

        // Settings
        settings_title:    { zh: '⚙️ 设置', en: '⚙️ Settings', vi: '⚙️ Cài Đặt' },
        settings_theme:    { zh: '🎨 主题', en: '🎨 Theme', vi: '🎨 Giao Diện' },
        settings_theme_val:{ zh: '暗黑模式', en: 'Dark Mode', vi: 'Tối' },
        settings_sound:    { zh: '🔊 音效', en: '🔊 Sound', vi: '🔊 Âm Thanh' },
        settings_sound_on: { zh: '开启', en: 'On', vi: 'Bật' },
        settings_count:    { zh: '⏱️ 默认题量', en: '⏱️ Default Count', vi: '⏱️ Số Câu' },
        settings_count_val:{ zh: '10题/组', en: '10/batch', vi: '10/lần' },
        settings_lang:     { zh: '🌐 语言', en: '🌐 Language', vi: '🌐 Ngôn Ngữ' },
        settings_reset:    { zh: '📊 数据重置', en: '📊 Reset Data', vi: '📊 Xóa Dữ Liệu' },
        settings_reset_btn:{ zh: '重置', en: 'Reset', vi: 'Xóa' },
        settings_feedback: { zh: '📨 反馈与建议', en: '📨 Feedback', vi: '📨 Góp Ý' },
        settings_fb_bug:   { zh: '🐛 报告Bug', en: '🐛 Report Bug', vi: '🐛 Báo Lỗi' },
        settings_fb_feature:{ zh: '💡 功能建议', en: '💡 Feature Request', vi: '💡 Đề Xuất' },
        settings_fb_question:{ zh: '❓ 题目问题', en: '❓ Question Issue', vi: '❓ Vấn Đề Câu Hỏi' },
        settings_fb_other: { zh: '📝 其他反馈', en: '📝 Other', vi: '📝 Khác' },
        settings_fb_placeholder: { zh: '描述你的问题或建议...', en: 'Describe your issue or suggestion...', vi: 'Mô tả vấn đề hoặc góp ý...' },
        settings_fb_send:  { zh: '发送反馈', en: 'Send Feedback', vi: 'Gửi Góp Ý' },
        settings_fb_sending:{ zh: '⏳ 发送中...', en: '⏳ Sending...', vi: '⏳ Đang gửi...' },
        settings_fb_ok:    { zh: '✅ 反馈已发送到邮箱！', en: '✅ Feedback sent!', vi: '✅ Đã gửi góp ý!' },
        settings_fb_saved: { zh: '✅ 反馈已保存！', en: '✅ Feedback saved!', vi: '✅ Đã lưu góp ý!' },
        settings_fb_fail:  { zh: '❌ 发送失败', en: '❌ Send failed', vi: '❌ Gửi thất bại' },
        settings_reset_confirm: { zh: '确定要删除所有数据？', en: 'Delete all data?', vi: 'Xóa tất cả dữ liệu?' },

        // Common
        loading:           { zh: '⏳ 加载中...', en: '⏳ Loading...', vi: '⏳ Đang tải...' },
        no_player:         { zh: '⚠️ 请先创建角色', en: '⚠️ Please create a character first', vi: '⚠️ Vui lòng tạo nhân vật trước' },
        retry:             { zh: '重试', en: 'Retry', vi: 'Thử Lại' },
        back:              { zh: '返回', en: 'Back', vi: 'Quay Lại' },
        prev_page:         { zh: '◀ 上一页', en: '◀ Prev', vi: '◀ Trước' },
        next_page:         { zh: '下一页 ▶', en: 'Next ▶', vi: 'Sau ▶' },
        total_items:       { zh: '共', en: 'Total: ', vi: 'Tổng: ' },

        // Boss names
        boss_trig:         { zh: '🐉 三角魔龙', en: '🐉 Trigon Dragon', vi: '🐉 Rồng Lượng Giác' },
        boss_seq:          { zh: '🔢 数列蛇妖', en: '🔢 Sequence Serpent', vi: '🔢 Rắn Dãy Số' },
        boss_prob:         { zh: '🎲 概率幽灵', en: '🎲 Probability Phantom', vi: '🎲 Ma Xác Suất' },
        boss_geo:          { zh: '📦 立方巨像', en: '📦 Cubic Colossus', vi: '📦 Tượng Khối Lập Phương' },
        boss_analytic:     { zh: '📈 曲线魔兽', en: '📈 Curve Beast', vi: '📈 Quái Đường Cong' },
        boss_derivative:   { zh: '📉 导数恶魔', en: '📉 Derivative Demon', vi: '📉 Quỷ Đạo Hàm' },
        boss_set:          { zh: '🔤 逻辑石像', en: '🔤 Logic Golem', vi: '🔤 Tượng Logic' },
        boss_complex:      { zh: '🧮 复数幻影', en: '🧮 Complex Phantom', vi: '🧮 Ảo Ảnh Số Phức' },

        // Module names
        module_1: { zh: '三角函数与解三角形', en: 'Trigonometry & Triangles', vi: 'Lượng Giác & Tam Giác' },
        module_2: { zh: '数列', en: 'Sequences', vi: 'Dãy Số' },
        module_3: { zh: '统计与概率', en: 'Statistics & Probability', vi: 'Thống Kê & Xác Suất' },
        module_4: { zh: '立体几何', en: 'Solid Geometry', vi: 'Hình Học Không Gian' },
        module_5: { zh: '解析几何', en: 'Analytic Geometry', vi: 'Hình Học Giải Tích' },
        module_6: { zh: '导数及其应用', en: 'Derivatives & Applications', vi: 'Đạo Hàm & Ứng Dụng' },
        module_7: { zh: '集合与常用逻辑', en: 'Sets & Logic', vi: 'Tập Hợp & Logic' },
        module_8: { zh: '复数与向量', en: 'Complex Numbers & Vectors', vi: 'Số Phức & Vector' },

        // Error types
        error_calculation: { zh: '计算错误', en: 'Calculation Error', vi: 'Lỗi Tính Toán' },
        error_logic:       { zh: '逻辑错误', en: 'Logic Error', vi: 'Lỗi Logic' },
        error_knowledge:   { zh: '知识漏洞', en: 'Knowledge Gap', vi: 'Lỗ Hổng Kiến Thức' },

        // Difficulty labels
        diff_easy:   { zh: '基础', en: 'Basic', vi: 'Cơ Bản' },
        diff_medium: { zh: '中档', en: 'Medium', vi: 'Trung Bình' },
        diff_hard:   { zh: '难题', en: 'Hard', vi: 'Khó' },

        // Round labels
        round_1: { zh: '第1轮·今日', en: 'Round 1 · Today', vi: 'Vòng 1 · Hôm Nay' },
        round_2: { zh: '第2轮·第2天', en: 'Round 2 · Day 2', vi: 'Vòng 2 · Ngày 2' },
        round_3: { zh: '第3轮·第7天', en: 'Round 3 · Day 7', vi: 'Vòng 3 · Ngày 7' },
        round_4: { zh: '第4轮·第21天', en: 'Round 4 · Day 21', vi: 'Vòng 4 · Ngày 21' },

        // Status labels
        status_mastered:   { zh: '已掌握', en: 'Mastered', vi: 'Đã Thuộc' },
        status_practicing: { zh: '练习中', en: 'Practicing', vi: 'Đang Luyện' },
        status_learning:   { zh: '学习中', en: 'Learning', vi: 'Đang Học' },
        status_new:        { zh: '未开始', en: 'New', vi: 'Mới' },

        // Question source labels
        source_real_exam:  { zh: '🏛️ 真题', en: '🏛️ Real Exam', vi: '🏛️ Đề Thi Thật' },
        source_curated:    { zh: '📝 精选', en: '📝 Curated', vi: '📝 Tuyển Chọn' },
        source_generated:  { zh: '🤖 生成', en: '🤖 Generated', vi: '🤖 AI Tạo' },

        // Misc
        weight_label:      { zh: '分', en: 'pts', vi: 'điểm' },
        concepts_label:    { zh: '个知识点', en: ' concepts', vi: ' khái niệm' },
        question_label:    { zh: '题', en: ' Qs', vi: ' câu' },
        xp_label:          { zh: 'XP', en: 'XP', vi: 'KN' },

        // Guild
        guild_title:      { zh: '🏰 公会大厅', en: '🏰 Guild Hall', vi: '🏰 Sảnh Công Hội' },
        guild_create_title:{ zh: '创建公会', en: 'Create Your Guild', vi: 'Tạo Công Hội' },
        guild_name_ph:    { zh: '公会名称', en: 'Guild name', vi: 'Tên công hội' },
        guild_desc_ph:    { zh: '描述（可选）', en: 'Description (optional)', vi: 'Mô tả (tùy chọn)' },
        guild_create_btn: { zh: '创建', en: 'Create', vi: 'Tạo' },
        guild_discover:   { zh: '发现公会', en: 'Discover Guilds', vi: 'Khám Phá Công Hội' },
        guild_no_guilds:  { zh: '还没有公会，创建第一个吧！', en: 'No guilds yet. Create the first one!', vi: 'Chưa có công hội nào. Hãy tạo đầu tiên!' },
        guild_join:       { zh: '加入公会', en: 'Join Guild', vi: 'Tham Gia' },
        guild_leave:      { zh: '离开公会', en: 'Leave Guild', vi: 'Rời Công Hội' },
        guild_leave_confirm:{ zh: '确定要离开公会吗？', en: 'Leave this guild?', vi: 'Rời công hội này?' },
        guild_members_label:{ zh: '成员', en: 'Members', vi: 'Thành Viên' },
        guild_weekly_xp:  { zh: '本周 XP', en: 'Weekly XP', vi: 'XP Tuần' },
        guild_daily_xp:   { zh: '今日 XP', en: 'Today XP', vi: 'XP Hôm Nay' },
        guild_tab_overview:{ zh: '🏰 概览', en: '🏰 Overview', vi: '🏰 Tổng Quan' },
        guild_tab_chat:   { zh: '💬 聊天', en: '💬 Chat', vi: '💬 Trò Chuyện' },
        guild_tab_boss:   { zh: '🐉 Boss', en: '🐉 Boss', vi: '🐉 Thủ Lĩnh' },
        guild_tab_feed:   { zh: '📜 动态', en: '📜 Feed', vi: '📜 Hoạt Động' },
        guild_chat_ph:    { zh: '输入消息...', en: 'Type a message...', vi: 'Nhập tin nhắn...' },
        guild_chat_send:  { zh: '发送', en: 'Send', vi: 'Gửi' },
        guild_chat_empty: { zh: '暂无消息，来说句话吧！', en: 'No messages yet. Say hello!', vi: 'Chưa có tin nhắn. Hãy chào mọi người!' },
        guild_boss_title: { zh: '公会 Boss', en: 'Guild Boss', vi: 'Thủ Lĩnh Công Hội' },
        guild_boss_hint:  { zh: '完成练习来贡献伤害！', en: 'Complete practice sessions to contribute damage!', vi: 'Hoàn thành bài tập để gây sát thương!' },
        guild_boss_atk:   { zh: '⚔️ 攻击 (50 伤害)', en: '⚔️ Attack (50 dmg)', vi: '⚔️ Tấn Công (50 dmg)' },
        guild_boss_killed:{ zh: '🏆 BOSS 已被击败！新 Boss 出现了！', en: '🏆 BOSS DEFEATED! New boss spawned!', vi: '🏆 ĐÃ HẠ BOSS! Thủ lĩnh mới xuất hiện!' },
        guild_boss_dmg:   { zh: '造成 50 点伤害！剩余 HP:', en: 'Dealt 50 damage! Boss HP: ', vi: 'Gây 50 sát thương! HP còn: ' },
        guild_feed_empty: { zh: '暂无动态', en: 'No activity yet', vi: 'Chưa có hoạt động' },
        guild_feed_joined:{ zh: '加入了公会', en: 'joined the guild', vi: 'đã tham gia công hội' },
        guild_feed_boss_kill:{ zh: '击杀了公会 BOSS！🎉', en: 'SLAYED THE BOSS! 🎉', vi: 'ĐÃ HẠ THỦ LĨNH! 🎉' },
        guild_create_ok:  { zh: '公会创建成功！', en: 'Guild created!', vi: 'Đã tạo công hội!' },
        guild_joined_ok:  { zh: '已加入公会！', en: 'Joined guild!', vi: 'Đã tham gia công hội!' },
        guild_left_ok:    { zh: '已离开公会', en: 'Left guild', vi: 'Đã rời công hội' },
        guild_name_taken: { zh: '公会名已被占用', en: 'Guild name already taken', vi: 'Tên công hội đã tồn tại' },
        guild_already_in: { zh: '你已经在一个公会中', en: 'You are already in a guild', vi: 'Bạn đã ở trong một công hội' },
        guild_load_fail:  { zh: '加载公会失败', en: 'Failed to load guilds', vi: 'Tải công hội thất bại' },
        guild_send_fail:  { zh: '发送失败', en: 'Send failed', vi: 'Gửi thất bại' },
        guild_desc_default:{ zh: '一群勇者的数学征途。', en: 'A brave guild on a math quest.', vi: 'Một công hội dũng cảm trên hành trình toán học.' },
        guild_on_quest:   { zh: '正在数学征途中！', en: 'On a quest to conquer math!', vi: 'Đang trên hành trình chinh phục toán học!' },
        guild_owner:      { zh: '👑 会长', en: '👑 Owner', vi: '👑 Hội Trưởng' },
        guild_member:     { zh: '⚔️ 成员', en: '⚔️ Member', vi: '⚔️ Thành Viên' },
    },

    t(key) { return (this._strings[key] || {})[this._lang] || (this._strings[key] || {}).zh || key; },

    setLang(lang) { this._lang = lang; localStorage.setItem('lang', lang); },

    applyAll() {
        // Sidebar nav items
        const navMap = {
            dashboard: 'sidebar_dashboard', tasks: 'sidebar_tasks', learn: 'sidebar_learn',
            practice: 'sidebar_practice', mistakes: 'sidebar_mistakes', progress: 'sidebar_progress',
            bank: 'sidebar_bank', guild: 'sidebar_guild', season: 'sidebar_season',
            achievements: 'sidebar_achievements', settings: 'sidebar_settings',
        };
        document.querySelectorAll('.nav-item').forEach(el => {
            const page = el.dataset.page;
            if (navMap[page]) el.textContent = this.t(navMap[page]);
        });
        // Live-update page title if active
        const page = window.location.hash.slice(1) || 'dashboard';
        const pageRenderers = { dashboard, tasks, learn, practice, mistakes, progress, bank, guild, season, achievements, settings };
        if (pageRenderers[page] && typeof pageRenderers[page].render === 'function') {
            pageRenderers[page].render();
        }
    },
};
