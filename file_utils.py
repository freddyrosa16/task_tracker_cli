import os
import json

def ensure_path(working_directory=None, file_path=None):
    if working_directory is None:
        working_directory = os.getcwd()
    
    if file_path is None:
        file_path = "tasks.json"

    abs_working_directory = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

    if not os.path.exists(abs_working_directory):
        os.makedirs(abs_working_directory, exist_ok=True)
    
    if not os.path.exists(target_path):
        try:
            with open(target_path, "w") as file:
                json.dump([], file)
        except Exception as e:
            print(f"Error: {e}")
    return target_path

file_path = ensure_path()
def validate_file_format(file_path):
    if os.path.getsize(file_path) == 0:
        try:
            with open(file_path, "w") as file:
                json.dump([], file)
        except Exception as e:
            print(f"Error: {e}")
    else:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
            
            if not isinstance(data, list):
                with open(file_path, "w") as file:
                    json.dump([], file)
            
            if not isinstance(data[0], dict):
                with open(file_path, "w") as file:
                    json.dump([], file) 
        except Exception as e:
            print(f"Error: {e}")
    return file_path

def load_tasks(file_path):
    validated_path = validate_file_format(file_path)
    try:
        with open(validated_path, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f"Error: {e}")
        return None
    return data