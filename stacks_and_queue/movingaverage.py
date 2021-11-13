class MovingAverage:
    def __init__(self,size:int) :
        """
         Initialize your data structure here.
         """
        self.array = []
        self.size = size
    
    def next(self,val: int) -> float:

        self.array.append(val)

        return print(sum(self.array[-self.size:])/min(len(self.array),self.size))


obj = MovingAverage(3)
obj.next(1)
obj.next(10)
obj.next(3)
obj.next(5)
"""
Example 1: 
Input ['MovingAverage','next','next','next','next',]
[[3],[1],[10],[3],[5]]
output 
[null,1.0,5.5,4.66667,6.0]
"""