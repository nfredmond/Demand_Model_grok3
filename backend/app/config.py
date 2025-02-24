import os
from fastapi import HTTPException, Header
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/transportation_db")

# Database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Authentication dependency
def get_current_user(authorization: str = Header(...)):
    if authorization != "Bearer secret-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"username": "testuser"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()