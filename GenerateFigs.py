from matplotlib import pyplot as plt        # import plotting funcs
from TimeFunctions import  time_function    # import the time function you will write
from Duplicates import has_duplicates_1     # import the has_duplicates functions you are interested in
from Duplicates import has_duplicates_2

# All code below is included as a demo. Feel free to change any of it.

##### Initialize datasets
# Pick 3 x-values
#x = [100, 500, 1000]
x = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]



##### Measure the running times
# Generate 3 corresponding y-values
y1 = []
y2 = []
y1_1 = []
y2_1 = []
for n in x:
    L = [i for i in range(n)] # Worst case: A list with no duplicates
    y1.append(time_function(has_duplicates_1, L)) # append running time to y

for m in x:
    L = [j for j in range(n)]
    y2.append(time_function(has_duplicates_2, L))

for i in y1:
    y1_1.append(i * 1000)
for j in y2:
    y2_1.append(i * 1000)
##### Plot datasets
plt.figure()                                                        # create a new figure
plt.scatter(x, y1, c='r', marker='x', label='has_duplicates_1')     # add scatter plot to figure
#plt.scatter(x, y2, c='b', marker ='d', label='has_duplicates_2')
plt.ylabel("running time (s)")# label y axis
plt.xlabel("number of items") #label x axis

plt.legend()                                                        # add legend to figure
#plt.show()                                                          # show figure on local computer
plt.savefig('fig_1.png')                                          # save figure

scale_factor = 1000
plt.figure()
plt.scatter(x, y1, c ='r', marker = 'x', label = 'has_duplicates_1')
plt.scatter(x, y2, c='b', marker='d', label='has_duplicates_2')
plt.ylabel("running time (s)")
plt.xlabel("number of items")
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
plt.ylim(0, 0.05)
plt.xlim(0, 1000)

plt.legend()
plt.show()
#plt.savefig('dups.png')
# Note: You can either use plt.show() or plt.savefig(). Using both does not work.



