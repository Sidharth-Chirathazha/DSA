class StackToQueue:

    def __init__(self):
        
        self.s1 = []
        self.s2 = []

    def enqueue(self,val):

        while self.s1:
             self.s2.append(self.s1.pop())
        self.s1.append(val)

        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1) == 0:
            return "Empty"

        return self.s1.pop()
    
    def top(self):
        if len(self.s1) == 0:
            return "Empty"
        
        return self.s1[-1]
    
sq = StackToQueue()
sq.enqueue(4)
sq.enqueue(9)
sq.enqueue(3)
sq.enqueue(2)
print(sq.top())
print(sq.dequeue())