row = 5
count = 0
for i in range(1, row):
    
    for j in range(1,i+1):
        count+=1
        c=count
    for k in range(1,i+1):
        print(c,'',end='')
        c-=1       
    print()       
