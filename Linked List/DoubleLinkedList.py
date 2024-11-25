class Node:

    def __init__(self,data,next,prev):
            self.data = data
            self.next = next
            self.prev = prev


class DoubleLinkedList:
      
    def __init__(self):
        self.head = None

    def get_last_node(self):
         
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_beginning(self,data):
         
         if self.head == None:
              node = Node(data,self.head,None)
              self.head = node
         else:
              node = Node(data,self.head,None)
              self.head.prev = node
              self.head = node

    def print_forward(self):
         if self.head == None:
              print("The Double Linked List is empty")
              return
         itr = self.head
         llstr = ''
         while itr:
              llstr += str(itr.data) + '<--->'
              itr = itr.next

         print("Link list in forward: ", llstr)

    def print_backward(self):
         if self.head == None:
              print("The Double Linked List is empty")
              return
         itr = self.get_last_node()
         llstr = ''
         while itr:
              llstr += str(itr.data) + '<--->'
              itr = itr.prev

         print("Link list in reverse: ", llstr)
    
    def insert_at_end(self,data):
         if self.head == None:
            self.head = Node(data,None,None)
            return
         
         itr = self.head
         while itr.next:
              itr = itr.next
         itr.next = Node(data,None,itr)

    def insert_values(self,data_list):
         self.head = None
         for data in data_list:
              self.insert_at_end(data)

    def get_length(self):
         itr = self.head
         count = 0
         while itr:
              itr = itr.next
              count += 1
         return count

    def insert_at(self,index,data):
         
         if index < 0 or index > self.get_length():
              raise Exception("Invalid Index")
         if index == 0:
              self.insert_at_beginning(data)
         
         itr = self.head
         count = 0
         while itr:
              if count == index-1:
                   node = Node(data,itr.next,itr)
                   if node.next:
                        node.next.prev = node
                   itr.next = node
                   break
              itr = itr.next
              count += 1
     
    def remove_at(self,index):
         if index<0 or index>=self.get_length():
              raise Exception("Invalid Index")
         if index == 0:
              self.head = self.head.next
              self.head.prev = None
              return
         
         itr = self.head
         count = 0
         while itr:
              if count == index:
                   itr.prev.next = itr.next
                   if itr.next:
                        itr.next.prev = itr.prev
                   break
              itr = itr.next
              count += 1

    def insert_after(self,data_after,data_to_insert):
         
         if self.head == None:
              return
         if self.head == data_after:
              self.head.next = Node(data_to_insert,self.head.next,self.head) 
              return
         itr = self.head
         while itr:
              if itr.data == data_after:
                   node = Node(data_to_insert,itr.next,itr)
                   if node.next:
                        node.next.prev = node
                   itr.next = node
                   break
              itr = itr.next

if __name__ == '__main__':
     
     dll = DoubleLinkedList()
     dll.insert_at_beginning(5)
     dll.insert_at_beginning(6)
     dll.insert_at_end(10)
     dll.insert_values([9,5,3,10,8,12])
     # dll.insert_at(4,13)
     # dll.remove_at(5)
     dll.insert_after(10,11)
     dll.print_forward()
     dll.print_backward()
     print(dll.get_length())
         