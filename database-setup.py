import sys, datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Book(Base):
   __tablename__ = 'request'

   id = Column(Integer, primary_key=True)
   component = Column(String(64), nullable=False)
   version = Column(String(64), nullable=False)
   owner = Column(String(64), nullable=False)
   status = Column(String(64), nullable=False)
   date = Column(DateTime, default=datetime.datetime.utcnow)

engine = create_engine('sqlite:///requests.db')

Base.metadata.create_all(engine)
