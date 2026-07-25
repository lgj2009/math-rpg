from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from database import init_db
from routers.players import router as players_router
from routers.practice import router as practice_router
from routers.mistakes import router as mistakes_router
from routers.blind_spots import router as blind_spots_router

app = FastAPI(title="Math RPG")

static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

app.include_router(players_router)
app.include_router(practice_router)
app.include_router(mistakes_router)
app.include_router(blind_spots_router)


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    from fastapi.responses import FileResponse
    return FileResponse(str(static_dir / "index.html"))
