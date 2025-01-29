# task_manager.py
tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{i + 1}. [{status}] {task['task']}")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Task {index + 1} marked as complete.")
    else:
        print("Invalid task number.")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task deleted: {removed_task['task']}")
    else:
        print("Invalid task number.")

if __name__ == "__main__":
    while True:
        print("\nPersonal Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark as complete: ")) - 1
            complete_task(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
