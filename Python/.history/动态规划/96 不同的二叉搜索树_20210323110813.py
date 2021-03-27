def numTrees(n):
    dp_table = [0] * n
    dp_table[0] = 1
    dp_table[1] = 2
    