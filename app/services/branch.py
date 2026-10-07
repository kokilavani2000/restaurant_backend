from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.branch import BranchCreate, BranchUpdate
from app.models.branch import Branch
from sqlalchemy import select
from app.repositories import branch as branch_repository

def create_branch(
    db: Session,
    branch: BranchCreate,
):
    new_branch = branch_repository.create_branch(
        db,
        name=branch.name,
        address=branch.address
    )
 
    return {
        "branch": new_branch,
        "message": "Branch created successfully"
    }


def get_branches(
    db: Session
):
     branches = branch_repository.get_branches(db)

     
     return {
         "branches": branches,
        "message": "branches fectch successfully"
    }

def get_branch(
    branch_id: int,
    db: Session,
):
    branch = branch_repository.get_branch(branch_id, db)

    if branch is None:
        raise HTTPException(
            status_code=404,
            detail="Branch not found",
        )
    
    return {
        "branch": branch,
        "message": "Branch fetched successfully"
    }

def update_branch(
    branch_id:int,
    branch_update: BranchUpdate,
    db:Session,
):

    branch = branch_repository.update_branch(
        branch_id,
        name=branch_update.name,
        address=branch_update.address,
        db=db
    )

    if branch is None:
        raise HTTPException(
            status_code = 404,
            detail = "Branch not found"
        )
    
    return  {"branch":branch, "message": "Branch updated successfully"}

def delete_branch(
    branch_id: int,
    db: Session,
):
    branch = branch_repository.delete_branch(branch_id, db)

    if branch is None:
        raise HTTPException(
            status_code=404,
            detail="Branch not found",
        )

    return {"message": "Branch deleted successfully"}