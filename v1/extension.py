from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#updates database url
DATABASE_URL = "mysql+mysqlconnector://root:MyStrongPass123!@192.168.1.100/bot"

# create engine
engine = create_engine(DATABASE_URL, echo=True)
#session factory
SessionLocal = sessionmaker(bind=engine)
#class for models
Base = declarative_base()