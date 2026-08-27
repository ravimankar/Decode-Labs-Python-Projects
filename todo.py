def show_menu():
    print("\n1. Task Add karo")
    print("2. Tasks Dekho")
    print("3. Band karo")

def add_task(tasks):
    task = input("Task likho: ")
    tasks.append(task)
    print("Task add ho gaya!")

def view_tasks(tasks):
    if not tasks:
        print("Koi task nahi hai abhi!")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def main():
    my_tasks = []
    while True:
        show_menu()
        choice = input("Kya karna hai (1/2/3): ")

        if choice == "1":
            add_task(my_tasks)
        elif choice == "2":
            view_tasks(my_tasks)
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Sahi option choose karo (1, 2, ya 3)")

if __name__ == "__main__":
    main()