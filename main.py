import sys
from delete import delete
from list import lists
from load_tasks import load_tasks
from add import add
from update import update
from mark_in_progress import mark_in_progress
from mark_done import mark_done

DATA_DIR = ".data"


def main():
    tasks = load_tasks(DATA_DIR)

    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        add(tasks, DATA_DIR)
    elif command == "delete":
        delete(tasks, DATA_DIR)
    elif command == "update":
        update(tasks, DATA_DIR)
    elif command == "list":
        lists(tasks)
    elif command == "mark-in-progress":
        mark_in_progress(tasks, DATA_DIR)
    elif command == "mark-done":
        mark_done(tasks, DATA_DIR)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
