class Queue:
    
    def __init__(self):
        self.q = []
        self.size = 0
        
    def enqueue(self,val):
        self.q.append(val)
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            return "Empty"
        self.size -= 1
        return self.q.pop(0)
    
    def top(self):
        if self.is_empty(self):
            return "Empty"
        return self.q[0]
        
    def is_empty(self):
        return len(self.q) == 0
        
    def display(self):
        print(self.q)
        
    def reverse(self):
        if self.is_empty():
            return "Empty"
        stack = []
        while not self.is_empty():
            stack.append(self.dequeue())
            
        while stack:
            self.enqueue(stack.pop())
        
q = Queue()
q.enqueue(6)
q.enqueue(3)
q.enqueue(7)
q.enqueue(8)
q.display()
q.reverse()
q.display()