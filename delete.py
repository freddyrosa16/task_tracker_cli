import json

from load_tasks import load_tasks


def delete(file_path, args):
    new_tasks = []
    tasks = load_tasks(file_path)

    for task in tasks:
        if not int(task["id"]) == int(args[1]):
            new_tasks.append(task)
    with open(file_path, "w") as file:
        json.dump(new_tasks, file, indent=4)
    return new_tasks
