class Node:

    def __init__(self,item):
        self.item = item
        self.next = None

class StackLinkedList:

    def __init__(self):
        self.top = None

    def push(self,item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top == None:
            return "The stack is empty"
        popped_value = self.top.item
        self.top = self.top.next
        return popped_value
    
    def peek(self):
        if self.top == None:
            return "The stack is empty"
        return self.top.item
    
    def is_empty(self):
        
        if self.top == None:
            return True
        else:
            return False
    
    def size(self):
        if self.top == None:
            return "The stack is empty"
        cur = self.top
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count
    
    def print_stack(self):
        if self.top == None:
            return "The stack is empty"
        cur = self.top
        llstr = ''
        while cur:
            llstr += str(cur.item)  + '--'
            cur = cur.next
        print(llstr)

stack_ll = StackLinkedList()
stack_ll.push(5)
stack_ll.push(6)
stack_ll.push(1)
stack_ll.push(8)
stack_ll.print_stack()
print(stack_ll.pop())
print(stack_ll.peek())
print(stack_ll.is_empty())
print(stack_ll.size())