from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

load_dotenv()

class AuthUtils:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hash_password(cls, password: str):
         return cls.pwd_context.hash(password[:72])

    @classmethod
    def verify_password(cls, plain, hashed):
        return cls.pwd_context.verify(plain, hashed)

    @classmethod
    def create_token(cls, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(hours=1)
        to_encode.update({"exp": expire})

        return jwt.encode(to_encode, cls.SECRET_KEY, algorithm=cls.ALGORITHM)

    @classmethod
    def decode_token(cls, token: str):
        return jwt.decode(token, cls.SECRET_KEY, algorithms=[cls.ALGORITHM])