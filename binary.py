def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    
    # If the element is not present in the list
    return -1

# Example usage
sorted_list = [3, 7, 11, 15, 19]
target_number = 10
index = binary_search(sorted_list, target_number)

if index != -1:
    print(f"The number {target_number} is found at index {index}.")
else:
    print(f"The number {target_number} is not found in the list.")