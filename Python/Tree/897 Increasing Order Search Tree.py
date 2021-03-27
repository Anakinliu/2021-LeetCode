class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

stack = []
def increasingBST(root):
    def increasingBST(root):
        if root:
            increasingBST(root.left)
            stack.append(root)
            increasingBST(root.right)
    increasingBST(root)
    for i in range(0, len(stack)-1):
        stack[i].right = stack[i+1]
        stack[i].left = None
    print(len(stack))
    return stack[0]
    
# @lee215
def increasingBST2(self, root, nxt = None):
    
    # if this null node was a left child, nxt is its parent
    # 如果这个 null 节点是一个左子，则tail是它的父
    # if this null node was a right child, nxt is its parent's parent
    # 如果这个 null 节点是一个右子，则tail是它最左的父的父
    if not root: 
        return nxt

    # recursive call, traversing left while passing in the current node as nxt
    res = self.increasingBST(root.left, root)

    # we don't want the current node to have a left child, only a single right child
    root.left = None

    # we set the current node's right child to be nxt
    # what is nxt? this part is important
    # if the current node is a left child, nxt will be its parent
    # 如果当前节点是一个左子，nxt会是它的父
    # else if the current node is a right child, nxt will be its parent's parent
    # 又如果当前node是一个右子，则nxt是它的父的父
    root.right = self.increasingBST(root.right, nxt)

    # 最后，res是原来的tree的最左的叶子节点，即最小的node
    # throughout the whole algorithm, res is the leaf of the leftmost path in the original tree
    # its the smallest node and thus will be the root of the modified tree
    return res


# n1 = TreeNode(5)
# n2 = TreeNode(3)
# n3 = TreeNode(6)
# n4 = TreeNode(2)
# n5 = TreeNode(4)
# n6 = TreeNode(8)
# n7 = TreeNode(1)
# n8 = TreeNode(7)
# n9 = TreeNode(9)
# n1.left, n1.right = n2, n3
# n2.left, n2.right = n4, n5
# n3.right = n6
# n4.left = n7
# n6.left, n6.right = n8, n9

n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(4)
n4 = TreeNode(3)
n1.left, n1.right = n2, n3
n3.left = n4

increasingBST(n1)

# t = n1
# while n1:
#     print(n1.val)
#     n1 = n1.right
# print(n1.left, n1.right)
# print(n2.left, n2.right)
# print(n3.left, n3.right)
# print(n4.left, n4.right)
# for i in stack:
#     print(i.val)
t = stack[0]
while t:
    print(t.val)
    t = t.right

