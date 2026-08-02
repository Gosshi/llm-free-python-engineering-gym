from diagnostic_api.models import Task, TaskCreate, TaskStatus, TaskUpdate
from diagnostic_api.repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    def create(self, payload: TaskCreate) -> Task:
        task = Task(
            id=self._repository.next_id(),
            title=payload.title,
            description=payload.description,
            priority=payload.priority,
            status=TaskStatus.TODO,
        )
        return self._repository.add(task)

    def list_tasks(self, status: TaskStatus | None = None) -> list[Task]:
        tasks = self._repository.list_all()
        if status is None:
            return tasks
        return [task for task in tasks if task.status == status]

    def get(self, task_id: int) -> Task | None:
        return self._repository.get(task_id)

    def update(self, task_id: int, payload: TaskUpdate) -> Task | None:
        raise NotImplementedError

    def delete(self, task_id: int) -> bool:
        raise NotImplementedError
