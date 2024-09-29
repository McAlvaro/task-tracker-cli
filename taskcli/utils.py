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
