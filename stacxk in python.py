class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)5
    
    stack.push(2)
    stack.push(3)
    
    print("Stack:", stack)
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack after pop:", stack)
    print("Is stack empty?", stack.is_empty())
    print("Stack size:", stack.size())
