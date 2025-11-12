import sys
import datetime
from save_tasks import save_task

def update(tasks, file_path):
    match = False
    args = sys.argv
    if len(args) < 3:
        raise IndexError("Please provide the necesary arguments.")
    for task in tasks:
        if int(args[1]) == int(task["id"]):
            match = True
            try:
                task["description"] = args[2]
                task["updatedAt"] = datetime.datetime.now().isoformat()
                save_task(tasks, file_path)
            except Exception as e:
                print(f"Error: {e}")
            print("Task has been updated succesfully.")
    if match == False:
        raise ValueError(f"Task with ID {args[1]} not found.")
