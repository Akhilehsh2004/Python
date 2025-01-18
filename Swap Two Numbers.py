def swap(a,b):
    
    a,b = b,a
    return a,b
    
    
a = input("Ener the value of a = ")
b = input("Ener the value of b = ")
   
    
a,b = swap(a,b)
    
print(f"After Swapping a = {a} and b = {b}")