class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    def dfs(r1, r2):
        if not r1 and r2:  # 一个非NOne一个None False
            return False
        if r1 and not r2:  # 一个None一个非None Flase
            return False
        if not r1 and not r2:  # 都是None返回 True
            return True

        return r1.val == r2.val and dfs(r1.left, r2.left) and dfs(r1.right, r2.right)
    return dfs(p, q)

p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p1.left = p2
p1.right = p3

q1 = TreeNode(1)
q2 = TreeNode(2)
q3 = TreeNode(3)
q1.left = q2
q1.right = q3

print(isSameTree(p1, q1))

