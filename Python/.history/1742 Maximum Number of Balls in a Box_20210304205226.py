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

"""
ball # --- box #
1 --------> 1
2 --------> 2
3 --------> 3
4 --------> 4
5 --------> 5
6 --------> 6
...
9 --------> 9
10 ------> 1
11 ------> 2
....
18 ------> 9
19 ------> 10
20 ------> 2
21 ------> 3
...
29 ------> 11
30 ------> 3
31 ------> 4
...
39 ------> 12
40 ------> 4
41 ------> 5
...
49 ------> 13
50 ------> 5
51 ------> 6
...
59 ------> 14
60 ------> 6
61 ------> 7
...
69 ------> 15
70 ------> 7
71 ------> 8
...
79 ------> 16
80 ------> 8
81 ------> 9
...
89 ------> 17
90 ------> 9
91 ------> 10
...
99 -----> 18
100 -----> 1
101 -----> 2
"""
# @rock
def countBalls2(self, lowLimit: int, highLimit: int) -> int:
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