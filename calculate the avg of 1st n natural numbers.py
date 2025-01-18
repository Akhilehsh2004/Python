n = int(input("Enter the value of n : "))
avg = 0.0
s = 0

for i in range(1,n+1):
    s = s+i
    avg = s/i
    
    print("The sum of the 1st",n,"natural numbers is",s)
    print("The avg of the 1st",n,"natural numbers is",avg)
