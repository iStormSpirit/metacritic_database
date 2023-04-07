from sqlalchemy import DATE, Column, Float, Integer, String

from db.db_coonection import Base


class Developer(Base):
    __tablename__ = 'developer'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), primary_key=True, index=True)

class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), primary_key=True, index=True)


class Platform(Base):
    __tablename__ = 'platform'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), primary_key=True, index=True)


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), primary_key=True, index=True)


class Game(Base):
    __tablename__ = 'Game'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), primary_key=True, index=True, nullable=False)
    detail_link = Column(String(150))
    release_date = Column(DATE)
    num_players = Column(String(50))
    meta_score = Column(Integer)
    user_score = Column(Float())
    image_link = Column(String(250))
    description = Column(String(1500))
