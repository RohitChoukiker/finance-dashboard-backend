from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class UserSignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)
    
    
    
class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str
    
class UserRoleUpdateRequest(BaseModel):
    user_id: int
    role: Literal["viewer", "analyst", "admin"]
    
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool


class Config:
    from_attributes = True