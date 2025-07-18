#db bağlantısını yönet

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = ""

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
