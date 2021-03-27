def sortArrayByParity(A):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] % 2 == 1 and A[j] % 2 == 0