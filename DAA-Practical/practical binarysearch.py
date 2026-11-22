def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1



sorted_nums = [10, 20, 30, 40, 50, 70, 80]
target_val = 70


result = binary_search_iterative(sorted_nums, target_val)


if result != -1:
    print(f"Binary Search (Iterative): Element {target_val} found at index {result}")
else:
    print("Element not found")