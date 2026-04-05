from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

from app.database import Base, db, engine
from app.exceptions import AppException
from app.module.auth.routes import router as auth_router
from app.module.transactions.routes import router as transaction_router
from app.module.audit.routes import router as audit_router
from app.module.auth.seed import seed_admin
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_session = next(db())
    seed_admin(db_session)
    yield

app = FastAPI(lifespan=lifespan)


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message}
    )

@app.get("/")
async def root():
    return {"message": "API is running"}

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(transaction_router, prefix="/transactions", tags=["Transactions"])
app.include_router(audit_router, prefix="/audit", tags=["Audit"])

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0", port=8000)