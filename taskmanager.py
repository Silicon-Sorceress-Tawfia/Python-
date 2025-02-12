import os
import pickle

TASKS_FILE = "tasks.dat"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'rb') as f:
            return pickle.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'wb') as f:
        pickle.dump(tasks, f)

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task['title']} - {task['status']}")

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {
        "title": title,
        "description": description,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("\nTask added successfully.\n")

def update_task(tasks):
    display_tasks(tasks)
    task_number = int(input("\nEnter task number to update: ")) - 1
    if task_number < 0 or task_number >= len(tasks):
        print("\nInvalid task number.\n")
        return
    new_status = input(f"Enter new status for task '{tasks[task_number]['title']}': ")
    tasks[task_number]['status'] = new_status
    save_tasks(tasks)
    print("\nTask updated successfully.\n")

def delete_task(tasks):
    display_tasks(tasks)
    task_number = int(input("\nEnter task number to delete: ")) - 1
    if task_number < 0 or task_number >= len(tasks):
        print("\nInvalid task number.\n")
        return
    tasks.pop(task_number)
    save_tasks(tasks)
    print("\nTask deleted successfully.\n")

def main():
    tasks = load_tasks()
    while True:
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice, please try again.\n")

if __name__ == "__main__":
    main()
