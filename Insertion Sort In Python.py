def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

# Main code
arr = [12, 53, 61, 70, 14, 88, 10, 5, 23, 1, 1000, 100]
insertionSort(arr)

for elem in arr:
    print(elem, end="       ")
           