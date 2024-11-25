from collections import deque

class QueueToStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.size = 0

    def push(self,val):
        
        self.q2.append(val)

        while self.q1:
            self.q2.append(self.q1.pop(0))

        self.q1,self.q2 = self.q2,self.q1
        self.size += 1

    def pop(self):
        if self.q1 == None:
            return "Empty"
        self.size -= 1
        return self.q1.pop(0)
    
    def top(self):
        if self.q1 == None:
            return "Empty"
        return  self.q1[0]
    
    def display(self):
        print(self.q1)
    
qs = QueueToStack()
qs.push(9)
qs.push(4)
qs.push(3)
qs.push(5)

print(qs.pop())
qs.display()