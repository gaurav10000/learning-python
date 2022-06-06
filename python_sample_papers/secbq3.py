a,b,c = [int(x) for x in input().split()]
x = [(-b + ((b**2) - (4*a*c))**0.5)/(2*a) , (-b - ((b**2) - (4*a*c))**0.5)/(2*a)]
print(f"x = {x[0]},{x[1]} ")