#program to reverse the given number
n=int(input())
i=0
while i<n:
    a=n
    n=int(n/10)
    dr=a%10
    print(dr,end="")
    
