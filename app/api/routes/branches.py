from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import db
from app.schemas.branch import BranchCreate, BranchUpdate
from app.models.branch import Branch
from sqlalchemy import select
from app.services import branch as branch_service

from app.db.dependencies  import get_db

router = APIRouter()


@router.post("/branches")
def create_branch(
    branch: BranchCreate,
    db: Session = Depends(get_db)
):
    return  branch_service.create_branch(db, branch) 


@router.get("/branches")
def get_branches(
    db: Session = Depends(get_db)
):
 return branch_service.get_branches(db)



    # this one also correct for a complex queries, bfilters, branc name = is or that, adrees like this

# @router.get("/branches/{branch_id}")
# def get_branches(
#     branch_id: int,
#     db: Session = Depends(get_db),
# ):
#     branches= db.scalars(select(Branch).where(Branch.id == branch_id)).first()

#     return {"branches": branches, "message": "branches fectch successfully"}





@router.get("/branches/{branch_id}")
def get_branch(
    branch_id: int,
    db: Session = Depends(get_db),
):

    return branch_service.get_branch(branch_id, db)


@router.put("/branches/{branch_id}")
def update_branch(
    branch_id:int,
    branch_update: BranchUpdate,
    db:Session=Depends(get_db),
):
    return branch_service.update_branch(branch_id,branch_update, db)



@router.delete("/branches/{branch_id}")
def delete_branch(
    branch_id:int,
    db:Session  = Depends(get_db)
):
 return branch_service.delete_branch(branch_id, db)