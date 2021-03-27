class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归求解
def maxDepth(root):
    if not root:
        return 0
    left_d = 1 + maxDepth(root.left)
    right_d = 1 + maxDepth(root.right)
    return max(left_d, left)