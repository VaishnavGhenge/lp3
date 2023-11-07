import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pivot_index = low + (high - low) // 2
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = partition(arr, low, high)
        deterministic_quick_sort(arr, low, pivot - 1)
        deterministic_quick_sort(arr, pivot + 1, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot - 1)
        randomized_quick_sort(arr, pivot + 1, high)

def analyze_sorting_algorithm(sort_function, algorithm_name, array_sizes):
    for size in array_sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]
        start_time = time.time()
        sort_function(arr, 0, size - 1)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{algorithm_name} Sort (Array size {size}): {execution_time:.6f} seconds")

if __name__ == '__main__':
    array_sizes = [100, 1000, 10000, 100000]  # Adjust array sizes as needed

    print("Performance analysis of Deterministic Quick Sort:")
    analyze_sorting_algorithm(deterministic_quick_sort, "Deterministic", array_sizes)

    print("\nPerformance analysis of Randomized Quick Sort:")
    analyze_sorting_algorithm(randomized_quick_sort, "Randomized", array_sizes)
