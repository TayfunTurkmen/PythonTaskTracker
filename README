# Task Tracker CLI

Task Tracker is a command-line interface (CLI) application for managing and tracking your tasks. It allows you to add, update, delete, and mark tasks as "todo," "in-progress," or "done." The tasks are stored in a JSON file and can be easily managed through a set of CLI commands.

## Features

- **Add a task**: Create a new task with a description.
- **Update a task**: Modify the description of an existing task.
- **Delete a task**: Remove a task by its unique ID.
- **Mark a task**: Set the task's status to "in-progress" or "done."
- **List tasks**: View all tasks or filter them by status ("todo," "in-progress," or "done").
- **Task management**: Each task includes an ID, description, status, createdAt, and updatedAt timestamps.

## Requirements

- Python 3.x
- No external libraries are required. This project only uses Python's built-in libraries (`argparse`, `json`, `os`, and `datetime`).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/task-tracker-cli.git
    cd task-tracker-cli
    ```

2. Ensure Python 3.x is installed on your system.

3. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # For Linux/macOS
    venv\Scripts\activate      # For Windows
    ```

## Usage

Once you are in the project directory, you can run the following commands:

### Add a Task

```bash
python task-cli.py add "Buy groceries"
```

Adds a new task with the description "Buy groceries."
Output: Task added successfully (ID: 1)

## Update a Task
```
python task-cli.py update 1 "Buy groceries and cook dinner"
```

Updates the description of the task with ID 1.

## Delete a Task
```
python task-cli.py delete 1
```

Deletes the task with ID 1.

## Mark a Task as In-Progress or Done
```
python task-cli.py mark-in-progress 1
```

Marks the task with ID 1 as "in-progress."

## List Tasks
```
python task-cli.py list
```

Lists all tasks.

You can filter tasks by status:
```
python task-cli.py list todo
python task-cli.py list in-progress
python task-cli.py list done
```

## Example of Listing Tasks
```
ID: 1, Description: Buy groceries, Status: todo, Created At: 2024-10-12T10:00:00, Updated At: 2024-10-12T10:00:00
ID: 2, Description: Complete Python project, Status: in-progress, Created At: 2024-10-13T08:00:00, Updated At: 2024-10-13T08:30:00
```

## Task Properties
Each task includes the following properties:

**id:** A unique identifier for the task.
**description:** A short description of the task.
**status:** The current status of the task (todo, in-progress, done).
createdAt:** The date and time when the task was created.
updatedAt:** The date and time when the task was last updated.

##File Storage
Tasks are stored in a JSON file (tasks.json) in the current directory. The file will be created automatically if it doesn't exist.

## Error Handling
If a task ID does not exist, an error message is displayed.
If you try to update or delete a non-existent task, you will be notified.
Proper error handling is in place for invalid inputs or missing files.
