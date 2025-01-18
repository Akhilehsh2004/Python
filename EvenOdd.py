def ans(n):
    
    if(n % 2==0):
        return 1
    else:
        return -1
    
n = int(input("Enter Your Number Sir = "))
flag = ans(n)

if(flag==1):
      print("Number is Even")
elif(flag==-1):
    print("Number is Odd")

