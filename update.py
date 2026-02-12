import sys
import json
from load_tasks import prepare_storage
from datetime import datetime


def update(file_path):
    tasks = prepare_storage(file_path)
    args = sys.argv[1:]
    if len(args) < 3:
        print("Error: Missing argument: ./task-cli update <id> <description>")
    try:
        for task in tasks:
            if int(args[1]) == int(task["id"]):
                task["description"] = args[2]
                task["updatedAt"] = datetime.now().isoformat()

            with open(file_path, "w") as file:
                json.dump(tasks, file, indent=4)
            return f"Task updated succesfully (ID: {task['id']})"
    except Exception as e:
        return f"Error: {e}"
