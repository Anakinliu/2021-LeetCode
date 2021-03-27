# https://labuladong.gitee.io/algo/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/%E5%88%A4%E6%96%AD%E5%9B%9E%E6%96%87%E9%93%BE%E8%A1%A8.html
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverse(node):
    if node:
        print(node.val)
        r = traverse(node.next)

head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
n3.next = None