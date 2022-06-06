l = [int(x) for x in input().split()]
result = [0,0]
for i in l:
    if i%2:
        result[0] += i**2
    else:
        result[1] += i**2
print(result)
