class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(node):
    # base case，一个node
    if node.next == None:
        return node