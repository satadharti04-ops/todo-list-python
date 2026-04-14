tasks = []

# Load tasks
try:
    with open("tasks.txt", "r") as f:
        tasks = f.read().splitlines()
except:
    pass

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

    elif choice == "3":
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)

    elif choice == "4":
        tasks.clear()
        print("All tasks cleared!")

    elif choice == "5":
        break

    # Save tasks
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(t + "\n")