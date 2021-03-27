# 我的解答
def mergeAlternately(word1, word2):
    res = []
    for a,b in zip(word1, word2):
        res.extend([a,b])
    if len(word1) < len(word2):
        res.append(word2[len(word1):])
    if len(word1) > len(word2):
        res.append(word1[len(word2):])
    return ''.join(res)

        def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res=''
        
        for i in range(min(len(word1),len(word2))):
            res += word1[i] + word2[i]
            
        return res + word1[i+1:] + word2[i+1:]