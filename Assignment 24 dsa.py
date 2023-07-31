def find_closest_elements(arr, k, x):
    left, right = 0, len(arr) - k

    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]

print(find_closest_elements([1, 2, 3, 4, 5], 4, 3))
# Output: [1, 2, 3, 4]

print(find_closest_elements([1, 2, 3, 4, 5], 4, -1))
# Output: [1, 2, 3, 4]
