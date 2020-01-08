from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Request, Base

engine = create_engine('sqlite:///requests.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
