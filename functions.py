import sys
import os
import json
from datetime import datetime

unavailable_id = set()

def load_tasks(absolute_path):
    if not os.path.exists(absolute_path):
        with open(absolute_path, "w") as f:
            json.dump([], f)
    else:
        if os.path.getsize(absolute_path) == 0:
            with open(absolute_path, "w") as f:
                json.dump([], f)
        try:
            with open(absolute_path, "r") as f:
                data = json.load(f)
            if not isinstance(data, list):
                with open(absolute_path, "w") as f:
                    json.dump([], f)
        except json.JSONDecodeError as e:
            print("Invalid JSON:", e)
            with open(absolute_path, "w") as f:
                json.dump([], f)
            print("It has been reset to []")

def save_tasks(tasks, absolute_path):
    with open(absolute_path, "w") as f:
        json.dump(tasks, f)

def add(tasks, absolute_path):
    # Create an unique ID number
    global unavailable_id
    try:
        with open(absolute_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return
    except json.JSONDecodeError:
        print("Error: The JSON data is invalid.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    existing_id = {task["id"] for task in data}
    id = 1
    while id in existing_id or id in unavailable_id:
        id += 1    

    # Short description of Task
    description = sys.argv[2]

    # Status is always Todo when created
    status = "Todo"

    # Time of Creation and Updated
    current_datetime = datetime.now().isoformat()

    new_task = {
        "id": id,
        "description": description,
        "status": status,
        "createdAt": current_datetime,
        "updatedAt": current_datetime
    }

    data.append(new_task)
    unavailable_id.add(id)

    save_tasks(data, absolute_path)
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)