from fastapi import APIRouter, Depends
from sqlalchemy.orm import session

from app.db.dependencies  import get_db

router = APIRouter()

@router.get("/branches")
def get_branches(db: session = Depends(get_db)):
    branches = [
        {"id": 1, "name": "Coimbatore"},
        {"id": 2, "name": "chennai"},
        {"id": 3, "name": "Bangalore"},
    ]
    return {"branches": branches, "message": "db connected successfully"}
