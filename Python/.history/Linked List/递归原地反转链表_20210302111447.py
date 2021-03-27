class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 反转整个列表
def reverseAll(node):
    # base case，只有一个node的链表反转的本身是自己
    if node.next == None:
        return node
    last = reverseAll(node.next)
    node.next.next = node  # 反转两个node的链表
    node.next = None  # 此时node在后面
    return last

# 反转前N个节点,// 反转以 head 为起点的 n 个节点，返回新的头结点
follow = None
def reverseFront(node, n):
    if n == 1:
        follow = node.next
        return node
    last = reverseFront(node.next, n-1)
    node.next.next = node
    node.next = follow
    return last
