class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseAll(node):
    if not node:
        return None
    pre = None
    cur = node
    nxt = node
    while cur != None:
        nxt = cur.next
        