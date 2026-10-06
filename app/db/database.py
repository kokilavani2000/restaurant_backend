from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = "postgresql+psycopg://postgres:root@localhost:5432/restaurant_db"
# DATABASE_URL=postgresql+psycopg://postgres:root@localhost:5432/ecommerce_fastapi
# SECRET_KEY=scretkeyjaskhajshasfafadsasfassfaaaaaaaaaas,xcncherkuybcoiqewm
# ALGORITHM =HS256

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine)

class Base(DeclarativeBase):
    pass