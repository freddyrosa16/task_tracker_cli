import os
import json
from check_set_up import set_up


def load_tasks(path):
    file_path = set_up(path)

    if not file_path:
        raise RuntimeError("File path was not provided")

    try:
        if os.path.getsize(file_path) == 0:
            data = []
        else:
            with open(file_path, "r") as file:
                data = json.load(file)

        if not isinstance(data, list) or not all(
            isinstance(task, dict) for task in data
        ):
            raise ValueError("Invalid task file structure")

        return data

    except (json.JSONDecodeError, ValueError):
        with open(file_path, "w") as file:
            json.dump([], file)
        print("File was corrupted and has been reset.")
        return []

    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []
