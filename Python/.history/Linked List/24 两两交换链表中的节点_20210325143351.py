class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head
    p = ListNode()
    p.next = head
    step = 2
    a = p  # a为带交换的两个节点的前一个节点
    s = p
    while p.next:
        step -= 1
        p = p.next
        if step == 0:
            step = 2
            b = p  # b为带交换的两个节点中右边的
            a.next.next = b.next
            b.next = a.next
            t = a.next
            a.next = b
            a = t
            p = t
            # print(p.val)
    return s.next