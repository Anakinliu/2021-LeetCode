def sortArrayByParity(A):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] & 1 == 0:
            i += 1
        if A[j] & 1 == 1:
            j -= 1
        if A[i] & 1 == 1 and A[j] & 1 == 0:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    return A

print(sortArrayByParity([9,10,11,12,13,3,1,2,4,5,6,7,8]))
