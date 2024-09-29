from datetime import datetime
from enum import Enum

from utils import Config

class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

def add_task(database : dict[str, dict], task_description: str) -> None:
    id = str(int(max("0", *database.keys())) + 1)
    created_at = datetime.today().isoformat()
    database[id] = {
        "id": id,
        "description": task_description,
        "status": "todo",
        "createdAt": created_at,
        "updatedAt": created_at
    }
    Config.save_database(database)
    print(f"Task added successfully (ID: {id})")


def update_task(database : dict[str, dict], task_id: str, task_description: str) -> None:
    updated_at = datetime.today().isoformat()
    database[task_id]["description"] = task_description
    database[task_id]["updatedAt"] = updated_at
    Config.save_database(database)
    print(f"Task updated successfully (ID: {task_id})")

def delete_task(database : dict[str, dict], task_id: str) -> None:
    del database[task_id]
    Config.save_database(database)
    print(f"Task deleted successfully (ID: {task_id})")

def mark_task_in_progress(database : dict[str, dict], task_id: str) -> None:
    database[task_id]["status"] = Status.IN_PROGRESS.value
    database[task_id]["updatedAt"] = datetime.today().isoformat()
    Config.save_database(database)

def mark_task_done(database : dict[str, dict], task_id: str) -> None:
    database[task_id]["status"] = Status.DONE.value
    database[task_id]["updatedAt"] = datetime.today().isoformat()
    Config.save_database(database)
