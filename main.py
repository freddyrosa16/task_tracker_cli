import sys
from add import add
from list import task_list, task_list_status
from update import update
from delete import delete
from mark import mark_in_progress, mark_done

def main():
    file_path = "tasks.json"
    args = sys.argv[1:]
    if len(args) < 1:
        print("Error: Enter more than one argument")

    if args[0] == "add":
        print(add(file_path, args[1]))
    elif args[0] == "update":
        print(update(file_path, args[1], args[2]))
    elif args[0] == "delete":
        delete(file_path, args[1])
    elif args[0] == "mark-in-progress":
        print(mark_in_progress(file_path, args[1]))
    elif args[0] == "mark-done":
        print(mark_done(file_path, args[1]))
    elif args[0] == "list" and len(args) > 1 and args[1] in ("todo", "in-progress", "done"):
        print(task_list_status(file_path, args[1]))
    elif args[0] == "list":
        print(task_list(file_path))



if __name__ == "__main__":
    main()
