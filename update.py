from datetime import datetime
from load_tasks import load_tasks
from save_tasks import save_tasks

def update(file_path, target_id, description):
    tasks = load_tasks(file_path)
    for task in tasks:
        if int(task["id"]) == int(target_id):
            task["description"] = description
            task["updatedAt"] = datetime.now().isoformat()
    save_tasks(file_path, tasks)
    return tasks
