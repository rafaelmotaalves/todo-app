from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

def create_db():    
    return create_engine('postgresql://postgres:password@localhost:15432/postgres', echo=True)

db = create_db()
Session = sessionmaker(db)
base = declarative_base()

def create_session():
    return Session()

def create_tables():
    base.metadata.create_all(db)