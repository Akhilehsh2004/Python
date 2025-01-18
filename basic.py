print(min(12,34,2,1,0))

print(max(12,34,2,1,0))

print(hex(26))


print(hex(260))

print(oct(260))

print(bin(260))


print (2 ** 4)

# Factorial Of A Number

import math 
print(math.factorial(5))


import math
print(math.sqrt(16))


import math
print (math.log10(1))


import math
print (math.exp(2))



import math
print(math.degrees(math.pi))

# Multi Line Sting (Using Triple Quotes)

print('''JAi Hind
      How Are You''')

# Use of string without Print Function

# String Literal Concatenation

print('Jai Hind' '......' 'Myself Akhilesh Pant')

# Unnicode String

print(u"Kese Ho")


print("What's Your Name ?")


      
      
print('What\'s Your Name ?')

print("The boy replies, \"My name is Aaditya.\"")


# Next Line: \n

print("Today Is 15 August.\nIndia became independent on this day")

# /t inserts tab in a string

print("Hello All. \t Welcome to the world of python.")

# If a single blackslach(\) at the end of th eline is added, rhen it indicatws that the string is continued in the next line but no ne line is added,then it indicates that sting is continued in the next line but no new line is added otherwise.

print(" Jai Hind, Myself Akhilesh Pant. \
Dream to serve in kashmir")

print("\\") 
print("\'")
print("\"")


print("\a")  # Output: Ring Bell

print("Hello\fWorld")

print("\o56") # Print the Octal Value

# Raw strings (If u wnat display the exactly the sam then do this)

print(R"What\'s your name")

# Commands to display 'Hello' left-justified, , and center-aligned in a field width of 30 Characters

print(format('Hello', '<30')) # left-justified


print(format('Hello', '>30')) # right-justified 


print(format('Hello', '^30')) # center-aligned


print('Hello', format('-','-<10'), 'World')


str1 = "Jai "
str2 = "Hind"


str1 += str2
print(str1)