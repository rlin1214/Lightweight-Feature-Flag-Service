from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from datetime import datetime

from database import Base


class FeatureFlag(Base):
    __tablename__ = "feature_flags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)

    enabled = Column(Boolean, default=False)

    # emergency kill switch
    kill_switch = Column(Boolean, default=False)

    # percentage rollout
    rollout_percentage = Column(Integer, default=0)

    # comma-separated user ids
    targeted_users = Column(Text, default="")


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    flag_name = Column(String)
    action = Column(String)

    changed_by = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    before_state = Column(Text)
    after_state = Column(Text)