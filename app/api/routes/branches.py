from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.branch import BranchCreate, BranchUpdate
from app.models.branch import Branch
from sqlalchemy import select


from app.db.dependencies  import get_db

router = APIRouter()


@router.post("/branches")
def create_branch(
    branch: BranchCreate,
    db: Session= Depends(get_db),
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
def get_branches(
    db: Session = Depends(get_db)
):
    branches = db.scalars(select(Branch)).all()

    return {"branches": branches, "message": "branches fectch successfully"}



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
    branch = db.get(Branch, branch_id)
    # here we are telling form the branch table get that barnch id equal values, which mena sthat branch id is primary key

    if branch is None:
        raise HTTPException(
            status_code=404,
            detail="Branch not found",
        )

    return branch


@router.put("/branches/{branch_id}")
def update_branch(
    branch_id:int,
    branch_update: BranchUpdate,
    db:Session=Depends(get_db),
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

@router.delete("/branches/{branch_id}")
def delete_branch(
    branch_id:int,
    db:Session  = Depends(get_db)
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