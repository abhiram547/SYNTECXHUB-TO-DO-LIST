import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except:
            return []
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    priority = input("Enter priority (High/Medium/Low): ")
    due_date = input("Enter due date (optional): ")

    tasks.append({
        "task": task,
        "priority": priority,
        "due_date": due_date,
        "done": False
    })

    save_tasks(tasks)
    print("✅ Task added successfully!")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n===== TO-DO LIST =====")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["done"] else "❌ Not Done"
        print(f"""
{i}. {task['task']}
   Priority : {task['priority']}
   Due Date : {task['due_date']}
   Status   : {status}
""")

# Mark task as done
def mark_done(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("Enter task number to mark as done: "))

        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed!")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("Enter task number to delete: "))

        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑 Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("""
======== TO-DO LIST MANAGER ========
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_done(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Exiting To-Do List Manager...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run program
if __name__ == "__main__":
    main()