def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Get user input for the array
arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))

# Sort the array using quicksort
sorted_arr = quicksort(arr)

# Print the sorted array
print("Sorted array is:", sorted_arr)
