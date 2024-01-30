import argparse
from task_manager import *

def main():
    parser = argparse.ArgumentParser(description="Task Manager")
    parser.add_argument("file_path", help="Path to the file with tasks and manager state")

    args = parser.parse_args()

    task_manager = TaskManager()

    try:
        task_manager.load_from_file(args.file_path)
        print("Loaded tasks and manager state from", args.file_path)
    except FileNotFoundError:
        print("File not found. Starting with an empty task manager.")

    while True:
        print("\n1. Add Task")
        print("2. Change Task Status")
        print("3. Cancel Task")
        print("4. Save and Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            status = TaskStatus.NEW.value
            created_at = str(datetime.now())
            status_changed_at = created_at

            new_task = Task(title, description, status, created_at, status_changed_at)
            task_manager.add_task(new_task)
            print("Task added successfully.")

        elif choice == '2':
            try:
                task_index = int(input("Enter the index of the task you want to change status for: "))
                new_status = input("Enter the new status (Новая/Выполняется/Ревью/Выполнено/Отменено): ")
                task_manager.change_task_status(task_index, TaskStatus(new_status).value)
                print("Task status changed successfully.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid task index.")

        elif choice == '3':
            try:
                task_index = int(input("Enter the index of the task you want to cancel: "))
                task_manager.cancel_task(task_index)
                print("Task canceled successfully.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid task index.")

        elif choice == '4':
            task_manager.save_to_file(args.file_path)
            print("Tasks and manager state saved. Exiting.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()