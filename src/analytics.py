class AnalyticsManager:

    def __init__(self, tasks):
        self.tasks = tasks

    def get_basic_statistics(self):
        total = len(self.tasks)
        completed = 0
        pending = 0

        for task in self.tasks:
            if task.status == "Completed":
                completed += 1
            else:
                pending += 1

        if total > 0:
            completion_rate = (completed / total) * 100
        else:
            completion_rate = 0

        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": round(completion_rate, 2)
    }

    def get_subject_workload(self):
        subject_count = {}

        for task in self.tasks:
            if task.subject in subject_count:
                subject_count[task.subject] += 1
            else:
                subject_count[task.subject] = 1

        return subject_count

    def get_priority_distribution(self):
        priority_count = {}

        for task in self.tasks:
            if task.priority in priority_count:
                priority_count[task.priority] += 1
            else:
                priority_count[task.priority] = 1

        return priority_count

    def get_completion_by_subject(self):
        subject_stats = {}

        for task in self.tasks:
            if task.subject not in subject_stats:
                subject_stats[task.subject] = [0, 0]

            subject_stats[task.subject][0] += 1

            if task.status == "Completed":
                subject_stats[task.subject][1] += 1

        return subject_stats