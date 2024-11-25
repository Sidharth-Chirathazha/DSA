class PriorityQueue:
    
    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self,val,priority):
        element = (priority,val)

        if self.queue == None:
            self.queue.append(element)
        else:
            inserted = False
            for i in range(len(self.queue)):
                if self.queue[i][0] > priority: # Higher priority means smaller value, that's why we are checking if the tuple first val is greater than priority
                    self.queue.insert(i,element)
                    inserted = True
                    break
            if not inserted:
                self.queue.append(element)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return "Empty"
        else:
            self.size -= 1
            return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if self.is_empty():
            return "Empty"
        else:
            return self.queue[-1]
        
    def display(self):
       print(self.queue)
        

pq = PriorityQueue()

pq.enqueue(5,3)
pq.enqueue(4,2)
pq.enqueue(7,4)
pq.enqueue(9,1)
pq.display()