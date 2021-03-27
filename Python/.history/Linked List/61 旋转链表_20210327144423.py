def rotateRight(head,):
    if not head:  # 0 node
        return None
    if not head.next:  # 1 node
        return head
    # 链表中节点的数目在范围 [0, 500] 内
    # 0 <= k <= 2 * 10^9
    a,b = head,head
    count = 1
    while b.next:
        count += 1
        b = b.next
    k = k % count
    if k == 0:
        return head
    else:
        k = count - k - 1
        while k > 0:
            a = a.next
            k -= 1
        res = a.next
        a.next = None
        b.next = head
        return res