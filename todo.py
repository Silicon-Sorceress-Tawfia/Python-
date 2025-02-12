import json
import os
import time

TASKS_FILE = "tasks.json"

class TodoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, title, description):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "status": "Pending",
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print("\nTask added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return
        print("\nYour Tasks:")
        for task in self.tasks:
            print(f"\nID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created At: {task['created_at']}")
            print("-" * 40)

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print("\nTask deleted successfully.")
        else:
            print("\nTask not found.")

    def update_task(self, task_id, title=None, description=None, status=None):
        task = self.get_task_by_id(task_id)
        if task:
            if title:
                task["title"] = title
            if description:
                task["description"] = description
            if status:
                task["status"] = status
            self.save_tasks()
            print("\nTask updated successfully.")
        else:
            print("\nTask not found.")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def mark_task_completed(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task["status"] = "Completed"
            self.save_tasks()
            print("\nTask marked as completed.")
        else:
            print("\nTask not found.")


def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")


def main():
    todo_list = TodoList()
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)

        elif choice == "2":
            todo_list.list_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (leave blank to skip): ")
            description = input("Enter new description (leave blank to skip): ")
            status = input("Enter new status (leave blank to skip): ")
            todo_list.update_task(task_id, title, description, status)

        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)

        elif choice == "5":
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list.mark_task_completed(task_id)

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice, please try again.")


if __name__ == "__main__":
    main()
