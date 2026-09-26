class ProgressManager:

    def __init__(self, tasks):
        self.tasks = tasks

    def mark_complete(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = "Completed"
                print("Task marked as completed.")
                return

        print("Task not found.")

    def get_pending_tasks(self):
        found = False

        for task in self.tasks:
            if task.status == "Pending":
                task.show_task()
                print("--------------------")
                found = True

        if not found:
            print("No pending tasks.")

    def get_progress(self):
        total = len(self.tasks)
        completed = 0

        for task in self.tasks:
            if task.status == "Completed":
                completed += 1

        pending = total - completed

        if total > 0:
            completion_rate = (completed / total) * 100
        else:
            completion_rate = 0

        print("\n========== PROGRESS ==========")
        print("Total Tasks:", total)
        print("Completed:", completed)
        print("Pending:", pending)
        print("Completion Rate:", round(completion_rate, 2), "%")