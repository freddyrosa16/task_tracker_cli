import json
import sys
import datetime

def add(tasks, file_path):
    args = sys.argv

    tasks_id = []
    if tasks == []:
        id_number = 1
    else:
        for task in tasks:
            tasks_id.append(task["id"])
        id_number = max(tasks_id) + 1
    
    description = args[1]
    status = "todo"

    new_task = {
        "id": id_number,
        "description": description,
        "status": status,
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat()
    }

    try:
        with open(file_path, "w") as file:
            tasks.append(new_task)
            json.dump(tasks, file)
    except Exception as e:
        print(f"Error: {e}")
    return "Task added succesfully."