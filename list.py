from load_tasks import load_tasks


def task_list(file_path):
    tasks = load_tasks(file_path)
    return tasks

def task_list_status(file_path, task_status):
    tasks = load_tasks(file_path)
    matched = []
    for task in tasks:
        if task["status"] == task_status:
            matched.append(task)
    return matched
