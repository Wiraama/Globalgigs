#from sqlalchemy import Column, Integer, String
#from v1.extension import Base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    tel_id = Column(String(255),nullable=False, unique=True)
    f_name = Column(String(255))
    l_name = Column(String(255))

    print(f"New User <{id}-{f_name} {l_name} added")
    
class Gigs(Base):
    __tablename__ = "gigs"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    about = Column(String(1024))
    link = Column(String(255), unique=True)
    
    print(f"New Gig <{id}-{title} added")"""
# sqlite database
class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    tel_id = db.Column(db.String(255),nullable=False, unique=True)
    f_name = db.Column(db.String(255))
    l_name = db.Column(db.String(255))

    print(f"New User <{id}-{f_name} {l_name} added")
    
class Gigs(db.Model):
    __tablename__ = "gigs"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    about = db.Column(db.String(1024))
    link = db.Column(db.String(255), unique=True)
    
    print(f"New Gig <{id}-{title} added")