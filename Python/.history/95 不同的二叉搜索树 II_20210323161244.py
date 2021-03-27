def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def generateTrees(self, n: int) -> List[TreeNode]:

    def build(left, right):
        if left > right:
            return [None]
        if left == right:
            return [TreeNode(left)]
        ans = []
        for i in range(left, right+1):
            # 每个节点作为root
            leftTrees = build(left, i-1)
            rightTrees = build(i+1, right)
            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    root = TreeNode(i)
                    root.left = leftTree
                    root.right = rightTree
                    ans.append(root)
        return ans

    return build(1, n)
        