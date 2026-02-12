import json
import sys
from load_tasks import prepare_storage
from datetime import datetime


def add(file_path):
    tasks = prepare_storage(file_path)
    args = sys.argv[1:]
    if len(args) < 2:
        return "Error: Argument Missing: ./task-cli add <argument(description)>"
    try:
        if len(tasks) == 0:
            id = 1
        else:
            id = max(task["id"] for task in tasks) + 1
        description = args[1]
        status = "todo"

        new_task = {
            "id": id,
            "description": description,
            "status": status,
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat(),
        }

        tasks.append(new_task)
        with open(file_path, "w") as file:
            json.dump(tasks, file, indent=4)
        return f"Task added succesfully (ID: {id})"

    except Exception as e:
        return f"Error: {e}"
