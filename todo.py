import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['task']}")
    print()

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Mark complete
def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task completed!")
    except:
        print("Invalid task number.")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted!")
    except:
        print("Invalid task number.")

# Main Program
def main():
    tasks = load_tasks()

    while True:
        print("""
====== TO-DO LIST ======
1. View Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()