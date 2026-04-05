from sqlalchemy import desc
from app.module.audit.model import AuditLog


class AuditRepository:

    def __init__(self, db):
        self.db = db

    def create_log(self, data):
        log = AuditLog(**data)
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log


    def get_logs(self, user_id=None, action=None, page=1, limit=10):
        query = self.db.query(AuditLog)

        if user_id is not None:
            query = query.filter(AuditLog.user_id == user_id)

        if action:
            query = query.filter(AuditLog.action == action)

        total = query.count()

        data = query.order_by(desc(AuditLog.created_at))\
            .offset((page - 1) * limit)\
            .limit(limit)\
            .all()

        return data, total