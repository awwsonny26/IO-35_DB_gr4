import uuid
import datetime as dt
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from .db import Base

def _uuid():
    return str(uuid.uuid4())

class Project(Base):
    __tablename__ = "projects"
    id = Column(String(36), primary_key=True, default=_uuid)
    name = Column(String(64), nullable=False)
    description = Column(Text)
    creation_date = Column(DateTime, default=dt.datetime.utcnow, nullable=False)
    status = Column(String(32), default="active", nullable=False)

class Board(Base):
    __tablename__ = "boards"
    id = Column(String(36), primary_key=True, default=_uuid)
    name = Column(String(64), nullable=False)
    project_id = Column(String(36), ForeignKey("projects.id"), nullable=False)

class Block(Base):
    __tablename__ = "blocks"
    id = Column(String(36), primary_key=True, default=_uuid)
    project_id = Column(String(36), ForeignKey("projects.id"), nullable=False)
    reason = Column(Text, nullable=False)
    until_date = Column(DateTime)
