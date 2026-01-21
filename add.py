import sys
import datetime
from save_tasks import save_tasks


def add(tasks, path):
    if tasks:
        id = max(task["id"] for task in tasks) + 1
    else:
        id = 1
    description = sys.argv[2]
    status = "todo"
    createdAt = datetime.datetime.now().isoformat()
    updatedAt = datetime.datetime.now().isoformat()

    new_task = {
        "id": id,
        "description": description,
        "status": status,
        "createdAt": createdAt,
        "updatedAt": updatedAt,
    }
    tasks.append(new_task)
    save_tasks(tasks, path)
    return new_task
