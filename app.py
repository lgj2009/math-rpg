from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from database import init_db

app = FastAPI(title="Math RPG")

static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def root():
    from fastapi.responses import FileResponse
    return FileResponse(str(static_dir / "index.html"))
