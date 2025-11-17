import sys
from save_tasks import save_task

def delete(tasks, file_path):
    args = sys.argv
    if len(args) < 2:
        raise IndexError("Please provide the necesary arguments.")
    tasks = [t for t in tasks if int(t["id"]) != int(args[1])]
    save_task(tasks, file_path)
    return tasks
            
