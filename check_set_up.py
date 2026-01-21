import os
import json


def set_up(path):
    dir_path = os.path.abspath(path)
    target_file = os.path.join(dir_path, "tasks.json")

    try:
        os.makedirs(dir_path, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory {dir_path}: {e}")

    try:
        if not os.path.exists(target_file):
            with open(target_file, "w") as file:
                json.dump([], file)
    except Exception as e:
        print(f"Error creating file {target_file}: {e}")

    return target_file
