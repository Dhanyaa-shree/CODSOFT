import os 
import json

DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as file:
            return json.load(file)
        return []
    
def save_tasks(tasks):
    with open(DATA_FILE,"w") as file:
        json.dump([],file)

def show_tasks(tasks):
    if not tasks:
        print("\nNo TASKS FOUND \n")
    else:
        print("\n TO-DO LIST")
        for i,task in enumerate (tasks,1):
            status = "✔️" if task["done"] else "❌"
            print(f"{i}.[{status}] {task['title']}")
        print()

def add_task(tasks):
    title = input("Enter task title:")
    tasks.append({"title": title,"done":False})
    save_tasks(tasks)
    print("Task added.\n")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to marks as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Tasks marked as complete. \n")
        else:
            print("Invalid task number. \n")
    except ValueError:
        print("Enter a valid number. \n")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete : ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted : {removed['title']}\n")
        else:
            print("Invalid task number. \n")
    except ValueError:
        print("Enter a valid number. \n")

def main():
    tasks = load_tasks()
    while True:
        print("1.show Tasks\n 2.Add Tasks\n 3.Completed Task\n4.Delete Task\n5.Exit")
        choice = input("choice an option : ")
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice ")


if __name__ == "__main__":
    main()



    