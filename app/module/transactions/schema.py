from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum
from uuid import UUID
from app.module.auth.schema import UserPublicResponse


class TransactionType(str, Enum):
    income = "income"
    expense = "expense"


class TransactionCreate(BaseModel):
    amount: float    
    type: TransactionType
    category: Optional[str] = None
    description: Optional[str] = None


class TransactionResponse(BaseModel):
    id: UUID
    user_id: UUID
    amount: float
    type: TransactionType
    category: Optional[str] = None
    description: Optional[str] = None
    created_at: datetime
    
    user: Optional[UserPublicResponse] = None

    class Config:
        from_attributes = True


class TransactionListResponse(BaseModel):
    message: str
    data: List[TransactionResponse]
    page: int
    limit: int
    total: int


class TransactionCreateResponse(BaseModel):
    message: str
    data: TransactionResponse

    class Config:
        from_attributes = True