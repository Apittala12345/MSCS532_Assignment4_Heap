"""
Assignment 4 - Heapsort Implementation (Max-Heap)

Heapsort steps:
1) Build a max-heap from the array (O(n))
2) Repeatedly swap the max (root) with last element and heapify (O(n log n))

Overall time complexity: O(n log n)
Space complexity: O(1) extra (in-place), ignoring recursion stack (we use iterative heapify)
"""


def heapify(arr, n, i):
    """
    Maintain max-heap property for subtree rooted at index i.
    n is the heap size.

    Time: O(log n) in worst case
    """
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else:
            break


def build_max_heap(arr):
    """
    Convert array into a max-heap.

    Time: O(n)
    """
    n = len(arr)
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heapsort(arr):
    """
    Sorts the array in ascending order using heapsort (in-place).

    Time: O(n log n)
    Space: O(1) extra
    """
    a = arr.copy()  # keep original safe; remove .copy() if you want true in-place
    n = len(a)

    build_max_heap(a)

    # Extract elements one by one
    for end in range(n - 1, 0, -1):
        # Move current root (max) to end
        a[0], a[end] = a[end], a[0]
        # Heapify reduced heap
        heapify(a, end, 0)

    return a


if __name__ == "__main__":
    tests = [
        [],
        [5],
        [3, 1, 2, 5, 4],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [2, 2, 2, 2, 2],
        [10, -1, 7, 3, 3, 0],
    ]

    for t in tests:
        sorted_arr = heapsort(t)
        print("Original:", t)
        print("Heapsort:", sorted_arr)
        print("Python  :", sorted(t))
        print("-" * 40)
