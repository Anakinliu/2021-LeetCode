class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = 10000
        self.next = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        i = 0
        node = self
        val = -1
        while node:
            if i == index:
                val = node.val
            i += 1
            node = node.next
        return val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val > 1000:
            self.val = val
        else:
            node = MyLinkedList()
            node.val = self.val
            node.next = self.next
            self.next = node
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
        if index == 0:
            self.addAtHead(val)
            return
        i = 0
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
        i = 0
        pre = self
        while pre and (i+1) != index:
            pre = pre.next
            i += 1
        if i+1 == index and pre:
            pre.next = pre.next.next


"""
["MyLinkedList","addAtHead","addAtTail","addAtHead","addAtTail",
"addAtHead","addAtHead","get","addAtHead","get","get","addAtTail"]
[[],[7],[7],[9],[8],[6],[0],[5],[0],[2],[5],[4]]
"""
# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList();
myLinkedList.addAtHead(7);
myLinkedList.addAtTail(7);
myLinkedList.addAtHead(9);
myLinkedList.addAtTail(8);
myLinkedList.addAtHead(6);
myLinkedList.addAtHead(0);
print('get', myLinkedList.get(5));           
# myLinkedList.addAtHead(0);
# print(myLinkedList.get(2));           
# print(myLinkedList.get(5));           
# myLinkedList.addAtTail(4);
            

t = myLinkedList
while t:
    print(t.val)
    t = t.next