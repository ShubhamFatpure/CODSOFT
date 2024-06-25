import datetime

tasks = []

def create_task(description, due_date=None):
    task = {
        'description': description,
        'due_date': due_date,
        'completed': False,
        'created_at': datetime.datetime.now(),
        'completed_at': datetime.datetime.now(),
        'updated_at': datetime.datetime.now()
    }
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("No tasks available.")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task['completed'] else "Pending"
        due_date = task['due_date'] if task['due_date'] else "No due date"
        created_at = task['created_at'].strftime("%Y-%m-%d %H:%M:%S")
        print(f"{index}. {task['description']} - {due_date} - {status} - Created at: {created_at}")

def update_task(index, description=None, due_date=None):
    if description:
        tasks[index]['description'] = description
    if due_date:
        tasks[index]['due_date'] = due_date
    tasks[index]['updated_at'] = datetime.datetime.now()

def complete_task(index):
    tasks[index]['completed'] = True
    tasks[index]['completed_at'] = datetime.datetime.now()

def delete_task(index):
    tasks.pop(index)

def input_due_date():
    date_str = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    if date_str:
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            return input_due_date()
    return None


# view detailed information for track to do list
def view_task_details(index):
    task = tasks[index]
    status = "Done" if task['completed'] else "Pending"
    due_date = task['due_date'] if task['due_date'] else "No due date"
    created_at = task['created_at'].strftime("%Y-%m-%d %H:%M:%S")
    completed_at = task['completed_at'].strftime("%Y-%m-%d %H:%M:%S") if task['completed_at'] else "Not completed"
    updated_at = task['updated_at'].strftime("%Y-%m-%d %H:%M:%S") if task['updated_at'] else "Not updated"
    print(f"Task: {task['description']}")
    print(f"Due Date: {due_date}")
    print(f"Status: {status}")
    print(f"Created at: {created_at}")
    print(f"Completed at: {completed_at}")
    print(f"Last Updated at: {updated_at}")


def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. View Task Details")
        print("4. Update Task")
        print("5. Mark Task as Complete")
        print("6. Delete Task")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input_due_date()
            create_task(description, due_date)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            index = int(input("Enter task number to view details: ")) - 1
            if 0 <= index < len(tasks):
                view_task_details(index)
            else:
                print("Invalid task number.")
        elif choice == '4':
            view_tasks()
            index = int(input("Enter task number to update: ")) - 1
            if 0 <= index < len(tasks):
                description = input("Enter new description (or leave blank): ")
                due_date = input_due_date()
                update_task(index, description, due_date)
            else:
                print("Invalid task number.")
        elif choice == '5':
            view_tasks()
            index = int(input("Enter task number to mark as complete: ")) - 1
            if 0 <= index < len(tasks):
                complete_task(index)
            else:
                print("Invalid task number.")
        elif choice == '6':
            view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                delete_task(index)
            else:
                print("Invalid task number.")
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

        # For Example
        # Finish the report
        # Call the plumber
        # Buy groceries
        # Book flight tickets