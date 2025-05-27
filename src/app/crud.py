from uuid import UUID
from sqlalchemy.orm import Session
from . import models, schemas

def create_project(db: Session, data: schemas.ProjectCreate):
    project = models.Project(**data.dict())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_project(db: Session, project_id: UUID):
    return db.get(models.Project, str(project_id))

def update_project(db: Session, project, data: schemas.ProjectUpdate):
    for k, v in data.dict(exclude_unset=True).items():
        setattr(project, k, v)
    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project):
    db.delete(project)
    db.commit()

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

def create_block(db: Session, project_id: UUID, data: schemas.BlockCreate):
    block = models.Block(project_id=str(project_id), **data.dict())
    db.add(block)
    db.commit()
    db.refresh(block)
    return block
