class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_lst = []
        self.out_lst = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_lst.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.out_lst:
            while self.in_lst:
                self.out_lst.append(self.in_lst.pop())
        return self.out_lst.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.out_lst:
            while self.in_lst:
                self.out_lst.append(self.in_lst.pop())
        return self.out_lst[-1]



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # 两个都是空时队列才是空
        return not self.out_lst and not self.in_lst



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()