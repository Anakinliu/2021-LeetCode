# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.inorder_stack = []
        self.idx = 0
        self.inorder()
    # 中序遍历迭代
    def inorder(self):
        p = self.root
        stack = []
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                self.inorder_stack.append(p.val)
                p = p.right

    def next(self) -> int:
        res = self.inorder_stack[self.idx]
        self.idx += 1
        return res

    def hasNext(self) -> bool:
        print(self.idx, len(self.inorder_stack))
        if self.idx < len(self.inorder_stack):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class BSTIterator2:
    
    def __init__(self, root: TreeNode):
        self.cur = root
        self.stack = []

    def next(self) -> int:
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        res = self.cur.val
        self.cur = self.cur.right
        return res

    def hasNext(self) -> bool:
        return self.stack or self.cur