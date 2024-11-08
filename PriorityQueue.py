class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:  # Adjusted for max-heap
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:  # Adjusted for max-heap
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:  # Adjusted for max-heap
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            raise IndexError("Priority queue is empty")
        if len(self.heap) == 1:
            return self.heap.pop()

        max_task = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_task

    def increase_key(self, task_id, new_priority):
        for index, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority < task.priority:
                    raise ValueError("New priority is lower than current priority")

                task.priority = new_priority
                self._heapify_up(index)
                return

        raise ValueError("Task not found in priority queue")

    def is_empty(self):
        return len(self.heap) == 0
