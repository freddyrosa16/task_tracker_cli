import datetime
import json

from load_tasks import load_tasks


def add(file_path, args):
    tasks = load_tasks(file_path)

    new_id = max((task.get("id", 0) for task in tasks), default=0) + 1
    description = args[1]
    status = "todo"
    createdAt = datetime.datetime.now().isoformat()
    updatedAt = datetime.datetime.now().isoformat()

    new_task = {
        "id": new_id,
        "description": description,
        "status": status,
        "createdAt": createdAt,
        "updatedAt": updatedAt,
    }

    tasks.append(new_task)
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)
    return tasks
