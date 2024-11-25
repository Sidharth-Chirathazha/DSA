class Heap:

    def __init__(self,capacity):

        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self,i):
        return (i-1)//2
    
    def getLeftIndex(self,i):
        return (2*i) + 1
    
    def getRightIndex(self,i):
        return (2*i) + 2
    
    def hasParent(self,i):
        return self.getParentIndex(i) >= 0
    
    def hasLeftChild(self,i):
        return self.getLeftIndex(i) < self.size
    
    def hasRightChild(self,i):
        return self.getRightIndex(i) < self.size
    
    def parent(self,i):
        return self.storage[self.getParentIndex(i)]
    
    def leftChild(self,i):
        return self.storage[self.getLeftIndex(i)]
    
    def rightChild(self,i):
        return self.storage[self.getRightIndex(i)]
    
    def isFull(self):
        return self.size == self.capacity
    
    def swap(self,i1,i2):
        temp = self.storage[i1]
        self.storage[i1] = self.storage[i2]
        self.storage[i2] = temp

    def insert(self,data):
        if self.isFull():
            return 
        self.storage[self.size] = data
        self.size += 1                                                  
        self.heapifyUp(self.size - 1)                                   

    def heapifyUp(self,i):                                             
        if (self.hasParent(i)) and (self.parent(i) > self.storage[i]): 
            self.swap(self.getParentIndex(i),i)                             
            self.heapifyUp(self.getParentIndex(i))                     
                                                                        
   
    def remove_min(self):
        if self.size == 0: 
            return
        data = self.storage[0]
        self.storage[0] = self.storage[self.size-1]
        self.storage[self.size-1] = 0
        self.size -= 1
        self.heapifyDown(0)                                           
        return data

    
    def heapifyDown(self,i):
        smallest = i                                                                  
        if self.hasLeftChild(i) and self.storage[smallest] > self.leftChild(i):    
            smallest = self.getLeftIndex(i)
        if self.hasRightChild(i) and self.storage[smallest] > self.rightChild(i):     
            smallest = self.getRightIndex(i)                                           
        if smallest != i:
            self.swap(i,smallest)                                                        
            self.heapifyDown(smallest)                                                      


h = Heap(7)

h.insert(8)
h.insert(6)
h.insert(10)
h.insert(4)
h.insert(9)
h.remove_min()
print(h.storage)