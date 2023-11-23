#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base

if models.storage_type == "db":
    class City(BaseModel, Base):

        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete-orphan")
else:

    class City(BaseModel):
        """ The city class, contains state ID and name """
        state_id = ""
        name = ""
