def Merge_sort(lista):
    if(len(lista) <= 1):
        return lista
    else:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        left = Merge_sort(left)
        right = Merge_sort(right)
        return Merge(left, right)

def Merge(left, right):
    ret_list = []
    l_index = 0
    r_index = 0
    while(l_index < len(left) or r_index < len(right)):
        if(l_index == len(left)):
            ret_list.append(right[r_index])
            r_index += 1
        elif(r_index == len(right)):
            ret_list.append(left[l_index])
            l_index += 1
        elif(left[l_index] < right[r_index]):
            ret_list.append(left[l_index])
            l_index += 1
        elif(left[l_index] > right[r_index]):
            ret_list.append(right[r_index])
            r_index += 1
    return ret_list
        