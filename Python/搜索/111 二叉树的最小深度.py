class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 深度优先搜索
def minDepth(root):
    if not root:
        return 0
    # root 是叶子节点
    if not (root.left or root.right):
        return 1
    
    min_depth = 10**6
    if root.left:
        min_depth = min(minDepth(root.left), min_depth)
    if root.right:
        min_depth = min(minDepth(root.right), min_depth)
    return min_depth + 1

"""
我们可以想到使用广度优先搜索的方法，遍历整棵树。

当我们找到一个叶子节点时，直接返回这个叶子节点的深度。
广度优先搜索的性质保证了最先搜索到的叶子节点的深度一定最小
"""
def min_depth2(root):
    if not root:
        return 0
        
    q = [(root, 1)]

    while q:
        node, depth = q.pop(0)
        if not (node.left or node.right):
            return depth
        if node.left:
            q.append((node.left), depth + 1)
        if node.right:
            q.append((node.right), depth + 1)
    return 0




