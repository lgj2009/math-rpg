# Task 16 Report — Dashboard + Progress API

## Files Created

- **`services/mastery_service.py`** — `calculate_mastery(player_id, module_id)` computes a 5-dimension score (accuracy_avg, speed_qualify, retention_score, mistake_clear_rate, stability_score) and persists the result to `module_mastery`. Status is determined from these dimensions against `config.MASTERY_ACCURACY` (0.90) and `config.MASTERY_MISTAKE_CLEAR` (1.0).

- **`routers/stats.py`** — Two endpoints:
  - `GET /api/players/{id}/dashboard` — returns `{player, estimated_score, module_masteries[{module_id, module_name, icon, accuracy_avg, speed_qualify, retention_score, mistake_clear_rate, stability_score, status}], streak_days, total_questions, total_correct}`
  - `GET /api/players/{id}/progress` — returns `{player_id, username, level, modules[...], total_questions, total_correct, overall_accuracy}`

## Files Modified

- **`app.py`** — Added `from routers.stats import router as stats_router` and `app.include_router(stats_router)`
- **`static/js/dashboard.js`** — Full SPA page module rendering stat tiles (estimated score, streak days, total questions, accuracy), a Chart.js doughnut ring chart showing module mastery distribution (mastered/practicing/learning/new), and a per-module status list with accuracy bars.
- **`static/js/progress.js`** — Full SPA page module rendering a Chart.js radar chart (5-dimension overall average + per-module overlay lines), a module tab selector with detail panel (per-dimension bars), and a full table of all modules with all dimensions.
- **`static/css/styles.css`** — Added styles for dashboard/progress: stat tiles, cards, ring chart legend, module status bars/badges, module tabs, detail score rows, progress table.

## Verification

Both API endpoints tested successfully against a running FastAPI instance. Dashboard returns 8 module masteries, estimated_score (0 for new players), streak_days, and total_questions computed from practice_records. Progress returns per-module 5-dimension data plus overall accuracy.

## Commit

`b5bf0db` feat: dashboard + progress API and frontend
