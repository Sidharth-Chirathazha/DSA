class TreeNode:

    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()



def build_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    mobile = TreeNode('Mobile')
    headphone = TreeNode('Headphone')
    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(headphone)

    acer = TreeNode('Acer')
    lenovo = TreeNode('Lenovo')
    asus = TreeNode('Asus')
    laptop.add_child(acer)
    laptop.add_child(lenovo)
    laptop.add_child(asus)

    samsung = TreeNode('Samsung')
    apple = TreeNode('Apple')
    xiaomi = TreeNode('Xiaomi')
    mobile.add_child(samsung)
    mobile.add_child(apple)
    mobile.add_child(xiaomi)

    beats = TreeNode('Beats')
    jbl = TreeNode('JBL')
    sony = TreeNode('Sony')
    headphone.add_child(beats)
    headphone.add_child(jbl)
    headphone.add_child(sony)

    return root

root = build_tree()

root.print_tree()