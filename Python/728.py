def selfDividingNumbers(left, right):
    res = []
    for n in range(left, right):
        s_n = str(n)
        ok = True
        for d in s_n:
            if d == '0':
                ok = False
                break
            if n % d != 0:
                ok = False
                break
        if ok:
            res.append(n)
    return 

# @PiscesDream
def selfDividingNumbers2(left, right):
    # 用and的短路效果判断i是否为0
    return [x for x in range(left, right+1) if all(int(i) and x%int(i)==0 for i in str(x))]

def selfDividingNumbers3(left, right):
    return [x for x in range(left, right+1) if all(i and x%i==0 for i in map(int, str(x)))]

print(selfDividingNumbers3(1,22))

