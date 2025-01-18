age = int(input("Enter your Age "))

vote = int(18)

if (age  > vote):
    print("You Are Eligible For Vote ")
    
else:
     wait = 18 - age
     print("You Have To wait For Another " + str(wait) + " Years To Cast Your Vote")
    