def merge(lista,sub1,sub2):
    i=j=0
    while i+j < len(lista):
        if j==len(sub2)or (i <len(sub1) and sub1[i] <sub2[j]):
            lista[i+j] = sub1[i]
            i+=1
        else:
            lista[i+j] = sub2[j]
            j+=1

def mergesort(lista):
    lenth = len(lista)
    if lenth < 2:
        return 
    cut = lenth // 2
    sub1 = lista[0:cut]
    sub2 = lista[cut:lenth]
    mergesort(sub1)
    mergesort(sub2)
    merge(lista,sub1,sub2)

lista = [12,43,13,51,65,15,75,24]
mergesort(lista)
print(lista)
