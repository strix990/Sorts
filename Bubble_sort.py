def Bubble_sort(lista):
    lista_swapped = [False for _ in range(len(lista))]
    while(True):
        swapped = False
        for i in range(len(lista)-1):
            if(lista_swapped[i+1]):
                break
            elif(lista[i] > lista[i+1]):
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i + 1] = temp
                swapped = True
        if(not swapped):
            return lista
        lista_swapped[i+1] = True
