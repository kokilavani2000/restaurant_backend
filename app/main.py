from fastapi import FastAPI
from app.api.routes.branches import router as branches_router

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}


app.include_router(branches_router)


