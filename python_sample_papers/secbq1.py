l = [int(x) for x in input().split()]
d = {x:l.count(x) for x in l}
print(max(d.values()))
