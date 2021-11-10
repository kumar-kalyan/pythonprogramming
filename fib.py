# Write a program to display the Fibonacci numbers.
print("program to display the Fibonacci numbers \n")
a = int(input('Enter the limit : '))
f1, f2 = 0, 1
print(f1,'\n',f2,'\n')
for i in range(2, a):
    temp = f1+f2
    print(temp,'\n')
    f1 = f2
    f2 = temp
