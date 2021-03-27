class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(node):
    # base case，只有一个node的反转的本身是自己
    if node.next == None:
        return node