class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.append(val)

    def dequeue(self):
        if self.queue == None:
            return "The queue is empty"
        else:
            return self.queue.pop(0)
        
    def peek(self):
        if self.queue == None:
            return "The queue is empty"
        else:
            return self.queue[0]
        
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    

q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(6)
q.enqueue(2)
print(q.dequeue())
print(q.peek())