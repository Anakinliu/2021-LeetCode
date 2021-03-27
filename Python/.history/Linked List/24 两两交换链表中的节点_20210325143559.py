class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
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

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
res = swapPairs(n1)
while res:
    print(res.val)
    res = res.next