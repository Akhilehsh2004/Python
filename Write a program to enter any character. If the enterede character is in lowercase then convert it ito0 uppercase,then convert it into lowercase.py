ch = input("Enter any character : ")
if(ch >= 'A' and ch <='z'):
    ch = ch.lower()
    print("The entred character was in uppercase. In lowercase it is : " + ch)
else:
    ch = ch.upper()
    print("The entred character was in lowercase. In uppercase it is : " + ch)