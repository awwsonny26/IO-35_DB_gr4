# Реалізація інформаційного та програмного забезпечення ⭐

## 📝 SQL-скрипт для створення початкового наповнення бази даних

_init.sql_

```sql
CREATE TABLE `User` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(64),
    `email` VARCHAR(128),
    `password` VARCHAR(64),
    `avatar` VARCHAR(128),
    `status` VARCHAR(32)
);

CREATE TABLE `Member` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT,
    `project_id` INT,
    `role_id` INT
);

CREATE TABLE `Ban` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT,
    `reason` TEXT,
    `untilDate` DATETIME
);

CREATE TABLE `Settings` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT,
    `key` VARCHAR(64),
    `value` TEXT
);

CREATE TABLE `Role` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(32),
    `description` TEXT
);

CREATE TABLE `Permission` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(64)
);

CREATE TABLE `Grant` (
    `role_id` INT,
    `permission_id` INT,
    PRIMARY KEY (`role_id`, `permission_id`)
);

CREATE TABLE `Project` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(64),
    `description` TEXT,
    `creationDate` DATETIME,
    `status` VARCHAR(32)
);

CREATE TABLE `Board` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(64),
    `project_id` INT
);

CREATE TABLE `Block` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `project_id` INT,
    `reason` TEXT,
    `untilDate` DATETIME
);

CREATE TABLE `Task` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(64),
    `description` TEXT,
    `status` VARCHAR(32),
    `startDate` DATE,
    `dueDate` DATE,
    `board_id` INT
);

CREATE TABLE `TaskComment` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `task_id` INT,
    `author_id` INT,
    `content` TEXT,
    `creationDate` DATETIME
);

CREATE TABLE `Assignee` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `task_id` INT,
    `user_id` INT
);

CREATE TABLE `Tag` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(32)
);

CREATE TABLE `TasksTag` (
    `task_id` INT,
    `tag_id` INT,
    PRIMARY KEY (`task_id`, `tag_id`)
);

ALTER TABLE `Member` ADD FOREIGN KEY (`user_id`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Ban` ADD FOREIGN KEY (`user_id`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Settings` ADD FOREIGN KEY (`user_id`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `TaskComment` ADD FOREIGN KEY (`author_id`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Assignee` ADD FOREIGN KEY (`user_id`) REFERENCES `User`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Member` ADD FOREIGN KEY (`project_id`) REFERENCES `Project`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Member` ADD FOREIGN KEY (`role_id`) REFERENCES `Role`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Grant` ADD FOREIGN KEY (`role_id`) REFERENCES `Role`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Grant` ADD FOREIGN KEY (`permission_id`) REFERENCES `Permission`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Board` ADD FOREIGN KEY (`project_id`) REFERENCES `Project`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Block` ADD FOREIGN KEY (`project_id`) REFERENCES `Project`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Task` ADD FOREIGN KEY (`board_id`) REFERENCES `Board`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `TaskComment` ADD FOREIGN KEY (`task_id`) REFERENCES `Task`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `Assignee` ADD FOREIGN KEY (`task_id`) REFERENCES `Task`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `TasksTag` ADD FOREIGN KEY (`task_id`) REFERENCES `Task`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE `TasksTag` ADD FOREIGN KEY (`tag_id`) REFERENCES `Tag`(`id`) ON DELETE CASCADE ON UPDATE CASCADE;
```

_seed.sql_

```sql
BEGIN;

INSERT INTO `Permission` (`name`) VALUES
  ('CREATE_USER'),
  ('AUTHORIZE_USER'),
  ('EDIT_USER'),
  ('DELETE_USER'),
  ('CREATE_PROJECT'),
  ('EDIT_PROJECT'),
  ('DELETE_PROJECT'),
  ('ADD_USER_TO_PROJECT'),
  ('REMOVE_USER_FROM_PROJECT'),
  ('CREATE_BOARD'),
  ('DELETE_BOARD'),
  ('BAN_USER'),
  ('UNBAN_USER'),
  ('EDIT_SYSTEM_SETTINGS'),
  ('CREATE_TASK'),
  ('EDIT_TASK'),
  ('DELETE_TASK'),
  ('CREATE_COMMENT'),
  ('EDIT_COMMENT'),
  ('DELETE_COMMENT');

INSERT INTO `Role` (`name`, `description`) VALUES
  ('USER', 'Basic user access'),
  ('MANAGER', 'Project and team management'),
  ('ADMINISTRATOR', 'Full system access');

-- USER (role_id = 1)
INSERT INTO `Grant` (`role_id`, `permission_id`) VALUES
  (1, 1),  -- CREATE_USER
  (1, 2),  -- AUTHORIZE_USER
  (1, 3),  -- EDIT_USER
  (1, 5),  -- CREATE_PROJECT
  (1, 6),  -- EDIT_PROJECT
  (1, 7);  -- DELETE_PROJECT

-- MANAGER (role_id = 2)
INSERT INTO `Grant` (`role_id`, `permission_id`) VALUES
  (2, 8),   -- ADD_USER_TO_PROJECT
  (2, 9),   -- REMOVE_USER_FROM_PROJECT
  (2, 10),  -- CREATE_BOARD
  (2, 11),  -- DELETE_BOARD

  (2, 15),  -- CREATE_TASK
  (2, 16),  -- EDIT_TASK
  (2, 17),  -- DELETE_TASK
  (2, 18),  -- CREATE_COMMENT
  (2, 19),  -- EDIT_COMMENT
  (2, 20);  -- DELETE_COMMENT

-- ADMINISTRATOR (role_id = 3)
INSERT INTO `Grant` (`role_id`, `permission_id`) VALUES
  (3, 4),   -- DELETE_USER
  (3, 6),   -- EDIT_PROJECT
  (3, 7),   -- DELETE_PROJECT
  (3, 8),   -- ADD_USER_TO_PROJECT
  (3, 9),   -- REMOVE_USER_FROM_PROJECT
  (3, 12),  -- BAN_USER
  (3, 13),  -- UNBAN_USER
  (3, 14);  -- EDIT_SYSTEM_SETTINGS

INSERT INTO `User` (`name`, `email`, `password`, `avatar`, `status`) VALUES
  ('Ivan Shevchenko', 'ivan@example.com', 'hashed_pass_1', 'https://example.com/ivan.jpg', 'ACTIVE'),
  ('Olha Bondarenko', 'olha@example.com', 'hashed_pass_2', NULL, 'ACTIVE'),
  ('Taras Petrenko', 'taras@example.com', 'hashed_pass_3', 'https://example.com/taras.jpg', 'ACTIVE');

INSERT INTO `Project` (`name`, `description`, `creationDate`, `status`) VALUES
  ('Task Manager App', 'A simple task management system', NOW(), 'ACTIVE');

-- Assuming users 1, 2, 3; roles 1 = USER, 2 = MANAGER, 3 = ADMINISTRATOR
INSERT INTO `Member` (`user_id`, `project_id`, `role_id`) VALUES
  (1, 1, 3),  -- Admin
  (2, 1, 2),  -- Manager
  (3, 1, 1);  -- Regular user

INSERT INTO `Board` (`name`, `project_id`) VALUES
  ('Development', 1),
  ('Design', 1);

INSERT INTO `Task` (`name`, `description`, `status`, `startDate`, `dueDate`, `board_id`) VALUES
  ('Design Login Page', 'UI/UX for login', 'OPEN', '2025-05-01', '2025-05-10', 2),
  ('Implement Auth Logic', 'NodeJS backend', 'IN_PROGRESS', '2025-05-02', '2025-05-12', 1);

INSERT INTO `TaskComment` (`task_id`, `author_id`, `content`, `creationDate`) VALUES
  (1, 2, 'Make sure to align with branding', NOW()),
  (2, 3, 'Need help with backend routing', NOW());

INSERT INTO `Tag` (`name`) VALUES
  ('Urgent'),
  ('UI'),
  ('Backend');

INSERT INTO `TasksTag` (`task_id`, `tag_id`) VALUES
  (1, 1),
  (1, 2),
  (2, 3);

INSERT INTO `Assignee` (`task_id`, `user_id`) VALUES
  (1, 2),
  (2, 3);

INSERT INTO `Ban` (`user_id`, `reason`, `untilDate`) VALUES
  (3, 'Spamming comments', '2025-06-01 00:00:00');

INSERT INTO `Settings` (`user_id`, `key`, `value`) VALUES
  (1, 'dark_mode', 'enabled'),
  (2, 'email_notifications', 'true');

COMMIT;
```

## 🐍 RESTful сервіс (Python + FastAPI)

### requirements.txt

```text
fastapi>=0.111
uvicorn[standard]>=0.29
sqlalchemy>=2.0
mysql-connector-python>=8.4
pydantic>=2.7
alembic>=1.13
python-dotenv>=1.0
```

### src/app/db.py

```python
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv(Path(__file__).resolve().parents[2] / ".env")
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL env var not set")

engine = create_engine(DATABASE_URL, pool_pre_ping=True, future=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)
Base = declarative_base()

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### src/app/models.py

```python
import uuid, datetime as dt
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from .db import Base

_uuid = lambda: str(uuid.uuid4())

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
```

### src/app/schemas.py

```python
from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=64)
    description: Optional[str]

class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=64)
    description: Optional[str]
    status: Optional[str] = Field(None, max_length=32)

class ProjectRead(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    creation_date: datetime
    status: str
    model_config = dict(from_attributes=True)

class BoardCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=64)

class BoardRead(BaseModel):
    id: UUID
    name: str
    project_id: UUID
    model_config = dict(from_attributes=True)

class BlockCreate(BaseModel):
    reason: str = Field(..., min_length=1)
    until_date: Optional[datetime]

class BlockRead(BaseModel):
    id: UUID
    project_id: UUID
    reason: str
    until_date: Optional[datetime]
    model_config = dict(from_attributes=True)
```

### src/app/crud.py

```python
from uuid import UUID
from sqlalchemy.orm import Session
from . import models, schemas

# Project

def create_project(db: Session, data: schemas.ProjectCreate):
    proj = models.Project(**data.dict())
    db.add(proj)
    db.commit()
    db.refresh(proj)
    return proj

def get_project(db: Session, project_id: UUID):
    return db.get(models.Project, str(project_id))

def update_project(db: Session, proj, data: schemas.ProjectUpdate):
    for k, v in data.dict(exclude_unset=True).items():
        setattr(proj, k, v)
    db.commit()
    db.refresh(proj)
    return proj

def delete_project(db: Session, proj):
    db.delete(proj)
    db.commit()

# Board

def create_board(db: Session, project_id: UUID, data: schemas.BoardCreate):
    board = models.Board(project_id=str(project_id), **data.dict())
    db.add(board)
    db.commit()
    db.refresh(board)
    return board

def get_board(db: Session, board_id: UUID):
    return db.get(models.Board, str(board_id))

def delete_board(db: Session, board):
    db.delete(board)
    db.commit()

# Block

def create_block(db: Session, project_id: UUID, data: schemas.BlockCreate):
    block = models.Block(project_id=str(project_id), **data.dict())
    db.add(block)
    db.commit()
    db.refresh(block)
    return block
```

### src/app/routers/projects.py

```python
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud, db

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=schemas.ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(data: schemas.ProjectCreate, session: Session = Depends(db.get_session)):
    if not data.name.strip():
        raise HTTPException(400, "NullProjectNameException")
    if len(data.name) > 64:
        raise HTTPException(400, "InvalidProjectNameException")
    return crud.create_project(session, data)

@router.get("/{project_id}", response_model=schemas.ProjectRead)
def get_project(project_id: UUID, session: Session = Depends(db.get_session)):
    project = crud.get_project(session, project_id)
    if not project:
        raise HTTPException(404, "ProjectNotFoundException")
    return project

@router.put("/{project_id}", response_model=schemas.ProjectRead)
def edit_project(project_id: UUID, data: schemas.ProjectUpdate, session: Session = Depends(db.get_session)):
    project = crud.get_project(session, project_id)
    if not project:
        raise HTTPException(404, "ProjectNotFoundException")
    return crud.update_project(session, project, data)

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: UUID, session: Session = Depends(db.get_session)):
    project = crud.get_project(session, project_id)
    if not project:
        raise HTTPException(404, "ProjectNotFoundException")
    crud.delete_project(session, project)
```

### src/app/routers/boards.py

```python
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud, db, models

router = APIRouter(prefix="/projects/{project_id}/boards", tags=["boards"])

@router.post("/", response_model=schemas.BoardRead, status_code=status.HTTP_201_CREATED)
def create_board(project_id: UUID, data: schemas.BoardCreate, session: Session = Depends(db.get_session)):
    if not data.name.strip():
        raise HTTPException(400, "CreateBoard_NoName_EXC")
    duplicate = session.query(models.Board).filter_by(project_id=str(project_id), name=data.name).first()
    if duplicate:
        raise HTTPException(409, "CreateBoard_ExistingName_EXC")
    if not crud.get_project(session, project_id):
        raise HTTPException(404, "ProjectNotFoundException")
    return crud.create_board(session, project_id, data)

@router.delete("/{board_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_board(project_id: UUID, board_id: UUID, session: Session = Depends(db.get_session)):
    board = crud.get_board(session, board_id)
    if not board or board.project_id != str(project_id):
        raise HTTPException(404, "DeleteBoard_InvalidName_EXC")
    crud.delete_board(session, board)
```

### src/app/routers/blocks.py

```python
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, crud, db, models

router = APIRouter(prefix="/projects/{project_id}/blocks", tags=["blocks"])

@router.post("/", response_model=schemas.BlockRead, status_code=status.HTTP_201_CREATED)
def block_project(project_id: UUID, data: schemas.BlockCreate, session: Session = Depends(db.get_session)):
    project = crud.get_project(session, project_id)
    if not project:
        raise HTTPException(404, "BlockProject_ProjectHasBeenRemoved_EXC")
    existing = session.query(models.Block).filter_by(project_id=str(project_id)).first()
    if existing:
        raise HTTPException(409, "BlockProject_ProjectHasBeenBlocked_EXC")
    return crud.create_block(session, project_id, data)
```

### src/app/main.py

```python
from fastapi import FastAPI
from .db import Base, engine
from .routers import projects, boards, blocks

app = FastAPI(title="Project Management API")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(projects.router)
app.include_router(boards.router)
app.include_router(blocks.router)
```