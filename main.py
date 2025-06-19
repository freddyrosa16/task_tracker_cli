import sys
import os
from functions import load_tasks, add


def main():
    relative_path = "tasks.json"
    absolute_path = os.path.abspath(relative_path)

    if len(sys.argv) < 3:
        return

    if sys.argv[1] == "add":
        tasks = load_tasks(absolute_path)
        add(tasks, absolute_path)


if __name__ == "__main__":
    main()