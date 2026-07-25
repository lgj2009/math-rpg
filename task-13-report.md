# Task 13 Report: Mistake Book + Monster Gallery Frontend

## Changes Made

### 1. `static/js/components.js` — Implemented `Components.bossCard()`
- Renders a boss card with: icon, name, HP bar (color-coded: green >50%, amber >25%, red <=25%), HP text, defeat count, and "攻击" button
- Card gets CSS class `boss-{boss_type}` for type-specific border accents

### 2. `static/js/mistakes.js` — Full implementation (replaced stub)
3-tab UI:
- **"📝 错题列表"**: Fetches `GET /players/{id}/mistakes` and renders cards showing module name (with icon), error-type badge (calculation/logic/knowledge_gap), retry status ("已掌握" or "已重试 N 次"), and "🔁 重做" button
- **"🐉 怪物图鉴"**: Fetches `GET /players/{id}/blind-spots` and renders a grid of `Components.bossCard()` with HP bars and attack button
- **"⚔️ 今日讨伐"**: Fetches `GET /players/{id}/blind-spots/due-today`, renders each round with the question, a text input for the answer, and a submit button

### 3. `static/css/styles.css` — Added styles for all new components
- `.tab-bar` / `.tab-btn` — tab navigation bar
- `.mistake-grid` / `.mistake-card` — mistake list cards with error-type badges
- `.error-badge` / `.error-{calculation|logic|knowledge_gap}` — color-coded error badges
- `.boss-grid` / `.boss-card` / `.boss-hp-bar` / `.boss-hp-fill` — monster gallery grid and HP bars
- `.boss-{calculation|logic|knowledge_gap|normal}` — boss-type border accents
- `.due-queue` / `.due-item` / `.due-answer-input` — due-today attack queue

### 4. `static/index.html` — Updated sidebar nav label
- Changed from "🐉 怪物图鉴" to "📝 错题本" to reflect the page's full scope

## API Endpoints Consumed
| View | Method | Endpoint |
|------|--------|----------|
| Mistake List | GET | `/api/players/{id}/mistakes` |
| Monster Gallery | GET | `/api/players/{id}/blind-spots` |
| Due Today | GET | `/api/players/{id}/blind-spots/due-today` |
| Retry Mistake | POST | `/api/players/{id}/mistakes/{mid}/retry` |
| Attack Boss | POST | `/api/players/{id}/blind-spots/{sid}/attack` |
| Module Lookup | GET | `/api/modules` |

## Verification
- Server started successfully on port 8765
- All static files served correctly
- Mistake list API returns 5 records with correct field structure
- Blind spots API returns 3 monsters with HP/damage/defeat tracking
- Due-today API returns pending rounds correctly
- Attack and retry POST endpoints work and return correct responses
