import os
import json

def load_tasks(file_path):
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
                datas = json.load(file)
            if not isinstance(datas, list):
                with open(file_path, "w") as file:
                    json.dump([], file)
                return []
            for data in datas:
                if not isinstance(data, dict):
                    with open(file_path, "w") as file:
                        json.dump([], file)
                    return []
            return datas
