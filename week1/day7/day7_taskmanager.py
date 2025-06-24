import os

# file to store to task

FILE_NAME = "tasks.txt"

# load task from file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" | ")
                tasks[int(task_id)] = {"title" : title, "status":status}
                
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")
        
def add_task(tasks):
    title = input("Enter task title : ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status":"incomplete"}
    print(f"Task '{title}' added.")


# view all task
def view_tasks(tasks):
    if not tasks:
        print("No Task avaliable.")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")

# Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complate :"))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task'{tasks[task_id]['title']}' marked as complete")
    else:
        print("task ID not Found.")
        
# delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to mark as complate :"))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("task ID not Found.")
        
# main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n Task manager menu :")
        print("1. Add task")
        print("2. view task")
        print("3. mark task")
        print("4. delete task ")
        print("5. exit")
        choice = input("Enter yor choice : ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("goodbye")
            break
        else:
            print("Inalid Choice. Please Try again")
            
if __name__ == "__main__":
    main()