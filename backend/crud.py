from sqlalchemy.orm import Session
from . import models, schemas

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(db: Session):
    return db.query(models.Transaction).all()

def get_balance(db: Session):
    transactions = db.query(models.Transaction).all()
    balance = sum(t.amount if t.type == "receita" else -t.amount for t in transactions)
    return balance