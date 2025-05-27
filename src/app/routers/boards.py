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
