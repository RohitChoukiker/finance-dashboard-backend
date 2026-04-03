from sqlalchemy import UUID, Column, String, Boolean
from app.database import Base
import uuid
    


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), default="viewer") 
    is_active = Column(Boolean, default=True)