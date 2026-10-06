from app.db.database import Base, engine
from app.models.branch import Branch

Base.metadata.create_all(bind=engine)