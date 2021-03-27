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
我们需要记住最大节点，而不是每次都尝试查找它们。
因此，我们需要具有顺序和层次结构的东西。
鉴于其需求，堆栈非常自然地满足了这一需求。
我们需要做的就是排序。

我们跟踪堆栈，并确保堆栈中的数字降序排列。
对每个 nums 的元素：
1. 如果 stack 是空，放入
2. 如果新的值小与stack顶的值，我们将其作为stack顶的right
3. 如果新的值更大，一直 pop 直到stack为空或者stack顶的值比新的值大，
pop时持续跟踪上一个pop的值
"""
def constructMaximumBinaryTree2(nums):
    stack = [TreeNode(nums[0])]
    for v in nums[1:]:
        node = TreeNode(v)
        if v < stack[-1].val:  # 如果新的值小与stack顶的值，我们将新值作为stack顶的right
            stack[-1].right = TreeNode(v)
        else:  # 如果新的值大与stack顶的值
            p = stack.pop()
            while v > p.val and stack:
                p = stack.pop()
            node.left = p
        stack.append(node)
    return stack[0]
