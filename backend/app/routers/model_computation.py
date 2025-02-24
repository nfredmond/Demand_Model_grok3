from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session
from app.tasks import run_demand_model
from app.config import get_db, get_current_user

router = APIRouter()

@router.post("/run")
async def run_model(
    project_id: int,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    if not project_id:
        raise HTTPException(status_code=400, detail="Project ID is required")
    background_tasks.add_task(run_demand_model, project_id)
    return {"message": f"Model run initiated for project {project_id}"}