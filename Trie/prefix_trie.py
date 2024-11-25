class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self,word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word
    
    def startswith(self,prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

t = Trie()

t.insert('cat')
t.insert('cattle')
print(t.search('cat'))
print(t.search('dog'))
print(t.search('cattle'))
print(t.startswith('catt'))
print(t.startswith('cato'))