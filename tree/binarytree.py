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

        # for inorder traversal we firstvisit the left--> Node--> right 
        # make a list to add everything in the tree 
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
        element = []
        # visit the node 
        element . append(self.data)

        if self.left:
            element += self.left.inorder_traversal()
        
        if self.right : 
            element += self.right.inorder_traversal()
    
    def postorder (self):
        element = []
        

        if self.left:
            element += self.left.inorder_traversal()
        
        if self.right : 
            element += self.right.inorder_traversal()
        
        element . append(self.data)


    
    def getval (self,val):
        if self.data ==val:
            return True
        
        if self.data > val :
            #value might be on the left side 
            if self.left is  None:
                return False
            else:
                return self.left.getval(val)
        if val > self.data :
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
            return 0 
    
    #def delete(sel,val):








# post traversal 
#pre order traversal 
#

root = Tree(9)
root.insert(5)
root.insert(2)
root.insert(4)
root.insert(11)

print(root.inorder_traversal())
'''def build_tree(data):
    bt = Tree(7)

    for _ in range (len(data)):
        bt.insert(data[_])
    
    return bt
if __name__ == "__main__":

    number = [15,10,20,12,3,1,13,6,11,4,14,9]
    binary_tree = build_tree(number)
    print(binary_tree.inorder_traversal())'''



    


    