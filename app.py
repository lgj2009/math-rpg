from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from database import init_db
from routers.players import router as players_router
from routers.practice import router as practice_router
from routers.mistakes import router as mistakes_router
from routers.blind_spots import router as blind_spots_router
from routers.tasks import router as tasks_router
from routers.stats import router as stats_router
from routers.feedback import router as feedback_router
from routers.bank import router as bank_router
from routers.combat import router as combat_router
from routers.learn import router as learn_router
from routers.auth import router as auth_router
from routers.guild import router as guild_router
from routers.achieve import router as achieve_router
from routers.seasons import router as seasons_router_new
from routers.membership import router as membership_router

app = FastAPI(title="Math RPG")

static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

app.include_router(players_router)
app.include_router(practice_router)
app.include_router(mistakes_router)
app.include_router(blind_spots_router)
app.include_router(tasks_router)
app.include_router(stats_router)
app.include_router(feedback_router)
app.include_router(bank_router)
app.include_router(combat_router)
app.include_router(learn_router)
app.include_router(auth_router)
app.include_router(guild_router)
app.include_router(achieve_router)
app.include_router(seasons_router_new)
app.include_router(membership_router)


@app.on_event("startup")
def startup():
    init_db()
    # Seeding done at build time (Dockerfile runs build_seed.py)
    pass


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    from fastapi.responses import FileResponse
    return FileResponse(str(static_dir / "index.html"))
