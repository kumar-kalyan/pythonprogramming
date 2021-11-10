#Write a program to swap two numbers using a third variable.
a = int(input('Enter a number'))
b = int(input('Enter another number'))
print('The given values are \n a =',a,'b =',b)
c = a #assigning the value of a in c 
a = b #assigning the value of b in a 
b = c #assigning the value of c in b
print('after swapping \n a =',a,'b =',b)
