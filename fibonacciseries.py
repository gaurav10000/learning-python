def fib(n):
    a = 0
    b = 1
    print(a,b,end = " ")
    for i in range(n):
        c = a + b
        print(c , end=" ")
        a = b
        b = c
        
n = int(input("Enter number of terms of series: "))
fib(n)
        
print("Hello")
