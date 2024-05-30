from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Board(Base):
    __tablename__ = 'boards'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    lists = relationship("List", back_populates="board")

class List(Base):
    __tablename__ = 'lists'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    board_id = Column(Integer, ForeignKey('boards.id'))
    board = relationship("Board", back_populates="lists")
    cards = relationship("Card", back_populates="list")

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    list_id = Column(Integer, ForeignKey('lists.id'))
    list = relationship("List", back_populates="cards")

class Checklist(Base):
    __tablename__ = 'checklists'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    card_id = Column(Integer, ForeignKey('cards.id'))

class Attachment(Base):
    __tablename__ = 'attachments'
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    card_id = Column(Integer, ForeignKey('cards.id'))

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    card_id = Column(Integer, ForeignKey('cards.id'))

DATABASE_URL = "sqlite:///./trello.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
