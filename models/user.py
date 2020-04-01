#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'  # TODO change simple attr to table users
    email = Column(
        String(128),
        nullable=False
    )
    password = Column(
        String(128),
        nullable=False
    )
    first_name = Column(
        String(128),
        nullable=True
    )
    last_name = Column(
        String(128),
        nullable=True
    )
    # TODO create relation with Place and Review
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
