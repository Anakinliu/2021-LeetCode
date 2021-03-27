class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 反转整个列表
def reverse(node):
    # base case，只有一个node的链表反转的本身是自己
    if node.next == None:
        return node
    last = reverse(node.next)
    node.next.next = node  # 反转两个node的链表
    node.next = None  # 此时node在后面
    return last

# 反转前N个节点
def reverse(node, n):
    follow = None
    def reverseFront(node, n):
        if n == 1:
            follow = node.next
            return node
        last = rev
