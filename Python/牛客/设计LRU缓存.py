def LRU(operators , k ):
    # write code here
    max_len = k
    keys = []
    d = dict()
    for ope in operators:
        if len(ope) == 3:
            # 添加，考虑是否超过缓存大小
            if len(keys) == max_len:
                to_del = keys.pop(0)
                del d[to_del]
            keys.append(ope[1])
            d[ope[1]] = ope[2]
        if len(ope) == 2:
            if ope[1] in keys:
                print(d[ope[1]])
            else:
                print(-1)

LRU([[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3)