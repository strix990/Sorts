def Insert_sort(lista):
    last_sorted_index = 0
    for _ in range(len(lista) -1):
        for x in range(last_sorted_index, -1,-1):
            if(lista[x+1] < lista[x]):
                temp = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = temp
        last_sorted_index += 1
    return lista
