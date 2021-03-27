class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if 