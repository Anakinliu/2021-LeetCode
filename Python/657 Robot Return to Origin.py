# 我的
def judgeCircle(moves):
    # 1 <= moves.length <= 2 * 104
    # 'U', 'D', 'L' and 'R'
    d = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    idx = 0
    p = [0,0]  # 用两个变量分别表示也行
    end = len(moves)
    while idx < end:
        p[0] += d[moves[idx]][0]
        p[1] += d[moves[idx]][1]
    if p != (0,0):
        return False
    else:
        return True

# aditya74 计算相反方向的数量是否相同
def judgeCircle2(moves): 
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
