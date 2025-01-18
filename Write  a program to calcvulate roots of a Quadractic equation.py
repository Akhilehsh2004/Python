a = int(input("Enter the values of a : "))
b = int(input("Enter the values of b : "))
c = int(input("Enter the values of c : "))

D = (b**2)-(4*a*c)

deno = 2*a

if(D > 0):
    print("Real Roots")
    root1 = (-b + D**0.5)/deno
    root2 = (-b - D**0.5)/deno
    print(" 1st Root Is = ", root1, "\t2nd Root Is = ", root2)
elif(D == 0):
    print("Equal Roots")
    root1 = -b/deno
    print("Root 1 & Root 2 = ", root1)
else:
    print("Imaginary Roots")