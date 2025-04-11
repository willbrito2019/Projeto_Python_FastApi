from pydantic import BaseModel

class TransactionCreate(BaseModel):
    description: str
    amount: float
    type: str  # "receita" ou "despesa"

class TransactionResponse(TransactionCreate):
    id: int
    class Config:
        from_attributes = True
