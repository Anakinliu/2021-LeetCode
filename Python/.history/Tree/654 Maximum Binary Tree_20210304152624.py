class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    # 最大值
    max_v = nums[0]
    index = 0
    for idx, v in enumerate(nums):
        if v > max_v:
            max_v = v
            index = idx
    print(index, max_v)
    node = TreeNode(max_v)
    node.left = constructMaximumBinaryTree(nums[:index])
    node.right = constructMaximumBinaryTree(nums[index+1:])
    return node

root = constructMaximumBinaryTree([3,2,1,6,0,5])

def trav(root):
    if root:
        print(root.val)
        trav(root.left)
        trav(root.right)

trav(root)


# @
"""
我们跟踪堆栈，并确保堆栈中的数字降序排列。
对每个 nums 的元素：
1. 如果 stack 是空， 
"""