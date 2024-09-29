import argparse
from functions import add_task, update_task
from utils import Config

def create_parser() -> argparse.ArgumentParser:
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

    return parser;

def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    database = Config().load_database()

    print(database)

    if args.command == "add":
        add_task(database, args.task_description)
    elif args.command == "update":
        update_task(database, str(args.task_id), args.task_description)
        print(f"Updating task: {args.task_description}")
    elif args.command == "delete":
        print(f"Deleting task: {args.task_id}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
