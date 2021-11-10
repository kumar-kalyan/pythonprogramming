#Write a program to swap two numbers without using a third variable.
print('program to swap two numbers without using a third variable\n')
a = int(input('Enter a number'))
b = int(input('Enter another number'))
print('The given values are \n a =',a,'b =',b)
a=a+b
b=a-b
a=a-b
print('\n The  values after swaping are \n a =',a,'b =',b)