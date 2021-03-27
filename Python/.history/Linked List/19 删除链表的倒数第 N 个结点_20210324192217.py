class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    gap = n  # 快慢指针之间的差距，
    p = ListNode(head.val)  #  
    p.next = head
    fast, slow = p,p
    while fast:  # 要使得fast到达null时，slow指向待删除的节点的前一个
        if gap < 0:
            slow = slow.next
        fast = fast.next
        gap -= 1
    # print(slow.val)
    if slow.next:
        slow.next = slow.next.next
    return p.next