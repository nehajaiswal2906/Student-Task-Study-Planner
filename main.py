from src.utils import display_menu
from src.task_manager import TaskManager
from src.deadline_manager import DeadlineManager
from src.analytics import AnalyticsManager
from src.progress_manager import ProgressManager
from src.reports import ReportManager
from src.storage import load_tasks, save_tasks
from src.validators import (
    validate_priority,
    validate_deadline,
    validate_not_empty,
    validate_task_id,
    validate_integer
)

manager = TaskManager()
manager.tasks = load_tasks()
deadline_manager = DeadlineManager(manager.tasks)
analytics_manager = AnalyticsManager(manager.tasks)
progress_manager = ProgressManager(manager.tasks)
report_manager = ReportManager(
    analytics_manager,
    deadline_manager
)

while True:
    display_menu()
    choice = input("Enter your choice:")

    if choice == "1":
        title = input("Enter task title: ")
        subject = input("Enter subject: ")
        priority = input("Enter priority: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")

        if not validate_not_empty(title):
            print("Title cannot be empty.")
            continue

        if not validate_not_empty(subject):
            print("Subject cannot be empty.")
            continue

        if not validate_priority(priority):
            print("Invalid priority. Use High, Medium, or Low.")
            continue

        if not validate_deadline(deadline):
            print("Invalid deadline. Use YYYY-MM-DD.")
            continue

        manager.add_task(title, subject, priority, deadline)
        save_tasks(manager.tasks)

        print("Task added successfully.")

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        keyword = input("Enter keyword to search: ")
        manager.search_tasks(keyword)

    elif choice == "4":
        task_id_input = input("Enter task ID to update: ")

        if not validate_integer(task_id_input):
            print("Task ID must be a number.")
            continue

        task_id = int(task_id_input)

        if not validate_task_id(task_id, manager.tasks):
            print("Invalid task ID.")
            continue

        title = input("Enter new title: ")
        subject = input("Enter new subject: ")
        priority = input("Enter new priority: ")
        deadline = input("Enter new deadline (YYYY-MM-DD): ")

        if not validate_not_empty(title):
            print("Title cannot be empty.")
            continue

        if not validate_not_empty(subject):
            print("Subject cannot be empty.")
            continue

        if not validate_priority(priority):
            print("Invalid priority. Use High, Medium, or Low.")
            continue

        if not validate_deadline(deadline):
            print("Invalid deadline. Use YYYY-MM-DD.")
            continue

        for task in manager.tasks:
            if task.task_id == task_id:
                task.title = title
                task.subject = subject
                task.priority = priority
                task.deadline = deadline
                break

        save_tasks(manager.tasks)
        print("Task updated successfully.")


    elif choice == "5":
        task_id_input = input("Enter task ID to delete: ")

        if not validate_integer(task_id_input):
            print("Task ID must be a number.")
            continue

        task_id = int(task_id_input)

        if not validate_task_id(task_id, manager.tasks):
            print("Invalid task ID.")
            continue

        manager.delete_task(task_id)
        save_tasks(manager.tasks)

    elif choice == "6":
        task_id_input = input("Enter task ID to mark complete: ")

        if not validate_integer(task_id_input):
            print("Task ID must be a number.")
            continue

        task_id = int(task_id_input)

        if not validate_task_id(task_id, manager.tasks):
            print("Invalid task ID.")
            continue

        progress_manager.mark_complete(task_id)
        save_tasks(manager.tasks)

    elif choice == "7":
        progress_manager.get_pending_tasks()

    elif choice == "8":
        print("\n1. Filter by Status")
        print("2. Filter by Priority")

        filter_choice = input("Enter choice: ")

        if filter_choice == "1":
            status = input("Enter status (Pending/Completed): ")
            manager.filter_tasks("status", status)

        elif filter_choice == "2":
            priority = input("Enter priority (High/Medium/Low): ")
            manager.filter_tasks("priority", priority)

        else:
            print("Invalid filter choice.")

    elif choice == "9":
        deadline_manager.get_overdue_tasks()

    elif choice=="10":
        deadline_manager.get_upcoming_tasks()

    elif choice == "11":
        print("1. Basic Statistics")
        print("2. Subject-wise Workload")
        print("3. Priority Distribution")
        print("4. Completion by Subject")

        analytics_choice = input("Enter choice: ")

        if analytics_choice == "1":
            statistics = analytics_manager.get_basic_statistics()

            print("\n========== TASK STATISTICS ==========")
            print("Total Tasks:", statistics["total"])
            print("Completed:", statistics["completed"])
            print("Pending:", statistics["pending"])
            print("Completion Rate:", statistics["completion_rate"], "%")

        elif analytics_choice == "2":
            subject_count = analytics_manager.get_subject_workload()

            print("\n========== SUBJECT-WISE WORKLOAD ==========")

            if not subject_count:
                print("No tasks available.")
            else:
                for subject, count in subject_count.items():
                    print(subject + ":", count, "tasks")

        elif analytics_choice == "3":
            priority_count = analytics_manager.get_priority_distribution()

            print("\n========== PRIORITY DISTRIBUTION ==========")

            if not priority_count:
                print("No tasks available.")
            else:
                for priority, count in priority_count.items():
                    print(priority + ":", count, "tasks")

        elif analytics_choice == "4":
            subject_stats = analytics_manager.get_completion_by_subject()

            print("\n========== COMPLETION BY SUBJECT ==========")

            if not subject_stats:
                print("No tasks available.")
            else:
                for subject, stats in subject_stats.items():
                    total = stats[0]
                    completed = stats[1]

                    print(subject + ":", completed, "/", total, "completed")

    elif choice == "12":
        report_manager.generate_report()

    elif choice == "13":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


