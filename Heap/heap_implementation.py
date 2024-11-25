class Heap:

    def __init__(self):
        self.heap = []

    def getParentIndex(self,i):
        return (i-1)//2
    
    def getLeftIndex(self,i):
        return (2*i) + 1
    
    def getRightIndex(self,i):
        return (2*i) + 2
    
    def hasLeftChild(self,i):
        return self.getLeftIndex(i) < len(self.heap)
    
    def hasRightChild(self,i):
        return self.getRightIndex(i) < len(self.heap)
    
    def get_parent(self,i):
        return self.heap[self.getParentIndex(i)]
    
    def get_left_child(self,i):
        return self.heap[self.getLeftIndex(i)]
    
    def get_right_child(self,i):
        return self.heap[self.getRightIndex(i)]
    
    def swap(self,i1,i2):
        self.heap[i1],self.heap[i2] = self.heap[i2],self.heap[i1]

    def insert(self,val):
        self.heap.append(val)
        self.heapifyUp(len(self.heap)-1)

    def heapifyUp(self,i):
        while i > 0 and self.get_parent(i) > self.heap[i]:
            self.swap(self.getParentIndex(i),i)
            i = self.getParentIndex(i)

    def extract_min(self):
        if len(self.heap) == None:
            return None
        data = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapifyDown(0)
        return data
    
    def heapifyDown(self,i):
        smallest = i
        if self.hasLeftChild(i) and self.heap[smallest] > self.get_left_child(i):
            smallest = self.getLeftIndex(i)
        if self.hasRightChild(i) and self.heap[smallest] > self.get_right_child(i):
            smallest = self.getRightIndex(i)
        if smallest != i:
            self.swap(i,smallest)
            self.heapifyDown(smallest)

    def buildHeap(self,arr):
        self.heap = arr[:]
        for i in range((len(self.heap)//2)-1,-1,-1):
            self.heapifyDown(i)

    def get_heap(self):
        return self.heap

    
h = Heap()
arr = [9,4,7,5,8,2,1,18,10,3]

h.buildHeap(arr)

print(h.get_heap())