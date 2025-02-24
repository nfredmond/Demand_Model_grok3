from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Zone, Demographic
from app.utils.file_processing import process_uploaded_file
from app.config import get_db, get_current_user

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    try:
        data = process_uploaded_file(file)
        for zone_data in data:
            zone = Zone(name=zone_data["name"], geometry=zone_data["geometry"])
            db.add(zone)
        db.commit()
        return {"message": "File uploaded and processed successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

@router.get("/demographics/{zone_id}")
async def get_demographics(
    zone_id: int,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    demographics = db.query(Demographic).filter(Demographic.zone_id == zone_id).first()
    if demographics:
        return {
            "zone_id": demographics.zone_id,
            "population": demographics.population,
            "employment": demographics.employment
        }
    raise HTTPException(status_code=404, detail="No demographics found for this zone")