import enum
from sqlalchemy import Column, Text, Enum, Integer
from sqlalchemy.ext.declarative import declarative_base  

from db import create_db

base = declarative_base()
class StatusEnum(enum.Enum):
    TODO = "TODO"
    DOING = "DOING"
    DONE = "DONE"

class Todo(base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    description = Column(Text, default="")
    status = Column(Enum(StatusEnum), default=StatusEnum.TODO)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title, 
            'description': self.description, 
            'status': self.status.value}

base.metadata.create_all(create_db())