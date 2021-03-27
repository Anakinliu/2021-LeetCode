def countBalls(lowLimit, highLimit):
    count = dict()
    for n in range(lowLimit, highLimit+1):
        n_str = str(n)
        s = sum(map(int, list(n_str)))
        if count
