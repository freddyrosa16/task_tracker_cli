import json
import os


def load_tasks(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump("[]", file)
    else:
        with open(file_path, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            with open(file_path, "w") as file:
                json.dump("[]", file)
        if not isinstance(data[0], dict):
            with open(file_path, "w") as file:
                json.dump("[]", file)
