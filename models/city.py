#!/usr/bin/python3
"""city class"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from models.place import Place


class City(BaseModel, Base):
    """This is the class for City
    Attributes: state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
