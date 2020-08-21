

    
T=int(input())    
 
for TC in range(T):
    term=int(input())
    termdic={}
    timelist=[]
    res=1
    for t in range(term):
        start,end=map(int,input().split())
        timelist.append([start,end])
    timelist.sort(key=lambda x:x[1],reverse=True)
    
    endpicked=timelist.pop()[1]
   
    while timelist:
        start,end=timelist.pop()
        
        if endpicked<=start:
            endpicked=end
            res+=1
    print("#%d %d" %(TC+1,res))
    
        
