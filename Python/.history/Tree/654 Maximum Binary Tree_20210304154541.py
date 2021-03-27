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
1. 如果 stack 是空，放入
2. 如果新的值小与stack顶的值，我们将其作为stack顶的right
3. 如果新的值更大，一直 pop 直到stack为空或者stack顶的值比新的值大，
pop时持续跟踪上一个pop的值
"""
def constructMaximumBinaryTree(nums):
    stack = []
    for v in nums:
        node = TreeNode(v)
        if not stack:
            stack.append(node)
            continue
        if v < stack[-1].val:
            stack[-1].right = TreeNode(v)
        else:
            p = stack.pop()
            while not stack and v > 
