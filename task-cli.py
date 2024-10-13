import argparse
import json
import os
from datetime import datetime

# Constants
TASK_FILE = "tasks.json"

# Initialize the JSON file if it doesn't exist
if not os.path.exists(TASK_FILE):
    with open(TASK_FILE, 'w') as file:
        json.dump([], file)

# Helper functions
def read_tasks():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

def write_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

# CLI Commands
def add_task(description):
    tasks = read_tasks()
    task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    write_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")

def update_task(task_id, description):
    tasks = read_tasks()
    task = find_task_by_id(tasks, task_id)
    if task:
        task['description'] = description
        task['updatedAt'] = datetime.now().isoformat()
        write_tasks(tasks)
        print(f"Task (ID: {task_id}) updated successfully.")
    else:
        print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = read_tasks()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) == len(updated_tasks):
        print(f"Task with ID {task_id} not found.")
    else:
        write_tasks(updated_tasks)
        print(f"Task (ID: {task_id}) deleted successfully.")

def mark_task(task_id, status):
    tasks = read_tasks()
    task = find_task_by_id(tasks, task_id)
    if task:
        task['status'] = status
        task['updatedAt'] = datetime.now().isoformat()
        write_tasks(tasks)
        print(f"Task (ID: {task_id}) marked as {status}.")
    else:
        print(f"Task with ID {task_id} not found.")

def list_tasks(status_filter=None):
    tasks = read_tasks()
    filtered_tasks = [task for task in tasks if not status_filter or task['status'] == status_filter]
    
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, "
                  f"Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
    else:
        print("No tasks found.")

# Main function to parse command line arguments
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    
    subparsers = parser.add_subparsers(dest='command')

    # Add task command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    # Update task command
    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='ID of the task to update')
    update_parser.add_argument('description', type=str, help='New description of the task')

    # Delete task command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')

    # Mark task as in-progress or done
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark a task as in-progress')
    mark_in_progress_parser.add_argument('id', type=int, help='ID of the task to mark as in-progress')

    mark_done_parser = subparsers.add_parser('mark-done', help='Mark a task as done')
    mark_done_parser.add_argument('id', type=int, help='ID of the task to mark as done')

    # List tasks command
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', type=str, nargs='?', help='Filter tasks by status (todo, in-progress, done)')

    # Parse arguments
    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'mark-in-progress':
        mark_task(args.id, 'in-progress')
    elif args.command == 'mark-done':
        mark_task(args.id, 'done')
    elif args.command == 'list':
        list_tasks(args.status)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
