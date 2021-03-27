def findTarget(root, k):
    lst = []
    def toLst(root):
        if root:
            toLst