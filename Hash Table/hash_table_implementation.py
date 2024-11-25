class Node:

    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self,key,value):
        node = self.head
        while node:
            if node.key == key:
                node.value = value
            node = node.next
        new_node = Node(key,value)
        new_node.next = self.head
        self.head = new_node

    def search(self,key):
        node = self.head
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return "Item not found"
    
    def delete(self,key):
        node = self.head
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.head = node.next
                print(f"Element from key {key} removed")
                return
            prev = node
            node = node.next
        print("Element not found")
        return
        
    def get_all_values(self):
        values = []
        node = self.head
        while node:
            values.append(node.value)
            node = node.next
        return values
    
class HashTable:

    def __init__(self,size):
        self.size = size
        self.arr = [LinkedList() for _ in range(self.size)]

    def get_hash(self,key):
        index = 0
        for ch in str(key):
            index += ord(ch)
        return index % self.size
    
    def __setitem__(self,key,value):
        index = self.get_hash(key)
        self.arr[index].insert(key,value)

    def __getitem__(self,key):
        index = self.get_hash(key)
        return self.arr[index].search(key)
    
    def __delitem__(self,key):
        index = self.get_hash(key)
        return self.arr[index].delete(key)
    
    def frequency(self):
        freq = {}
        for linked_list in self.arr:
            values = linked_list.get_all_values()
            for value in values:
                if value in freq:
                    freq[value] += 1
                else:
                    freq[value] = 1
        return freq
    

hash = HashTable(20)
hash[3] = 'mango'
hash[2] = 'apple'
hash[6] = 'orange'
hash[9] = 'orange'
hash[10] = 'mango'
hash[24] = 'orange'
print(hash[10])
print(hash.frequency())