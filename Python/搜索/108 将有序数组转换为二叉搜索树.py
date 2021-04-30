class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归，每次选节点都选择中间的，递归下去
def sortedArrayToBST(nums):
    def do(left, right):
        if left >= right:
            return None
        
        mid = (right + left) // 2
        root = TreeNode(nums[mid])
        root.left = do(left, mid)
        root.right = do(mid+1, right)
        return root

    return do(0, len(nums))
