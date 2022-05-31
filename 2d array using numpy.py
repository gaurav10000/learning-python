import numpy as np
print("Please enter rows and columns of array seperated by space")
m,n = map(int,input().split())
print("Please enter number seperated by spaces suitable for the size you enterd!")
arr = np.array([int(x) for x in input().split()])
arr = arr.reshape(m,n)
for i in arr:
    m = max(i)
    l = list(i)
    ind = l.index(max(i))
    i[ind],i[-1] = i[-1],i[ind]
print(arr)