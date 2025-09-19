import os
import json
from file_path import get_tasks_file_path
from save import save_tasks

def load_tasks():
    file_path = get_tasks_file_path()

    if not os.path.exists(file_path):
        tasks = []
        save_tasks(tasks)

    elif os.path.getsize(file_path) == 0:
        tasks = []
        save_tasks(tasks)
        
    else:
        try:
            with open(file_path, 'r') as file:
                tasks = json.load(file)
                if not isinstance(tasks, list):
                    tasks = []
                    save_tasks(tasks)
        except json.decoder.JSONDecodeError:
            tasks = []
            save_tasks(tasks)
    return tasks