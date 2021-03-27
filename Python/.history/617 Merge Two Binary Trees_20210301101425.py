# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    if not root1 and not root2:
        return None
    if root1 == None:
        
          

n4 = TreeNode(5,None,None)
n3 = TreeNode(2,None,None)
n2 = TreeNode(3,n4,None)
n1 = TreeNode(1,n2,n3)

m5 = TreeNode(7,None,None)
m4 = TreeNode(4,None,None)
m3 = TreeNode(3,None,m5)
m2 = TreeNode(1,None,m4)
m1 = TreeNode(2,m2,m3)
mergeTrees(n1,m1)
        
