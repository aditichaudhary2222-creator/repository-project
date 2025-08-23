tasks =[]
def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("/nYour To-Do Lists:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {tasks}")
            
def add_task():
    global tasks
    task= input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")
    
def remove_task():
    global tasks
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed!")
        except(ValueError,IndexError):
            print("Invalid task number!")
            
def main():
    while True:
        print("/nOptions: 1=Show  2=Add  3=Remove  4=Exit")
        choice = input("Choose: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
if __name__== "__main__":
    main()