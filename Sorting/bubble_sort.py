import timeit
from timeit import Timer
import numpy as np

t1 = Timer("test1()","from __main__ import test1")

t2 = Timer("test2()","from __main__ import test2")

def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                """temp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = temp"""
                a_list[i],a_list[i+1] = a_list[i+1], a_list[i]

def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1

    while pass_num > 0 and exchanges:
        exchanges = False
        pass_num = len(a_list) -1
        for i in range(pass_num):
            if a_list[i] > a_list[i+1]:
                exchanges = True
                a_list[i],a_list[i+1] = a_list[i+1],a_list[i]

#a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a_list = np.array(range(1000))

def test1():       
    bubble_sort(a_list)
  
def test2():       
    short_bubble_sort(a_list)  

print(t2.timeit(number=1000))
print(t1.timeit(number=1000))

print(a_list) 
