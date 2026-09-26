class Task:
    def __init__(self, task_id, title, subject, priority, deadline):
        self.task_id = task_id
        self.title = title
        self.subject = subject
        self.priority = priority
        self.deadline = deadline
        self.status = "Pending"

    def show_task(self):
        print("ID:", self.task_id)
        print("Title:", self.title)
        print("Subject:", self.subject)
        print("Priority:", self.priority)
        print("Deadline:", self.deadline)
        print("Status:", self.status)

class TaskManager:

    def __init__(self):
        self.tasks = []
    def add_task(self, title, subject, priority, deadline):
        task_id = len(self.tasks) + 1

        task = Task(
            task_id,
            title,
            subject,
            priority,
            deadline
        )

        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            task.show_task()
            print("--------------------")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                self.renumber_tasks()
                print("Task deleted successfully.")
                return

        print("Task not found.")

    def renumber_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            task.task_id = index

    def update_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new title: ")
                task.subject = input("Enter new subject: ")
                task.priority = input("Enter new priority: ")
                task.deadline = input("Enter new deadline: ")

                print("Task updated successfully.")
                return

        print("Task not found.") 


    def search_tasks(self, keyword):
        found = False

        for task in self.tasks:
            if keyword.lower() in task.title.lower():
                task.show_task()
                print("--------------------")
                found = True

        if not found:
            print("No matching tasks found.")

    def filter_tasks(self, category, value):
        found = False

        for task in self.tasks:
            if category == "status" and task.status.lower() == value.lower():
                task.show_task()
                print("--------------------")
                found = True

            elif category == "priority" and task.priority.lower() == value.lower():
                task.show_task()
                print("--------------------")
                found = True

        if not found:
            print("No matching tasks found.")
