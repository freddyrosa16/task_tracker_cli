import sys
from save_tasks import save_tasks


def delete(tasks, path):
    if len(sys.argv) < 3:
        print("Usage: python3 main.py delete <id>")
        return

    task_id = int(sys.argv[2])
    deleted = False

    for i in range(len(tasks) - 1, -1, -1):
        if int(tasks[i]["id"]) == task_id:
            del tasks[i]
            deleted = True
            break

    if deleted:
        save_tasks(tasks, path)
        print(f"Task {task_id} deleted")
    else:
        print(f"Task {task_id} not found")
