row=5
for i in range(row,0,-1):
    for j in range(0,row-i+1):
        print(" ",end='')
    for k in range(0,i):
        print("*",end='')    
    print()    