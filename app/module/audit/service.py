from app.module.audit.repository import AuditRepository
from app.exceptions import AppException


class AuditService:

    def __init__(self, db):
        self.repo = AuditRepository(db)

    def log(self, user_id, action, entity, entity_id=None, data=None):
        self.repo.create_log({
            "user_id": user_id,
            "action": action,
            "entity": entity,
            "entity_id": entity_id,
            "data": data  
        })

    
    def get_logs(self, user, user_id=None, action=None, page=1, limit=10):


        if user.role != "admin":
            raise AppException(403, "Only admin can access audit logs")

        logs, total = self.repo.get_logs(user_id, action, page, limit)

        return {
            "message": "Audit logs fetched successfully",
            "data": logs,
            "page": page,
            "limit": limit,
            "total": total
        }