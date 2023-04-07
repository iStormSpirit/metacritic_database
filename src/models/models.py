from sqlalchemy import (DATE, Column, Date, Float, ForeignKey, Integer, String,
                        Table)
from sqlalchemy.orm import relationship

from db.db_coonection import Base

games_genres = Table('games_genres', Base.metadata,
                     Column('game_id', Integer, ForeignKey('game.id')),
                     Column('genre_id', Integer, ForeignKey('genre.id'))
                     )

games_developers = Table('games_developers', Base.metadata,
                         Column('game_id', Integer, ForeignKey('game.id')),
                         Column('developer_id', Integer, ForeignKey('developer.id'))
                         )

games_platforms = Table('games_platforms', Base.metadata,
                        Column('game_id', Integer, ForeignKey('game.id')),
                        Column('platform_id', Integer, ForeignKey('platform.id'))
                        )


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    detail_link = Column(String(150))
    release_date = Column(DATE)
    num_players = Column(String(50))
    meta_score = Column(Integer)
    user_score = Column(Float())
    image_link = Column(String(250))
    description = Column(String(1500))
    game_publisher_id = Column(Integer, ForeignKey('publisher.id'))
    game_publisher = relationship("Publisher", back_populates="games")

    genres = relationship("Genre", secondary=games_genres, back_populates="games")
    developers = relationship("Developer", secondary=games_genres, back_populates="games")
    platforms = relationship("Platform", secondary=games_genres, back_populates="games")


class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    games: list[Game] = relationship('Game', back_populates="game_publisher")


class Developer(Base):
    __tablename__ = 'developer'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)

    games: list[Game] = relationship("Game", secondary=games_genres, back_populates="developers")


class Platform(Base):
    __tablename__ = 'platform'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)

    games: list[Game] = relationship("Game", secondary=games_genres, back_populates="platforms")


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)

    games: list[Game] = relationship("Game", secondary=games_genres, back_populates="genres")
