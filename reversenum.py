from  timeit import default_timer as timer
def rev(n):
     r = 0
     while(n>=1):
         temp = n%10
         r = r*10 + temp
         n = n//10
        
     return(r)
    
a = int(input("Enter a number: "))
start = timer()
print(rev(a))
stop = timer()
print(stop-start)
