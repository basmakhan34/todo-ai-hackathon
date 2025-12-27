# src/todo.py

"""
This module implements a simple in-memory Todo application.
"""

import sys

# In-memory storage for tasks.
# The key is the task ID (integer), and the value is a dictionary
# with 'title', 'description', and 'status'.
tasks = {}
next_id = 1


def add_task():
    """Adds a new task to the list."""
    global next_id
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks[next_id] = {
        "title": title,
        "description": description,
        "status": "Pending"
    }
    print(f"Task {next_id} added.")
    next_id += 1


def view_tasks():
    """Displays all tasks."""
    if not tasks:
        print("No tasks to show.")
        return

    print("\n--- Todo List ---")
    for task_id, task in tasks.items():
        print(f"ID: {task_id}, Status: {task['status']}, "
              f"Title: {task['title']}")
    print("-----------------\n")


def mark_complete():
    """Marks a task as complete."""
    try:
        task_id = int(input("Enter task ID to mark as complete: "))
        if task_id in tasks:
            tasks[task_id]["status"] = "Done"
            print(f"Task {task_id} marked as Done.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def update_task():
    """Updates an existing task."""
    try:
        task_id = int(input("Enter task ID to update: "))
        if task_id in tasks:
            new_title = input(f"Enter new title "
                              f"(current: {tasks[task_id]['title']}): ")
            new_description = input(
                "Enter new description (current: "
                f"{tasks[task_id]['description']}): "
            )

            if new_title:
                tasks[task_id]['title'] = new_title
            if new_description:
                tasks[task_id]['description'] = new_description
            print(f"Task {task_id} updated.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def delete_task():
    """Deletes a task."""
    try:
        task_id = int(input("Enter task ID to delete: "))
        if task_id in tasks:
            del tasks[task_id]
            print(f"Task {task_id} deleted.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def search_tasks():
    """Searches for tasks by title or description."""
    search_term = input("Enter search term: ").lower()
    found_tasks = False
    print("\n--- Search Results ---")
    for task_id, task in tasks.items():
        if (search_term in task['title'].lower() or
                search_term in task['description'].lower()):
            print(f"ID: {task_id}, Status: {task['status']}, "
                  f"Title: {task['title']}")
            found_tasks = True
    if not found_tasks:
        print("No tasks found.")
    print("----------------------\n")


def print_menu():
    """Prints the main menu."""
    print("\n--- Todo Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Search Tasks")
    print("7. Exit")
    print("-----------------\n")


def main():
    """Main function to run the Todo application."""
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_complete()
        elif choice == '4':
            update_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            search_tasks()
        elif choice == '7':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
