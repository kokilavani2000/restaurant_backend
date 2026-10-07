from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.branch import BranchCreate, BranchUpdate
from app.models.branch import Branch
from app.db.dependencies import get_db
from sqlalchemy import select

def create_branch(
    db: Session,
    branch: BranchCreate,
):
    new_branch= Branch(
        name=branch.name, 
        address=branch.address
    )

    db.add(new_branch)
    db.commit()
    db.refresh(new_branch)

    return {"branch": new_branch, "message": "Branch created successfully"}


def get_branches(
    db: Session
):
    branches = db.scalars(select(Branch)).all()

    return {"branches": branches, "message": "branches fectch successfully"}

def get_branch(
    branch_id: int,
    db: Session,
):
    branch = db.get(Branch, branch_id)
    # here we are telling form the branch table get that barnch id equal values, which mena sthat branch id is primary key

    if branch is None:
        raise HTTPException(
            status_code=404,
            detail="Branch not found",
        )

    return branch

def update_branch(
    branch_id:int,
    branch_update: BranchUpdate,
    db:Session,
):
    branch = db.get(Branch, branch_id)

    if branch is None:
        raise HTTPException(
            status_code = 404,
            detail = "Branch not found"
        )

    branch.name = branch_update.name
    branch.address = branch_update.address

    db.commit()
    db.refresh(branch)

    return  {"branch":branch, "message": "Branch updated successfully"}

def delete_branch(
    branch_id:int,
    db:Session
):
    branch = db.get(Branch, branch_id)

    if branch is None:
        raise HTTPException(
            status_code = 404,
            detail = "Branch not found"
        )

    db.delete(branch)
    db.commit()

    return {"message": "Branch deleted successfully"}