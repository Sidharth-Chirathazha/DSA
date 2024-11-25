class Stack:

    def __init__(self):
        self.s = []
        self.size = 0
        self.seen = set()

    def is_empty(self):
        return len(self.s) == 0
    
    def push(self,val):
        if not val in self.seen:
            self.s.append(val)
            self.seen.add(val)
            self.size += 1
        else:
            print("Element already exists")
            return
        
    def pop(self):
        if self.is_empty():
            return "Empty"
        self.size -= 1
        return self.s.pop()
    
    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.s[-1]
    
    def display(self):
        print(self.s)
    
s = Stack()
s.push(5)
s.push(3)
s.push(6)
s.display()
s.push(6)
s.push(5)
s.display()