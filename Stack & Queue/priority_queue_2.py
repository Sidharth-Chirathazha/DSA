class Queue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self,val):
        self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            return "Empty"
        max_val = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max_val]:
                max_val = i

        item = self.queue[max_val]
        del self.queue[max_val]
        return item
    
    def display(self):
        print(self.queue)

q = Queue()
q.enqueue(7)
q.enqueue(3)
q.enqueue(5)
q.enqueue(9)
q.display()
print(q.dequeue())
print(q.dequeue())