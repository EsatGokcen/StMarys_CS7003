tasks = []

def display_tasks():
    for task in tasks:
        print(task)


def add_task():
    add = input("What task would you like to add?: ")
    tasks.append(add)

def delete_task():
    delete = input("What task would you like to delete?: ")
    for task in tasks:
        if task == delete:
            tasks.remove(task)
            print("Task removed succesfully.")
        else:
            print("Could not find task...")

def main():
    while True:
        print("Options:\n1. View Tasks\n2. Add Task\n3. Delete Task")
        ask = input("\nChoice: ")
        print()

        if ask == "1":
            display_tasks()
        elif ask == "2":
            add_task()
        elif ask == "3":
            delete_task()
        else:
            break

if __name__ == '__main__':
    main()