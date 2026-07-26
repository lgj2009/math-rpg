"""GET/POST/DELETE /api/notes — user annotations on concepts."""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from database import get_db

router = APIRouter(prefix="/api/notes", tags=["notes"])


class NoteSave(BaseModel):
    player_id: int
    concept_name: str
    layer_id: int = 0
    note_text: str = Field(..., max_length=5000)


@router.get("/{player_id}/{concept_name}")
def get_notes(player_id: int, concept_name: str):
    db = get_db()
    rows = db.execute(
        "SELECT layer_id, note_text, updated_at FROM concept_notes WHERE player_id=? AND concept_name=? ORDER BY layer_id",
        (player_id, concept_name),
    ).fetchall()
    db.close()
    result = {}
    for r in rows:
        result[str(r["layer_id"])] = {"note_text": r["note_text"], "updated_at": r["updated_at"]}
    return result


@router.post("/save")
def save_note(body: NoteSave):
    db = get_db()
    db.execute(
        """INSERT INTO concept_notes (player_id, concept_name, layer_id, note_text, updated_at)
           VALUES (?,?,?,?,datetime('now'))
           ON CONFLICT(player_id, concept_name, layer_id) DO UPDATE SET note_text=?, updated_at=datetime('now')""",
        (body.player_id, body.concept_name, body.layer_id, body.note_text, body.note_text),
    )
    db.commit()
    db.close()
    return {"ok": True}


@router.delete("/{player_id}/{concept_name}/{layer_id}")
def delete_note(player_id: int, concept_name: str, layer_id: int):
    db = get_db()
    db.execute("DELETE FROM concept_notes WHERE player_id=? AND concept_name=? AND layer_id=?",
               (player_id, concept_name, layer_id))
    db.commit()
    db.close()
    return {"ok": True}
