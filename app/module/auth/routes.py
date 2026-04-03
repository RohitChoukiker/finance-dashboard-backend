from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import db, Base, engine
from app.module.auth.schemas import UserSignupRequest, UserLoginRequest, UserRoleUpdateRequest
from app.module.auth.service import AuthService
from app.module.auth.dependencies import get_current_user, role_required

router = APIRouter()



@router.post("/signup")
def signup(data: UserSignupRequest, db: Session = Depends(db)):
    service = AuthService(db)
    token = service.signup(data)
    return {
        "message": "User created successfully",
        "access_token": token
    }


@router.post("/login")
def login(data: UserLoginRequest, db: Session = Depends(db)):
    service = AuthService(db)
    token = service.login(data)
    return {
        "message": "Login successful",
        "access_token": token
    }

@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }

@router.put("/change-role")
def change_role(
    data: UserRoleUpdateRequest,
    db: Session = Depends(db),
    user=Depends(role_required(["admin"]))  
):
    service = AuthService(db)
    return service.change_role(data.user_id, data.role)