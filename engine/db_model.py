from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args = { "check_same_thread": False }
)

Base = declarative_base()

class File(Base):
    __tablename__ = "files"
    
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    path = Column(String)

SessionLocal = sessionmaker(autoflush = False, bind = engine)

if __name__ == "__main__":
    Base.metadata.create_all(bind = engine)