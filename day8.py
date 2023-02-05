#a program to find roots of a quadratic equation
import math
a=int(input())
b=int(input())
c=int(input())
if a==0 :
    print("it is not possible")
else:
    x=b**2-4*a*c
    d=math.sqrt(abs(x))
    if x>0:
        print("real and distinct roots")
        print((-b+x)/2*a)
        print((-b-x)/2*a)
    elif x==0:
        print("real and equal")
        print(-b/2*a)
    else:
        print("imaginary roots")
        print(-b/2*a,"+i",x)
        print(-b/(2*a),"- i",x)
