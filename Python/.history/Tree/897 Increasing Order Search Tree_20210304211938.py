class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(root):
    if root:
        
        left = increasingBST(root.left)
        # print(root.val)

        right = increasingBST(root.right)
        root.right
    return None
        

n1 = TreeNode(5)
n2 = TreeNode(3)
n3 = TreeNode(6)
n4 = TreeNode(2)
n5 = TreeNode(4)
n6 = TreeNode(8)
n7 = TreeNode(1)
n8 = TreeNode(7)
n9 = TreeNode(9)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.right = n6
n4.left = n7
n6.left, n6.right = n8, n9

increasingBST(n1)


