class Stack:
    
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self,val):
        self.stack.append(val)
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            return "Empty"
        self.size -= 1
        return self.stack.pop()
        
    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.stack[-1]
        
    def is_empty(self):
        return len(self.stack) == 0
        
    def display(self):
        if self.is_empty():
            return "Empty"
        print(self.stack)
        
    def remove_middle(self):
        mid = self.size//2
        c = 0
        temp = 0
        temp_s = []
        while self.stack:
            if c == mid:
                temp = self.pop()
            else:
                temp_s.append(self.pop())
            c += 1
        while temp_s:
            self.push(temp_s.pop())
        return f"Removed {temp} from middle"
        
s = Stack()
s.push(4)
s.push(8)
s.push(2)
s.push(5)
s.push(7)
s.display()
print(s.remove_middle())
s.display()