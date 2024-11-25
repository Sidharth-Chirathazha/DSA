

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
        else:
            node = Node(data,self.head)
            self.head = node
    
    def insert_list(self,data_list):
        for data in data_list:
            self.append(data)
            
    def print(self):
        if self.head == None:
            print("Empty Linked List")
            return
        cur = self.head
        llstr = ''
        while cur:
            llstr += str(cur.data) + '-->'
            cur = cur.next
        print(llstr)
        
    def reverse_half(self,head):
        if self.head == None or head is None:
            return
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
        
    def check_palindrome(self):
        if self.head == None:
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        first_half = self.head
        second_half = self.reverse_half(slow)
        while second_half:
            if second_half.data != first_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True
        
ll = LinkedList()
ll.insert_list([2,3,4,3,2])
# ll.prepend(5)
ll.print()
print(ll.check_palindrome())