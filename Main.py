from Bubble_sort import Bubble_sort
from Insert_sort import Insert_sort
from Select_sort import Select_sort
from Merge_sort import Merge_sort
import timeit
import copy
import random

def Call_sorting(i, lista):
    if(i == 1):
        Bubble_sort(lista)
    if(i == 2):
        Insert_sort(lista)
    if(i == 3):
        Select_sort(lista)
    if(i == 4):
        Merge_sort(lista)

def Main():
    Num_tests = 10000
    Num_algorithms = 4
    teste_lista = [random.randint(0, 1000) for _ in range(20)]
    time = [0 for _ in range(Num_algorithms)]
    for i in range(Num_algorithms):
        for _ in range(Num_tests):
            teste_run_lista = copy.deepcopy(teste_lista)
            start = timeit.default_timer()
            Call_sorting(i, teste_run_lista)
            time[i] += timeit.default_timer() - start
    print("Mean time for Bubble sort: " + str(time[0]/Num_tests))
    print("Mean time for Insert sort: " + str(time[1]/Num_tests))
    print("Mean time for Select sort: " + str(time[2]/Num_tests))
    print("Mean time for Merge sort: " + str(time[3]/Num_tests))

Main()
