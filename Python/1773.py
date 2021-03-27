def countMatches(items, ruleKey, ruleValue):
    rule_dct = ['type','color','name']
    res = 0
    for item in items:
        idx = rule_dct.index(ruleKey)
        if item[idx] == ruleValue:
            res += 1
        pass
    return res 
