print('Write a program to check if the year entered by the user is a leap year or not.\n')
year = int(input('Enter a year '))
flag = False
if(year % 400 == 0 ):
    flag=True
elif (year % 100 == 0):
    flag=False
elif (year % 4 == 0 ):
    flag= True
else:
    flag=False

print(year, 'is a leap year ') if flag else print(year, 'is not a leap year ')