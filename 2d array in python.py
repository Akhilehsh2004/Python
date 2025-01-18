# Python program to print elements of a 2D array

# 2D array declaration
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Printing elements of the 2D array
print("Elements Of The 2D array:")
for i in range(3):
    for j in range(3):
        print(array[i][j], end="  ")
    print()
