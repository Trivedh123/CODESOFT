import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []

    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file :
                line = line.strip()

                if "|" in line:
                    status , task = line.split("|", 1)
                    tasks.append({
                        "task": task,
                        "completed": status == "1"
                    })

    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            status = "1" if task["completed"] else "0"
            file.write(f"{status}|{task['task']}\n")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return 
    print("\n ----------- ToDo List ---------")

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. [{status}] {task['task']}")

    print()

def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append({
        "task": task_name,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully.\n")

def complete_task(tasks):
    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to mark as completed: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid task number.\n")

def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['task']}' deleted successfully.\n")
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Invalid input. Please enter a valid task number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("========== ToDo List Menu ==========")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)
        
        elif choice == "4":
            delete_task(tasks)
        
        elif choice == "5":
            print("Thank you for using the ToDo List application.")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()