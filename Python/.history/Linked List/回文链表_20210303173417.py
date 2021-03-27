# https://labuladong.gitee.io/algo/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/%E5%88%A4%E6%96%AD%E5%9B%9E%E6%96%87%E9%93%BE%E8%A1%A8.html
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
1. 【后序遍历】链表，可以得到反转链表的值
"""
def traverse(node):
    if node:
        traverse(node.next)
        print(node.val)

"""
2. 将栈里的节点与 left 做对比
"""
left = None
def isHuiWen(head):
    global left
    left = head
    return trav(head)

# 相当于一个栈, 递归调用需要O(N)的空间，时间复杂度
def trav(head):
    if not head:
        return True
    res = trav(head.next)
    global left
    if res and head.val == left.val:
        left = left.next
        return True
    else:
        return False

"""
3 快慢指针
"""
# 迭代方法，需要时间O(N)，空间O(1)
def findMidNode(head):
    if not head:
        return
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    if fast:  # 链表包含奇数个节点时，slow需要是中间靠后一个
        slow = slow.next
    return slow
# 迭代方法，需要时间O(N)，空间O(1)
def reverseAll(head):
    if not head:
        return None
    pre = None
    cur = head
    nxt = head
    while cur != None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre

def isHuiWen2(head):
    mid_node = findMidNode(head)
    left = head
    right = reverseAll(mid_node)
    # print(left.val)
    # print(right.val)
    # print()
    # 迭代方法，需要时间O(N)，空间O(1)
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    left.next = mid_node
    return True

head = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(5)
n3 = ListNode(5)
n4 = ListNode(3)
n5 = ListNode(1)


head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# traverse(head)
# print(isHuiWen(head))
# print(findMidNode(head).val)
# new = reverseAll(head)
# while new:
#     print(new.val)
#     new = new. next
print(isHuiWen2(head))
# 原链表是否被改变
new = head
while new:
    print(new.val)
    new = new. next