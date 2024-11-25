

class Stack:

    def __init__(self):
        self.container = list()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def second_largest(self):
        size = self.size()
        if size < 2:
            return "The stack as only 2 elements"
        
        largest = -1000
        second_largest = -1000
        while not self.is_empty():
            cur = self.pop()
            if cur > largest:
                second_largest = largest
                largest = cur
            elif cur > second_largest and cur < largest:
                second_largest = cur
        return second_largest

# def reverse(s):

#     stack = Stack()
#     for ch in s:
#         stack.push(ch)

#     rev_s = ''
#     while stack.size() > 0:
#         rev_s += stack.pop()

#     return rev_s

# s = 'Better days are coming'

# print(reverse(s))

stack = Stack()
stack.push(8)
stack.push(9)
stack.push(2)
stack.push(5)
stack.push(3)
print(stack.second_largest()) 
    


