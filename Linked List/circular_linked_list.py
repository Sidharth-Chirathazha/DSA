class Node:

    def __init__(self,data,next):
        self.data = data
        self.next = next

class CircularLinkedList:

    def __init__(self):
        self.head = None

    def append(self,data):

        if self.head == None:
            node = Node(data,None)
            self.head = node
            node.next = self.head
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = Node(data,self.head)
    
    def print(self):

        if self.head == None:
            print("The lt is empty")
            return
        cur = self.head
        llstr = ''
        while cur:
            llstr += str(cur.data) + '-->'
            if cur.next == self.head:
                break
            cur = cur.next
        print(llstr)

    def add_list(self,data_list):
        for data in data_list:
            self.append(data)

    def prepend(self,data):
        if self.head == None:
            node = Node(data,None)
            self.head = node
            node.next = self.head
        
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        node = Node(data,self.head)
        self.head = node
        cur.next = self.head

    def remove_element(self,val):

        if self.head == None:
            return
        if self.head.data == val and self.head.next == self.head:
            self.head = None
            return
        if self.head.data == val:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next

            cur.next = self.head.next
            self.head = self.head.next
            return
        cur = self.head
        prev = None
        while cur.next != self.head :
            if cur.data == val:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
        if cur.data == val:
            prev.next = cur.next

ll = CircularLinkedList()
ll.add_list([4,5,7,8])
ll.append(10)
ll.prepend(1)
ll.prepend(0)
ll.print()
ll.remove_element(10)
ll.print()