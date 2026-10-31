from load_tasks import load_tasks
from save_tasks import save_tasks


def mark_in_progress(file_path, task_id):
    tasks = load_tasks(file_path)
    for task in tasks:
        if int(task["id"]) == int(task_id):
            task["status"] = "in-progress"
    save_tasks(file_path, tasks)
    return tasks


def mark_done(file_path, task_id):
    tasks = load_tasks(file_path)
    for task in tasks:
        if int(task["id"]) == int(task_id):
            task["status"] = "done"
    save_tasks(file_path, tasks)
    return tasks
