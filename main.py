# What are the requirements?
# Take arguments to create a Todo Tracker in CLI
# If argument is ADD it should add a task with unique ID number, description, status, createdAt, updatedAt
# Delete task via ID number
# List tasks, all the tasks, and depending on the status
# Update the task via description


import sys
from add import add
from update import update_task
from delete import delete
from mark_in_progress import mark_in_progress
from mark_done import mark_done
from list_tasks import listing

def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print("Argument missing. Please Provide an extra argument.")
        return
    
    command = args[0]
    
    if command == "add":
        add()
    elif command == "update":
        update_task()
    elif command == "delete":
        delete()
    elif command == "mark-in-progress":
        mark_in_progress()
    elif command == "mark-done":
        mark_done()
    elif command == "list":
        listing()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()