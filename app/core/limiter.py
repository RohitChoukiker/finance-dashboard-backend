from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

def user_key(request: Request):
    auth = request.headers.get("Authorization")
    if auth:
        return auth.split(" ")[-1]
    return get_remote_address(request)

limiter = Limiter(key_func=user_key)