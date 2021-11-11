row=5
for i in range(0,row+1):
    for j in range(0,row-i):
        print(' ',end='')
    for k in range(1,i):
        print(k,'',end='')
    print()        