def fib(n):
    a = 1
    b = 1
    # print(a,b)
    for i in range(n):
        c = a + b
        print(1,1,c , end=" ")
        a = b
        b = c
        
n = int(input("Enter number of terms of series: "))
fib(n)
        

        