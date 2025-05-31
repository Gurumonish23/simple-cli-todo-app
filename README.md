# Simple CLI Todo App

This is a simple command-line interface (CLI) todo application written in Python. It allows you to add, view, and delete tasks.

## Features
- **Add a Task**: Add a new task with a description.
- **View Tasks**: View all tasks with their unique IDs.
- **Delete a Task**: Delete a task by its ID.

## Requirements
- Python 3.x

## Usage

1. **Add a Task**
   ```
   python todo.py add "Your task description"
   ```

2. **View Tasks**
   ```
   python todo.py view
   ```

3. **Delete a Task**
   ```
   python todo.py delete <task_id>
   ```

## Data Storage
Tasks are stored in a `tasks.json` file in the same directory as the script.

## Setup
Ensure you have Python installed, then run the script using the commands above.

## License
This project is open-source and available under the MIT License.