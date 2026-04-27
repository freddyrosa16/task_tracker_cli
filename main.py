import sys

from add import add
from delete import delete
from lists import lists
from mark_done import mark_done
from mark_in_progress import mark_in_progress
from update import update


def main():
    file_path = "tasks.json"

    args = sys.argv[1:]
    if len(args) < 1:
        print("Usage: task-cli <command>")
        return

    command = args[0]

    if command == "add":
        if len(args) < 2:
            print("Error: add requires a description")
            return
        add(file_path, args)
        print("Task added.")

    elif command == "list":
        status = args[1] if len(args) > 1 else None
        tasks = lists(file_path, status)
        for task in tasks:
            print(task)

    elif command == "update":
        if len(args) < 3:
            print("Error: update requires id and description")
            return
        update(file_path, args)
        print("Task updated.")

    elif command == "mark-in-progress":
        mark_in_progress(file_path, args)
        print("Task marked in progress.")

    elif command == "mark-done":
        mark_done(file_path, args)
        print("Task marked done.")

    elif command == "delete":
        delete(file_path, args)
        print("Task deleted.")

    else:
        print("Unknown command")


if "__main__" == __name__:
    main()
