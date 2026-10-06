from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from app.schemas.branch import BranchCreate, BranchUpdate
from app.models.branch import Branch


from app.db.dependencies  import get_db

router = APIRouter()


@router.post("/branches")
def create_branch(
    branch: BranchCreate,
    db: session= Depends(get_db),
):
    new_branch= Branch(
        name=branch.name, 
        address=branch.address
    )

    db.add(new_branch)
    db.commit()
    db.refresh(new_branch)

    return {"branch": new_branch, "message": "Branch created successfully"}


@router.get("/branches")
def get_branches(db: session = Depends(get_db)):
    branches = [
        {"id": 1, "name": "Coimbatore"},
        {"id": 2, "name": "chennai"},
        {"id": 3, "name": "Bangalore"},
    ]
    return {"branches": branches, "message": "db connected successfully"}
