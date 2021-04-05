# 2 5 7 => 27 
def do(n):
    t = [999] * (n+1)
    t[0] = 999
    t[1] = 999
    t[3] = 999
    t[4] = 2
    t[6] = 3

    t[7] = 1
    t[2] = 1
    t[5] = 1
    t_n = len(t)
    for i in range(8, t_n):
        t[i] = min(t[i-2], t[i-5], t[i-7]) + 1
    return t

print(do(27))


