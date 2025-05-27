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
