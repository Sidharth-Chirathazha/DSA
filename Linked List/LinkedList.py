class Node:

    def __init__(self,data,next):

        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data,None)

    def prepend(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return
        self.head = Node(data,self.head)
        

    def insert_list(self,data_list):
        self.head = None
        for data in data_list:
            self.append(data)

    def print(self):
        if self.head == None:
            print("The linked list is empty")
            return
        cur = self.head
        llstr = ''
        while cur:
            llstr += str(cur.data) + '-->'
            cur = cur.next
        print(llstr)

    def find_middle(self):
        if self.head == None:
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def get_length(self):
        if self.head == None:
            print("The linked list is empty ")
        cur = self.head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count

    def insert_in_middle(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return
        cur = self.head
        count = 0
        while cur:
            if count == (self.get_length()//2) - 1:
                cur.next = Node(data,cur.next)
                break
            cur = cur.next
            count += 1
    
    def reverse(self):
        if self.get_length() <= 1:
            self.print()
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def remove_dup(self):
        if self.head == None:
            return
        cur = self.head
        prev = None
        seen = set()
        while cur:
            if cur.data in seen:
                prev.next = cur.next
            else:
                seen.add(cur.data)
                prev = cur
            cur = cur.next

    def remove_even(self):
        if self.head == None:
            return

        while self.head and self.head.data %2 == 0:
            self.head = self.head.next

        cur = self.head

        while cur and cur.next:
            if cur.next.data %2 == 0:
                cur.next = cur.next.next
            else:
                cur = cur.next


ll = LinkedList()
ll.insert_list([4,5,7,8,4,9,8])
ll.print()
ll.insert_in_middle(10)
ll.print()
ll.prepend(2)
ll.append(9)
ll.print()
ll.reverse()
ll.remove_dup()
ll.print()
ll.remove_even()
ll.print()