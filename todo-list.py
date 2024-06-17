tasks = []
def add_task(task):
    tasks.append({"task":task, "completed":False})
    print("Tasks added successfully.")

def view_tasks():
    print("\n========= To-Do-List Application ===========")
    for i, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "✓"
        else:
            status = " "

        print(f"{i}. [{status}] {task['task']}")
    print()
def mark_completed(i):
    if 1 <= i <= len(tasks):
        tasks[i-1]["completed"] = True
        print("Tasks completed.")
    else:
         print("Invalid Task Number.")
def delete_task():
    if len(tasks) == 0:
        print("No Tasks to Delete.")
    else:     
          i = int(input("Enter the task number to delete: "))

          if 0 < i <= len(tasks):
              del tasks[i-1]
              print("Tasks deleted successfully.")
          else:
            print("Invalid Task Number.")

while True:
    print("\n========= To-Do-List Application ===========")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = (input("Enter your Choice: "))
    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        i = int(input("Enter the task number: "))
        mark_completed(i)
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank You for using the To-Do-List Application.")
        break
    else:
        print("Invalid choice. Please Try Again.")
    
    


      
      