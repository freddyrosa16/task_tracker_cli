import sys
import json
from load_tasks import prepare_storage


def delete(file_path):
    tasks = prepare_storage(file_path)
    args = sys.argv[1:]
    if len(args) < 2:
        return "Error: Missing Argument: ./task-cli delete <id>"

    try:
        task_id = int(args[1])
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                break

        with open(file_path, "w") as file:
            json.dump(tasks, file, indent=4)

        return f"Task {task['id']} has been deleted succesfully"
    except Exception as e:
        return f"Error: {e}"
