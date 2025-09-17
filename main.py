# What are the requirements?
# Take arguments to create a Todo Tracker in CLI
# If argument is ADD it should add a task with unique ID number, description, status, createdAt, updatedAt
# Delete task via ID number
# List tasks, all the tasks, and depending on the status
# Update the task via description


import os
import sys

def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print("Argument missing. Please Provide an extra argument.")
        return
    
    command = args[0]

    if command == "add":
        add()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "mark-in-progress":
        mark()
    elif command == "mark-done":
        mark()
    elif command == "list":
        listing()
    else:
        print(f"Unknown command: {command}")