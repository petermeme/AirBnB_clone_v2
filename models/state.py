#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy

import models
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    if models.storage_type == 'db':
        """
        State ORM
        """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    else:
        """ State class """
        name = ""

    @property
    def cities(self):
        all_cities = list(storage.all(City).values())
        return list(filter((lambda c: c.state_id == self.id), all_cities))

