"""
["RecentCounter","ping","ping","ping","ping","ping"]
[[],[642],[1849],[4921],[5936],[5957]]
"""

class RecentCounter:
    def __init__(self):
        self.left = 0  # 在当前范围内的索引
        self.lst = []  # 保存所有t
        self.right = 0

    def ping(self, t):
        if self.lst:
            while self.left <= self.right and self.lst[self.left] < t-3000:
                    self.left += 1
            self.right += 1
        self.lst.append(t)
        # print(self.left, self.right)
        return self.right - self.left + 1


class RecentCounter2:
    def __init__(self):
        self.lst = []  # 队列

    def ping(self, t):
        if self.lst:
            if 
        self.lst.append(t)
        return 


rc = RecentCounter2()
lst = [[642],[1849],[4921],[5936],[5957]]
for i in lst:
    print(rc.ping(i[0]))
