# 我的解答
def mergeAlternately(sword1, word2):
    res = []
    for a,b in zip(word1, word2):
        res.extend([a,b])
    if len(word1) < len(word2):
        res.append(word2[len(word1):])
    if len(word1) > len(word2):
        res.append(word1[len(word2):])
    return ''.join(res)