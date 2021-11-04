class Node:
    
    def __init__(self,val):
        # remember very node consists of prev,data and next  
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:

    def __init__(self):
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
        newnode = Node(val)
        newnode.next = self.head
        newnode.prev = None

        if self.head is not None:
            self.head.prev = newnode

        self.head = newnode
        

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)

        if self.head == None:
            self.head = newnode
            newnode.prev = None
            newnode.next= None
        
        end = self.head
        while end.next:
            end = end.next
        end.next=newnode
        newnode.pev = end
        newnode.next = None

        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)

        temp = self.head 
        for _ in range (index -1):
            temp = temp.next
        new_node.data = val
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node
        if new_node.next:
            new_node.next.prev=new_node
        
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return
         # Store head node
        temp = self.head
        
        # If head needs to be removed
        if index == 0:
            self.head = temp.next
            temp.next.prev=None
            temp = None
            return 
        for _ in range(index - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        prev = temp.prev
        temp.next = None
        temp.next = next
        temp.prev = prev
    
    def display (self):
        if self.head is None:
            print ("linked list is empty")
        else:
            temp = self.head
            while temp:
                print (temp.val, "<-->", end = "")
                temp =temp.next

        


obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.display()
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))
obj.display()  
        





'''Let's briefly review the performance of the singly linked list and doubly linked list.

They are similar in many operations:

Both of them are not able to access the data at a random position in constant time.
Both of them are able to add a new node after given node or at the beginning of the list in O(1) time.
Both of them are able to delete the first node in O(1) time.
But it is a little different to delete a given node (including the last node).

In a singly linked list, it is not able to get the previous node of a given node so we have to spend O(N) time to find out the previous node before deleting the given node.
In a doubly linked list, it will be much easier because we can get the previous node with the "prev" reference field. So we can delete a given node in O(1) time'''