tasks = []

def add_task(task):
    tasks.append(task)
    print("Task Added")

def remove_task(task):
    index = task - 1
    t = tasks[index]
    if t in tasks:
        remove = tasks.pop(index)
        print(f"Task {remove} Removed")
    else:
        print("Task not found")

def view_tasks():
    if tasks:
        print('--------------------')
        print("TODO'S")
        print('--------------------')
        for index, t in enumerate(tasks, start=1):
            print(f"{index} - {t}")
    else:
        print("No Tasks Available")

def main():
    while True:
        print('--------------------')
        print('TODO LIST')
        print('--------------------')
        inp = int(input("Enter Your choice(1,2,3,4):\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit\n"))
        if inp == 1:
            task = input("Enter Task: ")
            add_task(task)
        elif inp == 2:
            task = int(input("Enter Task Number To Remove: "))
            remove_task(task)
        elif inp == 3:
            view_tasks()
        elif inp == 4:
            print("Exiting...")
            exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()