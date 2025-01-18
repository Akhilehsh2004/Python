def fibonachi(n):
    if n<=0:
        return "Invalid Input"
    elif n==1:
        return 0 
    elif n==2:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)  
num=int(input("Enter the number = ")) 

if num <=0:
    
   print("Kindly Enter Any Valid Number positive grater thhan zero")
    
    
    
else:
   print("fibonachi Series")
   
   for i in range(1, num+1):
          print(fibonachi(i), end="  ")