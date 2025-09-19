import sys
from save import save_tasks
from load_tasks import load_tasks
from datetime import datetime

def update_task():
    tasks = load_tasks()
    args = sys.argv[1:]
    found = False

    if len(args) < 3:
        print("Argument missing. Please Provide an extra argument.")
        return

    description = args[2]

    try:
        argument_id = int(args[1])
        for task in tasks:
            if int(task["id"]) == argument_id:
                found = True
                task["description"] = description
                task["updatedAt"] = datetime.now().replace(minute=0, second=0, microsecond=0).isoformat()
                save_tasks(tasks)
                print("Task updated successfully")
                print(tasks)
                break
        if not found:
            print("Task id not found.")
    except ValueError:
        print("Invalid input. Please enter a number (integer).")
    except Exception as e:
            print(f"An unexpected error occurred: {e}")

