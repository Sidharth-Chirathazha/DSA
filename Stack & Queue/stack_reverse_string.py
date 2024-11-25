class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        return self.stack[0]
    
    # def size(self):
    #     return len()

def reverse(string):

    stack = Stack()

    for i in string:
        stack.push(i)

    rev_s = ''
    while not stack.is_empty():
        rev_s += stack.pop()

    return rev_s

s = 'Hello World'

print(reverse(s))

