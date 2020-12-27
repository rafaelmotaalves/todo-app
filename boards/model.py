import enum
from sqlalchemy import Column, Text, Enum, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from db import base

class Board(base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text)
    todos = relationship("Todo")

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title
        }