# TO-DO List Manager using File handling

file_name = "todolist.txt"
while True:
    print("=============================")
    print("     TO-DO LIST MANAGER   ")
    print("=============================")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Clear All Tasks")
    print("4. Exit")

    user_choice = input("Enter your choice(1-4):")

    if user_choice == "1":
        task = input("Enter the task: ")
        file = open(file_name, "a")
        file.write(task + "\n")
        file.close()
        print("Task added successfully!!")
    elif user_choice == "2":
        file = open(file_name, "a")
        file.close()

        file = open(file_name, "r")
        tasks = file.readlines()
        file.close() 

        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            i = 1
            for task in tasks:
                print(i, ".", task.strip())
                i = i + 1

    elif user_choice == "3":
        file = open(file_name, "w")
        file.close()
        print("All tasks cleared.")

    elif user_choice == "4":
        print("Dhanyabaad!! Feri aaunu hola")
        break

    else:
        print("Choice Milena hajurr4")