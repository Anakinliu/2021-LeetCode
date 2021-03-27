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

def reverseN

head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)

head.next = n1
n1.next = n2

new = reverseAll(head)
while new:
    print(new.val)
    new = new.next

