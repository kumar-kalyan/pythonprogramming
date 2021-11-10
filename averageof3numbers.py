# Write a program to find average of three numbers.
print('program to find average of three numbers \n')
num = []
for i in range(3):
    print('Enter the ', i, ' number ')
    x = int(input())
    num.append(x)

print('Input given by user \n',num)
sum = 0
for l in num:
    sum= sum+l 

avg=sum/3

print('The average of given numbers is ', avg)
