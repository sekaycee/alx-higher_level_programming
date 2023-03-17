#!/usr/bin/python3
''' Contain State class and Base, an instance of declarative_base() '''
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

meta = MetaData()
Base = declarative_base(metadata=meta)


class State(Base):
    ''' State class inherit from Base declarative_base()
    links to the MySQL table states
    Attr:
        id, name
    '''
    __tablename__ = 'states'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
