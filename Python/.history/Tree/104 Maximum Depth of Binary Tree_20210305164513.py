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

def maxDepth2(root):
    if not root:
        return 0
    left_d = maxDepth(root.left)
    right_d = maxDepth(root.right)
    return max(left_d, right_d) + 1

# 用栈进行迭代
def maxDepth3(root):
    if root:
        stack = [root]
    else:
        return None
    res = []
    while stack:
        node = stack[-1]
        res.append(node)
        


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
# n5 = TreeNode(7)
n1.left = n2
n1.right = n3
n3.left = n4
# n3.right = n5

print(maxDepth(n1))