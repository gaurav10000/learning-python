f = open("sample.txt","r")
l = f.readlines()
for i in l:
    x = i.strip()
    if x[0]in["a","A"]:
        print(i)


