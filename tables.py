# Write a program to print the multiplication table of a given number. The number has to be entered by the
# user.
print('Write a program to print the multiplication table of a given number \n')
a = int(input("Enter a number : "))
for i in range(1, 11):
    print(a, 'x', i, '=', a*i, '\n')
