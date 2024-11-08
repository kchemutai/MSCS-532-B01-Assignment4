from PriorityQueue import PriorityQueue
from Task import Task

def scheduler_simulation():
    pq = PriorityQueue()

    # Insert tasks with different priorities (higher values indicate higher priority)
    pq.insert(Task(task_id="Task1", priority=3, arrival_time="10:00", deadline="10:30"))
    pq.insert(Task(task_id="Task2", priority=5, arrival_time="10:05", deadline="10:25"))
    pq.insert(Task(task_id="Task3", priority=1, arrival_time="10:10", deadline="10:20"))

    # Extract tasks based on highest priority first
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Executing {task.task_id} with priority {task.priority}")

scheduler_simulation()