class heap():
    def __init__(self,A):
        self.size = len(A)
        self.lenth = len(A)
        self.list = ['-inf',]
        self.list.extend(A)

LEFT = lambda i:2*i
RIGHT = lambda i:2*i+1
PARENT = lambda i:i//2

def max_heapify(A,i):
    l = LEFT(i)
    r = RIGHT(i)
    if l <= A.size and A.list[l] >A.list[i]:
        largest = l
    else:
        largest = i
    if r <= A.size and A.list[r] >A.list[largest]:
        largest = r
    if largest != i:
        A.list[i],A.list[largest] = A.list[largest],A.list[i]
        max_heapify(A,largest)

def build_max_heap(A):
    for i in range(A.lenth//2,0,-1):
        max_heapify(A,i)

def heapsort(A):
    build_max_heap(A)
    for i in range(A.lenth,1,-1):
        A.list[1],A.list[i] = A.list[i],A.list[1]
        A.size -= 1
        max_heapify(A,1)

A = [1,6,23,64,29,54,76,15,34]
B = heap(A)
heapsort(B)
print(B.list)
