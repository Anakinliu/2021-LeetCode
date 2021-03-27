# 我的解答
def countBalls(lowLimit, highLimit):
    d = dict()
    for n in range(lowLimit, highLimit+1):
        n_str = str(n)
        s = sum(map(int, list(n_str)))
        if s not in d.keys():
            d[s] = 1
        else:
            d[s] += 1
    return max(d.values())

def countBalls(self, lowLimit: int, highLimit: int) -> int:
    box = [0] * 46
    lo, id = lowLimit, 0
    while lo > 0:
        id += lo % 10
        lo //= 10
    box[id] += 1
    for i in range(lowLimit + 1, highLimit + 1):
        while i % 10 == 0:
            id -= 9
            i //= 10
        id += 1
        box[id] += 1
    return max(box)