#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(
        String(128),
        nullable=False
    )
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete"
    )

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """get the cities"""
            cities_dic = []
            for value in models.storage.all().values():
                try:
                    if value.state_id == self.id:
                        cities_dic.append(value)
                except BaseException:
                    pass
            return cities_dic
