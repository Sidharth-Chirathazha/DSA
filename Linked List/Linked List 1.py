
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
        
    def display(self):
        if self.head == None:
            print("Linked list is empty")
            return
        cur = self.head
        llstr = ''
        while cur:
            llstr += str(cur.data) + '-->'
            cur = cur.next
        print(llstr)
    
    def insert_list(self,data_list):
        for data in data_list:
            self.append(data)
            
    def reverse(self):
        if self.head == None:
            return
        cur = self.head
        prev = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev
        
    def remove_dup(self):
        cur = self.head
        while cur:
            while cur.next and cur.next.data == cur.data:
                cur.next = cur.next.next 
            cur = cur.next

    def remove_dup_unsorted(self):
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
            
        


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_list([1,1,1,2,3,4,4,6,7,7,8,1])
    ll.remove_dup_unsorted()
    ll.display()