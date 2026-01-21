# Task Tracker CLI

A simple command-line task management application built with Python. Track your tasks with statuses, timestamps, and persistent storage.

## Features

- Add, update, and delete tasks
- Mark tasks as in-progress or done
- List all tasks or filter by status
- Automatic timestamping (creation and updates)
- JSON-based persistent storage
- Auto-incrementing task IDs

## Usage

Run commands using the main script:

```bash
python main.py <command> [args]
```

### Available Commands

**Add a new task**

```bash
python main.py add "Task description here"
```

**Update a task**

```bash
python main.py update <id> "New description"
```

**Delete a task**

```bash
python main.py delete <id>
```

**Mark task as in-progress**

```bash
python main.py mark-in-progress <id>
```

**Mark task as done**

```bash
python main.py mark-done <id>
```

**List all tasks**

```bash
python main.py list
```

**List tasks by status**

```bash
python main.py list todo
python main.py list in-progress
python main.py list done
```

## Data Storage

Tasks are stored in `.data/tasks.json` in the following format:

```json
[
  {
    "id": 1,
    "description": "Example task",
    "status": "todo",
    "createdAt": "2024-01-15T10:30:00.000000",
    "updatedAt": "2024-01-15T10:30:00.000000"
  }
]
```

The `.data` directory is automatically created on first run.

## Project Structure

```
.
├── main.py                 # Entry point and command router
├── add.py                  # Add new tasks
├── update.py               # Update task descriptions
├── delete.py               # Delete tasks
├── list.py                 # List and filter tasks
├── mark_in_progress.py     # Update task status to in-progress
├── mark_done.py            # Update task status to done
├── load_tasks.py           # Load tasks from storage
├── save_tasks.py           # Save tasks to storage
├── check_set_up.py         # Initialize data directory and file
└── .data/
    └── tasks.json          # Task storage (auto-generated)
```

## Task Statuses

- `todo` - Default status for new tasks
- `in-progress` - Tasks currently being worked on
- `done` - Completed tasks

## Examples

```bash
# Add a task
python main.py add "Write project documentation"
# Output: Creates task with ID 1

# Mark it as in-progress
python main.py mark-in-progress 1
# Output: Task 1 status updated

# Update the description
python main.py update 1 "Write comprehensive project documentation"
# Output: Task 1 updated

# List all in-progress tasks
python main.py list in-progress

# Mark as done
python main.py mark-done 1
# Output: Task 1 status updated

# Delete the task
python main.py delete 1
# Output: Task 1 deleted
```
