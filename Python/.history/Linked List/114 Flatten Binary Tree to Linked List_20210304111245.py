class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    # 函数无返回值
    def flat(node):
        if not node:
            return

        flat(node.left)
        flat(node.right)

        left = node.left
        right = node.right

        node.left = None
        if right:
            node.right = left
        
        p = right
        while right:
            right = right.right
        p.right = right