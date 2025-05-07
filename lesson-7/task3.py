import os
import sys
import json

# Placeholder for storage object
class JSONStorage:
    def __init__(self, filename):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, 'w') as file:
            json.dump([task.__dict__ for task in tasks], file, indent=4)

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                return [ToDo(**task) for task in json.load(file)]
        except FileNotFoundError:
            return []

storage = JSONStorage("tasks.json")

class ToDo:
    def __init__(self, Task_ID, Title, Description, due_date, status):
        self.Task_ID = Task_ID
        self.Title = Title
        self.Description = Description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f'{self.Task_ID}, {self.Title}, {self.Description}, {self.due_date}, {self.status}'

# Functions

def add():
    Task_ID = input('Enter Task ID: ')
    Title = input('Enter Title: ')
    Description = input('Enter Description: ')
    due_date = input('Enter Due Date: ')
    status = input('Enter Status (Pending/In Progress/Completed): ')
    task = ToDo(Task_ID, Title, Description, due_date, status)
    tasks = storage.load()
    tasks.append(task)
    storage.save(tasks)
    print("Task added successfully!")

def view():
    tasks = storage.load()
    if not tasks:
        print('No tasks found.')
    else:
        print('ALL TASKS:')
        for task in tasks:
            print(task)

def update():
    Task_ID = input("Enter Task ID to update: ")
    tasks = storage.load()
    for task in tasks:
        if task.Task_ID == Task_ID:
            task.Title = input("Enter new Title: ")
            task.Description = input("Enter new Description: ")
            task.due_date = input("Enter new Due Date: ")
            task.status = input("Enter new Status: ")
            storage.save(tasks)
            print("Task updated successfully!")
            return
    print("Task not found.")

def delete():
    Task_ID = input("Enter Task ID to delete: ")
    tasks = storage.load()
    tasks = [task for task in tasks if task.Task_ID != Task_ID]
    storage.save(tasks)
    print("Task deleted successfully!")

def filter_tasks_by_status():
    status = input("Enter status to filter by (Pending/In Progress/Completed): ")
    tasks = storage.load()
    filtered = [task for task in tasks if task.status.lower() == status.lower()]
    if not filtered:
        print("No tasks with that status.")
    else:
        print(f"Tasks with status '{status}':")
        for task in filtered:
            print(task)

def save_tasks():
    tasks = storage.load()
    storage.save(tasks)
    print("Tasks saved.")

def load_tasks():
    tasks = storage.load()
    print(f"Loaded {len(tasks)} tasks.")

def exit_program():
    print("Goodbye!")
    sys.exit()

# Main menu
if __name__ == '__main__':
    while True:
        print('\nWelcome to the To-Do Application!')
        print('1. Add a new task')
        print('2. View all tasks')
        print('3. Update a task')
        print('4. Delete a task')
        print('5. Filter tasks by status')
        print('6. Save tasks')
        print('7. Load tasks')
        print('8. Exit')

        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        elif choice == 5:
            filter_tasks_by_status()
        elif choice == 6:
            save_tasks()
        elif choice == 7:
            load_tasks()
        elif choice == 8:
            exit_program()
        else:
            print("Please enter a valid option (1-8).")
