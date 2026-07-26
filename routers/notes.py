"""GET/POST/DELETE /api/notes — user annotations on concepts."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from database import get_db

router = APIRouter(prefix="/api/notes", tags=["notes"])


class NoteSave(BaseModel):
    player_id: int
    concept_name: str
    note_text: str = Field(..., max_length=5000)


@router.get("/{player_id}/{concept_name}")
def get_note(player_id: int, concept_name: str):
    db = get_db()
    row = db.execute(
        "SELECT note_text, updated_at FROM concept_notes WHERE player_id=? AND concept_name=?",
        (player_id, concept_name),
    ).fetchone()
    db.close()
    if row:
        return {"note_text": row["note_text"], "updated_at": row["updated_at"]}
    return {"note_text": "", "updated_at": None}


@router.post("/save")
def save_note(body: NoteSave):
    db = get_db()
    db.execute(
        """INSERT INTO concept_notes (player_id, concept_name, note_text, updated_at)
           VALUES (?,?,?,datetime('now'))
           ON CONFLICT(player_id, concept_name) DO UPDATE SET note_text=?, updated_at=datetime('now')""",
        (body.player_id, body.concept_name, body.note_text, body.note_text),
    )
    db.commit()
    db.close()
    return {"ok": True}


@router.delete("/{player_id}/{concept_name}")
def delete_note(player_id: int, concept_name: str):
    db = get_db()
    db.execute("DELETE FROM concept_notes WHERE player_id=? AND concept_name=?", (player_id, concept_name))
    db.commit()
    db.close()
    return {"ok": True}
