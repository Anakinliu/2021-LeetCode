class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    def do(root):
        if not root:
            return 0
        # 计算每个节点的左右子树

        # left或者right为-1，表示已经不平衡了
        left = do(root.left) 
        if left == -1:
            return -1
        right = do(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    return do(root) != -1



p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p5 = TreeNode(5)
p6 = TreeNode(6)
p7 = TreeNode(7)
p1.left = p2
p1.right= p3
p2.left = p4
p2.right = p5
p4.left = p6
p4.right = p7
print(isBalanced(p1))


