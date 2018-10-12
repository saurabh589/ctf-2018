
# Python code to insert a node in AVL tree 
b = []
# Generic tree node class 
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  
# AVL tree class which supports the  
# Insert operation 
class AVL_Tree(object): 
  
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 


    def preOrder(self, root): 
        global b
        if not root: 
            return
     
        b.append(str(root.val))
        self.preOrder(root.left) 
        self.preOrder(root.right) 
  
  

myTree = AVL_Tree() 
root = None

a = [34,67,50,91,1,95,49,82,78,49,8,8,62,50,82,18,42,77,61,99,58,91,59,27,19,94,48,4,86,94,57,63,20,22,41,79,38,78,68,85,66,87,99,92,39,100,45,55,5,95,11,32,36,74,81,21,87,78,61,20,50,33,54,44,25,91,90,23,6,82,38,8,6,84,17,11,64,58,83,51,61,47,91,11,86,62,75,94,70,31,34,65,100,37,86,99,39,8,58,26]
for c in a:
    root = myTree.insert(root, c)
  
"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""
  
# Preorder Traversal 
print("Preorder traversal of the", 
      "constructed AVL tree is") 

myTree.preOrder(root) 
print(",".join(b))
