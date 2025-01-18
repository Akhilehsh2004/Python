def ans(hrs,min):
    
    min = hrs*60+min
    return min

h = int(input("Enter the hrs = "))
m = int(input("Enter the hrs = "))

m = ans(h,m)

print("Minutes = ",m)