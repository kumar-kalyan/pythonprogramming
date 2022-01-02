str = "Python is great and Java is also great"
mylist = str.split(" ")
str2 = ''
l = len(mylist)
print()
for i in mylist:
    c = mylist.count(i)
    if(c > 1):
        for j in range(0, c):
            mylist.remove(i)

for i in mylist:
    str2 +=i
    str2+=" "
print(str2)
