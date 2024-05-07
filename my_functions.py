import numpy as np
import random

class my_float(float):
    comparison_counter = 0

    def __eq__(self, other):
        my_float.comparison_counter += 1
        return super().__eq__( other)

    def __ne__(self, other):
        my_float.comparison_counter += 1
        return super().__ne__(other)

    def __lt__(self, other):
        my_float.comparison_counter += 1
        return super().__lt__(other)

    def __le__(self, other):
        my_float.comparison_counter += 1
        return super().__le__(other)

    def __gt__(self, other):
        my_float.comparison_counter += 1
        return super().__gt__(other)

    def __ge__(self, other):
        my_float.comparison_counter += 1
        return super().__ge__(other)

    # Add the other required magic methods

def my_generate_monotonic_matrix(size):
    n = size
    matrix = []
    Q = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            Q[i,j] = (i+j)
    return Q
    # Write your code that for a given size generates a square
    # row-column monotonic matrix
    pass

# Do not modify the function generate_monotonic_matrix
def generate_monotonic_matrix(size):
    n = size;
    Q = np.full([n, n], my_float)

    S_row_0 = 0
    for i in range(n):
        for j in range(n):
            delta = random.random()

            if (i == 0):
                S_row_0 += delta
                Q[i, j] = my_float(round(S_row_0, 1))
            elif (i != 0 and j == 0):
                Q[i, j]  = my_float(round(Q[i-1, j] + delta, 1))
            elif (i != 0 and j != 0):
                Q[i, j] = my_float(round(max(Q[i-1, j], Q[i, j-1]) + delta,1))

    return Q

def my_search_linear(Q, item):
   # new_Q = list(Q)
   # Implement a simple element-by-element search from left to right and top to bottem
   if item in Q:
       return True
   
   pass

def my_search(Q, item):

   # Implement an efficient version of the search for an element in a row-column
   # monotonic matrix Q
   if item in Q:
       return True
   pass
