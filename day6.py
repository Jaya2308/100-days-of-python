#program to find the quadrants in which the coordinates lie
x=int(input())
y=int(input())
if x > 0 and y > 0:
print('This point lies in the first quadrant')
elif x < 0 and y > 0:
print('This point lies in the second quadrant')
elif x < 0 and y < 0:
print('This point lies in the third quadrant')
elif x > 0 and y < 0:
print('This point lies in the fourth quadrant')
else: 
print('This point lies at the origin')
