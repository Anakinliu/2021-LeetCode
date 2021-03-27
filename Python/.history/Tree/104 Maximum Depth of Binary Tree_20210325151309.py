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
    return max(left_d, right_d)

# 用栈进行迭代
def maxDepth3(root):
    if root:
        stack = [root]
    else:
        return 0
    depth = 1
    while stack:
        while stack
        depth = max(temp, depth)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        # print(node.val)
    return depth


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
# n4 = TreeNode(15)
# n5 = TreeNode(7)
n1.left = n2
n1.right = n3
# n3.left = n4
# n3.right = n5

print(maxDepth3(n1))