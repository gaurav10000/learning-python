dic = {}
n = 5
for _ in range(n):
    dic.update({input():int(input())})
for i in dic.items():
    print(i)
print("Average of marks is: ",sum(dic.values())/n)
