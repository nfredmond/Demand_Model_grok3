from celery import Celery
from app.config import DATABASE_URL
from app.models import Zone, TripMatrix
from app.utils.model_utils import create_aequilibrae_project, compute_trip_matrix
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

logger = logging.getLogger(__name__)

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@celery_app.task
def run_demand_model(project_id: int):
    logger.info(f"Starting demand model for project {project_id}")
    try:
        project_path = create_aequilibrae_project(project_id)
        logger.info(f"AequilibraE project created at: {project_path}")
    except Exception as e:
        logger.error(f"Error creating AequilibraE project: {e}")
        return

    db = SessionLocal()
    try:
        zones = db.query(Zone).all()
        trip_matrix = compute_trip_matrix(zones, use_chunking=True)
        for trip in trip_matrix:
            db.add(TripMatrix(origin_zone_id=trip["origin"], dest_zone_id=trip["dest"], trips=trip["trips"]))
        db.commit()
        logger.info(f"Demand model run completed for project {project_id}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error during model computation: {e}")
    finally:
        db.close()