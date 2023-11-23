#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base

import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


if models.storage_type == "db":
    class Amenity(BaseModel, Base):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
else:
    class Amenity(BaseModel):
        name = ""
