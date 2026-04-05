from datetime import datetime
from sqlalchemy.orm import relationship
from app.database import Base
import uuid
from sqlalchemy import Boolean, Column, String, Float, DateTime, ForeignKey, UUID
from app.module.transactions.enums import TransactionCategory
from sqlalchemy.types import Enum as SQLAlchemyEnum

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    category = Column(SQLAlchemyEnum(TransactionCategory), nullable=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="transactions")
    is_deleted = Column(Boolean, default=False)