import timeit
import random as rn

def min_1(the_list):
    """An implementation of finding the minimum element using double for loops.
    O(n^2)"""
    min_elem = 0
    max_diff = 10000
    for each_elem in the_list:
        for inner_elem in the_list:
            diff = each_elem - inner_elem
            rel_diff = 10000 + diff
            if rel_diff < 10000 and rel_diff < max_diff:
                    min_elem = each_elem
                    max_diff = rel_diff
                
    return(min_elem)


def min_2(the_list):
    """An implementation of finding the minimum element using a single for loop.
    O(n)"""
    the_list.sort()
    return(the_list[0])


the_list = [rn.randint(0,1000) for i in range(1000)]
t = timeit.Timer("min_1(the_list)","from __main__ import the_list,min_1")


time = t.timeit(number=1)
print(time)
