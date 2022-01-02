mylist = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
list2=[]
num = 4
for i in mylist:
    y=list(i)
    for j in range(0,len(y)):
        y[j]+=num
    list2.append(tuple(y))  
print(mylist) 
print(list2)           
