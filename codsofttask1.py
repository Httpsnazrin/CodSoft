
tasks = []

def displayTasks():
    print("\nTo-Do List:")
    if not tasks:
        print("Assignment isn't found.")
    for i, task in enumerate(tasks):
        status = "✓" if task['completed'] else "✗"
        print(f"{i + 1}. {task['name']} [{status}]")
    print("\n")


def addTask():
    name = input("Enter task name: ")
    tasks.append({"name": name, "completed": False})
    print(f"Task '{name}' added.")

def markTaskComplete():
    displayTasks()
    task_num = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        print(f"Task '{tasks[task_num]['name']}' marked as complete.")
    else:
        print("Invalid task number.")

def deleteTask():
    displayTasks()
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        task = tasks.pop(task_num)
        print(f"Task '{task['name']}' deleted.")
    else:
        print("Invalid task number.")


def main():
    while True:
        print("Options: ")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            displayTasks()
        elif choice == "2":
            addTask()
        elif choice == "3":
            markTaskComplete()
        elif choice == "4":
            deleteTask()
        elif choice == "5":
            print("Well done!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
