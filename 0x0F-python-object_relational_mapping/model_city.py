#!/usr/bin/env python3
"""
defines a State class and a Base class of use with ORM
"""
from sqlalchemy import Column, Integer, String
from model_state import Base, State 


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): the city id of the clase
        name (str): The city name of the class
        state_id (int): the state the city belongs to
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'. nullable=False))
