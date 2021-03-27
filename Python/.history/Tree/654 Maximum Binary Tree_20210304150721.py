class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    #  
    max_v = nums[0]
    index = 0
    for idx, v in nums[1:]:
        if v > max_v:
            max_v = v
            index = idx
    node = TreeNode(max_v)
    node.left = constructMaximumBinaryTree(nums[:index])
    node.right = constructMaximumBinaryTree(nums[index+1:])
    return node

