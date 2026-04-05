from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum
from uuid import UUID
from app.module.auth.schema import UserPublicResponse
from app.module.transactions.enums import TransactionCategory


class TransactionType(str, Enum):
    income = "income"
    expense = "expense"


class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0, example=1000)
    type: TransactionType = Field(..., example="income")
    category: Optional[TransactionCategory] = Field(None, example="salary")
    description: Optional[str] = Field(None, example="Monthly salary")


class TransactionResponse(BaseModel):
    id: UUID
    user_id: UUID
    amount: float
    type: TransactionType
    category: Optional[TransactionCategory] = None
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
        
        
class CategorySummaryItem(BaseModel):
    category: str
    total: float
    percentage: float


class CategorySummaryResponse(BaseModel):
    message: str
    data: List[CategorySummaryItem]        