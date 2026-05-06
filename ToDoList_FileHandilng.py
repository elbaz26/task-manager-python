import json

print("WELCOME 👋")

FILE_NAME = "tasks.json"


# تحميل البيانات
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return ['study', 'gym', 'football']


# حفظ البيانات
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(MyList, file)


MyList = load_tasks()


def add_task():
    Task = input("Enter The Task You Want To Add: ").strip()

    if not Task:
        print("Task cannot be empty!")
        return

    MyList.append(Task)
    save_tasks()
    print("## Add Is Done ##")


def remove_task():
    show_task()

    try:
        Num = int(input("Enter Task Number To Remove: "))

        if 1 <= Num <= len(MyList):
            removed = MyList.pop(Num - 1)
            save_tasks()
            print(f"{removed} Removed ✔")
        else:
            print("Invalid Number ❌")

    except:
        print("Invalid Input ❌")


def show_task():
    if not MyList:
        print("No Tasks Yet!")
        return

    print("-" * 30)
    for i, n in enumerate(MyList, 1):
        print(f"{i}- {n}")
    print("-" * 30)


def edit_task():
    show_task()

    try:
        Num = int(input("Enter Task Number To Edit: "))

        if 1 <= Num <= len(MyList):
            new_task = input("Enter New Task: ").strip()

            if not new_task:
                print("Task cannot be empty!")
                return

            MyList[Num - 1] = new_task
            save_tasks()
            print("Edit Is Done ✔")

        else:
            print("Invalid Number ❌")

    except:
        print("Invalid Input ❌")


while True:

    print("=" * 40)
    print("1- Add Task")
    print("2- Remove Task")
    print("3- Show Tasks")
    print("4- Edit Task")
    print("5- Exit")
    print("=" * 40)

    try:
        Choice = int(input("Enter Number Of Choice: "))

        if Choice == 1:
            add_task()
        elif Choice == 2:
            remove_task()
        elif Choice == 3:
            show_task()
        elif Choice == 4:
            edit_task()
        elif Choice == 5:
            print("Bye 👋")
            break
        else:
            print("Wrong Choice!")

    except:
        print("Invalid Entry ❌")