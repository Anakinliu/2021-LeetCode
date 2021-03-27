class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 先中序转为有序数组，再用双指针法查找
# 时间复杂度O(N)+O(N)，空间O(N)+O(1)
def findTarget(root, k):
    lst = []
    def toLst(root):
        if root:
            toLst(root.left)
            lst.append(root.val)
            toLst(root.right)
    left = 0
    right = len(lst) - 1
    while left < right:
        if lst[left] + lst[right] < k:
            left += 1
        if lst[left] + lst[right] > k:
            right -= 1
    if lst[left] + lst[right] == k:
        return True
    return False

def findTarget2(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False