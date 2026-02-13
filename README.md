# Task Tracker CLI

A simple command-line task tracker to help you manage your to-do list. Track tasks with statuses, update descriptions, and filter by completion status.

## Features

- ✅ Add new tasks with automatic ID assignment
- 📝 Update task descriptions
- 🗑️ Delete tasks
- 🔄 Mark tasks as in-progress or done
- 📋 List all tasks or filter by status (todo, in-progress, done)
- 💾 Persistent storage using JSON

### Add a Task

Add a new task with a description. Tasks are automatically assigned a unique ID and set to "todo" status.

```bash
./task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

./task-cli add "Finish homework"
# Output: Task added successfully (ID: 2)
```

### Update a Task

Update the description of an existing task by its ID.

```bash
./task-cli update 1 "Buy groceries and cook dinner"
# Output: Task updated successfully (ID: 1)
```

### Delete a Task

Remove a task from your list by its ID.

```bash
./task-cli delete 1
# Output: Task 1 has been deleted successfully
```

### Mark Task In Progress

Change a task's status to "in-progress".

```bash
./task-cli mark-in-progress 2
# Output: Status of the task has been updated successfully (ID: 2)
```

### Mark Task Done

Change a task's status to "done".

```bash
./task-cli mark-done 2
# Output: Status of the task has been updated successfully (ID: 2)
```

### List Tasks

View all tasks or filter by status.

**List all tasks:**

```bash
./task-cli list
```

**List tasks by status:**

```bash
./task-cli list todo
./task-cli list in-progress
./task-cli list done
```

## Task Properties

Each task contains the following properties:

- `id`: Unique identifier (auto-generated)
- `description`: Task description
- `status`: Current status (`todo`, `in-progress`, or `done`)
- `createdAt`: Timestamp when task was created (ISO format)
- `updatedAt`: Timestamp when task was last modified (ISO format)

## Data Storage

Tasks are stored in `tasks.json` in the project directory. The file is automatically created on first use.

## Project Structure

```
task_tracker_cli/
├── task-cli              # Main executable (entry point)
├── add.py                # Add task functionality
├── update.py             # Update task functionality
├── delete.py             # Delete task functionality
├── mark_in_progress.py   # Mark task as in-progress
├── mark_done.py          # Mark task as done
├── listing.py            # List and filter tasks
├── load_tasks.py         # Storage initialization and loading
└── tasks.json            # Task data storage (auto-generated)
```

## Example Workflow

```bash
# Add some tasks
./task-cli add "Write documentation"
./task-cli add "Review code"
./task-cli add "Deploy to production"

# Start working on a task
./task-cli mark-in-progress 1

# Complete a task
./task-cli mark-done 1

# View all in-progress tasks
./task-cli list in-progress

# Update a task description
./task-cli update 2 "Review and approve pull requests"

# View all tasks
./task-cli list
```

