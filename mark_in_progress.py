import datetime
import json

from load_tasks import load_tasks


def mark_in_progress(file_path, args):
    tasks = load_tasks(file_path)

    for task in tasks:
        if int(task["id"]) == int(args[1]):
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.datetime.now().isoformat()
        with open(file_path, "w") as file:
            json.dump(task, file)
    return tasks
