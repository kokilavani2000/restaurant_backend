from app.db.database import SessionLocal

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# chkc why we did not habdle error logic?? excetion