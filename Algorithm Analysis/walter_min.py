import timeit
import random as rn

def min_walter(the_list):
    for i in range(len(the_list)-1):
        for j in range(len(the_list)-1):
            if the_list[j] < the_list[j+1]:
                flag = the_list[j]
                the_list[j] = the_list[j+1]
                the_list[j+1] = flag

    return(the_list[len(the_list)-1])


the_list = [rn.randint(0,10) for i in range(10000)]
print(the_list)
t = timeit.Timer("min_walter(the_list)","from __main__ import the_list,min_walter")

time = t.timeit(number=1)
print(time)



