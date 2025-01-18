math = int(input("Enter your Maths marks = "))
science = int(input("Enter your Science marks = "))
dsa = int(input("Enter your DSA marks = "))
OS = int(input("Enter your OS marks = "))

total = math + science + dsa + OS

avg = float(total)/4

print("Total = ", total, "\t Aggregate = ", avg)

if(avg >= 75):
    print("Distinction")
elif(avg >=60 and avg< 75):
    print("First Division")
elif(avg >=50 and avg< 60):
    print("Second Division")
elif(avg >=60 and avg< 75):
    print("Third Division")
else:
    print("Fail ! ")