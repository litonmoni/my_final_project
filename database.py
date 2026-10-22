from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL ="mysql+pymysql://root:root@localhost:3306/training_db"
DATABASE_URL = "postgresql+psycopg2://training_db_hcxj_user:nFpZE4Z2T4yUgNDVyrXT5BQzX72zjr50@dpg-dbctgggm7kps73csvvi0-a.oregon-postgres.render.com/training_db_hcxj"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()