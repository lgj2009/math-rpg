# Task 11 Report — Mistake API with Three-Question Method

## Status
All 4 steps completed successfully.

## Files Created
- `models/mistake.py` — Pydantic models: MistakeCreate, MistakeRetry, MistakeResponse
- `services/mistake_service.py` — Business logic: create with blind-spot auto-creation, list with filters, retry with energy refund + XP award
- `routers/mistakes.py` — FastAPI routes for POST (create), GET (list), POST /{id}/retry

## Files Modified
- `app.py` — registered the new mistakes router

## Commit
```
2ef081f feat: mistake API — create with 三问法, auto blind-spot, retry with energy refund
```

## Tests Performed (via curl)
| Test | Result |
|------|--------|
| POST /api/players/1/mistakes (with blind_spot_name) | 201, mistake created, blind spot auto-generated |
| POST /api/players/1/mistakes (no blind spot) | 201, mistake created |
| GET /api/players/1/mistakes | returns all mistakes for player |
| POST /api/players/1/mistakes/1/retry (first) | retry_count=1, XP_MISTAKE_RETRY awarded, energy refunded |
| POST /api/players/1/mistakes/1/retry (second) | mastered=true, blind_spot HP reduced by 25 |
| POST /api/players/1/mistakes/999/retry | 404 {detail: "not found"} |

## Verified Behavior
- Blind spot auto-created from mistake with name "Derivative basics" (module_ids=[1], hp_current=75 after 2 retries)
- Energy refunded via `FOCUS_COSTS["fill"] * ENERGY_REFUND_RATE`
- XP awarded via `award_xp(player_id, XP_MISTAKE_RETRY)`
