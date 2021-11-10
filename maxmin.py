# Write a program that prints minimum and maximum of five numbers entered by the user.
numbers = []
print('program that prints minimum and maximum of five numbers entered by the user \n')
for i in range(5):
    print('Enter the', i, 'st number')
    x = int(input())
    numbers.append(x)
print('Given  numbers \n',numbers)

for x in numbers:
    max=numbers[0]
    if(numbers[i]>max):
        max=numbers[i]
print('The maximum in the given array is',max)

for x in numbers:
    min=numbers[0]
    if(numbers[i]<min):
        min=numbers[i]

print('The minimum in the given array is',min)
