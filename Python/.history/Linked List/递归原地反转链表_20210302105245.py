class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(node):
    # base case， 
    if node.next == None:
        return node