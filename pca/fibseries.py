# Write a program to display the Fibonacci series up to a range. Fibonacci numbers are 0, 1, 1,
print('Write a program to display the Fibonacci series up to a range. Fibonacci numbers are 0, 1, 1,')
n = int(input('Enter a range \n'))
f1 = 0
f2 = 1
print(f1,'\n',f2)
for i in range(2, n):
    f = f1+f2
    print(f)
    f1 = f2
    f2 = f
