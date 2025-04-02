# To-Do List with Priority and Deadline

A simple, command-line Python application to manage tasks with priorities and deadlines. This project allows users to add tasks, assign them a priority (high, medium, low) and a deadline, view them sorted by priority, mark tasks as completed, and save everything to a file for persistence.

## Features
- **Add Tasks**: Input a task name, priority (high/medium/low), and deadline (e.g., 2025-04-10).
- **View Tasks**: See all tasks sorted by priority (high first), with their status (Pending or Done).
- **Mark Tasks Done**: Select a task by number to mark it as completed.
- **Persistent Storage**: Tasks are saved to `tasks.txt` and loaded automatically when the program starts.
- **User-Friendly Menu**: Easy-to-use interface with options to add, view, mark, or exit.

## How to Use
1. **Prerequisites**: You need Python 3.x installed on your computer.
2. **Setup**:
   - Clone or download this repository.
   - Navigate to the project folder in your terminal.
3. **Run the Program**:
   - Type `python todo.py` (replace `todo.py` with the actual filename).
4. **Interact**:
   - Choose from the menu:
     - `1`: Add a new task.
     - `2`: View all tasks.
     - `3`: Mark a task as done.
     - `4`: Exit the program.
   - Follow the prompts to enter task details or select tasks.

