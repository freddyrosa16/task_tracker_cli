# Task Tracker CLI

A command-line interface (CLI) tool for managing tasks. This application allows users to add, update, delete, and list tasks efficiently.

## Features

- **Add Tasks**: Create new tasks with a unique ID and default status.
- **Update Tasks**: Modify the description of existing tasks.
- **Delete Tasks**: Remove tasks from the list.
- **Change Status**: Update the status of tasks to "in-progress" or "done."
- **List Tasks**: View all tasks or filter by status.

## Requirements

- Python 3.x
- `json` and `os` modules (included in Python standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd task_tracker_cli
   ```
2. Ensure you have Python 3 installed on your system.

## Usage

Run the Application
To run the application, use the following command structure:

```bash
python3 main.py <command> [options]
```

## Add a Task

```bash
python3 main.py add "Task description"
```

Example:

```bash
python3 main.py add "Finish project report"
```

## Update a Task

```bash
python3 main.py update <task_id> "New description"
```

Example:

```bash
python3 main.py update 1 "Finish project report and send it to the manager"
```

## Delete a Task

```bash
python3 main.py delete <task_id>
```

Example:

```bash
python3 main.py delete 1
```

## Set Task In Progress

```bash
python3 main.py in-progress <task_id>
```

Example:

```bash
python3 main.py in-progress 2
```

## Set Task as Done

```bash
python3 main.py done <task_id>
```

Example:

```bash
python3 main.py done 2
```

## List All Tasks

```bash
python3 main.py list
```

## List Tasks by Status

```bash
python3 main.py list <status>
```

Example:

```bash
python3 main.py list todo
```

Example Output
When adding a task:

````bash
$ python3 main.py add "Finish project report"
[
{
"id": 1,
"description": "Finish project report",
"status": "todo",
"createdAt": "2023-06-22T08:35:23",
"updatedAt": "2023-06-22T08:35:23"
}
]
```

When listing tasks:

```bash
$ python3 main.py list
{
"id": 1,
"description": "Finish project report",
"status": "todo",
"createdAt": "2023-06-22T08:35:23",
"updatedAt": "2023-06-22T08:35:23"
}
````

## Error Handling

The application includes error handling for:

```bash
Invalid JSON data
File not found scenarios
Invalid command usage
License
This project is licensed under the MIT License. See the LICENSE file for details.

Copy

Feel free to replace `<repository-url>` with the actual URL of your project repository!
```
