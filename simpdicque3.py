f = open("abc.txt",'r')
g = open("xyz.txt",'w+')
h = open("fgh.txt",'w+')
s = f.read()
for i in s:
    if ord(i)>47 and ord(i)<58:
        h.write(i+" ")
    if ord(i)>96 and ord(i)<123 or ord(i)>64 and ord(i):
        g.write(i+" ")
g.seek(0)
h.seek(0)
print(g.read(),end = "\n")
print(h.read())
