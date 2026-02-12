import os
import json


def prepare_storage(file_path):
    try:
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                json.dump([], file, indent=4)
            return []
        else:
            with open(file_path, "r") as file:
                data = json.load(file)
            if os.path.getsize(file_path) == 0:
                with open(file_path, "w") as file:
                    json.dump([], file, indent=4)
                return []

            if not isinstance(data, list):
                with open(file_path, "w") as file:
                    json.dump([], file, indent=4)
                return []
            if not all(isinstance(item, dict) for item in data):
                with open(file_path, "w") as file:
                    json.dump([], file, indent=4)
                return []
        return data

    except Exception as e:
        return f"Error: {e}"
