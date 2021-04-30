class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 层序遍历。。。
def isSymmetric(root):
    dui = True
    lst = [root]
    while dui and lst:
        children = []
        vals = []
        while lst:
            child = lst.pop()
            if child.left:
                children.append(child.left)
                vals.append(child.left.val)
            else:
                vals.append(None)
            if child.right:
                children.append(child.right)
                vals.append(child.right.val)
            else:
                vals.append(None)
        lst = children
        print(vals)
        left = 0
        right = len(vals) - 1
        while left < right:
            if vals[left] != vals[right]:
                dui = False
            left += 1
            right -= 1
    return dui


