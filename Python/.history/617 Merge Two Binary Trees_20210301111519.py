# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    if root1 == None and root2 == None:
        return None
    if root1 == None:
        return root2
    if root2 == None:
        return root1
    queue = [[root1, root2]]
    new = []
    while queue:
        a, b = queue.pop(0)
        if a and b:
            # print(a.val + b.val)
            new.append(a.val + b.val)
            queue.append([a.left, b.left])
            queue.append([a.right, b.right])
        elif a:
            # print(a.val)
            new.append(a.val)
            queue.append([a.left, None])
            queue.append([a.right, None])
        elif b:
            # print(b.val)
            new.append(b.val)
            queue.append([None, b.left])
            queue.append([None, b.right])
        else:
            new.append(None)
    new = new[:7]
    print(new)
    # 根据层次遍历得到的结果，构造二叉树
    def insertLevelOrder(arr, root, i, n): 
        
        # Base case for recursion  
        if i < n: 
            temp = TreeNode(arr[i])  
            root = temp  
    
            # insert left child  
            root.left = insertLevelOrder(arr, root.left, 
                                        2 * i + 1, n)  
    
            # insert right child  
            root.right = insertLevelOrder(arr, root.right, 
                                        2 * i + 2, n) 

        return root 
 
    root3 = None
    root3 = insertLevelOrder(new, root3, 0, len(new)) 


# @ming_han
def mergeTrees2(self, t1, t2):
    """
    把t2合并到t1上
    """
    if t1 is None:
        return t2
                    
    stack = []
    stack.append((t1,t2))
    while stack:
        t = stack.pop()
        if t[1] is None:  # 把t2合并到t1上
            continue
        t[0].val += t[1].val
        
        if t[0].left is None:
            t[0].left = t[1].left
        else:
            stack.append((t[0].left,t[1].left))
        
        if t[0].right is None:
            t[0].right = t[1].right
        else:
            stack.append((t[0].right,t[1].right))
    return t1
          

n4 = TreeNode(5,None,None)
n3 = TreeNode(2,None,None)
n2 = TreeNode(3,n4,None)
n1 = TreeNode(1,n2,n3)

m5 = TreeNode(7,None,None)
m4 = TreeNode(4,None,None)
m3 = TreeNode(3,None,m5)
m2 = TreeNode(1,None,m4)
m1 = TreeNode(2,m2,m3)
mergeTrees(n1,m1)
        
