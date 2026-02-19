"""
Assignment 4 - Priority Queue using Binary Heap

Supports:
- extract_max / extract_min
- increase_key / decrease_key
- insert
- is_empty

Time Complexity:
insert         -> O(log n)
extract_max/min-> O(log n)
increase_key   -> O(log n)
decrease_key   -> O(log n)
is_empty       -> O(1)
"""


class PriorityQueue:
    """
    Heap-based priority queue.
    Works as max-heap or min-heap based on mode.
    """

    def __init__(self, mode="max"):
        if mode not in ("max", "min"):
            raise ValueError("Mode must be 'max' or 'min'")

        self.mode = mode
        self.heap = []
        self.position = {}  # task_id -> index

    # ---------------- Utility ----------------

    def is_empty(self):
        """Check if queue is empty. O(1)"""
        return len(self.heap) == 0

    def _higher_priority(self, a, b):
        if self.mode == "max":
            return a[0] > b[0]
        return a[0] < b[0]

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.position[self.heap[i][1]] = i
        self.position[self.heap[j][1]] = j

    def _bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2

            if self._higher_priority(self.heap[i], self.heap[parent]):
                self._swap(i, parent)
                i = parent
            else:
                break

    def _bubble_down(self, i):
        n = len(self.heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            best = i

            if left < n and self._higher_priority(self.heap[left], self.heap[best]):
                best = left

            if right < n and self._higher_priority(self.heap[right], self.heap[best]):
                best = right

            if best != i:
                self._swap(i, best)
                i = best
            else:
                break

    # ---------------- Core Operations ----------------

    def insert(self, task_id, task_name, priority):
        """
        Insert new task. O(log n)
        """
        if task_id in self.position:
            raise ValueError("Task already exists")

        node = [priority, task_id, task_name]
        self.heap.append(node)

        idx = len(self.heap) - 1
        self.position[task_id] = idx

        self._bubble_up(idx)

    def extract_top(self):
        """
        Remove and return highest (max) or lowest (min) priority task.
        O(log n)
        """
        if self.is_empty():
            return None

        top = self.heap[0]
        last = self.heap.pop()

        del self.position[top[1]]

        if self.heap:
            self.heap[0] = last
            self.position[last[1]] = 0
            self._bubble_down(0)

        return {
            "task_id": top[1],
            "task_name": top[2],
            "priority": top[0]
        }

    def extract_max(self):
        """Extract highest priority task. O(log n)"""
        return self.extract_top()

    def extract_min(self):
        """Extract lowest priority task. O(log n)"""
        return self.extract_top()

    def change_key(self, task_id, new_priority):
        """
        Change priority of existing task. O(log n)
        """
        if task_id not in self.position:
            raise KeyError("Task not found")

        i = self.position[task_id]
        old = self.heap[i][0]

        self.heap[i][0] = new_priority

        if self.mode == "max":
            if new_priority > old:
                self._bubble_up(i)
            else:
                self._bubble_down(i)
        else:
            if new_priority < old:
                self._bubble_up(i)
            else:
                self._bubble_down(i)

    def increase_key(self, task_id, new_priority):
        """
        Increase task priority. O(log n)
        """
        self.change_key(task_id, new_priority)

    def decrease_key(self, task_id, new_priority):
        """
        Decrease task priority. O(log n)
        """
        self.change_key(task_id, new_priority)


# ---------------- Testing ----------------

if __name__ == "__main__":

    pq = PriorityQueue(mode="max")

    pq.insert(1, "Email", 3)
    pq.insert(2, "Meeting", 8)
    pq.insert(3, "Coding", 5)

    print("Extract:", pq.extract_max())

    pq.increase_key(1, 10)

    print("Extract:", pq.extract_max())
    print("Extract:", pq.extract_max())

    print("Is empty?", pq.is_empty())
