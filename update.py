import sys
from save import save_tasks
from load_tasks import load_tasks

def update_task(description):
    tasks = load_tasks()
    args = sys.argv[1:]
    description = args[2]
    found = False

    try:
        argument_id = int(args[1])
        for task in tasks:
            if int(task["id"]) == argument_id:
                found = True
                task["description"] = description
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

