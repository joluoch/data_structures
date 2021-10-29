class Node:
    
    def __init__(self,val):
        # remember very node consists of next and data 
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        # we will have a head pointer to point and the current node 
        self.head= None
        

    def get(self, index: int) -> int:
        

        current = self.head #initialize temp
        count = 0 
        # move the head through the nodes if next node is not the last node and count
        # if our index is equal to the count then return the value 
        while current: 
            if count == index : 
                return current.val
            count+= 1
            current = current.next 
        
        
        
    def addAtHead(self, val: int) -> None:
        # initialize a new  node 
        # make the node head
        # move head to point at new node
        
        new_node = Node(val)
        new_node.next = self.head
        self.head= new_node 
        
    def addAtTail(self, val: int) -> None:
        # create a new node  
        # if list is empty then make the new node head 
        # else traverse till the last node 
        # change the next o last node
        
        new_node = Node(val)
        
        if self.head == None: 
            self.head = new_node 
            return 
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        # make a node 
        # make a temp to traverse
        # loop through the list 
        # then aadd 
        new_node = Node(val)

        temp = self.head 
        for _ in range (index -1):
            temp = temp.next
        new_node.data = val
        new_node.next = temp.next
        temp.next =new_node
        
    def print (self):
        if self.head is None:
            print ("linked list is empty")
        else:
            temp = self.head
            while temp:
                print (temp.data, "-->", end = "")
                temp =temp.next
    
    def deleteAtBegin(self):

        temp = self.head 
        self.head= temp.next 
        temp.next = None
    
    def deleteAtEnd (self):

        temp = self.head.next
        prev =self.head 
        while temp.next:
            temp = temp.next
            prev = prev.next
        prev.next = None


              

    def deleteAtIndex(self, index: int) -> None:

        # store head node 
        temp = self.head
        last =self.head.next
        prev =self.head 
        
        # if linked list is empty
        
        if self.head == None:
            return 
         
        # if head needs to be removed
        
        if index == 0 :
            self.head = temp.next 
            temp.next = None
            return 
    
        
        for i in range (1,index -1 ):
            last = last.next
            prev = prev.next
        prev.next = last.next
        last.next = None
    
    #function to print in reverse 
    
        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtHead(2)
obj.addAtHead(3)
obj.addAtTail(5)
obj.addAtIndex(2,5)
obj.deleteAtIndex(2)
param_1 = obj.get(3)