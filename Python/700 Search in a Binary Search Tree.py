# 暴力递归
def searchBST(root, val):
    # 在二叉搜索树中寻找并返回val节点
    if not root:
        return None
    if val < root.val:
        return searchBST(root.left, val)
    elif val > root.val:
        return searchBST(root.right, val)
    else:
        return root

# 迭代
def searchBST2(root, val):
    # 节点数量 [1, 5000]
    node = root
    while node and node.val == val:
        if node.val < val:
            node = node.right
        else:
            node = node.left
    return None