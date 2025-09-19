# Task Tracker CLI

A simple command-line interface (CLI) application for managing your tasks. Built with Python, this tool allows you to add, update, delete, and track the status of your tasks efficiently.

## Features

- ✅ **Add tasks** with unique IDs and timestamps
- ✏️ **Update task descriptions**
- 🗑️ **Delete tasks** by ID
- 📋 **List all tasks** or filter by status
- 🔄 **Mark tasks as in-progress**
- ✅ **Mark tasks as done**
- 💾 **Persistent storage** in JSON format
- 🏠 **Local storage** in user's home directory

## Installation

1. Clone the repository:

```bash
git clone https://github.com/freddyrosa16/task-tracker-cli.git
cd task-tracker-cli
```

2. Ensure you have Python 3.6+ installed:

```bash
python3 --version
```

3. No additional dependencies required - uses only Python standard library!

## Usage

### Add a Task

```bash
python3 main.py add "Buy groceries"
python3 main.py add "Complete project documentation"
```

### List Tasks

```bash
# List all tasks
python3 main.py list

# List tasks by status
python3 main.py list todo
python3 main.py list in-progress
python3 main.py list done
```

### Update a Task

```bash
python3 main.py update 1 "Buy organic groceries"
```

### Mark Task Status

```bash
# Mark task as in-progress
python3 main.py mark-in-progress 1

# Mark task as done
python3 main.py mark-done 1
```

### Delete a Task

```bash
python3 main.py delete 1
```

## Task Properties

Each task contains the following information:

- **id**: Unique identifier (auto-generated)
- **description**: Task description
- **status**: Current status (`todo`, `in-progress`, `done`)
- **createdAt**: When the task was created
- **updatedAt**: When the task was last modified

## File Structure

```
task-tracker-cli/
├── main.py              # Main application entry point
├── add.py               # Add task functionality
├── update.py            # Update task functionality
├── delete.py            # Delete task functionality
├── mark_in_progress.py  # Mark task as in-progress
├── mark_done.py         # Mark task as done
├── list_tasks.py        # List tasks functionality
├── load_tasks.py        # Load tasks from JSON
├── save.py              # Save tasks to JSON
├── file_path.py         # Handle file path operations
└── README.md            # This file
```

## Data Storage

Tasks are stored in a JSON file located at:

```
~/.tasktracker/tasks.json
```

The application automatically creates this directory and file on first use.

## Example Output

```bash
$ python3 main.py add "Learn Python"
Task added successfully

$ python3 main.py list
[{
  "id": 1,
  "description": "Learn Python",
  "status": "todo",
  "createdAt": "2025-09-19T16:00:00",
  "updatedAt": "2025-09-19T16:00:00"
}]

$ python3 main.py mark-in-progress 1
Status has been updated successfully.

$ python3 main.py mark-done 1
Status has been updated successfully.
```

## Error Handling

The application includes comprehensive error handling for:

- Invalid task IDs
- Missing arguments
- Non-existent tasks
- Corrupted data files
- File system permissions

## Requirements

- Python 3.6 or higher
- No external dependencies

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Project Roadmap

- [ ] Add due dates for tasks
- [ ] Priority levels (high, medium, low)
- [ ] Task categories/tags
- [ ] Export tasks to different formats
- [ ] Search functionality
- [ ] Task statistics and reports

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Built by [Freddy Rosa] - feel free to contact me!

---

**Happy task tracking! 🚀**
