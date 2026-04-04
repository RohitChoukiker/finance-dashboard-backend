from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import db
from app.module.auth.schemas import UserSignupRequest, UserLoginRequest
from app.module.auth.service import AuthService
from app.module.auth.dependencies import get_current_user, role_required
from uuid import UUID


router = APIRouter()


@router.post("/signup")
def signup(data: UserSignupRequest, db_session: Session = Depends(db)):
    service = AuthService(db_session)
    token = service.signup(data)
    return {
        "message": "User created successfully",
        "data": {
            "access_token": token
        }
    }



@router.post("/login")
def login(data: UserLoginRequest, db_session: Session = Depends(db)):
    service = AuthService(db_session)
    token = service.login(data)
    return {
        "message": "Login successful",
        "data": {
            "access_token": token
        }
    }


@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return {
        "message": "User fetched",
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "is_active": user.is_active
        }
    }


@router.get("/users")
def get_users(
    db_session: Session = Depends(db),
    current_user=Depends(role_required(["admin"]))
):
    service = AuthService(db_session)
    return service.get_all_users()



@router.get("/users/count")
def get_users_count(
    db_session: Session = Depends(db),
    current_user=Depends(role_required(["admin"]))
):
    service = AuthService(db_session)
    return service.get_users_count()



@router.put("/users/{user_id}/role")
def change_user_role(
    user_id: UUID,
    role: str,
    db_session: Session = Depends(db),
    current_user=Depends(role_required(["admin"]))
):
    service = AuthService(db_session)
    return service.change_role(user_id, role)


#
@router.put("/users/{user_id}/status")
def update_user_status(
    user_id: UUID,
    is_active: bool,
    db_session: Session = Depends(db),
    current_user=Depends(role_required(["admin"]))
):
    service = AuthService(db_session)
    return service.update_status(user_id, is_active)