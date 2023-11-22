#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from . import storage, storage_type

if storage_type == "db":
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    if storage_type == "db":
        id = Column(String(60), primary_key=TRUE, nullable=FALSE, unique=TRUE)
        created_at = Column(DateTime, default=datetime.utcnow(),
                            nullable=FALSE)
        updated_at = Column(DateTime, default=datetime.utcnow(),
                            nullable=FALSE)

    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        """Initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return dic

    def delete(self):
        """delete the current instance from the storage"""
        storage.delete(self)
