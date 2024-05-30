from pydantic import BaseModel
from typing import List, Optional

class CardBase(BaseModel):
    name: str
    description: Optional[str] = None

class CardCreate(CardBase):
    pass

class Card(CardBase):
    id: int
    list_id: int

    class Config:
        orm_mode = True

class ListBase(BaseModel):
    name: str

class ListCreate(ListBase):
    pass

class List(ListBase):
    id: int
    board_id: int
    cards: List[Card] = []

    class Config:
        orm_mode = True

class BoardBase(BaseModel):
    name: str

class BoardCreate(BoardBase):
    pass

class Board(BoardBase):
    id: int
    lists: List[List] = []

    class Config:
        orm_mode = True
