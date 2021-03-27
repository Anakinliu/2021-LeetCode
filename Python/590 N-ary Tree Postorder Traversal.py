class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
# N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

# 简单递归
def postorder(root):
    res = []
    def trav(root):
        if root:
            for child in root.children:
                trav(child)
            res.append(root.val)
    trav(root)
    return res

# 迭代,先前序遍历
def postorder2(root):
    stack = [root]  # 堆栈模仿递归
    res = []  # 保存访问过的值
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.extend(node.children)
    return res[::-1]  # 将前序遍历结果反转
