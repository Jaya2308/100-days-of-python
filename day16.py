#a program to identify if the number is Perfect number or not
num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if(sum==num):
    print("Perfect Number")
else:
    print("Not a perfect number")
