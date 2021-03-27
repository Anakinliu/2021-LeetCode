# https://labuladong.gitee.io/algo/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%B3%BB%E5%88%971.html
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
1,将 root 的左子树和右子树拉平。
2,将 root 的右子树接到左子树下方
3,然后将整个左子树作为右子树。
"""
def flatten(root):
    # 函数无返回值
    def flat(node):
        if not node:
            return

        flat(node.left)
        flat(node.right)

        # 暂存值
        left = node.left
        right = node.right

        # 将当前节点的 left 作为当前节点的 right
        node.left = None
        node.right = left

        # 
        p = node
        while p.right:
            p = p.right
        p.right = right
        