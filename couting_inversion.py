def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half, left_inversions = merge_sort(left_half)
    right_half, right_inversions = merge_sort(right_half)
    
    merged, merge_inversions = merge(left_half, right_half)
    total_inversions = left_inversions + right_inversions + merge_inversions
    
    return merged, total_inversions

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    inversions = 0 

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
            inversions += len(left) - left_index
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged, inversions

arr = list(map(int, input("Enter the elements of the array (space-separated): ").split()))

sorted_arr, inversions = merge_sort(arr)

print("Sorted array:", sorted_arr)
print("Number of inversions:", inversions)
