class Node:
    def __init__(self,key):
        self.val = key
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,key):
        if self.root == None:
            self.root = Node(key)
        else:
            self._insert(self.root,key)
    
    def _insert(self,node,key):
        if key < node.val:
            if node.left:
                self._insert(node.left,key)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self._insert(node.right,key)
            else:
                node.right = Node(key)

    def inorder(self,node):
        elements = []
        if node:
            if node.left:
                elements.extend(self.inorder(node.left))
            elements.append(node.val)
            if node.right:
                elements.extend(self.inorder(node.right))
        return elements
    
    def bfs(self):
        if self.root == None:
            return None
        q = [self.root]
        res = []
        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                res.append(node.val)
        return res
    
    def find_min(self,node):
        if node.left == None:
            return node.val
        return self.find_min(node.left)
    
    def find_max(self,node):
        if node.right == None:
            return node.val
        return self.find_max(node.right)
    
    def delete(self,node,key):
        if node == None:
            return node
        if key < node.val:
            node.left = self.delete(node.left,key)
        elif key > node.val:
            node.right = self.delete(node.right,key)
        else:
            if node.left == None and node.right == None:
                return None
            elif node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            
            min_val = self.find_min(node.right)
            node.val = min_val
            node.right = self.delete(node.right,min_val)

        return node
    
    def second_largest(self,root):
        if root.left and root.right is None:
            return self.find_max(root.left)
        node = root
        parent = None
        while node.right:
            parent = node
            node = node.right
        if node.left:
            return self.find_max(node.left)
        return parent.val if parent else None
    
    def second_smallest(self,root):
        if root.right and root.left is None:
            return self.find_min(root.right)
        node = root
        parent = None
        while node.left:
            parent = node
            node = node.left
        if node.right:
            return self.find_min(self.right)
        return parent.val if parent else None
    
    def max_depth(self,key):
        root = self.find_val(self.root,key)
        if root == None:
            return 0
        queue = [root]
        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level
    
    def find_val(self,root,key):
        if root.val == key:
            return root
        if key<root.val:
            if root.left:
                return self.find_val(root.left,key)
            else:
                return None
        else:
            if root.right:
                return self.find_val(root.right,key)
            else:
                return None

    def count_nodes(self,root):
        if root == None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)




    
tree = BST()
tree.insert(9)
tree.insert(7)
tree.insert(12)
tree.insert(4)
tree.insert(8)
tree.insert(10)
tree.insert(15)

tree.delete(tree.root,8)
print(tree.inorder(tree.root))
print(tree.bfs())
print(tree.find_max(tree.root))
print(tree.find_min(tree.root))
print(tree.second_largest(tree.root))
print(tree.second_smallest(tree.root))
print(tree.max_depth(15))
print(tree.count_nodes(tree.root))

