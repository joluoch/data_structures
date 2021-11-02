
'''stack implementation using arrays:
    LIFO'''
class MinStack(object):
    #Initialize the stack by min element as infinity
    min=float('inf')

    def __init__(self):
        self.min=float('inf')
        self.stack = []

    '''For push operation push(x)
        if x < min, then update min := x,
        push x into stack'''
    def push(self, x):
        if x<=self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)

    '''For pop operation pop()
        t := top element
        delete t from stack
        if t is min, then min := top element of the stack'''
    def pop(self):
        t = self.stack[-1]
        self.stack.pop()
        if self.min == t:
            self.min = self.stack[-1]
            self.stack.pop()

    # for top we get the last element on the stack
    def top(self):
        return self.stack[-1]

    #get the minimum value 
    def getMin(self):
        return self.min

    def isEmpty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else: 
            return False
    def length(self) -> int:
        return len(self.stack)
    
m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())
m.pop()
print(m.top())
print(m.getMin())