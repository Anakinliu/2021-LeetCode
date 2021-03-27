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