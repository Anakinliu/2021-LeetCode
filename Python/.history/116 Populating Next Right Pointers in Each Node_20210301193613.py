class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# 
def connect(root):
    def link2(n1, n2):
        if n1 and n2:
            n1.next = n2
            link2(n1.left, n2.right)
            link2(n2.left, n2.right)
            link2(n1.right, n2.left)
    link2(root.left, root.right)
    return root

# @OldCodingFarmer 递归
def connect1(self, root):
    if root and root.left and root.right:
        # 1.当前root节点需要把自己的左右子相连
        root.left.next = root.right
        if root.next:  # 2.当前节点与其兄弟相连时，将自己的右子与兄弟的左子相连
            root.right.next = root.next.left
        # 3. 先序遍历
        self.connect(root.left)
        self.connect(root.right)

# 广度    
def connect2(self, root):
    if not root:
        return 
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            queue.append(curr.left)
            queue.append(curr.right)
    
# DFS 
def connect3(self, root):
    if not root:
        return 
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            stack.append(curr.right)
            stack.append(curr.left)