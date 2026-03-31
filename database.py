from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base

DB_PATH = "facturas.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, echo=False)  # echo=True para ver SQL
SessionLocal = scoped_session(sessionmaker(bind=engine))

def init_db():
    """Crea las tablas si no existen."""
    Base.metadata.create_all(bind=engine)