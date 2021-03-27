class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def invertTree(root):
    if root:
        left = invertTree(root.left)
        right = invertTree(root.right)
        root.right = left
        root.left = right
    else:
        return None