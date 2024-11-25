class Stack:

    def __init__(self):

        self.s1 = []
        self.s2 = []

    def is_empty(self):
        return len(self.s1) == 0
    
    def push(self,val):
        self.s1.append(val)

    def pop(self):
        if self.s1 == None:
            return "Stack is empty"
        popped_value = self.s1.pop()
        return popped_value
    
    def top(self):
        if self.s1 == None:
            return "Stack is empty"
        return self.s1[-1]
    
    def print_stack(self):
        if self.s1 == None:
            return "Stack is empty"
        s_str = ''
        for val in reversed(self.s1):
            s_str += str(val) + '--'
        print(s_str)

    def sort_stack(self):
        while self.s1:
            temp = self.pop()

            while self.s2 and self.s2[-1] > temp:
                self.push(self.s2.pop())
            
            self.s2.append(temp)

        while self.s2:
            self.push(self.s2.pop())

        self.print_stack()



stack = Stack()
stack.push(9)
stack.push(6)
stack.push(4)
stack.push(5)
stack.print_stack()
stack.sort_stack()
