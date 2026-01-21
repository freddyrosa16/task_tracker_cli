import sys


def lists(tasks):
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == "list":
        print(tasks)
    if len(args) == 2 and args[0] == "list":
        status = args[1]
        print([task for task in tasks if task["status"] == status])
    return []
