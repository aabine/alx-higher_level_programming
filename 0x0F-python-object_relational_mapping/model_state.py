#!/usr/bin/python3
"""
State class and base class, an instance of declarative_base().
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, MetaData, String

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    """ State class with name and id attributes
    for each instance of the class.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
