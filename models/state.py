#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'  # TODO change simple attr to table states
    name = Column(
        String(128),
        nullable=False
    )
    cities = relationship('City', backref='state', cascade='all, delete')
