from load_tasks import load_tasks


def lists(file_path, status=None):
    tasks = load_tasks(file_path)
    if status:
        status = status.lower()
        return [task for task in tasks if task.get("status") == status]
    return tasks
