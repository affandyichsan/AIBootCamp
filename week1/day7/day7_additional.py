# add deadlines or priorities for tasks
# export tasks to a JSON or CSV file
# Support command-line arguments for quicker task manajemen

import os
import json
import csv
import argparse
import sys

FILE_NAME = "tasks.txt"

def task():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status, priority = line.strip().split(" | ")
                tasks[int(task_id)] = {"title" : title, "status":status, "priority":priority}
    return tasks

def add_task(tasks):
    title = input("Enter task title :")
    task_id = max(tasks.keys(), default=0) + 1
    priority = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status":"incomplete", "priority":priority}


# load task from file
def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 4:
                    task_id, title, status, priority = parts
                    tasks[int(task_id)] = {"title": title, "status": status, "priority": priority}
                else:
                    print(f"[Warning] Format tidak valid: {line.strip()}")
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}| {task['priority']}\n")
      
# view all task
def view_tasks(tasks):
    if not tasks:
        print("No Task avaliable.")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']} - {task['priority']}")

# Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complate :"))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task'{tasks[task_id]['title']}  - {tasks[task_id]['priority']}' marked as complete")
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
#export to json
def export_to_json(tasks, filename="task.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks berhasil diekspor ke {filename}")

def export_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Status", "Priority"])  # Header
        for task_id, task in tasks.items():
            writer.writerow([task_id, task["title"], task["status"], task["priority"]])
    print(f"Tasks berhasil diekspor ke {filename}")

# main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n Task manager menu :")
        print("1. Add task")
        print("2. view task")
        print("3. mark task")
        print("4. delete task ")
        print("5. Export to JSON")
        print("6. Export to CSV")
        print("7. exit")
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
            export_to_json(tasks)
        elif choice == "6":
            export_to_csv(tasks)
        elif choice == "7":
            save_tasks(tasks)
            print("goodbye")
            break
        else:
            print("Inalid Choice. Please Try again")
  
  
def cli_mode():
    parser = argparse.ArgumentParser(description="Simple Task Manager")

    parser.add_argument("--add", metavar="TITLE", help="Add a new task")
    parser.add_argument("--view", action="store_true", help="View all tasks")
    parser.add_argument("--done", type=int, metavar="ID", help="Mark task as complete")
    parser.add_argument("--delete", type=int, metavar="ID", help="Delete a task")
    parser.add_argument("--export-json", action="store_true", help="Export tasks to JSON")
    parser.add_argument("--export-csv", action="store_true", help="Export tasks to CSV")

    args = parser.parse_args()
    tasks = load_tasks()

    if args.add:
        task_id = max(tasks.keys(), default=0) + 1
        priority = input("Enter priority: ")
        tasks[task_id] = {"title": args.add, "status": "incomplete", "priority": priority}
        print(f"Task '{args.add}' added.")
        save_tasks(tasks)

    elif args.view:
        view_tasks(tasks)

    elif args.done is not None:
        if args.done in tasks:
            tasks[args.done]["status"] = "complete"
            print(f"Task '{tasks[args.done]['title']}' marked as complete.")
            save_tasks(tasks)
        else:
            print("Task ID not found.")

    elif args.delete is not None:
        if args.delete in tasks:
            deleted_task = tasks.pop(args.delete)
            print(f"Task '{deleted_task['title']}' deleted.")
            save_tasks(tasks)
        else:
            print("Task ID not found.")

    elif args.export_json:
        export_to_json(tasks)

    elif args.export_csv:
        export_to_csv(tasks)

    else:
        parser.print_help()

  
            
if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_mode()
    else:
        main()