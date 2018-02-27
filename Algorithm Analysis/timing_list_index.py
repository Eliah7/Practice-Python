import timeit
import matplotlib.pyplot as plt 

x = list(range(10))
timer = list()
for i in x:
    t = timeit.Timer("x[%d]" % i,"from __main__ import x")
    time = t.timeit(number=1000)
    timer.append(time)
    print("%d, %10.40f"% (i,time))

plt.title('Index operator is O(1)')
plt.ylabel('time taken for each index')
plt.xlabel('index in list')
plt.scatter(x,timer)
plt.show()
