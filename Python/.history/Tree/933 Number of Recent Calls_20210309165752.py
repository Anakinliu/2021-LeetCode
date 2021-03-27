["RecentCounter","ping","ping","ping","ping","ping"]
[[],[642],[1849],[4921],[5936],[5957]]

class RecentCounter:

    def __init__(self):
        self.left = 0
        self.lst = []
        self.right = 0

    def ping(self, t: int) -> int:
        if self.lst:
            while self.lst[self.left] < t-3000:
                    self.left += 1
            self.right += 1
        self.lst.append(t)
        return self.right - self.left + 1