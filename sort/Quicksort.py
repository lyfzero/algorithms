def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] < x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[r],A[i+1] = A[i+1],A[r]
    return i+1

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,p+1,r)

S = [12,43,61,65,23,71,23,16,56]
quicksort(S,0,len(S)-1)
print(S)