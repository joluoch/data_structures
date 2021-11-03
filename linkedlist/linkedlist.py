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
        
    def display (self):
        if self.head is None:
            print ("linked list is empty")
        else:
            temp = self.head
            while temp:
                print (temp.val, "-->", end = "")
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


        # If linked list is empty
        if self.head == None:
            return 
  
        # Store head node
        temp = self.head
  
        # If head needs to be removed
        if index == 0:
            self.head = temp.next
            temp = None
            return 
  
        # Find previous node of the node to be deleted
        for i in range(index -1 ):
            temp = temp.next
            if temp is None:
                break
  
        # If position is more than number of nodes
        if temp is None:
            return 
        if temp.next is None:
            return 
  
        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next
  
        # Unlink the node from linked list
        temp.next = None
  
        temp.next = next 
    
    '''
    function to check if a linked list has a cycle
    this can be solved in alot of ways .i will show you three common ways 
    https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
    1. by using hashtable : 
        Traverse the list one by one and keep putting the node addresses in a Hash Table. 
        At any point, if NULL is reached then return false, and if the next of the current nodes points to any of the previously stored nodes in 
         Hash then return true.

    2. by using Floyd’s Cycle-Finding Algorithm :
        This is the fastest method and has been described below:  
        1. Traverse linked list using two pointers.
        2. one pointer(slow_p) by one and another pointer(fast_p) by two.
        3. If these pointers meet at the same node then there is a loop. 
        4. If pointers do not meet then linked list doesn’t have a loop.
        


    3. by Marking visited nodes without modifying the linked list data structure :
        In this method, a temporary node is created. The next pointer of each node that is traversed is made to point to this temporary node. 
        This way we are using the next pointer of a node as a flag to indicate whether the node has been traversed or not. 
        Every node is checked to see if the next is pointing to a temporary node or not. 
        In the case of the first node of the loop, the second time we traverse it this condition will be true, hence we find that loop exists. 
        If we come across a node that points to null then the loop doesn’t exist. '''

    
    def detectLoop(self): # using floyd's cycle 
        
        slow_p = self.head

        fast_p = self.head

        while(slow_p and fast_p and fast_p.next):

            slow_p = slow_p.next

            fast_p = fast_p.next.next

            if slow_p == fast_p:


                return
    #checking where the cycle starts from 
    def detectCycle(self, head):

        # If list is empty or has only one node
        # without loop

        if head == None or head.next == None:

            return None

        slow = head 

        fast = head
        
        # Move slow and fast 1 and 2 steps
        # ahead respectively.
        slow = slow.next 

        fast = fast.next.next

        # Search for loop using slow and
        # fast pointers
        
        while fast and fast.next:

            if slow == fast:

                break
            slow = slow.next 

            fast = fast.next.next 

        # If loop does not exist
        if slow!= fast:

            return None

        slow = head

        # If loop exists. Start slow from
        # head and fast from meeting point.
        while slow != fast :

            slow = slow.next 

            fast = fast.next 

        return slow 
    
    '''intersection of two lists
        Using Two pointers : 

        1. Initialize two pointers ptr1 and ptr2  at the head1 and  head2.
        2. Traverse through the lists,one node at a time.
        3. When ptr1 reaches the end of a list, then redirect it to the head2.
        4. similarly when ptr2 reaches the end of a list, redirect it the head1.
        5. Once both of them go through reassigning, they will be equidistant from the collision point
        6. If at any node ptr1 meets ptr2, then it is the intersection node.
        7. After second iteration if there is no intersection node it returns NULL.'''

    def getIntersectionNode(self, headA, headB):
        
        p_1 = headA

        p_2 = headB
        
        if p_1 == None and p_2 == None:

            return None

        while p_1 != p_2 :

            p_1 = p_1.next

            p_2 = p_2.next 
            
            if p_1 == p_2:

                return p_1

            if p_1 ==None:

                p_1 = headB

            if p_2 == None:
                
                p_2 = headA

        return p_1
    
    #reversed linked list 
    def reverseList(self, head):
        
        if head is None or head.next is None:
            return head 
        #we will use two pointers alreadyreversed will point to the firt node and current will point to the next node
        # we will make already revversed, which is out head to point to none, meaning it has already been reversed 
        alreadyReversed,current = head,head.next
        alreadyReversed.next= None
        # while our next pointer, current isn't pointing to the original none(end)
        while current is not None:
            # we make another pointer that will store the third value in our original list 
            storePtr  = current.next
            #then we will reverse the third value to point the reversed which we moved one step forward
            current.next = alreadyReversed
            
            alreadyReversed = current
            current = storePtr
        return alreadyReversed 

        
    
        


# Your MyLinkedList object 
# will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.display()
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))
obj.display()


