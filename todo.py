import json
import argparse
import os

# File to store tasks
tasks_file = 'tasks.json'

# Ensure the tasks file exists
def ensure_tasks_file():
    if not os.path.exists(tasks_file):
        with open(tasks_file, 'w') as file:
            json.dump([], file)

# Load tasks from the file
def load_tasks():
    with open(tasks_file, 'r') as file:
        return json.load(file)

# Save tasks to the file
def save_tasks(tasks):
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({'id': task_id, 'description': description})
    save_tasks(tasks)
    print(f"Task added: {description}")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"{task['id']}: {task['description']}")

# Delete a task by ID
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Simple CLI Todo App')
    subparsers = parser.add_subparsers(dest='command')

    # Add task command
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('description', type=str, help='Description of the task')

    # View tasks command
    parser_view = subparsers.add_parser('view', help='View all tasks')

    # Delete task command
    parser_delete = subparsers.add_parser('delete', help='Delete a task by ID')
    parser_delete.add_argument('id', type=int, help='ID of the task to delete')

    args = parser.parse_args()

    ensure_tasks_file()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'view':
        view_tasks()
    elif args.command == 'delete':
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
