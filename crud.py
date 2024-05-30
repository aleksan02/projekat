from sqlalchemy.orm import Session
import models, schemas

def get_board(db: Session, board_id: int):
    return db.query(models.Board).filter(models.Board.id == board_id).first()

def get_cards(db: Session, list_id: int):
    return db.query(models.Card).filter(models.Card.list_id == list_id).all()

def create_board(db: Session, board: schemas.BoardCreate):
    db_board = models.Board(name=board.name)
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board

def create_list(db: Session, list: schemas.ListCreate, board_id: int):
    db_list = models.List(**list.dict(), board_id=board_id)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list

def create_card(db: Session, card: schemas.CardCreate, list_id: int):
    db_card = models.Card(**card.dict(), list_id=list_id)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card
