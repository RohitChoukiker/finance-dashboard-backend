from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.module.auth.utils import AuthUtils
from sqlalchemy.orm import Session
from app.database import db
from app.module.auth.repository import UserRepository
security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db_session: Session = Depends(db)
):
    try:
        token = credentials.credentials
        payload = AuthUtils.decode_token(token)
      

        email = payload.get("sub")

        repo = UserRepository(db_session)
        user = repo.get_by_email(email)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user
    except:
        raise HTTPException(status_code=401, detail="Invalid token")


def role_required(roles: list):
    def checker(user=Depends(get_current_user)):
        if user.get("role") not in roles:
            raise HTTPException(status_code=403, detail="Access denied")
        return user
    return checker