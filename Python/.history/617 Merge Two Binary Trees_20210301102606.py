# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    if root1 == None and root2 == None:
        return None
    if root1 == None:
        return root2
    if root2 == None:
        return root1
    queue = [[root1, root2]]
    while queue:
        a, b = queue.pop(0)
        if a and b:
            print(a.val + b.val)
            queue.append([a.left, b.left])
        elif a:
            print(a.val)
            queue.append([a.left, None])
        elif b:
            print(b.val)
            queue.append([None, b.left])
        if a.left and b.left:
            
        elif a.left:
            
        elif b.left:
            
        if a.right and b.right:
            queue.append([a.right, b.right])
        elif a.right:
            queue.append([a.right, None])
        elif b.right:
            queue.append([None, b.right])


          

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
        
