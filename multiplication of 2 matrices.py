import numpy as np
while True:
    r1,c1 = map(int,input("Enter r1 and c1:").split())
    r2,c2 = map(int,input("Enter r2 and c2:").split())
    if c1==r2:
        break
    else:
        print("Matrices of gievn order cannot be multiplied.Please again:")
print(f"Enter {r1*c1} elements of 1st matrix\n")
m1 = np.array([int(x) for x in input().split()])
m1 = m1.reshape(r1,c1)
print(f"Enter {r2*c2} elements of 2nd matrix\n")
m2 = np.array([int(x) for x in input().split()])
m2 = m2.reshape(r2,c2)
print(m1)
print(m2)
print(np.dot(m1,m2))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
