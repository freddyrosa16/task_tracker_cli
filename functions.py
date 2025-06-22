import sys
import os
import json
from datetime import datetime

unavailable_id = set()

def load_tasks(absolute_path):
    if not os.path.exists(absolute_path) or os.path.getsize(absolute_path) == 0:
        with open(absolute_path, "w") as f:
            json.dump([], f)
    try:
        with open(absolute_path, "r") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError("Data is not a list.")
        return data
    except json.JSONDecodeError as e:
        print("Invalid JSON:", e)
        with open(absolute_path, "w") as f:
            json.dump([], f)
        print("It has been reset to []")
        return []

def save_tasks(tasks, absolute_path):
    with open(absolute_path, "w") as f:
        json.dump(tasks, f)

def add(tasks, absolute_path):
    # Create an unique ID number
    global unavailable_id
    try:
        data = load_tasks(absolute_path)
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
    status = "todo"

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

def update(tasks, absolute_path):
    update_description = sys.argv[3]
    id_found = False
    # Loading tasks to work on
    try:
        data = load_tasks(absolute_path)
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return
    except json.JSONDecodeError:
        print("Error: The JSON data is invalid.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    # Comparing ID in JSON with the user one
    for task in data:
        try:
            if int(task["id"]) == int(sys.argv[2]):
                # Updating the description
                task["description"] = update_description
                id_found = True
                task["updatedAt"] = datetime.now().isoformat()
        except ValueError:
            print("Error: Invalid ID format.")
            return
    if not id_found:
        print("Error: No task found with the specified ID.")

    save_tasks(data, absolute_path)
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)

def delete(tasks, absolute_path):
    # Load tasks to delete
    try:
        data = load_tasks(absolute_path)
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        return
    except json.JSONDecodeError:
        print("Error: The JSON data is invalid.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    
    # Match ID in JSON with users
    for index, task in enumerate(data):
        try:
            if int(task["id"]) == int(sys.argv[2]):
                del data[index]
        except ValueError:
            print("Error: Invalid ID format.")
            return
    save_tasks(data, absolute_path)
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)

def in_progress(tasks, absolute_path):
    data = load_tasks(absolute_path)

    for task in data:
        try:
            if int(task["id"]) == int(sys.argv[2]):
                task["status"] = "in-progress"
                task["updatedAt"] = datetime.now().isoformat()
        except ValueError:
            print("Error: Invalid ID format.")
            return
        
    save_tasks(data, absolute_path)
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)

def done(tasks, absolute_path):
    data = load_tasks(absolute_path)

    for task in data:
        try:
            if int(task["id"]) == int(sys.argv[2]):
                task["status"] = "done"
                task["updatedAt"] = datetime.now().isoformat()
        except ValueError:
            print("Error: Invalid ID format.")
            return
        
    save_tasks(data, absolute_path)
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)

def listing(tasks, absolute_path):
    try:
        data = load_tasks(absolute_path)

        if len(sys.argv) > 2:
            status = sys.argv[2]
            for task in data:
                if str(task.get("status")) == str(status):
                    print(task)
        else:
            for task in data:
                print(task)
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except json.JSONDecodeError:
        print("Error: The JSON data is invalid.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

