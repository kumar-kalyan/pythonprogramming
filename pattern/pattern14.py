row = 5
for i in range(1,row+1):
    for j in range(1,row+1):
        if (i<j):
            print(j,'',end='')
        else:
            print(i,'',end='')    
    print()    