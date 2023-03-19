#!/usr/bin/python3
''' Contain the class definition of a State and an instance
Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    ''' City class inherit from Base declarative_base()
    links to the MySQL table states
    Attr:
        id, name, state_id
    '''
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
