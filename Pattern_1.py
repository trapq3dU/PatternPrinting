l=[]
print("Enter the number of rows you want to print ")
n=int(input())
for i in range(0,n+1):
    check=i
    while(check!=0):
        for j in range (0,i):
            if(check%2==0):
                l.append("O")
                check-=1
            else:
                l.append("X")
                check-=1
        
        #print(i,"......")        
        for x in range(0,2):
            for k in l:                
                print(k,end='')
            print('\n',end='')
        
        
        
    l=[]
    print("\n")
