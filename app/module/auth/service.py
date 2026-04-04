from app.module.auth.utils import AuthUtils
from app.module.auth.repository import UserRepository
from app.exceptions import AppException

class AuthService:

    def __init__(self, db):
        self.repo = UserRepository(db)
        
    def signup(self, data):
        existing = self.repo.get_by_email(data.email)

        if existing:
            raise AppException(400, "Email already exists")

        hashed = AuthUtils.hash_password(data.password)
        
        user = self.repo.create_user({
            "name": data.name,
            "email": data.email,
            "password": hashed,
            "role": "viewer"
        })

        return {
        "message": "User created successfully",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }

    def login(self, data):
        user = self.repo.get_by_email(data.email)

        if not user:
            raise AppException(404, "User not found")
        
        if not user.is_active:
            raise AppException(403, "User is deactivated")

        if not AuthUtils.verify_password(data.password, user.password):
            raise AppException(400, "Invalid credentials")

        return AuthUtils.create_token({
            "sub": user.email,
            "role": user.role
        })

    def change_role(self, user_id, role):
        user = self.repo.get_by_id(user_id)

        if not user:
            raise AppException(404, "User not found")

        self.repo.update_role(user, role)

        return {"message": "Role updated successfully"}
    
    
    def get_all_users(self):
        users = self.repo.get_all_users()
        return {
            "message": "Users fetched successfully",
            "data": [
                {
                    "id": u.id,
                    "name": u.name,
                    "email": u.email,
                    "role": u.role,
                    "is_active": u.is_active
                } for u in users
            ]
        }
        
    def get_users_count(self):
        count = self.repo.count_users()
        return {
            "message": "Users count fetched",
            "data": {"total_users": count}
        }
    
    
    def update_status(self, user_id, is_active):
        user = self.repo.get_by_id(user_id)

        if not user:
            raise AppException(404, "User not found")

        self.repo.update_status(user, is_active)

        return {
            "message": "User status updated"
        }
            
        