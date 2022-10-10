import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name=Column(String(50), nullable=False)
    email+Column(String(50), nullable=False)

class Personajes(Base):
    __tablename__ = 'personajes'
    per_id = Column(Integer, primary_key=True)
    per_name = Column(String(50), nullable=False)
    status=Column(String(50), nullable=False)
    species=Column(String(50), nullable=False)

class Episodios(Base):
    __tablename__ = 'episodios'
    epi_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    air_date=Column(String(50), nullable=False)
    episode=Column(String(50), nullable=False)

class Fav_Personajes(Base):
    __tablename__='fav_personajes'
    fav_per_id = Column(Integer, primary_key=True)
    user_id = Column(String(50), ForeignKey ("user.user_id"))
    per_id = Column(Integer, ForeignKey ("episodios.per_id"))
    rel = relationship(Episodios)
    rel= relationship (Personajes)

class Fav_Episodios(Base):
    __tablename__ = 'fav_episodios'
    fav_epi_id = Column(Integer, primary_key=True)
    user_id = Column(String(50), ForeignKey("user.user_id"))
    char_ID = Column(Integer, ForeignKey("personajes.epi_id"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')