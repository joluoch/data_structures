import collections
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

    def maxDepth(self,root):
        # Null node has 0 depth.
        if root == None:
            return 0

        # Get the depth of the left and right subtree 
        # using recursion.
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        # Choose the larger one and add the root to it.
        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth + 1


    #check if they are symmetrical 
    def isMirror(self,root1, root2):
    # If both trees are empty, then they are mirror images
        if root1 is None and root2 is None:
            return True
    
        """ For two trees to be mirror images,
            the following three conditions must be true
            1 - Their root node's key must be same
            2 - left subtree of left tree and right subtree
            of the right tree have to be mirror images
            3 - right subtree of left tree and left subtree
            of right tree have to be mirror images
        """
        if (root1 is not None and root2 is not None):
            if root1.key == root2.key:
                return (self.isMirror(root1.left, root2.right)and
                        self.isMirror(root1.right, root2.left))
    
        # If none of the above conditions is true then root1
        # and root2 are not mirror images
        return False
    
 
    def isSymmetric(self,root):
        # Check if tree is mirror of itself
        return self.isMirror(root, root)
        
    #check if a sum exists from root to leaf path 
    def hasPathSum(self, root,targetSum):
        if not root:   
            return False
        remaining = targetSum - root.val
        if not root.left and not root.right:
            
            if remaining == 0:
                
                return True
            
            return False
        

        if root.left and not root.right:
            
            return self.hasPathSum(root.left, remaining)
        

        if not root.left and root.right:
            
            return self.hasPathSum(root.right, remaining)

        if root.left and root.right:
            
            return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)

    # print out the values of each level [[1],[2,3],[4,5]]
    def levelOrder(self, root):
        levelorder=[]
        
        if root is None:
            return levelorder
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            List=[]
            
            while size >0:
                Node = queue.popleft()
                List.append(Node.val)
                size -=1
                
                if Node.left is not None:
                    queue.append(Node.left)
                if Node.right is not None:
                    
                    queue.append(Node.right)
            levelorder.append(List)
        return levelorder
        
        
       
        



    


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
    


''' def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        self.traverse(root, result)
        return result
    

    def traverse(self, root, result):
        if root == None:
            return
        
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)'''

'''   def isSymmetric(self, root) -> bool:
        def recur_search(left,right):
            if not left and not right: return True              # Both reach an end
            if not (left and right): return False               # Not match, when one has val but another doesn't
                                                                # Check "None" first for avoiding Null value access error
            if left.val == right.val:                           # Vals match, Check next level
                c_left = recur_search(left.left, right.right)   # Take node.left as a new sub-root. [root,left,right]
                c_right = recur_search(left.right, right.left)  # Take node.right as a new sub-root. [root,right,left]
                return c_left and c_right                       # Both new sub-root search should return True
            return False                                        # Two node's vals not match. 
        return recur_search(root.left, root.right)'''
