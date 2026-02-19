"""
Assignment 4 - Scheduler Simulation using Priority Queue (Heap)

Goal:
- Simulate a simple task scheduler where tasks have priorities.
- Higher priority tasks run first (max-heap).
- Demonstrate:
    - insert tasks
    - extract_max (run next task)
    - increase_key / decrease_key (priority change)
    - is_empty check

This simulation is simple and easy to explain in the report.
"""

from priority_queue import PriorityQueue


def run_scheduler_simulation():
    print("\n===== TASK SCHEDULER SIMULATION (MAX-HEAP) =====\n")

    # Create a scheduler priority queue (max-heap: highest priority runs first)
    scheduler = PriorityQueue(mode="max")

    # Step 1: Insert tasks (task_id, task_name, priority)
    print("Step 1: Adding tasks to scheduler...\n")
    scheduler.insert(1, "Submit Assignment", 9)
    scheduler.insert(2, "Attend Class", 7)
    scheduler.insert(3, "Email Professor", 5)
    scheduler.insert(4, "Work on Project", 8)
    scheduler.insert(5, "Break / Rest", 2)

    print("Tasks added. Scheduler is empty?", scheduler.is_empty(), "\n")

    # Step 2: Run the highest priority task
    print("Step 2: Run highest priority tasks...\n")
    task = scheduler.extract_max()
    print("Running:", task)

    task = scheduler.extract_max()
    print("Running:", task)

    # Step 3: Priority changes (simulate urgent update)
    print("\nStep 3: Priority update (increase/decrease_key)...\n")
    print("Email Professor becomes urgent -> increase priority to 10")
    scheduler.increase_key(3, 10)

    print("Break / Rest becomes less important -> decrease priority to 1")
    scheduler.decrease_key(5, 1)

    # Step 4: Continue scheduling until empty
    print("\nStep 4: Continue running tasks until scheduler is empty...\n")
    while not scheduler.is_empty():
        next_task = scheduler.extract_max()
        print("Running:", next_task)

    print("\nAll tasks completed. Scheduler is empty?", scheduler.is_empty())


if __name__ == "__main__":
    run_scheduler_simulation()
