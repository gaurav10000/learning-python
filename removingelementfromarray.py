import array as np
a = np.array('i',[int(x) for x in input().split()])
# b = np.array([])
x = int(input("Enter number: "))
for i in a:
    if i>=x:
        a.remove(i)
print(a)
