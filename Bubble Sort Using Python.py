def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)

# Main code
arr = [12, 53, 61, 70, 14, 88, 10, 5, 23, 1, 1000, 100]
bubbleSort(arr)

for elem in arr:
    print(elem, end="       ")