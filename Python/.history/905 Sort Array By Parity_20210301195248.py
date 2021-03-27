def sortArrayByParity(A):
    i = 0
    j = len(A) - 1
    while i < j:

        if A[i] & 1 == 0:
            i += 1
        if A[i] & 1 == 1:
            j -= 1
    return A

print(sortArrayByParity([3,1,2,4]))