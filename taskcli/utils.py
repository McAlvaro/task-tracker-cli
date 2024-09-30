import argparse
import json
import os

TASKS_FILE = "~/taskly.json"

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

        # Mark as in progress command
        mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress")
        mark_in_progress_parser.add_argument("task_id", type=int, help="Task ID")

        # Mark as done command
        mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
        mark_done_parser.add_argument("task_id", type=int, help="Task ID")

        # List command
        list_parser = subparsers.add_parser("list", help="List all tasks")
        list_subparsers = list_parser.add_subparsers(dest="status", help="Filter tasks by status")

        list_subparsers.add_parser("todo", help="List todo tasks")
        list_subparsers.add_parser("in-progress", help="List tasks in progress")
        list_subparsers.add_parser("done", help="List done tasks")

        return parser.parse_args();
