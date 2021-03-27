class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = 0
        self.next = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        i = 0
        node = self.next
        val = -1
        while node:
            if i == index:
                val = node.val
            else:
                i += 1
                node = node.next
        return val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.val = val
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self
        while node and node.next:
            node = node.next
        last = MyLinkedList()
        last.val = val
        node.next = last
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            return
        i = -1
        pre = self
        while pre and (i+1) != index:
            pre = pre.next
            i += 1
        if i+1 == index and pre:
            nt = pre.next
            node = MyLinkedList()
            node.val = val
            node.next = nt
            pre.next = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return
        i = -1
        pre = self
        while pre and (i+1) != index:
            pre = pre.next
            i += 1
        if i+1 == index and pre:
            pre.next = pre.next.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
# obj.deleteAtIndex(0)

t = obj
while t:
    print(t.val)
    t = t.next