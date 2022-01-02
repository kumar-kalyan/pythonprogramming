mylist=[(6, 24, 12), (60, 12, 6), (12, 18, 21)]
list2=[]
k=6
for i in mylist:
    y=list(i)
    c=0
    for j in range(0,len(y)):
        if(y[j]%k!=0):
            c=1
    if(c==0):
        list2.append(tuple(y))   

print(list2)