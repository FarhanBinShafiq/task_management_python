# To-Do List Manager with Priority and Deadline

def load_tasks():
    """Load tasks from a file, return an empty list if file doesn’t exist."""
    try:
        with open("tasks.txt", "r") as file:
            return eval(file.read()) 
    except (FileNotFoundError, SyntaxError):
        return []  

def save_tasks(tasks):
    """Save tasks to a file."""
    with open("tasks.txt", "w") as file:
        file.write(str(tasks))  

def add_task(tasks):
    """Add a new task with priority and deadline."""
    task_name = input("Enter task: ")
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ["high", "medium", "low"]:
            break
        print("Please enter high, medium, or low.")
    deadline = input("Deadline (e.g., 2025-04-10): ")
    task = {"name": task_name, "priority": priority, "deadline": deadline, "done": False}
    tasks.append(task)
    print(f"Added: {task_name}")

def view_tasks(tasks):
    """Show all tasks, sorted by priority (high first)."""
    if not tasks:
        print("No tasks yet!")
        return
    #  priority: high > medium > low
    sorted_tasks = sorted(tasks, key=lambda x: {"high": 0, "medium": 1, "low": 2}[x["priority"]])
    print("\nYour Tasks:")
    for i, task in enumerate(sorted_tasks, 1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['name']} - Priority: {task['priority']} - Deadline: {task['deadline']} - {status}")

def mark_done(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to mark done: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]["done"] = True
                print(f"Marked '{tasks[num]['name']}' as done!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a number!")

def main():
    """Main program loop."""
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Done")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Pick 1-4.")


if __name__ == "__main__":
    main()