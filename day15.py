import math
num=int(input("Enter a number: "))
Sum=0
fact=1
a=num
if(num==0):
    Sum=Sum+fact
else:
    while(a!=0):
        rem=a%10
        fact=math.factorial(rem)
        Sum=Sum+fact
        a=a//10
if(Sum==num):
    print("Strong number")
else:
    print("Not a strong number")
        
    
    
