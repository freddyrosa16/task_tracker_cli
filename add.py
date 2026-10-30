from datetime import datetime
from load_tasks import load_tasks
from save_tasks import save_tasks


def add(file_path, description):
    tasks = load_tasks(file_path)
    new_id = 1
    for task in tasks:
        if task["id"] >= new_id:
            new_id = task["id"] + 1

    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }

    tasks.append(new_task)
    save_tasks(file_path, tasks)
    return tasks
