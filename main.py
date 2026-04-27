import sys

from add import add
from mark_done import mark_done

# from delete import delete
# from lists import lists
from mark_in_progress import mark_in_progress
from update import update


def main():
    file_path = "tasks.json"

    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: python3 main.py <command> <id> <some description>")

    if args[0] == "add":
        print(add(file_path, args))
    if args[0] == "update":
        print(update(file_path, args))
    if args[0] == "mark-in-progress":
        print(mark_in_progress(file_path, args))
    if args[0] == "mark-done":
        print(mark_done(file_path, args))


if "__main__" == __name__:
    main()
