class Node:

    def __init__(self,key):
        self.data = key
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

        q = [self.root]

        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if node.left == None:
                    node.left = new_node
                    return
                else:
                    q.append(node.left)
                
                if node.right == None:
                    node.right = new_node
                    return
                else:
                    q.append(node.right)

    def invert_tree(self,root):
        if root == None:
            return None
        root.left,root.right = root.right,root.left

        self.invert_tree(root.left)
        self.invert_tree(root.right)

    
    def preorder(self,root):
        arr = []
        if root:
            arr.append(root.data)
            if root.left:
                arr.extend(self.preorder(root.left))
            if root.right:
                arr.extend(self.preorder(root.right))

        return arr
    

    
def is_same_tree(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    return (is_same_tree(root1.left,root2.left) and is_same_tree(root1.right,root2.right))
    

def is_bst(node,min=float('-inf'),max=float('inf')):

    if node == None:
        return True
    
    if not min < node.data < max:
        return False
    
    return (is_bst(node.left,min,node.data) and is_bst(node.right,node.data,max))


bt = BinaryTree()
bt1 = BinaryTree()

for i in [15,10,20,5,12,17]:
    bt.insert(i)

for i in [15,10,20,5,12,17]:
    bt1.insert(i)

# bt.invert_tree(bt.root)

print(is_bst(bt.root))

print(bt.preorder(bt.root))
print(is_same_tree(bt.root,bt1.root))



