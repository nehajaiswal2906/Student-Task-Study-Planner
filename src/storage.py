import json
from src.task_manager import Task
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "tasks.json"


def save_tasks(tasks):
    task_data = []

    for task in tasks:
        task_dict = {
            "task_id": task.task_id,
            "title": task.title,
            "subject": task.subject,
            "priority": task.priority,
            "deadline": task.deadline,
            "status": task.status
        }

        task_data.append(task_dict)

    with open(DATA_FILE, "w") as file:
        json.dump(task_data, file, indent=4)


def load_tasks():
    try:
        with open(DATA_FILE, "r") as file:
            task_data = json.load(file)

        tasks = []

        for data in task_data:
            task = Task(
                data["task_id"],
                data["title"],
                data["subject"],
                data["priority"],
                data["deadline"]
            )

            task.status = data["status"]
            tasks.append(task)

        return tasks

    except FileNotFoundError:
        return []