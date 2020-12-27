from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

__db__ = create_engine('postgresql://postgres:password@localhost:15432/postgres', echo=False) 
base = declarative_base()

def create_sessionmaker():
    return sessionmaker(__db__)

def create_tables():
    base.metadata.create_all(__db__)