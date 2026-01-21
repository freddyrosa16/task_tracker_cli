import sys
from save_tasks import save_tasks


def delete(tasks, path):
    for task in range(len(tasks) - 1, -1, -1):
        if int(tasks[task]["id"]) == int(sys.argv[2]):
            del tasks[task]
    save_tasks(tasks, path)
