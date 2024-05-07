import random
import time
from matplotlib import pyplot as plt
from Fitting import lin, quad, fit_data
def bubble_sort(L):
    n = len(L)          # no. of items in list
    for i in range(n):  # for every item
        for j in range(n):  # compare to every other item
            if L[i] < L[j]: # if out of order:
                L[i], L[j] = L[j], L[i] # swap items

# TODO: Add some code to generate lists for timing
L0 = []
n = 100
L = [random.randint(0, n) for i in range(n)]
n1 = 200
L1 = [random.randint(0, n1) for i in range(n1)]
n2 = 300
L2 = [random.randint(0, n2) for i in range(n2)]
n3 = 400
L3 = [random.randint(0, n3) for i in range(n3)]
n4 = 500
L4 = [random.randint(0, n4) for i in range(n4)]
n5 = 600
L5 = [random.randint(0, n5) for i in range(n5)]
n6 = 700
L6 = [random.randint(0, n6) for i in range(n6)]
n7 = 800
L7 = [random.randint(0, n7) for i in range(n7)]
n8 = 900
L8 = [random.randint(0, n8) for i in range(n8)]
n9 = 1000
L9 = [random.randint(0, n9) for i in range(n9)]

bubble_sort(L)
# TODO: Add some code to time functions
def time_function(func, args):
    start = time.time()
    func(args)
    time_taken = time.time()-start
    return time_taken
z = [L0, L, L1, L2, L3, L4, L5, L6, L7, L8, L9]
x = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
y1 = []
y = []
y_axis = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#print(x)
for i in z:
    y1.append(time_function(bubble_sort, i))
for j in y1:
    y.append(j*1000)

#print(y)
   
a = fit_data(lin, x, y)
b = fit_data(quad, x, y)

#print(y)
plt.figure()
plt.scatter(x, y, c='r', marker='x', label='function vs time')
plt.plot(x, a[2], c='b', label='best fit with lin')
plt.plot(x, b[2], c='g', label='best fit with quad')
plt.ylabel("running time (ms)")
plt.xlabel("length of list")
plt.ylim(0, 50)
plt.xlim(0, 1020)
plt.xticks(x)
plt.yticks(y_axis)
plt.legend()
#plt.show()
plt.savefig('bestfit.png')

