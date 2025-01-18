n = int(input("Enter the value of n = "))

sum = 0

for i in range(1, n+1):
    
    OP = (i**3)
    sum = sum + OP
    
print("Answer = ", sum)