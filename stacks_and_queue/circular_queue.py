class MyCircularQueue:

    def __init__(self, k: int):
        self.storage = [None]*k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.k = k 
        
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.tail = (self.tail + 1) % self.k #calculate new tail index
        self.storage[self.tail]=value
        self.size +=1
        
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty() :
            return False
        data = self.storage[self.head]
        
        self.head = (self.head + 1)% self.k # calculate new head position
        self.size -=1
        
        return True
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.storage[self.head]
        else:
            return -1
            
        

    def Rear(self) -> int:
        return self.storage[self.tail]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.k == self.size 
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(6)
print(obj.enQueue(6))
obj.Rear()
obj.Rear()
obj.deQueue()
obj.enQueue(5)
obj.Rear()
obj.deQueue()
print(obj.isEmpty())
print(obj.Front())
'''
obj.deQueue()
obj.deQueue()
obj.deQueue()
obj.isEmpty()
obj.isFull()
'''