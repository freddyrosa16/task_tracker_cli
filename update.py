import sys
import datetime
from save_tasks import save_tasks


def update(tasks, path):
    if len(sys.argv) < 4:
        print("Usage: python3 main.py update <id> <new description>")
        return

    task_id = int(sys.argv[2])
    description = " ".join(sys.argv[3:])
    updated = False

    for i in range(len(tasks) - 1, -1, -1):
        if int(tasks[i]["id"]) == task_id:
            tasks[i]["description"] = description
            tasks[i]["updatedAt"] = datetime.datetime.now().isoformat()
            updated = True
            break

    if updated:
        save_tasks(tasks, path)
        print(f"Task {task_id} updated")
    else:
        print(f"Task {task_id} not found")
