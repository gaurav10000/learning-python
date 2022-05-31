def isSorted(l):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return print("not sorted")
    return print("sorted")
l = [int(x) for x in input().split()]
isSorted(l)