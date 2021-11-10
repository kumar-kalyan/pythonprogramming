# Write a program to find and display the reverse of an integer number
print('Write a program to find and display the reverse of an integer number')
n = int(input("Enter a number"))
rev = 0
while(n > 0):
    r = n % 10
    rev = rev*10+r
    n = n//10

print('n=', n, 'rev=', rev)
