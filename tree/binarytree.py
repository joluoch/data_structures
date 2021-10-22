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



    


    