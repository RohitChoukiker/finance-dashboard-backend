from pydantic import BaseModel
from typing import Optional, Dict
from uuid import UUID
from datetime import datetime


class AuditLogResponse(BaseModel):
    id: UUID
    user_id: UUID
    action: str
    entity: str
    entity_id: Optional[UUID]
    data: Optional[Dict]
    created_at: datetime

class AuditLogListResponse(BaseModel):
    message: str
    data: list[AuditLogResponse]
    page: int
    limit: int
    total: int

    class Config:
        from_attributes = True