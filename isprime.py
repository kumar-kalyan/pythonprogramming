# Write a program to check whether a number is prime or not.
print('program to check whether a number is prime or not \n')
a = int(input("Enter a number"))
flag = 0
m = a//2
for i in range(2, m+1):

    if(a % i == 0):
        flag = 1
if(flag == 0):
    print(a, 'is a prime number ', flag)
else:
    print(a, 'is not a prime number ', flag)
