from sqlalchemy.orm import Session
from app.module.auth import model as models

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(models.User).filter(models.User.email == email).first()

    def get_by_id(self, user_id: int):
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def create_user(self, data: dict):
        user = models.User(**data)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_role(self, user, role: str):
        user.role = role
        self.db.commit()
        return user