class HashTable:

    def __init__(self):

        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for ch in key:
            h += ord(ch)
        return h % self.MAX
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for index,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

h = HashTable()
h['apple'] = 50
h['orange'] = 80
h['grape'] = 30
h['mango'] = 90
h['banana'] = 70

print(h['orange'])
print(h['apple'])
print(h['mango'])