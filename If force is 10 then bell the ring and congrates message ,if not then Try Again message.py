mass = float(input("Mass = "))
acc = float(input("Acceleration = "))

f = mass*acc


if(f==10):  
    print("\a")
    name = str(input("Enter your name,hero : "))
    print("You are right " + str(name))
else:
    print("Required Force Is 10 N, Try again")