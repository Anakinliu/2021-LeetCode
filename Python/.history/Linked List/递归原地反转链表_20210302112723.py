class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 反转整个列表,返回新的头结点
def reverseAll(node):
    # base case，只有一个node的链表反转的本身是自己
    if node.next == None:
        return node
    last = reverseAll(node.next)
    node.next.next = node  # 反转两个node的链表
    node.next = None  # 此时node在后面
    return last

# 反转前N个节点, 以 node 为起点的 n 个节点，返回新的头结点
"""
相比整个反转：
1、base case 变为 n == 1，反转一个元素，就是它本身，同时要记录后驱节点。

2、刚才我们直接把 head.next 设置为 null，
因为整个链表反转后原来的 head 变成了整个链表的最后一个节点。
但现在 head 节点在递归反转之后不一定是最后一个节点了，
所以要记录后驱 successor（第 n + 1 个节点），反转之后将 head 连接上。
"""
follow = None
def reverseFront(node, n):
    if n == 1:
        follow = node.next
        return node
    last = reverseFront(node.next, n-1)
    node.next.next = node
    node.next = follow  # 让反转之后的 head 节点和后面的节点连起来
    return last  # 新的头结点

# 
"""
如果 m != 1 怎么办？如果我们把 head 的索引视为 1，
那么我们是想从第 m 个元素开始反转对吧；如果把 head.next 
的索引视为 1 呢？那么相对于 head.next，
反转的区间应该是从第 m - 1 个元素开始的；那么对于 head.next.next 呢……
"""
def reverseBetween(node, m, n):
    if m == 1:
        reverseFront(node, n)
    reverseBetween(node.next, m-1, n-1)