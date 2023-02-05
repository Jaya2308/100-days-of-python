#a program to find Sum of digits of a number
n=int(input())
while n>0:
    x=int(n/10)
    di=n%10
    sum=x+di
    print(sum)
    break
    
