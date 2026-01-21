import sys
import datetime
from save_tasks import save_tasks


def add(tasks, path):
    if len(sys.argv) < 3:
        print("Usage: python3 main.py add <description>")
        return

    if tasks:
        task_id = max(task["id"] for task in tasks) + 1
    else:
        task_id = 1

    description = " ".join(sys.argv[2:])
    now = datetime.datetime.now().isoformat()

    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    }

    tasks.append(new_task)
    save_tasks(tasks, path)
    return new_task
