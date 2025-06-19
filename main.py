import sys
import os
from functions import load_tasks, add, update, delete


def main():
    relative_path = "tasks.json"
    absolute_path = os.path.abspath(relative_path)

    if len(sys.argv) < 3:
        return

    if sys.argv[1] == "add":
        tasks = load_tasks(absolute_path)
        add(tasks, absolute_path)
    elif sys.argv[1] == "update":
        tasks = load_tasks(absolute_path)
        update(tasks, absolute_path)
    elif sys.argv[1] == "delete":
        tasks = load_tasks(absolute_path)
        delete(tasks, absolute_path)


if __name__ == "__main__":
    main()