from taskcli.functions import add_task, list_tasks, update_task, delete_task, mark_task_in_progress, mark_task_done
from taskcli.utils import Config

def main() -> None:
    args = Config.load_command_args()
    database = Config.load_database()

    if args.command == "add":
        add_task(database, args.task_description)
    elif args.command == "update":
        update_task(database, str(args.task_id), args.task_description)
    elif args.command == "delete":
        delete_task(database, str(args.task_id))
    elif args.command == "mark-in-progress":
        mark_task_in_progress(database, str(args.task_id))
    elif args.command == "mark-done":
        mark_task_done(database, str(args.task_id))
    elif args.command == "list":
        list_tasks(database, args.status if args.status else "all")
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
