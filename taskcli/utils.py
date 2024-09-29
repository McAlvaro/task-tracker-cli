import argparse
import json
import os

TASKS_FILE = "tasks.json"

class Config:
    @staticmethod
    def load_database() -> dict:
        path = os.path.expanduser(TASKS_FILE)

        if not os.path.exists(path):
            defaul_data = {}
            with open(path, "w") as file:
                json.dump(defaul_data, file)

        with open(path, "r") as file:
            return json.load(file)

    @staticmethod
    def save_database(database: dict) -> None:
        path = os.path.expanduser(TASKS_FILE)
        with open(path, "w") as file:
            json.dump(database, file)

    @staticmethod
    def load_command_args() -> argparse.Namespace:
        parser = argparse.ArgumentParser(description="Task Tracker CLI")
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Add command
        add_parser = subparsers.add_parser("add", help="Add a task")
        add_parser.add_argument("task_description", type=str, help="Task description")

        # Update command
        update_parser = subparsers.add_parser("update", help="Update a task")
        update_parser.add_argument("task_id", type=int, help="Task ID")
        update_parser.add_argument("task_description", type=str, help="Task description")

        # Delete command
        delete_parser = subparsers.add_parser("delete", help="Delete a task")
        delete_parser.add_argument("task_id", type=int, help="Task ID")

        return parser.parse_args();
