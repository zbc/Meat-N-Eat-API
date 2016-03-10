import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    password_hash = Column(String(64), nullable = False)
    email = Column(String(64))
    picture = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    @property
    def serialize(self):
        return {
            'id':self.id,
            'email':self.email,
            'picture':self.picture,
        }

class Request(Base):
    id = Column(Integer, primary_key = True)
    meal_type = Column(String(32))
    location_string = Column(String(100))
    latitude = Column(String(32))
    longtitude = Column(String(32))
    meal_time = Column(DateTime)
    filled = Column(Boolean)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id':self.id,
            'meal_type':self.meal_type,
            'location_string':self.location_string,
            'latitude':self.latitude,
            'longtitude':self.longtitude,
            'meal_time':self.meal_time,
            'filled':self.filled,
            'user_id':self.user_id,
        }

class Proposal(Base):
