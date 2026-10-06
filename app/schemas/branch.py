from  pydantic import  BaseModel

class BranchCreate(BaseModel):
    name: str
    address: str


class BranchUpdate(BaseModel):
    name: str 
    address: str