class Node:

    def __init__(self,item):

        self.item = item
        self.next = None

class QueueLinkedList:

    def __init__(self):

        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self,data):
        node = Node(data)
        if self.rear == None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1
    
    def dequeue(self):
        if self.front == None:
            return "The queue is empty"
        item = self.front.item
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return item
    
    def peek(self):
        if self.front == None:
            return "The queue is empty"
        else:
            return self.front.item
    
    def get_size(self):
        return self.size
    
q_ll = QueueLinkedList()

q_ll.enqueue(9)
q_ll.enqueue(4)
q_ll.enqueue(10)
q_ll.enqueue(3)
print(q_ll.dequeue())
print(q_ll.peek())
print(q_ll.get_size())
