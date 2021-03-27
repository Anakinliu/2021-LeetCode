class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n):
    # 构建不同的
    lst = [v for v in range(1,n+1)]
    def child(nums):
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        