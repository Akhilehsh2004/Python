def check_relation(a, b):
    if a == b:
        return 0
    if a > b:
        return 1
    if a < b:
        return -1

# Declare the variables and call the function
a = 3
b = 2

# Call the function and store the result
res = check_relation(a, b)

# Check the result and print the appropriate message
if res == 0:
    print("a is equal to b")
elif res == 1:
    print("a is greater than b")
elif res == -1:
    print("a is less than b")
