class Stack:
    
    def __init__(self):
        
        self.s = []
    
    def push(self,val):
        self.s.append(val)
    
    def pop(self):
        if self.is_empty():
            return "Empty"
        return self.s.pop()
        
    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.s[-1]
    
    def is_empty(self):
        return len(self.s) == 0
        
    def display(self):
        if self.is_empty():
            return "Empty"
        print(self.s)
        
    def reverse(self):
        if self.is_empty():
            return "Empty"
        temp_stack = []
        while self.s:
            temp_stack.append(self.pop())
        self.s = temp_stack
        
s = Stack()
s.push(5)
s.push(4)
s.push(9)
s.push(3)
s.display()
s.reverse()
s.display()
print(s.pop())