from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
from typing import Literal
from app.module.auth.enums import UserRole

class UserSignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)
    
    
class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str
    
class UserRoleUpdateRequest(BaseModel):
    user_id: UUID
    role: UserRole
    
class UserResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: UserRole
    is_active: bool
    
class UserPublicResponse(BaseModel):
    name: str
    email: EmailStr
    
    class Config:
        from_attributes = True