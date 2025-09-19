import sys
from load_tasks import load_tasks
from datetime import datetime
from save import save_tasks

def add():
    tasks = load_tasks()
    args = sys.argv[1:]

    if len(args) < 2:
        print("Argument missing. Please Provide an extra argument.")
        return
    
    description = args[1]

    if tasks == []:
        id_number = 1
    else:
        id_number = max(task['id'] for task in tasks) + 1
    
    new_task = {
        "id": id_number,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().replace(minute=0, second=0, microsecond=0).isoformat(),
        "updatedAt": datetime.now().replace(minute=0, second=0, microsecond=0).isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added successfully")
    print(tasks)