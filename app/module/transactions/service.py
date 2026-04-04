from sqlalchemy import func, extract
from app.module.transactions.repository import TransactionRepository
from app.module.transactions.model import Transaction
from app.exceptions import AppException


class TransactionService:

    def __init__(self, db):
        self.repo = TransactionRepository(db)

 
    def create_transaction(self, data, user):
        transaction = self.repo.create({
            "user_id": user.id,
            "amount": data.amount,
            "type": data.type,
            "category": data.category,
            "description": data.description
        })
        return {"message": "Transaction created", "data": transaction}

    def get_transactions(self, user, type=None, search=None, sort_by="created_at", order="desc", page=1, limit=10):

        if user.role == "viewer":
            transactions, total = self.repo.get_all(user.id, type, search, sort_by, order, page, limit)
        else:
            transactions, total = self.repo.get_all(None, type, search, sort_by, order, page, limit)

        return {
            "message": "Transactions fetched successfully",
            "data": transactions,
            "page": page,
            "limit": limit,
            "total": total
        }

 
    def get_transaction_by_id(self, transaction_id, user):
        transaction = self.repo.get_by_id(transaction_id)

        if not transaction:
            raise AppException(404, "Transaction not found")

        if user.role == "viewer" and transaction.user_id != user.id:
            raise AppException(403, "Unauthorized")

        return transaction

  
    def update_transaction(self, transaction_id, data, user):
        transaction = self.repo.get_by_id(transaction_id)

        if not transaction:
            raise AppException(404, "Transaction not found")


        if user.role != "admin" and transaction.user_id != user.id:
            raise AppException(403, "Unauthorized")

        updated_tx = self.repo.update(transaction, data)

        return {"message": "Transaction updated", "data": updated_tx}

    
    def delete_transaction(self, transaction_id, user):
        transaction = self.repo.get_by_id(transaction_id)

        if not transaction:
            raise AppException(404, "Transaction not found")

      
        if user.role != "admin" and transaction.user_id != user.id:
            raise AppException(403, "Unauthorized")

        self.repo.delete(transaction)

        return {"message": "Transaction deleted"}

   
    def get_summary(self, user):
        query = self.repo.db.query(Transaction)

        if user.role == "viewer":
            query = query.filter(Transaction.user_id == user.id)

        total_income = query.filter(Transaction.type == "income")\
            .with_entities(func.sum(Transaction.amount)).scalar() or 0

        total_expense = query.filter(Transaction.type == "expense")\
            .with_entities(func.sum(Transaction.amount)).scalar() or 0

        return {
            "message": "Dashboard summary",
            "data": {
                "total_income": total_income,
                "total_expense": total_expense,
                "balance": total_income - total_expense
            }
        }


    def category_summary(self, user):
        query = self.repo.db.query(
            Transaction.category,
            func.sum(Transaction.amount).label("total")
        )

        if user.role == "viewer":
            query = query.filter(Transaction.user_id == user.id)

        result = query.group_by(Transaction.category).all()

        return {
            "message": "Category summary",
            "data": [{"category": r[0], "total": r[1]} for r in result]
        }


    
    def monthly_summary(self, user):
        query = self.repo.db.query(
            extract('month', Transaction.created_at).label("month"),
            Transaction.type,
            func.sum(Transaction.amount).label("total")
        )

        if user.role == "viewer":
            query = query.filter(Transaction.user_id == user.id)

        result = query.group_by(
            extract('month', Transaction.created_at),
            Transaction.type
        ).all()

        return {
            "message": "Monthly summary",
            "data": [
                {
                    "month": int(r.month),
                    "type": r.type,
                    "total": r.total
                }
                for r in result
            ]
        }