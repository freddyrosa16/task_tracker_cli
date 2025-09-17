import os

def get_tasks_file_path():
    home_directory = os.path.expanduser("~")
    tasktracker_directory = os.path.join(home_directory, ".tasktracker")

    if not os.path.exists(tasktracker_directory):
        os.makedirs(tasktracker_directory, exist_ok=True)

    task_file = os.path.join(tasktracker_directory, "tasks.json")

    return task_file