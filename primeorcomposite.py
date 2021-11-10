print('Write a program to take input a number and check if the number is a prime or composite number')
n = int(input("Enter a number"))
flag = 0
for i in range(2, n):
    if(n % i == 0):
        flag += 1
if(n == 1):
    print('1 is neither composite nor a prime number')
elif(flag >= 1):
    print(n, ' is a composite number')
else:
    print(n, ' is a prime number')
