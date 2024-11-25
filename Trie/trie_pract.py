class Node:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd
    
    def auto_complete(self,prefix):
        res = []
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]
        self._find_words(cur,prefix,res)
        return res

    def _find_words(self,node,prefix,res):
        if node.isEnd:
            res.append(prefix)

        for char,c_node in  node.children.items():
            self._find_words(c_node,prefix + char, res)      



trie = Trie()
words = ["dog", "deer", "deal", "cat", "can", "candy"]
for word in words:
    trie.insert(word)
print(trie.auto_complete("can"))