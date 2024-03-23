import random

def Select_sort(lista):
    for i in range(len(lista) - 1):
        minimum_pos = i
        for y in range(i+1,len(lista) - 1,1):
            if(lista[y] < lista[i]):
                minimum_pos = y
        if(minimum_pos != i):
            temp = lista[i]
            lista[i] = lista[minimum_pos]
            lista[minimum_pos] = temp
    return lista
