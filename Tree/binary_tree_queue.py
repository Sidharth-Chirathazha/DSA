class Node:

    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):

        self.root = None

    def insert(self,key):

        new_node = Node(key)
        if self.root == None:
            self.root = new_node
            return
        
        queue = [self.root]

        while queue:

            node = queue.pop(0)
            if node.left == None:
                node.left = new_node
                return
            else:
                queue.append(node.left)

            if node.right == None:
                node.right = new_node
                return
            else:
                queue.append(node.right)

    def inorder(self,node):
        elements = []
        if node.left:
            elements += self.inorder(node.left)
        # print(node.val,end=" ")
        elements.append(node.val)
        if node.right:
            elements += self.inorder(node.right)
        return elements

    def max_depth(self):
        if self.root == None:
            return 0
        queue = [self.root]
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
    
def is_same(node1,node2):
    
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None or node1.val != node2.val:
        return False
    return (is_same(node1.left,node2.left) and is_same(node1.right,node2.right))


t = BinaryTree()
t1 = BinaryTree()
t.insert(9)
t.insert(5)
t.insert(10)
t.insert(2)
t.insert(6)
t.insert(18)
t.insert(3)

t1.insert(9)
t1.insert(5)
t1.insert(10)
t1.insert(2)
t1.insert(6)
t1.insert(18)
t1.insert(3)

print(t1.inorder(t1.root))
print(is_same(t.root,t1.root))
print("\n",t.max_depth())
