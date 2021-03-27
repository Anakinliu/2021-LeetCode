class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def invertTree(root):
    left = invertTree(root.left)
    invertTree(root.right)