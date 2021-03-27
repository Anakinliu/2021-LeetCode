class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k):
    lst = []
    def toLst(root):
        if root:
            toLst(root.left)
            lst.append()
            toLst(root.right)