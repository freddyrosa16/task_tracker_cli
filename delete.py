from load_tasks import load_tasks
from save_tasks import save_tasks


def delete(file_path, task_id):
    tasks = load_tasks(file_path)
    for task in tasks:
        if int(task["id"]) == int(task_id):
            print(f"Task id {task['id']} has been deleted.")
            tasks.remove(task)
            break
    save_tasks(file_path, tasks)
