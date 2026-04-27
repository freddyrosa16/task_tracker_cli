# 📝 Task Tracker CLI

A simple command-line task management tool built with Python. It allows
you to create, update, track, and delete tasks stored in a local JSON
file.

------------------------------------------------------------------------

## 🚀 Features

-   ➕ Add new tasks
-   📋 List all tasks
-   🔍 Filter tasks by status (`todo`, `in-progress`, `done`)
-   ✏️ Update task descriptions
-   ⏳ Mark tasks as in progress
-   ✅ Mark tasks as done
-   🗑️ Delete tasks
-   💾 Persistent storage using `tasks.json`

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python 3
-   JSON (for storage)

------------------------------------------------------------------------

## 📂 Project Structure

    task_tracker_cli/
    │── main.py
    │── add.py
    │── update.py
    │── delete.py
    │── lists.py
    │── mark_in_progress.py
    │── mark_done.py
    │── load_tasks.py
    │── tasks.json

------------------------------------------------------------------------

## ▶️ How to Run

``` bash
python3 main.py <command> [arguments]
```

------------------------------------------------------------------------

## 📌 Commands

### ➕ Add Task

``` bash
python3 main.py add "Buy groceries"
```

### 📋 List Tasks

``` bash
python3 main.py list
```

### 🔍 List by Status

``` bash
python3 main.py list todo
python3 main.py list in-progress
python3 main.py list done
```

### ✏️ Update Task

``` bash
python3 main.py update 1 "Buy groceries and cook dinner"
```

### ⏳ Mark In Progress

``` bash
python3 main.py mark-in-progress 1
```

### ✅ Mark Done

``` bash
python3 main.py mark-done 1
```

### 🗑️ Delete Task

``` bash
python3 main.py delete 1
```

------------------------------------------------------------------------

## 🧾 Task Format

Each task is stored like this:

``` json
{
  "id": 1,
  "description": "Buy groceries",
  "status": "todo",
  "createdAt": "2026-01-01T12:00:00",
  "updatedAt": "2026-01-01T12:00:00"
}
```

------------------------------------------------------------------------

## 🧠 Core Concepts

-   File handling with JSON
-   CLI argument parsing (`sys.argv`)
-   CRUD operations
-   Basic data validation
-   Modular code structure

------------------------------------------------------------------------

## ⚡ Future Improvements

-   Add due dates
-   Add priority levels
-   Pretty CLI output (tables/colors)
-   Add search functionality
-   Convert into a full app (web or GUI)

------------------------------------------------------------------------

## 📌 Notes

-   Tasks are stored locally in `tasks.json`
-   File is auto-created if it doesn't exist
-   Invalid file structures are reset automatically

------------------------------------------------------------------------

Simple, clean, and a great foundation for bigger projects 🚀
