# Function to create an empty stack. It initializes the size of the stack as 0.
def createStack():
    stack = []
    return stack

# Function to determine the size of the stack.
def size(stack):
    return len(stack)

# Stack is empty if the size is 0.
def isEmpty(stack):
    return size(stack) == 0

# Function to add an item to the stack (Push). It increases size by 1.
def push(stack, item):
    stack.append(item)  

# Function to remove an item from the stack (Pop). It decreases size by 1.
def pop(stack):
    if isEmpty(stack):
        return None
    return stack.pop()

# A stack-based function to reverse a string.
def reverse(string):
    n = len(string)
    
    # Create an empty stack.
    stack = createStack()
    
    # Push all characters of the string to the stack.
    for i in range(n):
        push(stack, string[i])
    
    # Making the stack empty since all characters are saved in the stack.
    reversed_string = ""
    
    # Pop all characters from the stack and put them back into the strinAg in reversed order.
    while not isEmpty(stack):
        reversed_string += pop(stack)
    
    return reversed_string

# Driver program to test the above function.
user_input = input("Enter a string to reverse: ")
reversed_string = reverse(user_input)
print("Reversed String Is: " + reversed_string)