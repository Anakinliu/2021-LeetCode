# https://labuladong.gitee.io/algo/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/%E5%88%A4%E6%96%AD%E5%9B%9E%E6%96%87%E9%93%BE%E8%A1%A8.html
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 【后序遍历】链表，可以得到反转链表的值
def traverse(node):
    if node:
        traverse(node.next)
        print(node.val)

def isHuiWen

head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)

head.next = n1
n1.next = n2
n2.next = n3

traverse(head)