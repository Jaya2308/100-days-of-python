#sum on n natural numbers
num = int(input('Enter a number:'))
if num < 0:
   num = input('invalid number give a positive value')
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum of the natural numbers is:", sum)
