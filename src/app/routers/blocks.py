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
