from sqlalchemy.orm import Session
from app.module.auth.repository import UserRepository
from app.module.auth.utils import AuthUtils

def seed_admin(db: Session):
    repo = UserRepository(db)

    admin_email = "admin@gmail.com"
    admin_password = "admin123"

    existing_admin = repo.get_by_email(admin_email)

    if existing_admin:
        print("Admin already exists")
        return

    hashed_password = AuthUtils.hash_password(admin_password)

    repo.create_user({
        "name": "Admin",
        "email": admin_email,
        "password": hashed_password,
        "role": "admin"
    })

    print("Admin user created")