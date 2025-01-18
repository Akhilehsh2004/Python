def increment(y):
    return (lambda x: x+1)(y)
a = 100
print("a = ",a)
print("a after incrementing = ")
b=increment(a)
print(b)