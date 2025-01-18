def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap after finding the minimum element in the rest of the array
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

array = [18, 34, 12, 10, 12, 5, 23, 7]
sorted_array = selection_sort(array)
print("Sorted Array:", sorted_array)
                                    
                                             