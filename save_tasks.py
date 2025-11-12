import json

def save_task(tasks, file_path):
    try:
        with open(file_path, "w") as file:
            json.dump(tasks, file)
    except Exception as e:
        print(f"Error: {e}")