def sumOfUnique(nums):
    nums_dct = dict()
    for n in nums:
        if n not in nums_dct.keys():
            nums_dct[n] = 1
        else:
            nums_dct[n] += 1
    res = 0
    for k,v in nums_dct.items():
        if v == 1:
            res += k
    return res