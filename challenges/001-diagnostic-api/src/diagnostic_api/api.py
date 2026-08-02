from fastapi import APIRouter, HTTPException, Response, status

from diagnostic_api.models import TaskCreate, TaskResponse, TaskStatus, TaskUpdate
from diagnostic_api.service import TaskService


def create_router(service: TaskService) -> APIRouter:
    router = APIRouter(prefix="/tasks", tags=["tasks"])

    @router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
    def create_task(payload: TaskCreate) -> TaskResponse:
        return TaskResponse.model_validate(service.create(payload), from_attributes=True)

    @router.get("", response_model=list[TaskResponse])
    def list_tasks(status: TaskStatus | None = None) -> list[TaskResponse]:
        tasks = service.list_tasks(status)
        return [TaskResponse.model_validate(task, from_attributes=True) for task in tasks]

    @router.get("/{task_id}", response_model=TaskResponse)
    def get_task(task_id: int) -> TaskResponse:
        task = service.get(task_id)
        if task is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return TaskResponse.model_validate(task, from_attributes=True)

    @router.patch("/{task_id}", response_model=TaskResponse)
    def update_task(task_id: int, payload: TaskUpdate) -> TaskResponse:
        raise NotImplementedError

    @router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_task(task_id: int) -> Response:
        raise NotImplementedError

    return router
