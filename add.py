import json
import sys
from file_path import get_task_file_path
from load_tasks import load_tasks
from datetime import datetime
from save import save_tasks

def add(description):
    tasks = load_tasks()
    args = sys.argv[1:]
    description = args[1]

    if tasks == []:
        id_number = 1
    else:
        id_number = max(task['id'] for task in tasks) + 1
    
    new_task = {
        "id": id_number,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().replace(minute=0, second=0, microsecond=0),
        "updatedAt": datetime.now().replace(minute=0, second=0, microsecond=0)
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added successfully")