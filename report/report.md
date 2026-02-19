# Assignment 4: Heap Data Structures: Implementation, Analysis, and Applications
**Course:** MSCS-532 Algorithms and Data Structures  
**Student:** Anusha Pittala  
**Term:** 2026 Spring  

---

## 1. Introduction
Heap data structures are important because they provide an efficient way to always access the largest or smallest element. This assignment implements Heapsort and a heap-based Priority Queue, then demonstrates a task scheduling simulation. The goal is to connect heap theory (heap property and time complexity) to real behavior in scheduling.

---

## 2. Heapsort Implementation

### 2.1 Design and Implementation
Heapsort was implemented using a **max-heap**:
1. Build a max-heap from the array.
2. Swap the root (maximum) with the last element.
3. Reduce heap size and heapify again.
4. Repeat until the array is sorted.

### 2.2 Time Complexity
- Heapify: **O(log n)**  
- Build heap: **O(n)**  
- Extract max n times: **n × O(log n) = O(n log n)**  

**Total time complexity:** **O(n log n)**  
**Space complexity:** **O(1)** extra (in-place style), ignoring minor overhead.

---

## 3. Priority Queue Using a Binary Heap

### 3.1 Data Structure Choice
A binary heap was used because it supports fast insertion and fast extraction of the highest-priority task.

### 3.2 Operations and Complexity

#### is_empty()
Checks if the heap has 0 elements.  
**Time:** O(1)

#### insert(task, priority)
Adds the task at the end and bubbles it up to maintain heap property.  
**Time:** O(log n)

#### extract_max/min()
Removes and returns the root element (highest or lowest priority).  
Steps: swap root with last, remove last, bubble down.  
**Time:** O(log n)

#### increase/decrease_key(task, new_priority)
Updates an existing task’s priority and repositions it:
- Higher priority → bubble up
- Lower priority → bubble down  
**Time:** O(log n)

---

## 4. Scheduler Simulation Results
A simple scheduler was implemented with the max-heap priority queue. Tasks with higher priority were executed first. During the simulation, one task’s priority was increased and another was decreased. The scheduler immediately reflected those changes, which shows why heaps are useful in real scheduling systems.

Observed behavior:
- Highest-priority tasks ran first.
- Priority updates changed the execution order.
- Low-priority tasks naturally moved to the end.

---

## 5. Conclusion
This assignment showed that heaps are efficient and practical. Heapsort provided O(n log n) sorting by using a max-heap. The priority queue supported insert, extract, and priority updates efficiently, and it worked well in the scheduler simulation. Overall, heap-based structures are a good fit for systems that need frequent access to max/min elements and dynamic priority changes.

---

## References
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
