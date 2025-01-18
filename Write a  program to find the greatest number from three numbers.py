a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

if((a > b) and (a > c)):
    print("1st number is the largest ")
elif((b > a) and (b > c)):
    print("2nd number is the largest ")
else:
    print("3rd number is the largest ")

