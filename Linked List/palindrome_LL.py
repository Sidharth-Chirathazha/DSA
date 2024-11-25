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

    def insert_list(self,data_list):
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

    def reverse(self,head):
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
    
    def is_palindrome(self):
        if self.head == None or self.head.next == None:
            return True
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first_half = self.head
        second_half = self.reverse(slow)

        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

ll = LinkedList()
ll.insert_list([1,2,2,1])

ll.print()
print(ll.is_palindrome())
 