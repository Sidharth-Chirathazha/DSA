class Node:

    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data,None)

    def get_length(self):
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
        return count

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def print(self):
        if self.head == None:
            print("Linked list is empty")
        cur = self.head
        llstr = ''
        while cur:
            llstr += str(cur.data) + '-->'
            cur = cur.next
        print(llstr)
    
    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def insert_at_middle(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return

        if self.get_length() == 1:
            self.insert_at_end(data)
            return

        cur = self.head
        count = 0
        while cur:
            if count == (self.get_length()//2)-1:
                cur.next = Node(data,cur.next)
                break
            cur = cur.next
            count += 1

if __name__ == '__main__':

    ll = LinkedList()
    ll.insert_values([2,1])
    ll.insert_at_middle(5)
    ll.print()
    # ll.reverse()
    # ll.print()