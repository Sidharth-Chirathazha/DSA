class BinarySearchTree:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]
        
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
    
        return elements

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def second_largest(self):

        if self.left and not self.right:
            return self.left.find_max()
        
        cur = self
        parent = None

        while cur.right:
            parent = cur
            cur = cur.right

        if cur.left:
            return cur.left.find_max()
        
        return parent.data if parent else None
    
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left == None and self.right == None:
                return None
            elif self.left == None:
                return self.right
            elif self.right == None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
             
        return self


def build_tree(elements):

    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

lst = [5,9,2,4,10,15,7,1,12,5]
nums_tree = build_tree(lst)
print(nums_tree.in_order_traversal())
# print(nums_tree.search(10))
# print(nums_tree.pre_order_traversal())
# print(nums_tree.post_order_traversal())
# print(nums_tree.find_max())
# print(nums_tree.find_min())
# print(nums_tree.calculate_sum())
print(nums_tree.second_largest())
print(nums_tree.in_order_traversal())