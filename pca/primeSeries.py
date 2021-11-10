# Find all Prime Numbers between 1 to N
print('Find all Prime Numbers between 1 to N')
n = int(input('Please enter the range'))
for num in range(2, n+1):
    for i in range(2, num//2+1):
        if (num % i) == 0:
            break
    else:
        print(num)
