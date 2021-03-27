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
    for idx, v in enumerate(nums[1:]:
        if v > max_v:
            max_v = v
            index = idx
    node = TreeNode(max_v)
    node.left = constructMaximumBinaryTree(nums[:index])
    node.right = constructMaximumBinaryTree(nums[index+1:])
    return node

root = constructMaximumBinaryTree([3,2,1,6,0,5])

def trav(root):
    print(root.val)
    trav(root.left)
    trav(root.right)

trav(root)