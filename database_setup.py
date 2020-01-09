import sys, datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Request(Base):
   __tablename__ = 'request'

   id = Column(Integer, primary_key=True)
   component = Column(String(64), nullable=False)
   version = Column(String(64), nullable=False)
   owner = Column(String(64), nullable=False)
   status = Column(String(64), nullable=False)
   date = Column(DateTime, default=datetime.datetime.utcnow)

   @property
   def serialize(self):
      return {
      'id': self.id,
      'component': self.component,
      'version': self.version,
      'owner': self.owner,
      'status': self.status,
      'date': self.date,
   }

engine = create_engine('sqlite:///requests.db')

Base.metadata.create_all(engine)
