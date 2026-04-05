from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from uuid import UUID

from app.database import db
from app.module.audit.service import AuditService
from app.module.audit.schema import AuditLogListResponse
from app.module.auth.dependencies import role_required

router = APIRouter()


@router.get("", response_model=AuditLogListResponse)
def get_audit_logs(
    user_id: Optional[UUID] = None,
    action: Optional[str] = None,
    page: int = 1,
    limit: int = 10,
    db_session: Session = Depends(db),
    user=Depends(role_required(["admin"]))   
):
    return AuditService(db_session).get_logs(user, user_id, action, page, limit)