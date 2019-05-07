def merge(sub1,sub2):
    i=j=0
    lista = []
    while i < len(sub1) and j < len(sub2):
        if sub1[i] < sub2[j]:
            lista.append(sub1[i])
            i+=1
        else:
            lista.append(sub2[j])
            j+=1
    if i >= len(sub1):
        lista.extend(sub2[j:])
    else:
        lista.extend(sub1[i:])
    return lista

def mergesort(lista):
    lenth = len(lista)
    if lenth < 2:
        return lista
    cut = lenth // 2
    sub1 = mergesort(lista[:cut])
    sub2 = mergesort(lista[cut:])
    listb = merge(sub1,sub2)
    return listb

lista = [12,43,13,51,65,15,75,24]
listb=mergesort(lista)
print(listb)