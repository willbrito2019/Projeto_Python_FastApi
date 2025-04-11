from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, Base
from . import crud, schemas

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/transactions/", response_model=schemas.TransactionResponse)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, transaction)

@app.get("/transactions/")
def read_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

@app.get("/balance/")
def read_balance(db: Session = Depends(get_db)):
    return {"balance": crud.get_balance(db)}