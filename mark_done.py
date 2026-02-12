import sys
import json
from datetime import datetime
from load_tasks import prepare_storage


def mark_done(file_path):
    tasks = prepare_storage(file_path)
    args = sys.argv[1:]
    if len(args) < 2:
        print("Error: missing argument: ./task-cli mark-done <id>")

    try:
        task_id = int(args[1])
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                task["updatedAt"] = datetime.now(), isoformat()

            with open(file_path, "w") as file:
                json.dump(tasks, file_path, indent=4)
            print(f"Status of the task has been updated succesfully (ID: {task['id']})")
    except Exception as e:
        print(f"Error: {e}")
