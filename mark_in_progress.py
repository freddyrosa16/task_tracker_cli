import sys
import json
from load_tasks import prepare_storage
from datetime import datetime


def mark_in_progress(file_path):
    tasks = prepare_storage(file_path)
    args = sys.argv[1:]
    if len(args) < 2:
        print("Error: Missing argument: ./task-cli mark-in-progress <id>")

    try:
        task_id = int(args[1])
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "in-progress"
                task["updatedAt"] = datetime.now().isoformat()

            with open(file_path, "w") as file:
                json.dump(tasks, file, indent=4)
            return f"Status of the task has been updated succesfully (ID: {task['id']})"
    except Exception as e:
        return f"Error: {e}"
