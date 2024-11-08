class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        # For max-heap, tasks with higher priority values are considered "less than"
        return self.priority > other.priority  # Reversed comparison for max-heap
