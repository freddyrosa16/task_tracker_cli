import json
from file_path import get_task_file_path


def save_tasks(tasks):
    with open(get_task_file_path(), 'w') as file:
        json.dump(tasks, file, indent=4)