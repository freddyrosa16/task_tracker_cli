import sys
from load_tasks import prepare_storage


def lists(file_path):
    tasks = prepare_storage(file_path)
    args = sys.argv[1:]
    if len(args) < 1:
        print("Error: missing argument: ./task-cli <argument> <status>")

    try:
        if len(args) == 1:
            return tasks
        matching_tasks = []
        for task in tasks:
            if args[0] == "list" and args[1] == "todo":
                if task["status"] == "todo":
                    matching_tasks.append(task)
            if args[0] == "list" and args[1] == "in-progress":
                if task["status"] == "in-progress":
                    matching_tasks.append(task)
            if args[0] == "list" and args[1] == "done":
                if task["status"] == "done":
                    matching_tasks.append(task)
        return matching_tasks
    except Exception as e:
        print(f"Error: {e}")
