from dataclasses import dataclass
from enum import Enum
from datetime import datetime
import json

class TaskStatus(Enum):
    NEW = 'Новая'
    IN_PROGRESS = 'Выполняется'
    UNDER_REVIEW = 'Ревью'
    COMPLETED = 'Выполнено'
    CANCELED = 'Отменено'

@dataclass
class Task:
    title: str
    description: str
    status: str
    created_at: str
    status_changed_at: str

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
        self.tasks.append(task)
        self.history.append(f"Добавлена задача '{task.title}' со статусом '{task.status}'")

    def change_task_status(self, task_index, new_status):
        task = self.tasks[task_index]
        old_status = task.status
        task.status = new_status
        task.status_changed_at = str(datetime.now())
        self.history.append(f"Статус задачи '{task.title}' изменен с '{old_status}' на '{new_status}'")

    def cancel_task(self, task_index):
        self.change_task_status(task_index, TaskStatus.CANCELED.value)

    def save_to_file(self, file_path):
        with open(file_path, 'w') as file:
            data = {
                'tasks': [task.__dict__ for task in self.tasks],
                'history': self.history
            }
            json.dump(data, file, ensure_ascii=False, indent=2)

    def load_from_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            self.tasks = [Task(**task_data) for task_data in data['tasks']]
            self.history = data['history']