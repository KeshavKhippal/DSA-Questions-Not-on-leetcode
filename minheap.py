class MinHeap:
    def __init__(self):
        self.heap=[]
    def push(self,val):
        if not self.heap:
            self.heap.append(val)
        else:
            self.heap.append(val)
            self._bubble_up(len(self.heap)-1) #appended at ed
    def _bubble_up(self,index):
        while index>0:
            parent=(index-1)//2
            
            if self.heap[parent]<self.heap[index]:
                break
            self.heap[parent],self.heap[index]=self.heap[index],self.heap[parent]
            index=parent
    def pop(self):
        if not self.heap: #heap empty
            return None
        
        min_val=self.heap[0]
        last=self.heap.pop()
        
        if self.heap:
            self.heap[0]=last
            self._bubble_down(0)
        return min_val
    def _bubble_down(self,index):
        n=len(self.heap)
        while True:
            smallest=index
            l=2*index+1
            r=2*index+2
            
            if l<n and self.heap[l]<self.heap[smallest]:
                smallest=l
                
            if r<n and self.heap[r]<self.heap[smallest]:
                smallest=r
            if smallest==index:
                break
            self.heap[smallest],self.heap[index]=self.heap[index],self.heap[smallest]
            index=smallest
h=MinHeap()



h.push(5)
h.push(3)
h.push(6)
h.push(1)
h.push(9)

print(h.heap)

print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())
print(h.pop())