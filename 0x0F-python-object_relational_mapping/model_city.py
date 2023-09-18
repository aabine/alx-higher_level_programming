#!/usr/bin/python3
""" Create a model for a city """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey

metaData = MetaData()
Base = declarative_base(metadata=metaData)

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),nullable=False)
