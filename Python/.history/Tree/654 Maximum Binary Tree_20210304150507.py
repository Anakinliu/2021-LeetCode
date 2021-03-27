class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    max_v = nums[0]
    idx = 0
    for idx, i in nums[1:]:
        if 
    node = TreeNode()