from sqlalchemy import asc, desc, or_
from app.module.transactions import model as models


class TransactionRepository:

    def __init__(self, db):
        self.db = db

    def create(self, data):
        transaction = models.Transaction(**data)
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def get_all(self, user_id=None, type=None,category=None, search=None, sort_by="created_at", order="desc", page=1, limit=10):
        query = self.db.query(models.Transaction)
        query = query.filter(models.Transaction.is_deleted.is_(False))

        if user_id is not None:
            query = query.filter(models.Transaction.user_id == user_id)

        if type:
            query = query.filter(models.Transaction.type == type)
            
        if category:    
            query = query.filter(models.Transaction.category == category)

        if search:
            query = query.filter(
                or_(
                    models.Transaction.category.ilike(f"%{search}%"),
                    models.Transaction.description.ilike(f"%{search}%")
                )
            )


        allowed_sort_fields = ["amount", "created_at", "type"]
        if sort_by not in allowed_sort_fields:
            sort_by = "created_at"

        sort_column = getattr(models.Transaction, sort_by)

        if order == "desc":
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        total = query.count()
        data = query.offset((page - 1) * limit).limit(limit).all()

        return data, total
    
    

    def get_by_id(self, transaction_id):
        return self.db.query(models.Transaction).filter(
            models.Transaction.id == transaction_id,
            models.Transaction.is_deleted.is_(False)
        ).first()

    def update(self, transaction, data):
        transaction.amount = data.amount
        transaction.type = data.type
        transaction.category = data.category
        transaction.description = data.description

        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def hard_delete(self, transaction):
        self.db.delete(transaction)
        self.db.commit()