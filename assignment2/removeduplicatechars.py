str='HELLO'
mylist= []
for i in str:
    c= str.count(i)
    if(c>1 and mylist.count(i)<1):
        mylist.append(i)

print("the duplicate characters in the given string :")
for j in mylist:
    print(j)