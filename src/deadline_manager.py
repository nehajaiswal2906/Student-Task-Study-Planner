from datetime import datetime, timedelta

class DeadlineManager:

    def __init__(self, tasks):
        self.tasks = tasks

    def get_overdue_tasks(self):
        today = datetime.today().date()
        found = False

        for task in self.tasks:
            deadline = datetime.strptime(task.deadline,"%Y-%m-%d").date()

            if deadline < today and task.status != "Completed":
                task.show_task()
                print("OVERDUE")
                print("--------------------")
                found = True

        if not found:
            print("No overdue tasks.")
            
    def get_upcoming_tasks(self):
        today = datetime.today().date()
        next_week = today + timedelta(days=7)

        found = False

        for task in self.tasks:
            deadline = datetime.strptime(
                task.deadline,
                "%Y-%m-%d"
            ).date()

            if today <= deadline <= next_week and task.status != "Completed":
                task.show_task()
                print("UPCOMING")
                print("--------------------")
                found = True

        if not found:
            print("No upcoming tasks.")


    def count_overdue_tasks(self):
        today = datetime.today().date()
        count = 0

        for task in self.tasks:
            deadline = datetime.strptime(
                task.deadline,
                "%Y-%m-%d"
            ).date()

            if deadline < today and task.status != "Completed":
                count += 1

        return count

    def count_upcoming_tasks(self):
        today = datetime.today().date()
        next_week = today + timedelta(days=7)
        count = 0

        for task in self.tasks:
            deadline = datetime.strptime(
                task.deadline,
                "%Y-%m-%d"
            ).date()

            if today <= deadline <= next_week and task.status != "Completed":
                count += 1

        return count