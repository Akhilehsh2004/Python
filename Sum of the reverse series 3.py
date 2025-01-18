n = int(input("Enter the value of n = "))

sum = 0.0

for i in range(1,n+1):
    
    OP = float(i**i)/i
    sum = sum + OP
    
print("Answer = ", sum)