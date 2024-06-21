#!/usr/bin/python3
"""Module that defines a class State"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

PORT = 3306
HOST = 'localhost'


class City(Base):
    """Class State"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
