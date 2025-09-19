import sys
from save import save_tasks
from load_tasks import load_tasks

def delete():
    tasks = load_tasks()
    args = sys.argv[1:]
    found = False

    if len(args) < 2:
        print("Argument missing. Please Provide an extra argument.")
        return

    try:
        argument_id = int(args[1])
        for task in tasks:
            if int(task["id"]) == argument_id:
                found = True
                tasks.remove(task)
                save_tasks(tasks)
                print("Task deleted successfully")
                print(tasks)
                break
        if not found:
            print("Task id not found.")
    except ValueError:
        print("Invalid input. Please enter a number (integer).")
    except Exception as e:
            print(f"An unexpected error occurred: {e}")