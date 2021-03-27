https://labuladong.gitee.io/algo/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/k%E4%B8%AA%E4%B8%80%E7%BB%84%E5%8F%8D%E8%BD%AC%E9%93%BE%E8%A1%A8.html# 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 反转整个
def reverseAll(node):
    if not node:
        return None
    pre = None
    cur = node
    nxt = node
    while cur != None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre

# 反转前 N 个节点，反转整个链表可以视为end为None
def reverseN(head, end):
    if not head:
        return None
    pre = None
    cur = head
    nxt = head
    while cur != end:  # 这里改了
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre

# leetcode 25. Reverse Nodes in k-Group
def reverseKGroup(head, k):
    if not head:
        return None
    # print(head.val)
    left = head
    right = head
    i = 1
    while i <= k:
        if not right:
            return head
        right = right.next
        i += 1
    # print(left.val)
    # print(right.val)
    new_head = reverseN(left, right)
    # print(new_head.val)
    left.next = reverseKGroup(right, k)
    return new_head


head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
n3.next = None

head.next = n1
n1.next = n2
n2.next = n3

# new = reverseAll(head)
# new = reverseN(n2, None)
new = reverseKGroup(head, 2)
while new:
    print(new.val)
    new = new.next

