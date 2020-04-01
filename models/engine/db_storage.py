#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from os import getenv


class DBStorage():
    """Class to manage the data in database"""

    __engine = None
    __session = None

    def __init__(self):
        """Contructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Select data from table"""
        records = []
        if cls is not None:
            records = self.__session.query(cls).all()
        else:
            listClass = [State, City]
            for nameClase in listClass:
                temp = self.__session.query(nameClase).all()
                records.extend(temp)

        dict_return = {}
        for row in records:
            attr_key = "{}.{}".format(type(row).__name__, row.id)
            attr_value = row
            dict_return[attr_key] = attr_value
        return dict_return

    def new(self, obj):
        """add to session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Confirm all the changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the datav"""
        if obj:
            self.__session.query(obj).delete(synchronize_session='fetch')

    def reload(self):
        """create the session"""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session()
