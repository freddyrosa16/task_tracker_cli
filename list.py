from load_tasks import load_tasks


def task_list(file_path):
    tasks = load_tasks(file_path)
    return tasks
