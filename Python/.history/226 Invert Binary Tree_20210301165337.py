"""
https://labuladong.gitee.io/algo/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%B3%BB%E5%88%971.html
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 后序 
def invertTree(root):
    if root:
        left = invertTree(root.left)
        right = invertTree(root.right)
        root.right = left
        root.left = right
        return root
    else:
        return None