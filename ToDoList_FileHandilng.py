import json

FILE_NAME = "tasks.json"

# =========================
# Load & Save
# =========================
def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)


tasks = load_tasks()

print("WELCOME 👋")

# =========================
# Functions
# =========================
def add_task():
    task = input("Enter task: ").strip()
    if not task:
        print("Task cannot be empty!")
        return
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully ✔")


def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("-" * 30)
    for i, task in enumerate(tasks, 1):
        print(f"{i}- {task}")
    print("-" * 30)


def remove_task():
    show_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number!")
    except:
        print("Invalid input!")


def edit_task():
    show_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter task number to edit: "))
        if 1 <= index <= len(tasks):
            new_task = input("Enter new task: ").strip()
            if not new_task:
                print("Task cannot be empty!")
                return
            tasks[index - 1] = new_task
            save_tasks(tasks)
            print("Task updated ✔")
        else:
            print("Invalid number!")
    except:
        print("Invalid input!")


# =========================
# Main Loop
# =========================
while True:
    print("=" * 40)
    print("1- Add Task")
    print("2- Remove Task")
    print("3- Show Tasks")
    print("4- Edit Task")
    print("5- Exit")
    print("=" * 40)

    try:
        choice = int(input("Choose: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            show_tasks()
        elif choice == 4:
            edit_task()
        elif choice == 5:
            print("Bye 👋")
            break
        else:
            print("Invalid choice!")

    except:
        print("Please enter a number!")