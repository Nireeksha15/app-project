import os

# Function to display the menu
def display_menu():
    print("\nTo-Do List App")
    print("1. View tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. Delete task")
    print("5. Exit")

# Function to load tasks from the file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    return []

# Function to save tasks to the file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added.")

# Function to edit a task
def edit_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to edit: ")) - 1
    if 0 <= task_num < len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_num] = new_task
        print("Task updated.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted.")
    else:
        print("Invalid task number.")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(filename, tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
