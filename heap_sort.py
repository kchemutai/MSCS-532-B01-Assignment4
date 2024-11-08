import time
import random

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)  # Heapify the root

def heapsort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

def test_heapsort():
    test_cases = [
        {
            "name": "Empty Array",
            "input": [],
            "expected": []
        },
        {
            "name": "Single Element",
            "input": [1],
            "expected": [1]
        },
        {
            "name": "Two Elements",
            "input": [2, 1],
            "expected": [1, 2]
        },
        {
            "name": "Small Random Array",
            "input": [3, 1, 4, 1, 5, 9, 2, 6],
            "expected": sorted([3, 1, 4, 1, 5, 9, 2, 6])
        },
        {
            "name": "Sorted Array",
            "input": [1, 2, 3, 4, 5, 6, 7, 8],
            "expected": [1, 2, 3, 4, 5, 6, 7, 8]
        },
        {
            "name": "Reverse Sorted Array",
            "input": [8, 7, 6, 5, 4, 3, 2, 1],
            "expected": [1, 2, 3, 4, 5, 6, 7, 8]
        },
        {
            "name": "Large Random Array",
            "input": random.sample(range(1, 1000), 100),
            "expected": sorted(random.sample(range(1, 1000), 100))
        }
    ]

    for case in test_cases:
        arr = case["input"].copy()
        heapsort(arr)
        result = "Passed" if arr == case["expected"] else "Failed"
        print(f"{case['name']} - {result}")
        print(f"After Heapsort: {arr}\n")

#test_heapsort()
