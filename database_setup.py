import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class ClickCounter(Base):
    __tablename__ = 'clickCounter'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Images(Base):
	__tablename__= 'imagesTable'
	name = Column(String(15),primary_key=True)
	description = Column(String(500))
	matches = Column(Integer)
	wins = Column(Integer)
	loses=Column(Integer)

class Matches(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True)
    winner = Column(String(250), nullable=False)
    loser = Column(String(250), nullable=False)
    position = Column(Integer, nullable = False)

engine = create_engine('sqlite:///paissatge.db')
Base.metadata.create_all(engine)

