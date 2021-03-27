class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(root):
        def link2(n1, n2):
            
            n1.next = n2

            link2(n1.left, n2.right)
            link2(n2.left, n2.right)
            link2(n1.)