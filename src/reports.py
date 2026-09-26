class ReportManager:

    def __init__(self, analytics_manager, deadline_manager):
        self.analytics_manager = analytics_manager
        self.deadline_manager = deadline_manager

    def generate_report(self):
        statistics = self.analytics_manager.get_basic_statistics()

        print("\n========================================")
        print("        STUDENT PRODUCTIVITY REPORT")
        print("========================================")

        print("\nTASK SUMMARY")
        print("Total Tasks       :", statistics["total"])
        print("Completed         :", statistics["completed"])
        print("Pending           :", statistics["pending"])
        print("Completion Rate   :", statistics["completion_rate"], "%")

        overdue = self.deadline_manager.count_overdue_tasks()
        upcoming = self.deadline_manager.count_upcoming_tasks()

        print("\nDEADLINE SUMMARY")
        print("Overdue           :", overdue)
        print("Upcoming (7 days) :", upcoming)

        subject_count = self.analytics_manager.get_subject_workload()

        print("\nSUBJECT WORKLOAD")

        if not subject_count:
            print("No tasks available.")
        else:
            for subject, count in subject_count.items():
                print(subject + ":", count, "tasks")

        priority_count = self.analytics_manager.get_priority_distribution()

        print("\nPRIORITY DISTRIBUTION")

        if not priority_count:
            print("No tasks available.")
        else:
            for priority, count in priority_count.items():
                print(priority + ":", count, "tasks")


        subject_stats = self.analytics_manager.get_completion_by_subject()

        print("\nCOMPLETION BY SUBJECT")

        if not subject_stats:
            print("No tasks available.")
        else:
            for subject, stats in subject_stats.items():
                total = stats[0]
                completed = stats[1]

                print(subject + ":", completed, "/", total, "completed")

        completion_rate = statistics["completion_rate"]

        if completion_rate >= 80:
            productivity = "Excellent"
        elif completion_rate >= 60:
            productivity = "Good"
        elif completion_rate >= 40:
            productivity = "Average"
        else:
            productivity = "Needs Improvement"

        print("\n========================================")
        print("Overall Productivity:", productivity)
        print("========================================")