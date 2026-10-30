import json

def save_tasks(file_path, tasks):
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)
