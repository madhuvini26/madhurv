limit1=int(input("Enter upper limit:"))

c=0

m=2

while(c<limit1):
    
    for n in range(1,m+1):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if(c>limit1):
            break
        if(a==0 or b==0 or c==0):
            break
        print(a,b,c)
        
m=m+1
