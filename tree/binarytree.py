class Tree:
    def __init__ (self,data):
        self.left = None
        self.right = None
        self.data = data


    def insert (self, data):

        if self.data == data:
            return False # checking for duplicate 

        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)# we call recursively the insert function will movingdown the left
            else: 
                #if we find the correct position toinsert it then we crete the node
                self.left = Tree (data)
                return True 
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True 



    def inorder_traversal (self):

        # for inorder traversal we first visit the left--> Node--> right 

        # make a list to hold  everything in the tree 
        element = []

        # visit the left side first 
        if self.left:
            element += self.left.inorder_traversal()
        
        # visit the node 
        element . append(self.data)

        #visit the right 

        if self.right : 
            element += self.right.inorder_traversal()

        return element


    def preorder (self):
        # ROOT --> LEFT --> RIGHT
        element = []
        # visit the node 
        element . append(self.data)

        if self.left:
            element += self.left.inorder_traversal()
        
        if self.right : 
            element += self.right.inorder_traversal()
        
        return element

    
    def postorder (self):
        # LEFT --> RIGHT --> ROOT 
        element = []
        

        if self.left:
            element += self.left.inorder_traversal()
        
        if self.right : 
            element += self.right.inorder_traversal()
        
        element . append(self.data)

        return element



    def getval (self,val):
        if self.data ==val:
            return True
        
        if self.data > val :
            # If the value is less that head 
            #value might be on the left side 
            if self.left is  None:
                return False
            else:
                return self.left.getval(val)
        if val > self.data :
            # if value is greater than 
            # value might be on the right side 
            if self.right is None:
                return False 
            else:
                return self.right.getval(val)



    def size(self):
        # addition is 1 + the size of the left subtree + the size of the right subtree 
        if self.left is not None  and self.right is not None :
            return 1 + self.left.size()+self.right.size()
        else:
            return 0 #
    

    def find_max(self):
        #finding tthe maximum value, as always the right size is expectd to have greater values than the left side so we will check the right and not left 

        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def find_min (self):
        if self.left is None:
            return self.data
        return self.left.find_min()
        

    def delete(self,val):

        if val < self.data:#left side
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data: # val is on the right 
            if self.right:
                self.right = self.right.delete(val)

        else:
            # if parent has no children  
            if self.left is None and self.right is None:
                return None

            # if the parent has only child on the right 
            if self.left is None:
                return self.right

            # if parent has only child on the left 
            if self.right is None:
                return self.right 

        
             # using the minimum value of the right side for replancement after deletion 
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

            # using the maximum value of the left side for replancement after deletion 
            '''max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)'''

        return self







root = Tree(17)
root.insert(4)
root.insert(1)
root.insert(20)
root.insert(9)
root.insert(23)
root.insert(18)
root.insert(34)


print(root.inorder_traversal())
print(root.preorder())
print(root.postorder())
print(root.getval(5))
print(root.size())
print(root.find_max())
print(root.find_min())
root.delete(20)
print("After deleting 20 ",root.inorder_traversal())
    


    