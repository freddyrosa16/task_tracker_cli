import json
from check_set_up import set_up


def save_tasks(tasks, path):
    file_path = set_up(path)
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=2)
