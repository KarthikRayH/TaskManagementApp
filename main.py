from task_manager import *
from recommender import recommend_task

initialize_file()

while True:

    print("\n===== TASK MANAGEMENT APP =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Recommend Task")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        task = input("Enter Task Name: ")

        try:
            priority = int(input("Enter Priority (1-10): "))
        except:
            print("Invalid Priority!")
            continue

        add_task(task, priority)

        print("Task Added Successfully!")

    elif choice == "2":

        task = input("Enter Task Name to Remove: ")

        remove_task(task)

        print("Task Removed Successfully!")

    elif choice == "3":

        list_tasks()

    elif choice == "4":

        df = get_tasks()

        task = recommend_task(df)

        if task:
            print(f"\nRecommended Task: {task}")
        else:
            print("\nNot enough data for recommendation.")

    elif choice == "5":

        print("Exiting Application...")
        break

    else:
        print("Invalid Choice!")
