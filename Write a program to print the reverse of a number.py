def reverse_number(num):
    reversend_num = 0
    
    while num > 0:
        remainder = num % 10
        reversed_num = (reversed_num * 10) + remainder
        num = num // 10
        
        
    return reversed_num
    
number = int(input("Enter a numbern : "))
print("Reversed number: ", reverse_number(number))
        