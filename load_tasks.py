import json
import os


def load_tasks(file_path):
    try:
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([], file)
                return []
        else:
            if os.path.getsize(file_path) == 0:
                with open(file_path, "w") as file:
                    json.dump([], file)
                    return []
            else:
                with open(file_path, "r") as file:
                    data = json.load(file)
                    if not isinstance(data[0], list) or not isinstance(data[1], dict):
                        with open(file_path, "w") as file:
                            json.dump([], file)
                            return []
                    return data

    except Exception as e:
        return f"Error: {e}"
