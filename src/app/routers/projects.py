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
