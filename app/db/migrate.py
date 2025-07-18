from app.db.models import Base
from app.db.database import engine

def create_tables():
    print("db tables are creating...")
    Base.metadata.create_all(bind=engine)
    print("tables are ok")

if __name__ == "__main__":
    create_tables()

# scheme oluşturmak için
# python -m app.db.migrate