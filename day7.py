#a program to find Number of days in a given month of a given year
month=int(input("Enter the number of the month"))
year=int(input("Enter the year"))
if(month == 2 and (year%400 == 0) or ((year%100 != 0) and (year%4 == 0))):
    print('Number of days is 29')
elif(month == 2):
    print('Number of days is 28')
elif(month == 1 or 3 or 5 or 7 or 8 or 10 or 12):
    print('Number of days is 31')
else:
    print('Number of days is 30')
    
