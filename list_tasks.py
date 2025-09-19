import sys
from load_tasks import load_tasks

def listing():
    tasks = load_tasks()
    args = sys.argv[1:]
    found = False

    try:
        if len(args) == 1 and args[0] == "list":
            print(tasks)
        else:
            for task in tasks:
                if task["status"] == args[1]:
                    found = True
                    print(task)
        if not found:
            print("Task status not found.")
    except ValueError:
        print("Invalid input. Please enter a string status (todo, in-progress, done).")
    except Exception as e:
            print(f"An unexpected error occurred: {e}")
            