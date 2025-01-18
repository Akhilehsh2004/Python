n = int(input("Ente rthe number : "))
s = 0
num = n

while(n>0):
    r = n % 10
    s = s + (r**3)
    n = n/10
    
if(s==num):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")