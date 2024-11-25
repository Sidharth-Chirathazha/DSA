
#STACK USING ONE QUEUE

class QueueToStack:

    def __init__(self):
        self.q = []

    def push(self,val):
        self.q.append(val)

    def pop(self):
        if len(self.q) == 0:
            return "Empty"
        for i in range(len(self.q)-1):
            self.push(self.q.pop(0))
        return self.q.pop(0)
    
    def peek(self):
        if len(self.q) == 0:
            return "Empty"
        return self.q[-1]
    

qs = QueueToStack()
qs.push(3)
qs.push(5)
qs.push(2)
qs.push(4)
print(qs.peek())
print(qs.pop())
