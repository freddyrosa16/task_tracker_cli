import json
from file_path import get_tasks_file_path


def save_tasks(tasks):
    with open(get_tasks_file_path(), 'w') as file:
        json.dump(tasks, file, indent=4)