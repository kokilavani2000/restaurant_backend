from sqlalchemy.orm import Session
from app.models.branch import Branch
from sqlalchemy import select
from fastapi import HTTPException

def create_branch(
        db: Session,
        name:str,
        address:str
):
    new_branch= Branch(
        name=name, 
        address=address
    )

    db.add(new_branch)
    db.commit()
    db.refresh(new_branch)

    return new_branch

def get_branches(
    db: Session
):

    branches = db.scalars(select(Branch)).all()

    return branches



def get_branch(
    branch_id:int,
    db:Session
):
    branch = db.get(Branch, branch_id)

    if branch is None:
        return None
    # here we are telling form the branch table get that barnch id equal values, which mena sthat branch id is primary key

    return branch

def update_branch(
    branch_id:int,
    name:str,
    address:str,
    db:Session,
):
    branch = db.get(Branch, branch_id)

    if branch is None:
        return None

    branch.name = name
    branch.address = address

    db.commit()
    db.refresh(branch)

    return branch

def delete_branch(
    branch_id: int,
    db: Session,
):
    branch = db.get(Branch, branch_id)

    if branch is None:
        return None

    db.delete(branch)
    db.commit()

    return branch