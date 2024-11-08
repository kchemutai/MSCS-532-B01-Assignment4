import time
import random

from heap_sort import heapsort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return time.time() - start_time

def compare_algorithms():
    sizes = [1000, 5000, 10000]  # Test with different input sizes
    sorts = {
        'Heapsort': heapsort,
        'Quicksort': quicksort,
        'Mergesort': mergesort
    }
    distributions = {
        'Sorted': lambda size: list(range(size)),
        'Reverse Sorted': lambda size: list(range(size, 0, -1)),
        'Random': lambda size: [random.randint(0, size) for _ in range(size)]
    }

    for size in sizes:
        print(f"\nArray Size: {size}")
        for dist_name, generate in distributions.items():
            print(f"\nDistribution: {dist_name}")
            arr = generate(size)
            for sort_name, sort_func in sorts.items():
                if sort_name == 'Heapsort':
                    arr_copy = arr.copy()
                    time_taken = measure_time(sort_func, arr_copy)
                else:
                    time_taken = measure_time(lambda x: sort_func(x), arr)
                print(f"{sort_name}: {time_taken:.6f} seconds")

compare_algorithms()
