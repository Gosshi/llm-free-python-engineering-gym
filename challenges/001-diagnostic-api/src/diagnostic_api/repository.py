from diagnostic_api.models import Task


class TaskRepository:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, task: Task) -> Task:
        self._tasks[task.id] = task
        self._next_id = max(self._next_id, task.id + 1)
        return task

    def next_id(self) -> int:
        task_id = self._next_id
        self._next_id += 1
        return task_id

    def list_all(self) -> list[Task]:
        return list(self._tasks.values())

    def get(self, task_id: int) -> Task | None:
        return self._tasks.get(str(task_id))

    def remove(self, task_id: int) -> Task | None:
        return self._tasks.pop(task_id, None)
