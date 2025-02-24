from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.utils.llm_utils import query_llm
from app.config import get_db, get_current_user
from app.models import TripMatrix

router = APIRouter()

@router.post("/query")
async def llm_query(
    query: str,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    results = db.query(TripMatrix).all()
    formatted_results = [
        {"origin": r.origin_zone_id, "dest": r.dest_zone_id, "trips": r.trips}
        for r in results
    ]
    answer = query_llm(query, formatted_results)
    return {"answer": answer}