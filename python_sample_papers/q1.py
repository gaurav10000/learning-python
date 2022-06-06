s = input()
for i in s.split():
    for j in range(len(i)-1,-1,-1):
        print(i[j],end = "")
    print(" ",end = "")
