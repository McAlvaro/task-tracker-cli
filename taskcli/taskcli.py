from functions import add_task, update_task, delete_task
from utils import Config

def main() -> None:
    args = Config.load_command_args()
    database = Config.load_database()

    print(database)

    if args.command == "add":
        add_task(database, args.task_description)
    elif args.command == "update":
        update_task(database, str(args.task_id), args.task_description)
    elif args.command == "delete":
        delete_task(database, str(args.task_id))
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
