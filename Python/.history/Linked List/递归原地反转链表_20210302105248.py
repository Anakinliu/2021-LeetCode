class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(node):
    # base case，链表只有一个 
    if node.next == None:
        return node