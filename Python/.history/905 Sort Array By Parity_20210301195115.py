def sortArrayByParity(A):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] & 1 == 1 and A[j] & 1 == 0:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1