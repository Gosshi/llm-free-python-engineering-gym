from fastapi import FastAPI

from diagnostic_api.api import create_router
from diagnostic_api.repository import TaskRepository
from diagnostic_api.service import TaskService


def create_app() -> FastAPI:
    app = FastAPI(title="Diagnostic Task API")
    repository = TaskRepository()
    service = TaskService(repository)
    app.include_router(create_router(service))
    return app


app = create_app()
