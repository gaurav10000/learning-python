import numpy as np
x,y = [int(x) for x in input("Enter order of matrix: ").split()]
a = np.array([int(x) for x in input(f"Enter {x*y} elements of array 1: ").split()])
# a2 = np.array([int(x) for x in input(f"Enter {x*y} elements of array 2: ").split()])
a = a.reshape(x,y)
# a2 = a2.reshape(x,y)
for i in a:
    max = max(i)
    i
