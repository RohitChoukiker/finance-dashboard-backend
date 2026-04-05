from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from uuid import UUID

from app.database import db
from app.module.transactions.schema import CategorySummaryResponse, TransactionCreate, TransactionCreateResponse, TransactionListResponse, TransactionResponse
from app.module.auth.dependencies import get_current_user, role_required
from app.module.transactions.service import TransactionService

router = APIRouter()


@router.post("", response_model=TransactionCreateResponse)
def create_transaction(
    data: TransactionCreate,
    db_session: Session = Depends(db),
    user=Depends(role_required(["admin", "viewer"]))
):
    return TransactionService(db_session).create_transaction(data, user)


@router.get("", response_model=TransactionListResponse)
def get_transactions(
    type: Optional[str] = None,
    category: Optional[str] = None,
    search: Optional[str] = None,  
    sort_by: Optional[str] = "created_at",  
    order: Optional[str] = "desc",
    page: int = 1,
    limit: int = 10,
    db_session: Session = Depends(db),
    user=Depends(role_required(["admin", "analyst", "viewer"]))
):
    return TransactionService(db_session).get_transactions(user, type, category, search, sort_by, order, page, limit)


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(
    transaction_id: UUID,
    db_session: Session = Depends(db),
    user=Depends(role_required(["admin", "analyst", "viewer"]))
):
    return TransactionService(db_session).get_transaction_by_id(transaction_id, user)



@router.put("/{transaction_id}")
def update_transaction(
    transaction_id: UUID,
    data: TransactionCreate,
    db_session: Session = Depends(db),
    user=Depends(role_required(["admin"]))
):
    return TransactionService(db_session).update_transaction(transaction_id, data, user)


@router.delete("/{transaction_id}")
def delete_transaction(
    transaction_id: UUID,
    db_session: Session = Depends(db),
    user=Depends(role_required(["admin"]))
):
    return TransactionService(db_session).delete_transaction(transaction_id, user)



@router.get("/dashboard/summary", response_model=dict)
def get_summary(
    db_session: Session = Depends(db),
     user=Depends(get_current_user)
):
    return TransactionService(db_session).get_summary(user)


@router.get("/dashboard/category", response_model=CategorySummaryResponse)
def category_summary(
    db_session: Session = Depends(db),
    user=Depends(get_current_user)
):
    return TransactionService(db_session).category_summary(user)


@router.get("/dashboard/monthly")
def monthly_summary(
    db_session: Session = Depends(db),
    user=Depends(get_current_user)
):
    return TransactionService(db_session).monthly_summary(user)