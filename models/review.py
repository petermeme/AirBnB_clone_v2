#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    if models.storage_type == "db":
        """ Review classto store review information """
        __tablename__ = "reviews"
        place_id = Column(String(60), ForeignKey("places.id"),
                          nullable = False)
        user_id = Column(String(60), ForeignKey("users.id"),
                          nullable = False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
