import sys
import datetime
from save_tasks import save_tasks


def mark_in_progress(tasks, path):
    if len(sys.argv) < 3:
        print("Usage: python3 main.py mark-in-progress <id>")
        return
    
    task_id = int(sys.argv[2])
    updated = False

    for i in range(len(tasks) - 1, -1, -1):
        if int(tasks[i]["id"]) == task_id:
            tasks[i]["status"] = "in-progress"
            tasks[i]["updatedAt"] = datetime.datetime.now().isoformat()
            updated = True
            break

    if updated:
        save_tasks(tasks, path)
        print(f"Task {task_id} status updated")
    else:
        print(f"Task {task_id} status not found")