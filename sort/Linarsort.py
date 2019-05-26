def coutingsort(A,k,m):
    C = [0]*k
    B = [0]*len(A)
    for j in range(0,len(A)):
        C[int(A[j][m])] += 1
    for i in range(1,k):
        C[i] = C[i-1] + C[i]
    for j in range(len(A)-1,-1,-1):
        B[C[int(A[j][m])]-1] = A[j]
        C[int(A[j][m])] -= 1
    return B
    
def radixsort(A,d,radix):
    for i in range(d-1,-1,-1):
        A = coutingsort(A,radix,i)
    return A

A = ['16432','56431','11636','48656','48653','21456','71342']
B = radixsort(A,len(A[0]),10)
print(B)