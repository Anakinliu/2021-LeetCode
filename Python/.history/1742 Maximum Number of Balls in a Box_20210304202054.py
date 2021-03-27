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
